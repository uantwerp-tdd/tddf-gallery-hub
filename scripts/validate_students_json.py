#!/usr/bin/env python3
"""
validate_students_json.py — schema check for data/students.json.

Run automatically by .github/workflows/validate.yml on every pull
request. Exits non-zero (fails the check) if the file isn't valid JSON,
a required field is missing, a URL doesn't look like a URL, or there
are duplicate studentIds.

Also runnable locally: python scripts/validate_students_json.py
"""

import json
import re
import sys

REQUIRED_FIELDS = ["name", "studentId", "repoUrl", "pagesUrl", "modelType", "challenge"]
VALID_MODEL_TYPES = {"Teachable Machine", "Roboflow"}
GITHUB_REPO_RE = re.compile(r"^https://github\.com/[^/\s]+/[^/\s]+/?$")
PAGES_URL_RE = re.compile(r"^https://[^/\s]+\.github\.io/.*$")

DATA_FILE = "data/students.json"


def main():
    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            raw = f.read()
    except FileNotFoundError:
        print(f"::error::{DATA_FILE} not found")
        sys.exit(1)

    try:
        entries = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"::error::{DATA_FILE} is not valid JSON: {e}")
        sys.exit(1)

    if not isinstance(entries, list):
        print(f"::error::{DATA_FILE} must be a JSON array of entries")
        sys.exit(1)

    errors = []
    seen_ids = {}
    for i, entry in enumerate(entries):
        label = entry.get("name", f"entry #{i}") if isinstance(entry, dict) else f"entry #{i}"

        if not isinstance(entry, dict):
            errors.append(f"{label}: entry is not a JSON object")
            continue

        for field in REQUIRED_FIELDS:
            value = entry.get(field)
            is_missing = value is None or (isinstance(value, str) and not value.strip())
            if is_missing:
                errors.append(f"{label}: missing or empty required field '{field}'")

        if entry.get("modelType") and entry["modelType"] not in VALID_MODEL_TYPES:
            errors.append(
                f"{label}: modelType must be exactly one of {sorted(VALID_MODEL_TYPES)}, "
                f"got '{entry['modelType']}'"
            )

        if entry.get("repoUrl") and not GITHUB_REPO_RE.match(entry["repoUrl"]):
            errors.append(f"{label}: repoUrl doesn't look like https://github.com/<owner>/<repo>")

        if entry.get("pagesUrl") and not PAGES_URL_RE.match(entry["pagesUrl"]):
            errors.append(f"{label}: pagesUrl doesn't look like https://<owner>.github.io/...")

        sid = entry.get("studentId")
        if sid:
            if sid in seen_ids:
                errors.append(f"{label}: duplicate studentId '{sid}' (also used by {seen_ids[sid]})")
            else:
                seen_ids[sid] = label

    if errors:
        for e in errors:
            print(f"::error::{e}")
        print(f"\n{len(errors)} problem(s) found in {DATA_FILE}.")
        sys.exit(1)

    print(f"{DATA_FILE} OK — {len(entries)} entries validated.")


if __name__ == "__main__":
    main()

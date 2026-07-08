# TDD Fundamentals Pipeline — Class Gallery

This repo is the class-wide index for the Technology-Driven Design
Fundamentals Pipeline assignment. It does two things:

1. **Hosts a gallery page** (via GitHub Pages) listing every student's
   deployed interface — one place to see all of them instead of
   tracking 90 individual repo links.
2. **Is the mechanism students use to add themselves** — via a pull
   request to `data/students.json`, validated automatically. See
   [CONTRIBUTING.md](./CONTRIBUTING.md).

## Setup (instructor, one-time)

1. Push this repo to your org, e.g.
   `github.com/uantwerp-tdd/tddf-gallery` (naming it after the course,
   not the year — the org and this pattern are meant to persist across
   cohorts).
2. **Settings → Pages → Source: Deploy from a branch → main → / (root)**.
3. The gallery goes live at
   `https://uantwerp-tdd.github.io/tddf-gallery/`.
4. Share that URL (and a link to this repo) with students alongside the
   individual project template repo.
5. **Settings → General → Pull Requests**: consider requiring at least
   one approving review before merge (you, obviously) so nothing lands
   without a look — the automatic JSON check catches format errors, not
   whether the project is actually any good.

## Reviewing pull requests

Each PR touches exactly one entry in `data/students.json` (the CI check
will complain if a PR looks malformed or touches unrelated content).
Practically: open the PR, check the "Files changed" tab, click the live
link once, merge. At ~90 students spread across a semester this is a
handful of PRs a week, not a backlog.

## Turning the gallery data into a spreadsheet

If you'd rather work from Excel than the live page — for cross-checking
against Blackboard submissions, or annotating who's been flagged — use
`export_gallery_to_excel.py` (in the main deliverables, not this repo).
It reads `data/students.json` straight from GitHub and writes a
clickable `.xlsx`.

## Files

```
├── index.html                        # the gallery page itself
├── data/students.json                # one entry per student, source of truth
├── scripts/validate_students_json.py # schema check, run by CI
├── .github/workflows/validate.yml    # runs the check on every PR
├── .github/PULL_REQUEST_TEMPLATE/    # checklist shown on new PRs
└── CONTRIBUTING.md                   # student-facing how-to
```

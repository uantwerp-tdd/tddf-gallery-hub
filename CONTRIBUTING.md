# Add your project to the class gallery

No local git needed — everything below happens in the browser. This is
also your first real pull request, which is the point: this is exactly
how open-source contributions work in the real world.

## Steps

1. Make sure your own interface repo is already deployed and working
   (you should have a live GitHub Pages URL you can click and it works).
2. Open **`data/students.json`** in this repo on GitHub.
3. Click the pencil icon (**"Edit this file"**) top right.
   - If you're not a member of this org, GitHub will say *"You need to
     fork this repository"* — click **Fork this repository and propose
     changes**. This is normal and expected; it happens automatically.
4. Add your entry to the JSON array. Copy this block, fill it in, and
   place a comma after the previous entry if there is one:

   ```json
   {
     "name": "A handle that does not identify you",
     "repoUrl": "https://github.com/<you>/<your-repo>",
     "pagesUrl": "https://<you>.github.io/<your-repo>/",
     "modelType": "Teachable Machine",
     "challenge": "One sentence describing your challenge/component."
   }
   ```

   `name` must be a handle, not your real name. Nothing on GitHub may
   identify you: no name, student ID, e-mail address or photo, and use a
   GitHub username that does not contain your name. This page is public
   and searchable. Your link reaches the instructor only through your
   submission document and your Blackboard submission.

   `modelType` must be exactly `"Teachable Machine"` or `"Roboflow"`.

5. Scroll down to **"Propose changes"**. Write a commit message like
   `Add <your handle>`.
6. Click **Propose changes**, then **Create pull request** on the next
   screen.
7. A check will run automatically and tell you within ~30 seconds
   whether your entry is valid JSON with all required fields. If it
   fails, click into the failed check for details, go back and edit
   your file (same PR, just edit again), it re-checks automatically.
8. Once the check passes, the instructor will review and merge. Your
   card will then appear on the class gallery page.

## Troubleshooting

- **"Invalid JSON" check failure**: almost always a missing comma
  between entries, or a trailing comma after the last entry. Trailing
  commas are not allowed in JSON.
- **Already have an entry and need to update it** (new URL, fixed a
  typo): edit the file again the same way — find your existing entry
  and change it, don't add a duplicate.

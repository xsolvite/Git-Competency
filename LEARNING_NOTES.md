# Git Competency Learning Notes

## Competency: Advanced Git and Version Control

**Learning resource:** [Git for Professionals — freeCodeCamp (YouTube)](https://www.youtube.com/watch?v=Uszj_k0DGsg)

These notes summarize the Git concepts I am applying to the **Evidence Record Checker**, a small Python practice project related to my SupplementsRx AI capstone. The checker validates metadata in fictional evidence records; it does not determine whether medical claims are true.

## 1. Branching and collaboration

A branch lets me work on a feature without changing the stable `main` branch. For example, I can develop documentation separately from Python validation logic:

```bash
git switch main
git switch -c feature/add-learning-notes
```

When the change is ready, I can commit it, push the branch, and open a pull request for review:

```bash
git add LEARNING_NOTES.md
git commit -m "docs: add Git competency learning notes"
git push -u origin feature/add-learning-notes
```

**Why it matters:** In a team capstone, developers can work on retrieval, data processing, and evaluation in parallel while reviewing each other's changes before merging.

## 2. Merge vs. rebase

- **Merge** combines histories and can create a merge commit. It preserves the original structure of the branches.
- **Rebase** replays commits onto a different base. It can make history easier to read, but it changes commit identifiers.

I would generally use a pull request and merge for changes shared with teammates. I would only rebase commits on a branch I control, and avoid rebasing shared branches without team agreement.

## 3. Handling merge conflicts

A conflict can occur when two branches modify the same lines of a file. A basic resolution process is:

1. Open the conflicted file and find the `<<<<<<<`, `=======`, and `>>>>>>>` markers.
2. Decide how the two changes should be combined, then remove the markers.
3. Run the relevant tests to confirm the merged result still works.
4. Stage the corrected file and complete the merge or rebase.

For a merge, the final commands are typically `git add <file>` and `git commit`. During a rebase, they are `git add <file>` and `git rebase --continue`.

## 4. Useful Git habits

- Make small commits with clear, descriptive messages.
- Review changes with `git diff` and `git status` before committing.
- Inspect history using `git log --oneline --graph --all`.
- Run tests before opening or merging a pull request.
- Do not commit secrets, credentials, or large generated model/data files.

For this repository, I can check the Python tests with:

```bash
python -m unittest discover -s tests
```

## 5. Connection to my capstone and career

Version control is especially important for an AI/ML project because changes to preprocessing, retrieval logic, prompts, and evaluation scripts can affect results. Keeping clear Git history makes experiments easier to reproduce, compare, and debug. It also makes collaboration safer when several team members contribute to the same codebase.

## Next steps

- Push this notes file on its own feature branch.
- Open a pull request that explains the change.
- Review the diff, merge the pull request, and capture the GitHub link or screenshot as evidence for the competency assignment.
- Add a short note here afterward describing one specific Git problem I encountered and how I resolved it.

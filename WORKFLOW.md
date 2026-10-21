# Team workflow demonstration

1. Open an issue with the desired change and create a dedicated branch.
2. Keep implementation and documentation changes in focused commits.
3. Run `python -m unittest discover -s tests` before requesting review.
4. Review the diff and discuss the intended change in a pull request.
5. Merge only after checks and teammate review. Never rebase a shared branch without agreement.

To view branches and merges: `git log --oneline --decorate --graph --all`.
To inspect a commit: `git show <sha>`.
To inspect working changes: `git diff`.

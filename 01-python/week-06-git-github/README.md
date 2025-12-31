# Week 06 — Git & GitHub

Goal: learn a simple, repeatable workflow for making changes safely.

## Everyday workflow (cheat sheet)

```bash
# 1) Make sure you're up to date
git checkout main
git pull

# 2) Create a feature branch
git checkout -b feature/my-change

# 3) Work + check status often
git status
git diff

# 4) Stage changes
git add -A

# 5) Commit with a clear message
git commit -m "Describe the change"

# 6) Push branch
git push -u origin feature/my-change

# 7) Open a Pull Request (PR) on GitHub
```

## Commit tips

- Prefer small commits that do one thing.
- Write messages in the imperative mood:
  - ✅ "Add retry logic to API client"
  - ✅ "Fix typo in README"
  - ❌ "Added retry logic"
- Include context in the PR description (what/why).

## Useful commands

```bash
git log --oneline --decorate --graph --all
git restore --staged <file>
git restore <file>
git branch -vv
```

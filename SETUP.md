# Setup - publish the monorepo

The folder is already assembled. All three analyses are in place with real content:

```
movie-analysis/
  index.html              landing page linking all analyses
  README.md
  SETUP.md
  the-black-dog/          The Black Gold dossier (index.html + 2 reports + README)
  spirit-analysis/        from prudhvi1709/spiritanalysis
  romanchakam-analysis/   from prudhvi1709/romanchakam-analysis
```

Only publishing remains. Run these in Terminal:

```bash
cd ~/Desktop/github/movie-analysis
git init
git add .
git commit -m "Consolidate movie analyses into one repo"

# with the GitHub CLI:
gh repo create movie-analysis --public --source=. --remote=origin --push

# or manually, after creating an empty repo on github.com:
# git remote add origin https://github.com/prudhvi1709/movie-analysis.git
# git branch -M main
# git push -u origin main
```

## GitHub Pages (optional)
Repo Settings to Pages, Source = main branch / root.
Live at https://prudhvi1709.github.io/movie-analysis/ , each film at /the-black-dog/, /spirit-analysis/, /romanchakam-analysis/.

## Notes
- The spirit and romanchakam folders are plain copies (no nested .git), so they commit cleanly into this single repo. Their original repos on GitHub are untouched.
- This flattens the source repos' commit history. To preserve history instead, use git submodules; ask and I will provide those commands.

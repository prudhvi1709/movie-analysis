# Movie Analysis

One destination for data-backed film analysis: release-date strategy, competition mapping, promotion planning, and social-buzz breakdowns across titles.

A static landing page (`index.html`) links every analysis. The site is ready to host on GitHub Pages.

## Contents

| Film | Folder | Status | What's inside |
|------|--------|--------|----------------|
| The Black Gold | [`the-black-dog/`](./the-black-dog/) | Live | Release date + teaser/trailer schedule, promotion plan, real X social-buzz history, influencer outreach |
| Spirit | [`spirit-analysis/`](./spirit-analysis/) | Live | Social-media analytics dashboard (Prabhas, dir. Sandeep Reddy Vanga). Copied from `prudhvi1709/spiritanalysis` |
| Romanchakam | [`romanchakam-analysis/`](./romanchakam-analysis/) | Live | First-look reception report (Bhadrakali Pictures). Copied from `prudhvi1709/romanchakam-analysis` |
| Romanchakam (Trailer) | [`romanchakam-trailer-analysis/`](./romanchakam-trailer-analysis/) | Live | Cross-platform trailer reception report (X, YouTube, Reddit, Google Trends) |
| Romanchakam (Release) | [`romanchakam-release-analysis/`](./romanchakam-release-analysis/) | Live | Release-day reception report (X, Reddit): press reviews, audience sentiment, box office |

## Structure

```
movie-analysis/
  index.html            # landing page linking all analyses
  README.md             # this file
  the-black-dog/
    index.html          # complete strategy dossier (main)
    release-promo-strategy.html
    social-history.html
    README.md
  spirit-analysis/      # contents of the spirit-analysis repo
  romanchakam-analysis/ # contents of the romanchakam-analysis repo
```

## How this was assembled (monorepo)

The two existing repositories were copied in as subfolders, so everything lives in one place under a single repo. See [`SETUP.md`](./SETUP.md) for the exact commands.

## Hosting on GitHub Pages

1. Push this folder as a repo (for example `movie-analysis`).
2. In the repo: Settings to Pages, set Source to `main` branch, root.
3. The site goes live at `https://prudhvi1709.github.io/movie-analysis/`, with each film at `/the-black-dog/`, `/spirit-analysis/`, `/romanchakam-analysis/`.

## Adding a new analysis later

1. Create a new subfolder (for example `new-film/`) with its `index.html`.
2. Add a matching card to `index.html` and a row to the table above.

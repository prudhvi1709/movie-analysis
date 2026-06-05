# Romanchakam — First-Look Reception Analysis

A social-media reception report for the first-look announcement of **Romanchakam**, a musical romantic comedy from Bhadrakali Pictures presented by Sandeep Reddy Vanga (announced May 29, 2026).

Built in the style of the [Spirit first-look analysis](https://github.com/prudhvi1709/spiritanalysis).

## Live dashboard

Open **`index.html`** in any browser. It is fully self-contained — all data is embedded inline and the charts are drawn with plain SVG/CSS, so there are **no external dependencies** and it works offline. To host it: enable GitHub Pages on this repo and point it at the root; `index.html` is the entry point.

## Key findings

- **138 unique opinion-bearing tweets** analyzed (100 replies + 20 quote-tweets + 18 hashtag/trade posts).
- Sentiment: **30.4% positive, 61.6% neutral, 8.0% negative**.
- **45% of direct responses** (replies + quotes) are asking about **Spirit / Prabhas** rather than Romanchakam — the single biggest theme, and the launch's most reachable built-in audience.
- Announcement reach: **194.6K views, 7.3K likes, 624 reposts, 116 replies** (~4.2% engagement); the `#Romanchakam` trend carried ~49.6K total posts.
- Music (Vasuki Vaibhav / T-Series) and the "presented by Vanga" framing draw the strongest organic positivity.
- **Google Trends (past 7 days):** search interest is overwhelmingly **Andhra Pradesh (100) and Telangana (82)**, with minor blips in Jharkhand (39), Uttarakhand (34) and Karnataka (17); worldwide, India is effectively the only country with meaningful volume. Shown as an India state choropleth map (real simplified boundaries) + worldwide panel in the dashboard. Values are Google's relative 0–100 interest score, not absolute counts.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The self-contained dashboard (only file needed to view the report) |
| `build_data.py` | Reproducible script: holds the classified tweet dataset and computes all metrics, writing the JSON files |
| `combined_analysis.json` | Full analysis output (film info, announcement metrics, sentiment, themes, top contributors, methodology) |
| `sentiment_analysis.json` | Sentiment and Spirit-share figures |
| `top_contributors.json` | Highest-engagement tweets in the sample |
| `film_data.json` | Film metadata and announcement metrics |

To regenerate the JSON from the dataset:

```bash
python3 build_data.py
```

## Methodology & limitations

Tweets were collected via browser from the announcement's replies, quote-tweets, and the `#Romanchakam` hashtag feed (posts dated May 28–31, 2026), then deduplicated. Sentiment and theme were assigned by manual review of each tweet, including English, Telugu, and transliterated-Telugu content. The "Spirit %" is measured over the 120 direct responses (replies + quotes).

This is a **curated sample** of the highest-visibility and most-engaged posts within a ~49.6K-post trend, not the full population — treat percentages as directional. One trade claim circulating in the data (Netflix streaming rights) is **unverified** and flagged as such in the dashboard.

## Source

First-look post: [@imvangasandeep on X](https://x.com/imvangasandeep/status/2060323229768749264)

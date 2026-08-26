# Romanchakam: Trailer Reception Report

A cross-platform read on how the **Romanchakam** trailer (dropped 25 August 2026, 8:10 PM IST; film releases 3 September 2026) landed with audiences on X, YouTube, and Reddit, plus Google Trends search interest.

This is a companion to [`../romanchakam-analysis`](../romanchakam-analysis) (Part A: release strategy, Part B: first-look/announcement reception). This report supersedes only the release date from Part A - Part A modeled a preferred 28 August date; the confirmed release is 3 September 2026.

## Live dashboard

Open **`index.html`** in any browser. It is fully self-contained - all data is embedded inline and the charts are drawn with plain SVG/CSS, so there are **no external dependencies** and it works offline.

## Key findings

- **Reach is strong, but the positive narrative is mostly promotional.** 600K+ YouTube views and 1.5M+ cumulative X impressions (sum across posts, not unique reach) in under 28 hours. On X, 92 posts across 16 near-identical text clusters came from studio/PR/trade accounts, plus roughly 250 more trade-press posts quoting launch-event soundbites - a promotional layer that is positive by construction.
- **Organic reaction is a different story.** Among 34 opinion-bearing direct replies to the announcement (of 61 total; the rest are pure Spirit/Prabhas asks, spam, or empty), sentiment is **41.2% positive vs 47.1% negative** - net slightly negative. On YouTube, the top 163 comments reviewed (99% of total comment likes) split **52.8% negative vs 11.7% positive**. Reddit's main r/tollywood thread sits at a **0.38 upvote ratio**.
- **The criticism is specific and repeats across platforms:** trailer cut/editing ("poor flow," "random scenes"), comedy not landing ("didn't laugh once"), and skepticism about lead actor Sumanth Prabhas's casting. "Looks like a high-budget short film" is the single most-liked YouTube comment (739 likes).
- **The Spirit/Prabhas tangent recurs, smaller than before.** 24.6% of all direct replies are off-topic Spirit/Prabhas asks (Part B measured 45% on the bare announcement) - expected to shrink once there's an actual trailer to react to, but still a real drag on signal.
- **A genuine late positive signal, not yet fully captured:** ~22 hours after the drop, Prabhas posted an Instagram story praising the trailer, which started circulating on X via reposts in the final hours of this capture window. Its full effect isn't visible yet - see Limitations.
- **The studio's "first U/A" family-friendly PR angle got zero organic pickup** anywhere in the sample reviewed, despite heavy trade-press repetition.
- **Google Trends:** search interest is almost entirely India (Telangana 100, Andhra Pradesh 94, much smaller Karnataka/Odisha/Tamil Nadu), spiking cleanly with the trailer drop and peaking the next morning as people caught up on it.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The self-contained dashboard (only file needed to view the report) |
| `build_data.py` | Reproducible script: holds the classified dataset and computes all metrics, writing the JSON files |
| `combined_analysis.json` | Full analysis output (film info, YouTube/X/Reddit/Trends data, methodology) |
| `sentiment_analysis.json` | Sentiment breakdowns by channel |
| `top_contributors.json` | Notable positive/negative quotes across channels |
| `film_data.json` | Film/trailer metadata |

To regenerate the JSON from the dataset:

```bash
python3 build_data.py
```

## Methodology & limitations

- **X:** user-scraped keyword search ("Romanchakam"), hashtag search (#Romanchakam / #RomanchakamTrailer), and direct replies to the announcement post - 521 raw posts, 451 unique after deduping by link. Sentiment on the 61 direct replies was assigned by manual review; 34 are opinion-bearing (the other 27 are pure Spirit/other-film asks, spam, or empty text) and excluded from the sentiment split, matching the Part B method.
- **YouTube:** `yt-dlp` against the public trailer URL for view/like/comment counts and all 392 comments; the top 163 by like-count (99% of total comment likes) were reviewed manually for sentiment. This is a **count-based** split, reported as primary - a like-weighted number would be dominated by a handful of the most-liked comments and overstate how many people actually weighed in.
- **Reddit:** `rdt-cli` (authenticated) direct thread reads plus keyword search.
- **Google Trends:** trends.google.com, past-7-days window, India subregion and worldwide.
- **This is a curated, high-engagement sample, not the full population** - treat percentages as directional.
- **X "impressions" figures are cumulative** (summed across posts), not unique reach.
- **Instagram was not sampled directly** - no reliable read-only tool was available at capture time. The Prabhas endorsement is known only via X reposts of his IG story text.
- **The Prabhas Instagram endorsement landed ~22 hours post-drop**, in the final hours of this capture window - a follow-up pull at T+48h is recommended to see its full effect on organic sentiment.
- **A small regional/dialect undercurrent** appeared in low volume on all three platforms (2 of 61 X replies, one YouTube sub-thread, one Reddit comment removed for rule violations). Flagged for awareness, not sized as a sentiment driver, and not quoted verbatim.

## Source

Trailer: [youtu.be/c5IXkos5XMI](https://youtu.be/c5IXkos5XMI)

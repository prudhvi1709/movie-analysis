# Romanchakam: Release Reception Report

A read on how **Romanchakam** (night premieres 2 September 2026, wide release 3 September 2026) landed with critics, X audiences, and Reddit once people actually watched it - as opposed to reacting to a trailer.

This is a companion to [`../romanchakam-analysis`](../romanchakam-analysis) (Part A/B: release strategy, first-look/announcement reception) and [`../romanchakam-trailer-analysis`](../romanchakam-trailer-analysis) (trailer reception, 25-26 Aug).

## Live dashboard

Open **`index.html`** in any browser. It is fully self-contained - all data is embedded inline and the charts are drawn with plain SVG/CSS, so there are **no external dependencies** and it works offline.

## Key findings

- **Three channels, three different verdicts.** Press/critic reviews (19 sampled, 11 with an explicit rating) average **2.39/5** - 58% mixed, 37% negative, only 1 clearly positive. Ordinary X audience posts (30 opinion-bearing, of 516 unique pulled) skew **60% positive vs 30% negative**. Reddit's r/tollywood release megathread runs **81% negative** (16 opinion-bearing voices of 57 comments read).
- **Nobody disputes the film's weak spot - they disagree on whether it matters.** Press and Reddit both call the romance/story thin; the recurring specific criticism is that the lead's performance imitates Naveen Polishetty and leans on *Jathi Ratnalu*'s style without matching it. X's organic posters treat the comedy (especially Narendra Ravi's "Chintu") and Vasuki Vaibhav's music as enough to call it a fun watch anyway.
- **The "paid review" argument is not just noise - there's a concrete data point behind it.** Two accounts (ReviewerBossu, PanIndiaReview) posted near-identical "1st half review" text 42 minutes apart on 2 Sep. Both were excluded from the organic-audience count and reported separately as evidence for the suspicion raised independently on both X and Reddit ("paid one's don't cmt").
- **Mahesh Babu's endorsement (36,313 likes, 2.71M views on his own account) is the single highest-engagement post in the whole dataset** - an order of magnitude above any organic review or reaction. Vijay Deverakonda also made a live promotional appearance. Prabhas's support is referenced repeatedly via fan/PR accounts but wasn't sampled from his own handle in this pull.
- **Box office opened modestly**: ~Rs1.45-2.00 Cr Nett/Gross India on Day 1 across 1,394 shows (figures vary by tracker), with Telangana contributing roughly two-thirds of the All-India total and Andhra Pradesh underperforming by comparison. USA premieres did $41K, growing to $70K+ by Day 2; UK screens (Cineworld) reported near-full houses.
- **YouTube and Google Trends were not part of this pull** - only X and Reddit data was gathered this round, a gap versus the trailer report's coverage.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The self-contained dashboard (only file needed to view the report) |
| `build_data.py` | Reproducible script: holds the classified dataset and computes all metrics, writing the JSON files |
| `combined_analysis.json` | Full analysis output (film info, X/Reddit/box-office data, methodology) |
| `sentiment_analysis.json` | Sentiment breakdowns by channel |
| `top_contributors.json` | Notable positive/negative/mixed quotes across channels |
| `film_data.json` | Film metadata |

To regenerate the JSON from the dataset:

```bash
python3 build_data.py
```

## Methodology & limitations

- **X:** user-scraped data from two pulls (86 + 453 posts), deduped by link to 516 unique posts. Classified by manual review into: press/critic reviews (19, treated as their own layer since it's the most comparable signal), organic audience posts (30 opinion-bearing, excluding studio/PR templates and box-office numbers), celebrity endorsements, and the "paid review" controversy thread. This is a curated, high-engagement-weighted sample, not the full population - treat percentages as directional.
- **Reddit:** `rdt-cli` against the r/tollywood release megathread, top-sorted with a 300-comment limit and `--expand-more`; 57 of the 60 comments Reddit reports on the thread were retrieved. Sentiment counted per distinct opinion-bearing voice (a user repeating the same opinion across a reply chain is counted once); AutoModerator, deleted/removed comments, and pure tangents (questions, sarcasm-only exchanges) are excluded.
- **Box-office figures come entirely from the X promotional/trade layer**, not an audited trade source, and vary by up to Rs0.5 Cr across trackers for the same day - treat as directional.
- **Two "review" posts (ReviewerBossu, PanIndiaReview) were found to share near-identical phrasing** posted 42 minutes apart and were excluded from the organic-audience count as likely syndicated/coordinated content.
- **One viewer (UrstruulyDinesh) posted three different reactions across the day** (two positive, one negative) - a reminder that a per-post sentiment tag is not the same as a single stable per-viewer verdict; this is inherent to sampling posts rather than people.
- **YouTube and Google Trends were not sampled in this pull.**

## Source

Reddit megathread: [r/tollywood - Romanchakam (2026) Review/Discussion Thread](https://www.reddit.com/r/tollywood/comments/1w5k8y0/romanchakam_2026_reviewdiscussion_thread_spoilers/)

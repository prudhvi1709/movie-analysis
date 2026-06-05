# Spirit Movie - Social Media Analytics Dashboard

**Director:** Sandeep Reddy Vanga
**Lead Actor:** Prabhas
**First Look Release:** January 1, 2026

---

## Overview

Interactive analytics dashboard presenting comprehensive social media performance data for the Spirit First Look reveal. Built with 100% actual data from Twitter/X, Instagram, and YouTube platforms.

## Key Metrics

- **529 tweets analyzed** (388 replies + 141 trending tweets)
- **Sentiment:** 40.6% Positive, 56.5% Neutral, 2.8% Negative
- **Engagement Rate:** 5.5% (Very Strong)
- **Total Views:** 2.2M+ (Twitter) + 2.1M+ (Instagram)
- **Geographic Focus:** Telangana (100 index), Andhra Pradesh (97 index)

## Features

### 📊 Data Visualizations
- 3-Phase Sentiment Evolution (Audio Teaser → Pre-Poster → Post-Poster)
- Platform-wise engagement comparison
- State-wise market index (Telangana baseline: 100)
- Hourly activity timeline (IST)
- Top 10 reply contributors with hover tooltips

### 🎯 Strategic Insights
- Sentiment trajectory analysis
- Box office projections (960-2000 cr range)
- Market strength indicators
- Influencer partnership ROI
- Comparison with Animal pre-teaser performance

### ⚡ Real-Time Features
- Interactive charts (Chart.js 4.4.0)
- Custom tooltips on hover
- Fan account flagging
- Responsive design

## Technology Stack

- **Frontend:** Pure HTML5, CSS3, Vanilla JavaScript
- **Charting:** Chart.js 4.4.0
- **Data Format:** JSON
- **No dependencies** (CDN-based Chart.js only)

## Data Sources

All metrics sourced from actual social media posts:
- Twitter/X: @imvangasandeep, @InSpiritMode (fan), trending #SpiritFirstLook
- Instagram: @actorprabhas, @imvangasandeep
- Analysis Period: October 23, 2025 - January 2, 2026

## Files Structure

```
srv/
├── index.html                          # Main dashboard
├── actual_hourly_activity.json         # Hourly Twitter activity (IST)
├── combined_twitter_analysis.json      # Comprehensive Twitter metrics
├── top_contributors.json               # Top 10 reply contributors
├── README.md                           # This file
└── .gitignore                          # Git ignore rules
```

## Usage

Simply open `index.html` in any modern web browser. No server or build process required.

```bash
# Local viewing
open index.html

# Or serve with any HTTP server
python3 -m http.server 8000
# Then visit: http://localhost:8000
```

## Key Findings

### Sentiment Momentum
- **Audio Teaser (Oct 23):** 35.0% positive, 9.9% negative
- **Pre-Poster (Dec 25-31):** 65.8% positive, 1.2% negative
- **Post-Poster (Jan 1):** 68.5% positive, 1.6% negative

**Insight:** 88% reduction in negativity over 2.5 months - campaign successfully converted skeptics.

### Market Performance
- Spirit launched **8.9% stronger** than Animal (40.6% vs 31.7% positive)
- Telangana & Andhra Pradesh markets at 97-100 index (premium pricing justified)
- USA leads international market with 27.8% share

### Strategic Gaps
- T-Series (270M+ subscribers) hasn't posted on YouTube/Instagram yet
- Fan account (@InSpiritMode) outperforms official accounts in engagement efficiency (3.63% vs 1.91%)

## Box Office Projection

**Conservative:** 960 crores (beating Animal's 917 cr)
**Optimistic:** 2000+ crores (Bahubali 2 territory)

Based on: Sentiment trajectory, star power, genre timing, and Animal baseline performance.

---

## Data Integrity

✅ All sentiment percentages based on actual tweet analysis
✅ No synthetic or projected engagement data
✅ Fan accounts clearly flagged
✅ Sample sizes cited for all metrics
✅ IST timezone corrections applied to all timestamps

## Credits

**Data Collection & Analysis:** Twitter/X scraping, sentiment classification, geographic indexing
**Dashboard Development:** Interactive visualization with Chart.js
**Analysis Period:** 70 days (Oct 23, 2025 - Jan 2, 2026)

---

## License

MIT License - Copyright (c) 2026 Prudhvi Krovvidi

See [LICENSE](LICENSE) file for details.

---

**Last Updated:** January 2, 2026
**Version:** 1.0 (Director Meeting Edition)
**Author:** Prudhvi Krovvidi

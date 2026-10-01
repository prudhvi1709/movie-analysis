# Spirit: worldwide hype review

Companion report for Sandeep Reddy Vanga covering January 1 - October 1, 2026, worldwide. Display dates use Asia/Kolkata. The historical first-look dashboard remains separate.

Open `index.html` directly, through a local HTTP server, or on the collection's existing static host. When sharing the report as files, include the entire `spirit-hype-analysis` folder so styles, interactions and evidence downloads remain available. The analysis, tables and charts remain readable without JavaScript. JavaScript only adds theme selection and an evidence filter; selections are stored in the URL.

## Sources and method

- User-supplied X file: 375 unique links; 277 rows in the IST window, including false positives. The September-heavy selection is not a platform-volume sample. Raw attachment remains outside the repository. SHA-256 and coverage counts are in `evidence.json`.
- ChatGPT in Brave: public-source discovery, followed by independent checks of key chronology against public reporting and X. Its draft was not a source.
- Logged-in X in Brave: public posts and official account attribution. Eight selected post counters were checked live on October 1. Other selected counters retain the supplied snapshot, whose capture time is unknown. No private account data or session credentials are included.
- Reddit via RDTCLI: searches for `Spirit` in `tollywood` and `BollyBlindsNGossip`, top and new sort, year window, limit 100, full text. Four slices returned 334 rows and 215 unique IDs before date/relevance filtering. Eight selected threads yielded 437 comment records. Selected high-score comments were reviewed qualitatively, not exhaustively classified.
- Google Trends in Brave: worldwide, all categories, Web Search, January 1 - October 1. `Spirit Prabhas` exported through the UI; `spirit 2027` transcribed from the visible weekly table after its CSV action was blocked by Brave. Each series is independently normalized. The first boundary and final partial weeks are flagged. Regional data uses only the primary query. Generic `Spirit movie` was excluded as a headline measure because it mixed unrelated films.

## Reproduction

Example RDTCLI searches:

```sh
rdt search Spirit -r tollywood --sort top --time year --limit 100 --json --full-text -o /tmp/spirit-tollywood-top.json
rdt search Spirit -r tollywood --sort new --time year --limit 100 --json --full-text -o /tmp/spirit-tollywood-new.json
rdt search Spirit -r BollyBlindsNGossip --sort top --time year --limit 100 --json --full-text -o /tmp/spirit-bolly-top.json
rdt search Spirit -r BollyBlindsNGossip --sort new --time year --limit 100 --json --full-text -o /tmp/spirit-bolly-new.json
rdt read 1weaq3i --sort top --limit 60 --json
```

Search indexes and social counters may change on repeat capture. Follow the linked posts and article dates, rather than treating present counters as launch-day performance. Casting status and release statements can change; this report preserves the research cutoff.

## Files

- `index.html`, `report.css`, `report.js`: static report and optional interactions.
- `evidence.json`: distilled public source metadata, selected X evidence, Reddit thread metadata, search values and limitations.
- `search-interest.csv`: 40 observed weekly values, with boundary and partial flags.
- `regional-interest.csv`: 22 nonblank regional observations, including values below 1.

No sentiment percentages, unified hype score, unique worldwide reach, causal publicity effects or box-office projections are inferred. Country search indexes describe normalized intensity, not audience share. English queries are not a full measure of native-language markets.

## Verification

Rendered October 1 at 1440, 768 and 375 pixels with the installed Playwright verification skill: no reported console, request, accessible-name, heading-order or page-overflow findings. Theme/filter URL persistence, invalid query fallback, keyboard skip navigation and no-JavaScript evidence visibility passed separate browser checks. Desktop, mobile and light-theme screenshots were inspected. IST sample counts and the primary search series were independently recomputed from the supplied attachment and downloaded CSV. These checks do not turn the selected social sample into a representative survey.

Direct-file sharing was additionally checked: theme selection, evidence filtering, query persistence, keyboard skip navigation and no-JavaScript content passed on the `file:` URL. The script uses a deferred, scoped classic script so local-file opening does not trigger module CORS restrictions.

## Visual edition

The report now opens with less prose and six visual views:

- A date-positioned event rail beneath the search curves, separating official / reported maker statements, fan activity, and other attention. Twelve selected events link to sources; selection is bookmarkable through the `event` query parameter. Nearby events are stacked within their lane without changing their date position.
- January and September example panels, explicitly not measured conversation shares or equal-duration engagement comparisons.
- A release-date, casting and certificate tracker distinguishing announcements, intentions, unconfirmed claims and the audit cutoff.
- A six-question reception matrix using selected comment paraphrases. Supporting, skeptical and mixed/questioning labels describe individual examples toward each question, not whole threads. Empty cells mean no example selected. Enter opens a cell; arrow keys move between available cells.
- A ranked regional search dot plot. Values below 1 remain categorical, and missing observations are distinguished from zero interest. The full regional table is expandable.
- A proposed audience-question / asset / follow-up-check map. These are campaign recommendations, not measured outcomes.

Full chronology, discussion summaries, regional values, campaign ownership and source ledger are expandable. No new platform totals, sentiment proportions or competitor benchmarks were inferred. `visual-evidence.json` records the selected events and manually coded comment references. The original `evidence.json` and CSV observations remain unchanged.

The visual edition passed the Playwright page checks at 1440, 768 and 375 pixels on its local-file URL. Separate checks covered event selection and URL restoration, previous/next bounds, invalid-event fallback, reception keyboard navigation, existing theme/source filter behavior and no-JavaScript access. Source comment IDs were checked against the RDTCLI retrievals. Desktop/mobile and light-theme screenshots were reviewed; crowded event labels and mobile country-label sizing were corrected.

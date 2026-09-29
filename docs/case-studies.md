# Measured results

Every number on this page comes from a project report, a decision log or a machine-readable state file written during the mission. Clients are anonymised: no name, no link, no screenshot. Dates are given by month.

## How the numbers were measured

- **Lighthouse** is run on mobile emulation against the public production URL, never against a local build or a protected preview.
- **Best-of-N.** The build server is shared between missions. On identical code, the performance score was observed swinging from 95 to 57 depending on CPU load. Each report therefore records the best run and the median of 3 to 5 sequential runs.
- **Third-party audit.** An independent French audit tool scores five axes: technical, AI readiness (GEO), content, performance and trust. It does not re-score a URL it has already seen, so each iteration is audited on a fresh public URL.
- **Scroll hero playback** is measured in Chrome from a cold cache, throttled to 10 Mbit/s with 100 ms latency, counting frames actually presented (`requestVideoFrameCallback`).

## Summary

| Project | Type | Lighthouse mobile (Perf / A11y / BP / SEO) | Third-party audit | Iterations |
|---|---|---|---|---|
| Jeweller | Prospecting demo | 92 / 100 / 100 / 100 | 83 to 93 | 5 audited versions |
| Property management firm | Prospecting demo | 95 to 98 / 100 / 100 / 100 | 95 on first audit | 0 corrective pass |
| Wine merchant | Prospecting demo | 94 to 98, median 97 / 100 / 100 / 100 | 95 on first audit | 4 hero iterations |
| Estate agency C | Prospecting demo | 99 best, 96 median / 100 / 100 / 100 | 96 | V1 plus 3 feedback loops |
| Estate agency B | Prospecting demo | 97 to 99 / 100 / 100 / 100 | 88 to 90 | 3 feedback loops |
| Estate agency A | Prospecting demo | 94 best, 91 median / 100 / 100 / 100 | 89 | 7 versions |
| Estate agency D | Prospecting demo | 95 / 100 / 100 / 100 | not audited | V1 plus 5 feedback loops |
| Law practice | Delivered site | 93 / 100 / 100 / 100 | not audited | 4 versions |
| Professional athlete | Prospecting demo | 96 / 100 / 100 / 100 | not audited | V1 plus 5 feedback loops |
| Watch store | E-commerce | 98, 96, 95 / 96 / 100 / n.a. | not audited | 43 feedback loops |

The watch store SEO score is not reported: the measured deployment was a set of design samples, deliberately closed to indexing.

## Jeweller: from 83 to 93 on a third-party audit

Independent jeweller with a workshop and shop. Art direction in Product mode. August 2026.

| Axis | Before | After |
|---|---|---|
| Global score | 83 | 93 |
| Trust | 80 | 100 |
| Content | not recorded | 100 |
| Performance | 84 | 92 |
| Technical | not recorded | 91 |
| AI readiness | 83 | 87 |

Sequence across five audited URLs: 83, 85, 87, 92, 93.

What moved the score:

- **A visible date.** The footer had no "last updated" line. Adding it, with matching `datePublished` and `dateModified` in the structured data, took Trust from 80 to 100.
- **One structured data graph.** Business, organisation, person, page, article and FAQ are linked by `@id` in a single `@graph`.
- **Named rules for AI crawlers** in `robots.txt`, instead of a wildcard.
- **A real article** of about 800 words answering the trade's most common customer question.

This project is where the SEO skill comes from. Every later project applied the same base on day one.

## Property management firm: 95 on the first audit

Independent property management firm. August 2026.

- Third-party audit: **95 / 100 on the first submission**, with no corrective version. Trust 100, content 100, performance 95, technical 93, AI readiness 91.
- Lighthouse mobile: 95 to 98 / 100 / 100 / 100.
- Self-hosted fonts: 4 WOFF2 files, 85 KB in total.

A first hero, purely typographic, scored 98 on performance and was rejected by the decision maker in one sentence: the prospect has to see himself in the page. The final hero is an image. The score is not the brief.

## Wine merchant: 95 on the first audit, with a scroll-driven hero

Independent wine shop with no previous website. August 2026.

- Third-party audit: **95 / 100 on the first submission**.
- Lighthouse mobile, best of 5: performance 94 to 98, median 97. Accessibility 96 then 100. Best practices 100. SEO 100.
- Scroll sequence: 450 frames, 45 MB on desktop. Mobile loads 1 frame in 5, about 9 MB.
- A sharper cut at 1920 px and 48 frames per second weighed 102 MB and was rejected.

The frames are requested on the first user gesture, not at page load, which is why a 45 MB sequence coexists with a performance score of 97.

## Estate agency C: five runs, all reported

Independent estate agency. August 2026.

- Lighthouse performance, five sequential runs: **87, 98, 96, 96, 99**. Best 99, median 96. No corrective pass was needed.
- Worst run: FCP 1.6 s, LCP 2.9 s, TBT 240 ms, CLS 0.
- Accessibility, best practices and SEO: 100.
- Third-party audit: 96 / 100, technical axis 100.
- After each of the three feedback loops the measurement was repeated: 98 best and 96 median, then 98 and 97, then 97 and 96.

The run at 87 is published with the others. A single run on a shared server proves nothing in either direction.

## Law practice: blocking time divided by 21

Independent lawyer opening a solo practice. Regulated profession. August 2026.

- Replacing JavaScript scroll reveals by CSS scroll-driven animations: **Total Blocking Time from 860 ms to 40 ms**.
- Acceptance run, best of 3: performance 93, accessibility 100, best practices 100.
- SEO scores **69 with the indexing gate closed and 100 with it open**. The 69 is intended: professional rules require the site to be declared to the bar before it goes public, so the site ships with `noindex` and a single flag opens it.
- Zero console error and zero Content Security Policy violation at acceptance.

Ethics rules shape the design as much as the copy: no review, no testimonial, no rating, no client name, no superlative.

## Watch store: a scroll hero that starts in under two seconds

Young brand of hand-assembled automatic watches, sold online only. Headless storefront in two languages, 10 products and 39 variants. September 2026.

| Measure | Before | After |
|---|---|---|
| First animated frame, desktop | 39.353 s | 1.874 s |
| First animated frame, mobile | 17.668 s | 1.457 s |
| Desktop hero file | 14 020 710 bytes | 6 971 216 bytes |
| Frames presented over a 10 s scroll | 181 | 594 |
| Longest pause during the scroll | 634 ms | 33.6 ms |
| Lighthouse performance, frames deferred to first gesture | 74 | 96 |

What was done:

- **Two defects, two fixes.** The desktop problem was network starvation of a progressive image sequence. The mobile problem was too few distinct visual states. They were reproduced and fixed separately.
- **Native video transport** instead of hundreds of image requests, with a player that keeps a single seek in flight and always jumps to the latest target.
- **A smaller file played better.** Halving the desktop file raised presented frames from 181 to 594. A shorter keyframe interval or a bigger file did not guarantee a smoother scroll: only measurement did.
- **A timestamp remux without re-encoding** removed seek stalls on WebKit: 62 isolated seeks with a maximum of 71 ms and no pause above 250 ms, where four pauses of several hundred milliseconds were seen before.

The project went through 43 numbered feedback loops in nine days.

## Estate agencies A, B and D

- **Agency A** went through 7 versions in four days. Best practices rose from 77 to 100 once a form posting to a `mailto:` address was replaced. The scroll sequence grew from 72 frames (3.6 MB) to 360 frames (22 MB) over four versions, with mobile loading 1 frame in 3.
- **Agency B** moved from 88 to 90 on the third-party audit. Its hero is a 719-frame sequence, obtained by stabilising a 15-second generated clip and interpolating it to 48 frames per second. Mobile loads 1 frame in 6.
- **Agency D** shipped its first version at 95 / 100 / 100 / 100 with no corrective pass, then took five feedback loops. Accessibility dropped to 97 during one loop and was brought back to 100.

## How long a mission takes

No project logged its hours, so no hourly figure is claimed. Two things are recorded.

**Calendar time**, from the mission dates in the reports:

| Project | From first build to measured delivery |
|---|---|
| Property management firm | 3 days |
| Wine merchant | 3 days |
| Estate agency B | 4 days |
| Estate agency A | 4 days |
| Estate agency C | 2 days |
| Estate agency D | 6 days |
| Law practice | 8 days |

**Commit activity**, computed from Git history. A session is a run of commits less than 90 minutes apart, counted as its span plus 30 minutes.

| Project | Commits | Sessions | Active hours (lower bound) |
|---|---|---|---|
| Estate agency D | 17 | 5 | 5.1 |
| Estate agency C | 11 | 2 | 4.0 |
| Estate agency A | 9 | 4 | 3.9 |
| Professional athlete | 7 | 3 | 3.4 |
| Law practice | 8 | 4 | 3.2 |

These hours are a floor, not an estimate of the whole mission. Research, onboarding and the art-direction checkpoint happen before the first commit and are not counted.

Two durations are written in the skills themselves:

- The SEO base costs about **one hour when applied at creation**. Catching up afterwards cost a whole version.
- Expect **2 to 4 feedback loops** after the first version goes live.

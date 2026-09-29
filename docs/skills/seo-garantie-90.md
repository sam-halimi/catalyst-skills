# seo-garantie-90

Build-time SEO playbook for Next.js sites that targets Lighthouse SEO 100, mobile Performance >= 90 and a score >= 90 on the third-party auditor seaudit.fr from the first version of a site.

## What it does

- Gives a V1 build checklist: URL architecture, metadata, one JSON-LD `@graph`, visible trust signals, an Article page, semantic Q/A and lists, security headers, robots rules for AI crawlers, IndexNow.
- Documents nine mistakes made on earlier projects, with the score each one cost where it was measured.
- Defines an audit protocol based on a fresh public URL for each audit, and a list of mandatory checks before delivery.
- Describes a method to rebuild the scoring grid of any audit tool from its public methodology. The grid rebuilt for seaudit.fr is 100 % on-page and is kept private; the public copy contains a summary only.

## When it runs

- Skill name: `seo-garantie-90`. No slash command is defined in the skill file.
- Triggers stated in the frontmatter: creation of any new client site or demo, before any SEO audit, when an audit score stagnates, when the agency's SEO guarantee has to be explained.

## Inputs and outputs

Inputs:
- Real client data: name, address, phone, email, opening hours, social and directory profiles, Google listing URL.
- A real person for author and founder, or the legal publication director found in the company registry. Otherwise the author is the Organization.
- Geo coordinates verified through Nominatim.
- The audit tool's public methodology and FAQ pages, fetched again before each audit.
- The rendered HTML of the deployed page (curl), used for every count.

Outputs:
- `app/site.ts` exporting `SITE_URL`, from which all absolute URLs derive.
- `app/llms.txt/route.ts`, `app/robots.ts`, a sitemap that includes legal pages, `public/.well-known/security.txt`.
- `next.config.ts` with AVIF/WebP formats, cache TTL and security headers including a CSP.
- One JSON-LD `@graph` in the layout, plus `FAQPage` in the page.
- A visible FAQ, visible `ol`/`ul` lists, footer signals (year, real social links, Google reviews link, legal links, update date).
- A `/conseils` page with an article and `Article` schema.
- An IndexNow key file and an `npm run indexnow` script.
- Before/after screenshots of the touched areas. The skill does not specify a report file.

## How it works

1. Set the target: three gates in order (Lighthouse scores, third-party audit >= 90, zero art-direction regression).
2. Lay the architecture before any code: `SITE_URL` centralised, `llms.txt` as a route handler.
3. Write metadata for the layout and each page; count title and description on the rendered HTML.
4. Build one JSON-LD `@graph` with entities linked by `@id`, respecting the documented NO-GO list.
5. Add visible signals: footer links and dates, visible FAQ, `tel:` and `mailto:` links, real heading hierarchy.
6. Create the `/conseils` Article page and also declare the Article in the home page `@graph` with `hasPart`, because the tool audits only the submitted URL.
7. Turn Q/A and lists into real elements on the audited page: `h3` inside `summary`, real `ol`/`ul` outside collapsed `details`, a factual Person entity.
8. Apply the technical layer: image formats, security headers and CSP, robots rules, security.txt, sitemap, font variable audit, IndexNow.
9. Run the pre-delivery checks: build, JSON-LD parsing on rendered HTML, Puppeteer on real Chrome, Lighthouse, screenshots.
10. Run the audit on a fresh URL: fetch the tool's methodology again to confirm the grid has not changed, change `SITE_URL`, build and deploy, add the versioned domain, run IndexNow, verify with curl, then hand over the URL.
11. If a score stagnates: rebuild the tool's grid from its methodology, verify it by exact recalculation of the obtained score, cross-check item by item against rendered HTML, fix only the unchecked items, audit again on a fresh URL.

## Human gates

The skill defines no formal approval checkpoint. The human touchpoints it states are:
- Every added signal must be invisible or validated (gate 3 of the target).
- The audit URL is handed over only after all checks on rendered HTML are green.
- Real data comes from the client and is never invented: opening hours are omitted if not supplied.
- When another audit tool is involved, its exact URL is requested from Sam.
- Bing Webmaster Tools and Bing Places remain manual.

## Autonomy

The skill file does not define guided, key checkpoints, autonomous or break_the_rules modes, and does not say how its behaviour changes between them. Its rules (no invented data, checks before handing over an audit URL) are written without reference to a mode.

## Hard rules and budgets

- Lighthouse SEO = 100, Accessibility >= 95, mobile Performance >= 90, measured best-of-3.
- Third-party audit >= 90.
- Title 30 to 70 characters, no em dash, counted with `wc -m`.
- Meta description 120 to 160 characters (the tool accepts 70 to 170), counted on rendered HTML.
- Exactly one `h1`, at least 2 `h2`, at least 300 words (legal pages excluded), alt text on at least 50 % of images.
- Visible FAQ of 6 to 8 questions placed after the CTA, with at least one list in an answer.
- Article page of about 800 words with byline, visible date, lists, internal links and cited external sources.
- JSON-LD NO-GO list: `contactPoint`, `areaServed`, `currenciesAccepted`/`paymentAccepted`, Product with Offer without price, self-declared `aggregateRating`.
- `openingHoursSpecification` only if hours are displayed on the site, in 2 ranges when there is a lunch break.
- CSP with `'unsafe-inline'`; `'unsafe-eval'` in dev only; HSTS not duplicated; zero CSP violation in the console.
- Images: AVIF and WebP, `minimumCacheTTL: 2678400`.
- Named robots rules for 12 listed crawlers plus a wildcard.
- IndexNow key of 32 hex characters.
- One fresh URL per audit, made public with `vercel domains add`, not `alias set`.
- SEO items checked again on rendered HTML after every design feedback loop.
- No composite score is guaranteed for a tool whose grid is unknown.

## Measured results

All figures are seaudit.fr scores stated in the skill, client names replaced by trade labels.
- The jeweller (reference project): 83 to 93 out of 100 in 4 iterations (Trust 100, Content 100, Performance 92, Technical 91, GEO 87).
- The property management firm: 95/100 on the first audit (Trust 100, Content 100, Performance 95, Technical 93, GEO 91), Lighthouse 95-98/100/100/100.
- The wine merchant: 95/100 on the first audit.
- Estate agency A: 89; GEO 76 when the Article existed only on a sub-page; Trust 100 with directory profiles in place of social networks.
- Estate agency B: 90 in 3 iterations; meta description of 167 characters gave Content 82, 144 characters gave 92; GEO 70 with lists only inside the FAQ accordion, +4 after moving lists outside it, +4 after adding a Person entity; GEO 66 after a design change removed the only visible lists.
- Missing date: Trust capped at 80; adding a visible date and the schema dates gave +20 points (80 to 100).
- PSI quota case: displayed 90 with the Performance axis empty, weighted recalculation on the other four axes 89.9.
- Fonts: 6 families shipped, 4 never used.

## Files

- `skills/seo-garantie-90/SKILL.md`: the whole playbook (target, grid summary, V1 checklist, validations, audit protocol, pre-delivery checks, documented mistakes, method when a score stagnates).

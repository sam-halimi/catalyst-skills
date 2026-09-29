# shopify-ecommerce-build

Builds or resumes a headless Next.js store on a VPS and Vercel connected to Shopify: catalogue, variants, cart, checkout state, separate Admin API tooling, emails, deployment and acceptance.

## What it does

The skill is a shared procedure for two agents: Claude builds the next store on the VPS, Codex makes targeted fixes. It lets either one work without redoing the Shopify connection or breaking functions already delivered.

It covers four topics, each in its own reference file: connecting a new Shopify store, the storefront architecture and features, build and publication operations, and one anonymised case (the watch store) with its real limits.

It separates presentation (photos, texts, sections, typography) from commerce (prices, stock, variants, cart, discounts). Shopify is the authority for every amount. The skill states that the next store reuses the procedures and the architecture, not the ids, keys, stock, secrets or commercial rules of the reference store.

## When it runs

- Skill name: `shopify-ecommerce-build`. No slash command is written in the skill files.
- Triggers stated in the description: building or resuming a Next.js store connected to Shopify, and preparing the Shopify connection of a new client store.
- Neighbouring skills named for the hero and lead capture: `scroll-frames-3d`, `popup-conversion`, `plinko-popup`.

## Inputs and outputs

Inputs:
- The real project and its instructions: CLAUDE.md/AGENTS.md, operations documents, package.json, dependency versions, current state.
- Store facts: canonical myshopify.com domain, owning organisation, store name, currency, markets, target channel, existing products, payment mode.
- Server-side environment variables: SHOPIFY_STORE_DOMAIN, SHOPIFY_STOREFRONT_ACCESS_TOKEN, SHOPIFY_API_VERSION, and the SHOPIFY_ENABLED and CHECKOUT_ENABLED flags.
- The authorizations given by Sam in the current thread.
- The official Shopify documentation, re-read at setup time.

Outputs:
- One site folder (`sites/site-<client>`) and one separate administration folder (`integrations/<client>-shopify`) per client.
- A new secrets directory, token cache, cookie secrets and isolated email storage per client.
- A catalogue map written before the components.
- A catalogue export taken before any Admin write. Mutations are GraphQL/variables files with a plan step before `--apply`.
- A timestamped targeted archive when the checkout has no Git.
- A Vercel deployment, with the real alias tested and the deployment id recorded.
- An updated project operations log and project markers, and a report that keeps what was not tested.

## How it works

1. Read the real project and its instructions. Identify the job: new store, data migration, Shopify hookup or fix. Replay only the missing decisions.
2. For a new connection, record the store facts and create the per-client folders, secrets directory, token cache and email storage.
3. Configure the Headless channel and the Storefront access, make products available on the channel, read catalogue and variants from Storefront and compare them with the Admin catalogue.
4. Set up Admin authentication server-side, then verify the scopes really granted with `auth-check`.
5. Import and map: read and export existing products first, map a stable presentation key to handle, SKU and option, fetch the real variant GIDs by reading.
6. Build the storefront: catalogue and product pages, server-side cart on the Storefront Cart API, checkout state, discounts, gifts, personalization, languages, currency display, email capture with consent.
7. Build and publish: `npm ci` on a fresh checkout, `npm test` then `npm run build`, check Vercel env names and targets without printing values, publish, test the real alias.
8. Run the acceptance list and keep untested items in the report.
9. Update the project operations log and markers. Synchronise the shared skill and compare SHA-256.

## Human gates

- Sam's current instructions override historical defaults.
- An authorization for one fix is not a general authorization for price, stock, email or product publication.
- Price and stock mutations happen only on explicit request, from ids that were read, with an export before the write, userErrors inspected and a re-read afterwards.
- A product publication or a channel change is not implied by a design change.
- Publication follows the authorization given in the thread.
- Before checkout opens, the merchant validates company and legal data, payment methods, shipping, markets, taxes, real stock and sales policy.
- An indicative currency conversion is built only when explicitly authorized.
- An authorization to update skills and memory for one cycle is not a perpetual one.

## Autonomy

The skill files name no autonomy mode (guided, key checkpoints, autonomous after art-direction GO, break_the_rules). Two related statements exist. An authorized fix does not require replaying the new-mission questionnaire. Art-direction onboarding rules apply to design decisions not yet taken, not to a repair already requested.

## Hard rules and budgets

- In Shopify mode a failure shows unavailability or an error and keeps the cart. No local price is invented and there is no silent return to demo mode.
- SHOPIFY_ENABLED and CHECKOUT_ENABLED are independent. Payment is not reopened during an unrelated deployment.
- No Admin key in NEXT_PUBLIC, in the frontend or in the site deployment. Secrets never appear in shell, logs, reports or screenshots.
- Admin token cache: atomic write, file mode 600, directory mode 700, early expiry of 60 s, renewal after a 401, redirects refused, exact HTTPS host.
- An existing client's Admin tool is never pointed at another store by changing its domain.
- A verified stable API version is pinned. `unstable` is never used in production.
- Environment is configured for Production and Preview. A `.env.local` on the VPS is not sent to Vercel.
- A colour change updates SKU, photo, price and availability together. The first available variant never replaces a sold-out choice.
- Cart cookie: HttpOnly, signed with a long secret. Client mutations are serialised. Checkout URLs are HTTPS on a validated host.
- No fictitious stock to pass a smoke test.
- A converted amount is display only, marked with `≈`, with the EUR reference in the cart. It is never sent to cart mutations or checkout.
- Mobile menus: 44 px targets, tested at a 320 px viewport.
- Lead storage: permissions 700/600, pinned private CA, no `rejectUnauthorized=false`, defined RPC actions only, SQLite copied with `sqlite3.Connection.backup`, never with `cp`.
- Builds never share one `.next` folder and never kill another site's processes.

## Measured results

All from the watch store case:
- Shopify API version verified on that project: 2026-07. Vercel CLI observed: 59.15.1.
- Scroll hero V2: 817 frames (409 originals, 408 optical intermediates), 48 fps master remuxed to 24 fps without re-encoding, media duration 34.041667 s.
- Desktop encode 1600x900, CRF 25, GOP 16: 6,971,216 bytes. Mobile encode 540x960, CRF 24, GOP 8: 4,211,187 bytes.
- Seven display currencies. Checkout remained closed.

## Files

- `skills/shopify-ecommerce-build/SKILL.md`: scope, routing to the references, precedence of current instructions.
- `skills/shopify-ecommerce-build/references/shopify-setup.md`: new store connection, Headless, Admin authentication, scopes, import and mapping.
- `skills/shopify-ecommerce-build/references/storefront.md`: sources of truth, catalogue, cart, payment, discounts, currency, emails, acceptance list.
- `skills/shopify-ecommerce-build/references/operations.md`: resume, Vercel build, skill synchronisation, lead storage operations.
- `skills/shopify-ecommerce-build/references/cas-boutique-horlogere.md`: the anonymised watch store case.

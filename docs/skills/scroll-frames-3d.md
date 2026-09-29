# scroll-frames-3d

Guide shared by Claude and Codex to create, fix and integrate a hero section whose video is scrubbed by page scroll: keyframes, clip joins, real frame density, WebP extraction or native video transport, loading, mobile and QA.

## What it does

- Covers media production: keyframes, N-1 clips for N keyframes, join correction, optical-flow densification, H.264 encoding, timestamp remux for delivery.
- Specifies the player: native MP4 source driven by seeks, index-to-time mapping, loader, reduced-motion path, suspend and resume, watchdogs, cleanup.
- Defines a QA protocol that separates initial delay, network behaviour and fluidity during a continuous scroll.
- Documents one reference case (the watch store, V2 fix) with its measurements and limits.
- Keeps an older technique (WebP frames drawn on a canvas, preload on first user gesture) in `references/historical.md` as context only. The skill states that it is superseded.
- States that it imposes no generated video, vendor or frame quota on other projects, and that it also guides a quick fix of an existing hero without relaunching the site design.

## When it runs

- Skill name: `scroll-frames-3d`. No slash command is written in the skill files.
- Trigger stated in the frontmatter: a travelling shot or a product reveal that was explicitly requested.
- Historical trigger (superseded): only when the narrative of the site carries a camera move, never as decoration.

## Inputs and outputs

Inputs:
- Project decisions, the validated master video and its manifest.
- Keyframes and generated clips (4 keyframes and 3 clips in the reference case).
- The project's private operations log (publication status, V2 measurements), external to the skill folder.
- ffprobe readings: dimensions, frame rate, exact frame count, duration, orientation, audio.
- Measured network and decoder behaviour, used to size the H.264 encode.

Outputs:
- A manifest listing files, dimensions, indices and provenance.
- A corrected master video and a report of the cuts.
- An interpolated master of 817 frames at 48 fps (409 originals at even indices, 408 optical intermediates).
- Delivery files `/hero-video-v2/desktop.mp4` (1600x900) and `/hero-video-v2/mobile.mp4` (540x960), remuxed to a 24 fps clock without re-encoding.
- A separate poster (index 0) and a static final image for reduced motion.
- Player code `lib/hero-video-player.ts`, used by `components/hero-scrub.tsx`.
- Verification scripts and JSON reports, kept in the private project repository.
- A final QA report: media and versions, URL tested, protocol, pixels, fluidity, menu and commerce checks, limits, backup.

## How it works

1. Read the project decisions, locate the validated master and the manifest. Do not regenerate if the existing edit is sufficient.
2. Inventory with ffprobe, keep the originals, name each keyframe and clip by its pair of bounds, fix one master format for all clips.
3. When generation is authorised: produce N-1 clips in order, passing keyframe x as the real start image and keyframe x+1 as the real end image. Keep the job id and wait for the final status.
4. Decode the real first and last frames and compare them to the keyframes. Inspect at least half a second on each side of every join. Keep one occurrence of a shared boundary frame. Realign geometrically before any cross-fade.
5. To densify an accepted edit: compute one optical intermediate between each of the 408 consecutive pairs, verify the count of 817 and the identity of the 409 originals, derive desktop and mobile from the same interpolated source.
6. Encode H.264 at 48 fps, then remux to a 24 fps delivery clock with `-c:v copy` and a bitstream filter that doubles timestamps. Prove parity with the framemd5 of all 817 decoded frames.
7. Implement or fix the player: single active seek, latest target replaces stale ones, loader removed only when the completed seek still matches the current target.
8. Run the QA file before publication: source and encoding, install and loading, seeks and resume, fluidity protocol, join pixels, intermediates, menus, a real browser.
9. Before editing the skill itself, compare the shared copy with the server copy and synchronise explicitly.

## Human gates

- Sam's current requests and arbitrations override every historical example.
- No purchase and no new generation without the authorisation that applies to that expense.
- Request parameters, model, format, duration, audio and quote are read again before the authorised run.
- The master edit is the one accepted by Sam. Interpolation is used only if requested and controlled.
- Historical (superseded): checkpoint with Sam on keyframes before any video generation.

## Autonomy

The skill files name no autonomy mode. They do not define guided, key checkpoints, autonomous after art-direction GO or break_the_rules behaviour, and do not say how the skill changes between them. The gates above are written without reference to a mode.

## Hard rules and budgets

- Raising the declared FPS or duplicating frames adds no motion. Only real intermediates add visual states.
- Index mapping `round(progress*(frameCount-1))`, range 0 to 816. Seek target `(index+0.5)/24`.
- Video is `muted`, `playsInline`, cover, with no linear `play()` and no `fastSeek`.
- Seek smoothing 55 ms. Direct jump when the player is not ready or the gap exceeds FPS/2 (12 indices).
- One stabilisation of 150 ms after first readiness, not added to first display, not repeated per seek.
- Watchdogs: initial 12 s, seek 2.5 s, armed after the `currentTime` setter returns.
- IntersectionObserver `rootMargin` of -64 px. Off hero or hidden tab: RAF and timers stopped, pause, `preload="none"`.
- Reduced motion: static final image in the HTML, no video player, no sequence download.
- Text animation offsets strictly increasing within [0,1].
- Desktop encode: 1600x900, CRF 25, GOP 16, no B-frames, preset slow, VBV maxrate 4.5 Mbit/s, bufsize 2.25 Mbit, yuv420p, `+faststart`.
- Mobile encode: 540x960, CRF 24, GOP 8, no B-frames, cropped 608x1080 at x=656, y=0 from the 1920x1080 source.
- Keyframes at indices 0/336/576/816, verified as I-frames with ffprobe.
- Shared boundary frames kept once: total n1+n2+n3-2, recomputed from decoded files.
- Asset paths are versioned whenever bytes change. Bytes and SHA are recorded for the encoded files.
- QA protocol: 0 to 816 over 10 s and 336 to 816 over 18 s, cold, at 10 Mbit/s with 100 ms latency and unthrottled. Desktop 1440x900 DPR 1, mobile 390x844 DPR 2.
- 160 ms wait after a seek before a pixel capture. An equal dataset index or `currentTime` is never a PASS.
- No iPhone FPS promise without a measurement on a physical device.
- Header menus: 44 px touch targets, panels inside a 320 px viewport.
- Historical (superseded): Performance best-of-5 >= 90, preload on first gesture with a 3.5 s fallback, DPR capped at 2, wrapper `h-[320svh]`, loader fade-out 450 ms.

## Measured results

All figures are stated in the skill files for the watch store, unless noted.
- Progressive WebP desktop before the fix: 7.201 s without a new draw during a 10 s traversal.
- First native desktop file of 14 MB: 181 presentations over 10 s, maximum pause 634 ms.
- Compact desktop file of 6.97 MB: 594 rVFC presentations over 10 s, maximum pause 33.6 ms, first image at 1.84 s (cold Chrome, 10 Mbit/s, 100 ms).
- After remux, desktop Chrome: first image 1.88 s, 592 presentations over 10 s, maximum pause 33.9 ms.
- After remux, mobile Chrome: first image 1.745 s, 474 distinct rVFC positions over the 18 s slow segment, maximum pause 93 ms. V1 gave 239 positions and 86 ms.
- Windows WebKit, unthrottled: 139 decoded positions over 10 s with two peaks of 275 and 325 ms, 271 positions over 18 s with a maximum of 186 ms.
- Isolated WebKit test, same 62 seeks: four pauses of about 5 s at 48 fps, maximum 71 ms after the 24 fps remux.
- Traversal with one RAF between seeks: 0 to 816 in 10.3 s, 228 seeks, maximum 117 ms. Without a render interval, one pause of 5,098 ms remains at frame 6.
- Remux parity: no difference in the framemd5 of the 817 decoded frames, mobile file 4.21 MB.
- Public startup: 7.815 s and 6.107 s on the first passes, then 1.193 s on a later navigation. The cause of the slow passes is not proven.
- No physical iPhone was tested.
- Historical, other projects: median Performance 85 to 92 with preload on first gesture, 719 frames instead of 360 after interpolation, 102 MB reduced to 45 MB with 1440 px and 30 fps.

## Files

- `skills/scroll-frames-3d/SKILL.md`: entry point, four steps, precedence rules.
- `skills/scroll-frames-3d/references/media.md`: inventory, generation, joins, densification, encoding, remux, WebP extraction.
- `skills/scroll-frames-3d/references/player.md`: player contract, mapping, seeks, lifecycle, loader, accessibility.
- `skills/scroll-frames-3d/references/qa.md`: QA protocol, measurements, public validation, menus.
- `skills/scroll-frames-3d/references/cas-boutique-horlogere.md`: anonymised reference case.
- `skills/scroll-frames-3d/references/historical.md`: superseded technique, kept as context.

# Ad Creative CTA Guidelines

This rule documents the call-to-action (CTA) and creative direction standards used
in the `tools/generate_ad_images.py` ad generation pipeline. Apply these principles
any time you add a new brand, write ad copy for an existing brand, or update the
`AD_SYSTEM_PROMPT` in the generator.

## CTA Best Practices

Every ad generated for this site follows these rules:

- **Action-oriented verbs.** CTA button or text must open with a verb: "Shop Now",
  "Get Yours", "Save Today". Never a noun or passive phrase.
- **Value proposition front-and-center.** The discount percentage or dollar amount
  must be one of the first readable elements. Do not bury it below the fold or
  in small type.
- **Urgency.** Include a time anchor ("Today", "Limited Time") to create a reason
  to act. Keep it honest — do not invent deadlines that do not exist.
- **Code visibility.** The discount code (`SIMEONONSECURITY`) must be a focal
  element of the ad. Display it as a coupon badge or pill. It is not an afterthought.
- **High contrast.** CTA text must stand out sharply against the background. Yellow
  (`#fbbf24`) on dark navy (`#111827`) is the house standard. Never low-contrast
  gray-on-gray or light-on-light.
- **Scannable in under two seconds.** One clear offer, one CTA, one code. No
  competing calls to action in the same ad unit.
- **Brand name always visible.** The brand name must appear as a readable element,
  not hidden in a logo alone.

## HTML Ad Partial Standards

Every brand ad partial (lazy, eager, eager-floating) must follow this structure:

- Discount code displayed with `color: #93c5fd` (light blue) on dark background.
- CTA text displayed with `color: #fbbf24` (yellow) as a `<strong>` element.
- Background for the CTA strip: `#111827` (near-black).
- Link uses `rel="noopener nofollow sponsored"` on all sponsor links.
- `title` attribute on the `<a>` tag names the brand, the product category, and
  the discount code.
- Lazy variants: `fetchpriority="low" loading="lazy"`.
- Eager variants: `fetchpriority="high" loading="eager"`.
- Floating variants: `position: fixed; bottom: 20px; left: 20px; z-index: 9999`.
  Hidden on viewports below 900px via `@media (min-width: 900px)`.

## Sentinel-Crop Pipeline

The image generation pipeline uses a sentinel-colour technique to handle extreme
aspect ratios (such as the 728×90 leaderboard banner):

1. The prompt instructs the image model to fill all canvas area outside the ad
   content band with solid bright-magenta `#FF00FF`.
2. After generation, PIL scans every pixel, finds the bounding box of all
   non-magenta pixels, and crops to that box.
3. The cropped image is resized to the exact target pixel dimensions.
4. Output is saved as WebP quality 85.

The sentinel colour `#FF00FF` must never appear in actual brand artwork or copy.

## Brand Color Palette (STS Collective product lines)

All three STS Collective product-line brands (RayHunter, FlockYou, Eye Spy) share
the STS Collective palette:

| Role    | Hex       | Usage                            |
|---------|-----------|----------------------------------|
| Primary | `#1a1a2e` | Ad content band background       |
| Accent  | `#f5a623` | Product highlights, borders      |
| CTA     | `#fbbf24` | `<strong>` CTA text in partials  |
| Code    | `#93c5fd` | Discount code text in partials   |
| Strip   | `#111827` | CTA strip background in partials |

## Adding a New Brand

When adding a new brand to `tools/generate_ad_images.py`:

1. Add an entry to the `BRANDS` list with keys: `slug`, `name`, `url`, `tagline`,
   `product_descriptor`, `audience`, `colors`, `discount`, `ads`.
2. `product_descriptor` must name what the brand sells in four to six words. It
   appears as a subtitle in the generated ad so viewers know immediately what the
   brand offers.
3. Create three HTML partials in `layouts/partials/ads/<parent-folder>/`:
   - `<slug>-lazy.html` — `fetchpriority="low" loading="lazy"`
   - `<slug>-eager.html` — `fetchpriority="high" loading="eager"`
   - `<slug>-eager-floating.html` — fixed position, 255×212 image, hidden below 900px
4. Add the lazy partial path to the `$ads` slice in
   `layouts/partials/ads/random-lazy.html`.
5. Run the generator to produce the WebP images:
   `.venv/bin/python tools/generate_ad_images.py --brand <slug>`
6. Commit the generated images in `assets/img/ads/<slug>/` alongside the partials.

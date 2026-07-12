# JSolution Limited — Website

A multi-page site for JSolution Ltd. (exclusive Kenyan distributor of Siesto
Green's encapsulated organic biofertilizers & biopesticides).

## Pages
- `index.html` — Home
- `about.html` — About, Mission/Vision, technology explainer, application steps, precautions
- `products.html` — Full filterable catalogue (24 items)
- `contact.html` — Contact form, details, Google Map
- `products/<slug>.html` — One dedicated page per product, each with its own
  "Order Now" form (name + phone, product name is prefilled as a hidden field)

## To finish the site
1. **Drop your image assets into `assets/img/`** using the exact filenames
   already referenced in the HTML (matching the names from your brief):
   logo, loading logo, hero video (`HERO-1.mp4`), all product images, and
   certification logos. Nothing else needs to change — every `<img>`/`<video>`
   tag already points at the right filename.
2. **Add your Web3Forms access key.** Every form (`contact.html` and every
   product order form) has an empty `<input type="hidden" name="access_key" value="">`
   — just paste your key into each `value=""`. Until then, forms show a
   friendly message asking the visitor to call/email directly instead of
   submitting.
3. Update the placeholder social links (`#`) in the header/footer once your
   social profiles are ready.
4. Optional: regenerate all 24 product pages any time by editing the
   `PRODUCTS` list in `build.py` and running `python3 build.py` — this
   rebuilds every page from the shared templates so header/footer/styling
   always stay in sync.

## Design notes
- Colors come straight from your `colors.txt` (dominant green `#06a750`,
  lime `#85c440`, teal `#44a6af`), extended with a deep forest tone for
  grounding and a soil-amber accent used only for the Kits category.
- The recurring two-tone pill/capsule shape (dividers, category tags, stat
  markers) is the site's signature motif, echoing the encapsulation
  technology itself.
- Fully responsive, with a mobile slide-in menu, scroll-reveal animation,
  and `prefers-reduced-motion` support.

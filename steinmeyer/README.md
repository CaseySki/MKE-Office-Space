# The Steinmeyer Building — Marketing Site

Standalone single-page site telling the history of the Steinmeyer Building (205 West
Highland Avenue, Milwaukee) and marketing it for lease. Self-contained — no build step,
no dependency on the Ogden `site/` or `template/` folders in this repo.

## Preview locally

```bash
cd steinmeyer
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Structure

- `index.html` — all sections (Hero, History, Architecture, Spaces, District, Leasing, Footer)
- `css/style.css` — all styles
- `js/main.js` — mobile nav, "click to hear the inscription" (uses the browser's built-in
  Web Speech API, no audio file needed), the district Leaflet map, and the inquiry form
- `images/` — empty; see "Replacing placeholder photos" below

## Replacing placeholder photos

Every photo slot is currently a styled placeholder block (`<div class="photo ...">`) with
a caption describing exactly what should go there, e.g. *"Photo placeholder — Steinmeyer
Building corner facade, Highland Ave & Old World 3rd St."* This environment couldn't
download images directly, so real photos need to be dropped in by hand:

1. Save a real photo into `steinmeyer/images/` (e.g. `exterior-corner.jpg`).
2. Find the matching `<div class="photo photo--...">` in `index.html` and replace it with
   an `<img>` tag, e.g.:
   ```html
   <img src="images/exterior-corner.jpg" alt="Steinmeyer Building corner facade">
   ```
3. Delete the placeholder's `<span class="photo-caption">` (or keep it as a figcaption if
   you want the caption to stay visible).

Sources worth checking for real, usable photos of the building:

- Milwaukee Public Library historic photo collection — [Steinmeyer Building in the 1980s](https://content.mpl.org/digital/collection/HstoricPho/id/838/), [Remember When... Milwaukeeans shopped at Steinmeyer's?](https://content.mpl.org/digital/collection/RememberWhe/id/454/)
- [Wisconsin Historical Society — W.M. Steinmeyer Co. photograph](https://www.wisconsinhistory.org/Records/Image/IM47746)
- [John December's MKE photo album](https://johndecember.com/places/mke/album/steinmeyerbuildingphotos.html) — modern exterior/detail shots
- [HMdb.org historical marker page](https://www.hmdb.org/m.asp?m=43013) — marker + building photos
- [Urban Milwaukee building profile](https://urbanmilwaukee.com/building/steinmeyer-building/)
- Ogden & Company's own leasing brochure for this building (check with the leasing team) —
  likely the best source of current interior/exterior photos

Check licensing/permission before publishing any third-party photo commercially; several
of the above are archival/public collections but terms vary by source.

## Notes

- Fonts (Fraunces, Inter) load from Google Fonts CDN; the district map uses Leaflet 1.9.4
  + CARTO tiles from unpkg/CDN — same pattern as the main Ogden site. These didn't load in
  this sandboxed environment (outbound network is restricted here), but will work fine for
  real site visitors.
- The inquiry form has no backend — it currently just shows a confirmation message on
  submit. Wire it to a real endpoint (Formspree, a mailto, a Sheets webhook, etc.) before
  launch.
- Leasing contacts (Luke Fehrenbach, Richard Reinders) and the Ogden & Company tagline were
  pulled from `site/data/contacts.json` and `site/index.html` for consistency — update if
  a different broker should be listed for this property.

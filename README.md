# Yellow Squiggles Are People

A 5-minute lightning talk about web accessibility — specifically, what one ESLint `jsx-a11y` warning revealed about who gets locked out of inaccessible UI.

Delivered to the Dev Academy cohort on **Friday 2026-05-22** by Serina McFall.

## The pitch

A real moment with a yellow ESLint squiggle on a `<div onClick>` opens a 5-minute talk about who gets locked out of inaccessible UI, the three-piece fix, and why "just use native HTML" is the best advice — framed by the speaker's own experience as a dyslexic developer who values squiggle-free code.

## What's in this repo

| Path | What it is |
|------|------------|
| [`design.md`](design.md) | Full talk design — outcome, structure, slide-by-slide content, accessibility meta-rules, scope discipline |
| [`speaker-script.md`](speaker-script.md) | The words spoken on stage |
| [`slides-build-sheet.md`](slides-build-sheet.md) | Visual and layout brief for each slide |
| [`build_deck.py`](build_deck.py) | Script that builds the Google Slides deck via the `gws` CLI |
| [`code-samples/`](code-samples/) | Broken-on-purpose React and ESLint examples used in slide screenshots |

## The code samples

Each file in [`code-samples/`](code-samples/) is meant to **show** an accessibility problem (or its fix) in screenshots — not to ship to production:

- `ClickyDiv.tsx` — the broken `<div onClick>` example (Slide 2)
- `ClickyDivFixed.tsx` — the same logic with `role="button"`, `tabIndex`, and `onKeyDown` (Slide 4, left)
- `JustAButton.tsx` — the better way: a native `<button>` (Slide 4, right)

Setup instructions live in [`code-samples/README.md`](code-samples/README.md).

## Building the deck

The Google Slides deck is built programmatically by [`build_deck.py`](build_deck.py) using the `gws` (Google Workspace) CLI against a fixed presentation ID. The script is idempotent at the API level — re-running it on the same presentation will fail with "already exists" errors. To rebuild cleanly, create a new presentation and update `PRESENTATION_ID`.

## Why "Yellow Squiggles Are People"

> Yellow squiggles aren't nitpicks. They're people.
>
> Your future user. Your future self. Better software.

## References

- MDN — [ARIA button role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/button_role)
- MDN — [tabindex](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex)
- [eslint-plugin-jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y)
- W3C WAI — [APG Button Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/)

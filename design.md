# Lightning Talk Design — "Yellow Squiggles Are People"

**Date:** 2026-05-22 (Friday)
**Speaker:** Serina McFall
**Length:** 5 minutes
**Audience:** Dev Academy cohort + facilitators
**Topic:** Web accessibility — specifically, what one ESLint `jsx-a11y` warning revealed about excluding users with disabilities.

---

## One-line pitch

A real moment with a yellow ESLint squiggle on a `<div onClick>` opens a 5-minute talk about who gets locked out of inaccessible UI, the three-piece fix, and why "just use native HTML" is the best advice — framed by the speaker's own experience as a dyslexic developer who values squiggle-free code.

## Outcome

By the end of 5 minutes, the audience should walk away with:

1. **One sticky line** — *"Yellow squiggles aren't nitpicks. They're people."*
2. **One sticky habit** — reach for `<button>` (and other native HTML elements) before reaching for `<div>`.
3. **One sticky reason** — three concrete groups of real people get locked out when you don't.

---

## Structure (story-driven)

| Time | Beat | Slide | Talking thrust |
|------|------|-------|----------------|
| 0:00–0:30 | **The squiggle** | Title + speaker name | "Last week I was doing the React state kata. Made a clickable div. Got a yellow squiggle. It bugged me — and that led me down a rabbit hole. Spoiler: it wasn't a nitpick." |
| 0:30–1:30 | **Why squiggles bug me** | Screenshot: editor showing yellow squiggle on `<div onClick>`. Note about Lexend / dyslexia-friendly setup. | "I'm dyslexic. Reading code is hard. Yellow and red squiggles drain my focus, so I keep my editor squiggle-free — and that means I have to learn what the squiggles are telling me." |
| 1:30–3:00 | **Who got locked out** | Three personas, one icon + one sentence each: keyboard user, screen reader user, switch / eye-tracking user | "When you put `onClick` on a `<div>` without keyboard support, three groups get locked out: keyboard users (motor disabilities, RSI, broken mouse) — can't even Tab to it; screen reader users — a `<div>` isn't announced as interactive; switch + eye-tracking users — they all work through the keyboard layer." |
| 3:00–4:00 | **The fix** | Code: three pieces — `role="button"`, `tabIndex={0}`, `onKeyDown` handler for Enter/Space — then a big arrow pointing to a single `<button>` | "Three-piece fix. OR: just use `<button>`. Native HTML already does all this for you. Reach for `<div>` **last**, not first." |
| 4:00–5:00 | **Why this matters** | Single statement, large type: *"Yellow squiggles aren't nitpicks. They're people."* | "Me having dyslexia is what made me notice. But every developer should care — your future user, your future self, your future product. Empathy is a developer skill." |

---

## Slide-by-slide content

### Slide 1 — Title

- **Title:** Yellow Squiggles Are People
- **Subtitle:** What one ESLint warning taught me about who I was excluding
- **Speaker:** Serina McFall · Dev Academy · 2026-05-22

### Slide 2 — The squiggle

- **Screenshot:** VS Code (or editor of choice) showing a `<div onClick={...}>` with the yellow `jsx-a11y` underline
- **Caption:** *"This is a yellow squiggle. It bugged me, and I had to know why."*

### Slide 3 — Three locked-out groups

Three columns or rows, each with:

- **Icon** (simple, high-contrast)
- **Who they are** (one short phrase)
- **What breaks for them** (one short phrase)

| Persona | Who | What breaks |
|---------|-----|-------------|
| Keyboard-only | Motor impairment, RSI, broken mouse | Can't Tab to a `<div>` |
| Screen reader | Blind, low-vision | A `<div>` isn't announced as interactive |
| Switch / eye-tracking | Severe motor impairment | These work through the keyboard layer |

### Slide 4 — The fix

Top half — the three-piece manual fix:
```jsx
<div
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) => (e.key === 'Enter' || e.key === ' ') && handleClick()}
>
  Click me
</div>
```

Bottom half — the better way:
```jsx
<button onClick={handleClick}>Click me</button>
```

With a big arrow or "OR" between them. The takeaway line on the slide: **"Use native HTML first. Reach for `<div>` last."**

### Slide 5 — Close

- **Big statement:** *"Yellow squiggles aren't nitpicks. They're people."*
- **Small footnote:** "Future user. Future self. Better software."

---

## Meta-rule: the slides themselves must be accessible

This is the meta-credibility check. Walking the talk while giving the talk.

- **Body font:** Lexend or Atkinson Hyperlegible. Big — minimum 24pt for body, 36pt+ for headings.
- **Contrast:** WCAG AA minimum (4.5:1 for body, 3:1 for headings). Test with a contrast checker.
- **Alt text:** Every image, screenshot, and icon has meaningful alt text. Describe what the image *shows*, not "image of…" / "screenshot of…".
- **No flashing animations.** Respect `prefers-reduced-motion` if the tool supports it.
- **Descriptive slide titles.** Each slide title makes sense out of context.
- **Code is readable.** Big enough to read from the back, syntax-highlighted with sufficient contrast.

---

## What's intentionally NOT in the talk (scope discipline)

- ARIA beyond `role="button"` (other roles are a rabbit hole)
- WCAG levels A/AA/AAA (interesting but eats time)
- A list of every assistive technology that exists (the three personas cover the principle)
- A tour of NZ legal requirements (different talk)
- A live demo (decided against — too risky for a 5-min slot)

---

## Locked-in decisions

- **Slide tool:** Google Slides (recommended by Dev Academy)
- **Title:** "Yellow Squiggles Are People" — confirmed
- **Icon set:** Lucide (free, accessible, simple SVG downloads from lucide.dev — works as Insert → Image in Google Slides)

## Open for implementation phase

1. **Screenshot source?** Real screenshot of Serina's own editor showing the squiggle on her React state kata code (most authentic) vs. a clean reproduction.
2. **Rehearsal plan?** How many run-throughs before Friday, with whom (husband per the 4-step protocol? Cohort buddy?).

---

## Related references

- The original Discord post (Serina's own writing, this talk's seed)
- MDN — [ARIA button role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/button_role)
- MDN — [tabindex](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex)
- [eslint-plugin-jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y)
- W3C WAI — [APG Button Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/)

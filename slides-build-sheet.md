# Slides Build Sheet — Google Slides

Follow this like a checklist. Open Google Slides, create a new blank presentation, set the theme/font/colours first (Step 0), then build slide by slide.

---

## Step 0 — Set the deck-wide defaults

**Theme:** Blank / Simple.

**Fonts** (Insert → Header & footer area, or via Slide → Theme):
- **Headings:** Atkinson Hyperlegible Bold (or Lexend Bold) at 40–48 pt
- **Body:** Atkinson Hyperlegible or Lexend at 24–28 pt
- **Code:** JetBrains Mono or Fira Code at 22–24 pt

If Atkinson Hyperlegible isn't in Google Fonts directly, use **Lexend** as fallback — both are dyslexia-friendly.

**Colours** (high contrast — pick one of these palettes):
- Light: background `#FFFFFF`, text `#1A1A1A`, accent `#FFB300` (squiggle yellow!)
- Dark: background `#1A1A1A`, text `#F5F5F5`, accent `#FFB300`

**Slide size:** Default 16:9 widescreen.

**Animation:** None. (Respect `prefers-reduced-motion` ethos even though Google Slides doesn't honour it directly.)

---

## Slide 1 — Title

**Layout:** Title slide (centred).

**Text:**
- Title (large): **Yellow Squiggles Are People**
- Subtitle (smaller): *What one ESLint warning taught me about who I was excluding*
- Footer (small, bottom): Serina McFall · Dev Academy · 22 May 2026

**Visual:** Optional — a small yellow squiggle underline graphic under the title. You can draw one with the line tool (squiggle shape) or use the `wavy underline` from inserted symbols.

**Alt text (for any decorative graphic):** Mark as decorative.

---

## Slide 2 — The squiggle (screenshot slide)

**Layout:** Title at top, large image below.

**Title text:** *Last week, this happened.*

**Visual:** **Screenshot of broken `<div onClick>` code with the yellow squiggle visible in your editor.**

### How to capture the screenshot

The broken-code file lives at `code-samples/ClickyDiv.tsx` in this folder. First-time setup (run once):

```bash
cd /home/serina/Dev-Academy/projects/lightning-talk-accessibility/code-samples
npm install
```

Then to screenshot:

1. Open `code-samples/` in VS Code (`code .` from inside the folder)
2. Open `ClickyDiv.tsx`
3. Wait a second or two — the yellow `jsx-a11y` squiggle should appear under `<div`
4. Screenshot with Greenshot / Snip & Sketch — just the code block with squiggle visible
5. Save the screenshot

The folder stays in place for future talks/demos that need the same example — no rebuild needed.

**Alt text for the screenshot:** *"VS Code showing a clickable div component with a yellow ESLint warning underline."*

---

## Slide 3 — Who got locked out

**Layout:** Three equal columns OR three rows. Each cell has: icon (top/left), person name (heading), one-line explanation (body).

### Column / Row 1 — Keyboard users

- **Icon:** keyboard (Lucide → `keyboard`. Download SVG from [lucide.dev](https://lucide.dev) and insert as image.)
- **Heading:** Keyboard users
- **Body:** Motor impairments, RSI, broken mouse. **Can't Tab to a `<div>`.**

### Column / Row 2 — Screen reader users

- **Icon:** speaker / accessibility (Lucide → `accessibility` or `speaker`)
- **Heading:** Screen reader users
- **Body:** Blind, low-vision. **A `<div>` isn't announced as interactive.**

### Column / Row 3 — Switch & eye-tracking users

- **Icon:** eye or scan (Lucide → `eye` or `scan-line`)
- **Heading:** Switch & eye-tracking users
- **Body:** Severe motor impairments. **All work through the keyboard layer.**

**Alt text for each icon:** Describe what the icon depicts — e.g., *"A simple line drawing of a keyboard"* — not "icon of…" / "image of…".

---

## Slide 4 — The fix

**Layout:** Two stacked code blocks with a big arrow or "OR" between them.

### Top half — The three-piece fix

**Caption above the code:** *Or you can do this…*

**Code block:**

```jsx
<div
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) =>
    (e.key === 'Enter' || e.key === ' ') && handleClick()
  }
>
  Click me
</div>
```

### Middle — The pivot

A large arrow pointing down, OR the word **"OR"** in big type in a yellow accent box.

### Bottom half — The right way

**Caption above the code:** *…or you can just do this.*

**Code block:**

```jsx
<button onClick={handleClick}>Click me</button>
```

**Big takeaway line at the bottom of the slide:** **"Use native HTML first. Reach for `<div>` last."**

---

## Slide 5 — Why this matters / Close

**Layout:** Almost-empty slide with one big statement, centred.

**Big text (large heading):**

> **Yellow squiggles aren't nitpicks.**
> **They're people.**

**Small footer text (subtle, bottom):**

*Your future user. Your future self. Better software.*

**Optional:** Your name + a contact / GitHub handle in the very bottom corner if you want people to reach out after.

---

## Accessibility sanity check before you finish

Run through this list once the deck is built:

- [ ] All fonts are Atkinson Hyperlegible / Lexend / JetBrains Mono — no Times, no Comic, no Arial body
- [ ] All body text is at least 24 pt; all headings 36 pt+
- [ ] Contrast checked on every slide (use [WebAIM contrast checker](https://webaim.org/resources/contrastchecker/) with your background + text hex codes — aim for 4.5:1 minimum)
- [ ] Every image has alt text (right-click image → Alt text → write a description WITHOUT the words "photo / image / picture")
- [ ] Decorative shapes/squiggles marked as decorative
- [ ] No flashing or auto-advancing animations
- [ ] Every slide title is descriptive and makes sense out of context
- [ ] Code on slides is big enough to read from the back of the room
- [ ] Test in **Presenter View** to check timing fits 5 minutes

---

## When you've built each slide

Take a screenshot and drop it in here. I'll review for accessibility, layout, copy fit, and whether it matches the script's pacing.

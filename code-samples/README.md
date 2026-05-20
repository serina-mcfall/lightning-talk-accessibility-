# Code samples — Yellow Squiggles Are People

Broken-on-purpose code used as visual examples in the lightning talk. Each file is meant to **show** an accessibility problem (or its fix) in screenshots — not to run in production.

## Setup (first time only)

```bash
cd /home/serina/Dev-Academy/projects/lightning-talk-accessibility/code-samples
npm install
```

This installs ESLint + `eslint-plugin-jsx-a11y` locally so the yellow squiggles actually appear when you open these files in VS Code.

## Taking a screenshot

1. Open this `code-samples/` folder in VS Code (`code .` from inside it)
2. Open `ClickyDiv.tsx`
3. Wait a second or two — yellow squiggle should appear under `<div` (the `jsx-a11y/click-events-have-key-events` rule firing)
4. Screenshot with Greenshot / Snip & Sketch
5. Save the image somewhere useful — e.g. drop a folder called `screenshots/` alongside this README

## Files

- **`ClickyDiv.tsx`** — the broken `<div onClick>` example. Used in Slide 2 of the talk.
- **`package.json`** — minimal devDeps to enable linting.
- **`eslint.config.js`** — flat config that activates `jsx-a11y` recommended rules.

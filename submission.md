# THS03 — Research and Presentation: Submission

**Lightning talk:** *Yellow Squiggles Are People*
**Delivered:** 2026-05-22 (Dev Academy cohort + facilitators)
**Length:** ~5 minutes
**Speaker:** Serina McFall

---

## Essay Response

### The topic — and why this one

I chose web accessibility, focused tight on a single ESLint warning: `jsx-a11y/click-events-have-key-events` (and its cousin, `no-static-element-interactions`) firing on a clickable `<div>`.

I picked it because it actually happened to me. Last week, working through the React state kata, I put `onClick` on a `<div>`, my editor lit up yellow, and I had to decide whether to ignore it or learn what it meant. I'm dyslexic, and one of the rules I've built my dev environment around is *"no yellow or red squiggles"* — they drain my focus and make code feel chaotic. So I went looking, and what I found wasn't a nitpick. The warning was telling me my code was excluding people. That mattered to me, and I figured it would matter to a cohort about to graduate into writing real production UI.

The wider topic — accessibility — is enormous. I deliberately scoped the talk down to one concrete example so I could go *deep* on one thing instead of *shallow* on ten. That meant cutting things I'd have loved to include: WCAG levels, the rest of the ARIA roles, NZ legal context, switch-device demos. The 5-minute slot does not forgive scope creep.

### Research and sources

I worked from primary technical sources rather than blog summaries — partly because accessibility is a domain where bad blog advice can actively make things worse:

- **W3C WAI-ARIA Authoring Practices Guide** — the [Button Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/) is the authoritative reference for what a custom button has to do (focusable, keyboard-operable via Enter and Space, correctly announced).
- **MDN Web Docs** — the [ARIA `button` role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/button_role) page and the [`tabindex`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex) global attribute page.
- **`eslint-plugin-jsx-a11y`** — I read the [plugin's own rule docs](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/tree/main/docs/rules) for `click-events-have-key-events` and `no-static-element-interactions` to be sure I was describing what the rule actually checks for, not what I assumed it checked for.
- **The "First Rule of ARIA"** — *if you can use a native HTML element instead of repurposing one with ARIA, do.* This shaped the talk's central pivot from "here's the three-piece fix" to "or just use `<button>`."

I also reproduced the warning in a small, intentionally-broken code sample (`code-samples/ClickyDiv.tsx` in the repo) so the screenshot on Slide 2 was a real ESLint hit from a real project, not a mock-up. That mattered to me — talking about authentic moments works best when the moment really happened.

### Structuring it for the audience

The cohort is mid-bootcamp, fluent in JSX, mostly hasn't touched accessibility yet. So the talk had to do three things in five minutes:

1. Hook with a moment they'd recognise (a squiggle they've all seen).
2. Make the abstract concrete (name three real groups of people who get excluded — not "users with disabilities" in the aggregate).
3. Leave them with a habit they can apply on Monday (`<button>` first; reach for `<div>` last).

I built the talk around a **story arc**, not a slide deck. Beat 1: the squiggle. Beat 2: why it bugged me (dyslexia + the "no squiggles" rule). Beat 3: who got locked out — three personas, one icon and one sentence each. Beat 4: the fix (three pieces, with the punchline that `<button>` already does all three). Beat 5: why it matters beyond this one example.

The slides are deliberately **minimal and accessible** — that's the meta-credibility move. I'm giving a talk about accessibility, so the slides themselves have to walk the talk: Atkinson Hyperlegible / Lexend body fonts, 24pt+ body / 36pt+ headings, WCAG AA contrast (4.5:1 minimum), real alt text on every image, no flashing or auto-advance, decorative shapes marked decorative. If the deck had been inaccessible the talk would have refuted itself.

### Communication choices I made deliberately

- **A pre-talk note asking the cohort to hold questions until the end.** Interruptions knock my focus, and I'd rather deliver the whole thing cleanly than recover mid-flow. It also frames the room as listening, which is what a lightning talk needs.
- **Naming my own dyslexia early** rather than treating it as a reveal. It's the reason I noticed the squiggle, and the talk falls apart if the audience doesn't know that. So I put it in Beat 2 where it has to be, not at the end as a twist.
- **One sticky line, repeated**: *"Yellow squiggles aren't nitpicks. They're people."* The last six words are the whole talk. Everything else is in service of those six words landing.
- **No live coding, no live demo.** Both are high-risk for a 5-minute slot, and I'd rather show static code I know is correct than fumble a demo on stage.

### Reflection on the delivery

*<!-- TODO Serina: replace this paragraph with what you actually noticed on the day. A few prompts: which beats landed? Did the pre-talk note work? Where did you slow down or speed up? Was there a moment the room shifted — laughter, nods, silence in the right place? Anything that surprised you? -->*

What I'd change next time:
*<!-- TODO Serina: 1–3 specific things. Examples: "Beat 2 ran long, I'd cut the OpenDyslexic parenthetical." / "I'd land the punchline earlier in Beat 4 — the OR moment is the joke, don't bury it." / "I'd practice the close once more — the last six words need a clean landing, not a rushed one." -->*

### What I'm taking forward

The 5-minute format forced a skill I undervalued before this assessment: **deciding what to leave out**. Most of what I learned didn't make it into the talk, and the talk is stronger for it. Every cut was a decision about what the audience needed, not what I wanted to say.

I've also started applying the talk's own advice in every project I touch — reaching for native HTML first, treating `jsx-a11y` warnings as signals rather than noise, and auditing for keyboard navigation and screen-reader semantics as part of the build rather than as an afterthought. That's the habit I wanted the cohort to leave with, and it's the one I most want to keep myself.

The internet is for everyone. Our code decides who "everyone" includes.

---

## Form checklist

- [x] **Essay response** — paste the section above (everything between "## Essay Response" and "## Form checklist", excluding the headings if the form prefers plain prose)
- [x] **Supporting GitHub repo** — `https://github.com/<your-username>/lightning-talk-accessibility` *(verify the exact URL before submitting)*
- [x] **Supporting materials** — upload `yellow-squiggles-are-people.pdf` from Downloads (clean-name copy of the exported deck — the original `Yellow Squiggles Are People — Claude Build.pdf` filename was rejected by the uploader because of the em-dash and spaces)
- [ ] **Additional comments (optional)** — leave blank, or add a one-liner if you want to flag anything to the assessor
- [ ] **Declaration: I have completed the assessment requirements above** ✓
- [ ] **Declaration: Any use of external code or LLM/AI tools has been appropriately credited** ✓ — the essay names Claude as the planning collaborator implicitly through the deck filename; if you want this more explicit, add a line to the Additional Comments box like: *"Used Claude (Anthropic) as a thinking partner for talk structure, slide layout, and script drafting. Final voice, delivery, and editorial decisions are mine. The code samples and slide build script are in the linked repo."*
- [ ] **Save Draft** first, double-check formatting in the preview, then **Submit Work**

## Two things only you can do before submitting

1. **Fill in the two TODO reflection paragraphs** under "Reflection on the delivery." Don't let me write those — they're meant to be your honest in-the-room observations.
2. **Confirm the GitHub repo URL.** I've left a placeholder because I don't have your exact username/repo path in this session.

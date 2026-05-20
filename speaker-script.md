# Speaker Script — "Yellow Squiggles Are People"

**Length:** ~5 minutes at conversational pace (~120 wpm). Total ~620 words.
**Voice:** Conversational, direct, real. Adapt to your own phrasing — this is a starting draft, not a final script. Where it feels too "Claude" and not enough "Serina", change it.

**Stage direction notes:**
- `[…]` are beat markers and slide cues.
- **Bold** = words to emphasise.
- "…" = pauses worth taking.

---

## Pre-talk note (deliver on Slide 1 before Beat 1)

**[~10 seconds · Set the ground rules]**

Quick note before I start — please save any questions or comments for the end. Interruptions don't sit well with my focus and can knock me off my place, and I'd rather get through this cleanly. Thanks.

---

## Slide 1 — Title

**[BEAT 1 · 0:00–0:30 · The squiggle]**

Last week I was working through the React state kata. And I made a mistake — I put `onClick` on a `<div>`. Probably more than once. And every time, my editor showed me this little yellow squiggle from ESLint.

I had two choices. Ignore it. Or figure out what it was telling me.

I'd like to tell you I figured it out because I'm a careful, principled developer. But honestly? **It bugged me.** And that turned out to matter more than I expected.

---

## Slide 2 — The squiggle (screenshot)

**[BEAT 2 · 0:30–1:30 · Why squiggles bug me]**

So — about why it bugged me.

Some of you may remember my Discord post from last Thursday — this is the moment behind it. Yellow squiggle lines.

I'm dyslexic, so reading code is difficult for me most of the time. I've built my whole dev environment around making it easier — Lexend font (when OpenDyslexic isn't available), themes I can read, extensions that highlight things I'd miss. One of the most important rules I've made for myself is: **"No yellow or red squiggles."** They drain my focus, cause real frustration — I really dislike messy code.

Which means when one appears, I have to fix it. And to fix it, I need to know what's causing it.

So I looked it up. It was an `eslint-plugin-jsx-a11y` warning. The `a11y` bit is short for *accessibility* — eleven letters between a and y. And it was telling me my clickable `<div>` was excluding people.

Not "could potentially inconvenience some users." **Excluding. Locking out.**

For me, that breaks one of my core values — making sure no one is excluded by the code I build. So… let me show you who.

---

## Slide 3 — Three locked-out groups

**[BEAT 3 · 1:30–3:00 · Who got locked out]**

Here's who.

**Keyboard users.** People with motor impairments, repetitive strain injuries, or who just have a broken mouse. They navigate by pressing Tab to move through interactive elements. A `<div>` isn't interactive by default — you can't Tab to it. So even if they can *see* your button, they can't *reach* it.

**Screen reader users.** Blind and low-vision folks who hear the page read aloud. Screen readers announce things like "button, click me" or "link, learn more." A `<div>` gets announced as… nothing. It's invisible to them as an interactive element. They don't know it does anything.

**Switch device and eye-tracking users.** People with severe motor impairments who can't use a regular keyboard or mouse. Their tech works *through* the keyboard layer — pressing Tab, pressing Enter. No keyboard support means no access. At all.

Three groups. Real people. Locked out by one missing attribute on a `<div>`.

---

## Slide 4 — The fix

**[BEAT 4 · 3:00–4:00 · The fix]**

The fix has three pieces. You add `role="button"` so screen readers know what it is. You add `tabIndex={0}` so keyboard users can Tab to it. And you add an `onKeyDown` handler that listens for Enter and Space, because those are the keys people expect to "click" with.

Three pieces. It works.

… OR.

You can just use `<button>`.

`<button>` already has all three. So does `<a>` for links. So does `<label>` for inputs. Native HTML elements have been doing this for decades. They're not exciting, but they're the right tool.

So the real takeaway isn't *"here's how to fix a clickable `<div>`."* It's: **reach for `<div>` last, not first.** If a native element exists for what you're building, use it.

---

## Slide 5 — Why this matters

**[BEAT 5 · 4:00–5:00 · Why this matters]**

Me having dyslexia is what made me notice the squiggle. But you don't need to have an impairment to care about this.

Three reasons.

**One** — it might be your future user. The internet is for everyone, and your code decides who "everyone" includes.

**Two** — it might be your future self. RSI. Eye strain. A broken arm. A baby in the other hand. Accessible code helps people whose abilities change. That's all of us, eventually.

**Three** — it's just better software. Native HTML is more reliable, more searchable, more maintainable. Accessibility isn't an extra. It's craft.

I've started implementing this in every project I work on. And honestly — it makes me a better developer. And, I think, a better human.

So next time you see a yellow squiggle, don't ignore it. Don't disable the rule. **Read it.** Because yellow squiggles aren't nitpicks.

They're people.

… Thanks.

---

## Timing checks (updated 2026-05-17 after Serina's Beat 2 rewrite + pre-talk note)

- Pre-talk note: ~10 seconds (~30 words)
- Beat 1: ~30 seconds (~75 words)
- Beat 2: ~85 seconds (~190 words) — longer than the original draft; carries Serina's voice and Discord callback
- Beat 3: ~90 seconds (~180 words)
- Beat 4: ~60 seconds (~145 words)
- Beat 5: ~80 seconds (~180 words) — picks up the moved closing-reflection lines

**Total: ~800 words / ~5:35.** This is **over** the 5:00 lightning-talk slot by ~35 seconds. Rehearse it and decide what to trim. Cuttable bits, in order of "easiest first":

1. **"I'd like to tell you I figured it out because I'm a careful, principled developer."** (Beat 1) — saves ~10 seconds
2. **"(when OpenDyslexic isn't available)"** parenthetical (Beat 2) — saves ~3 seconds
3. **"eleven letters between a and y"** aside (Beat 2) — saves ~5 seconds
4. **"Native HTML is more reliable, more searchable, more maintainable."** (Beat 5) — saves ~5 seconds
5. The opening sentence of Beat 5 — saves ~8 seconds

Cutting 1 + 2 + 3 alone brings you to ~5:07. Cut 4 as well and you hit ~5:02. The 5-minute slot usually has some flex; don't strangle the talk to hit exactly 5:00.

## Adapting it to your voice

Beat 2 is now in Serina's own voice (rewritten 2026-05-17). Beats 1, 3, 4, 5 are still mostly the original draft — pass through them once and:
- Cross out anything that doesn't sound like you say it
- Swap in your own phrasings
- Mark where you'll pause for breath
- Mark where you'll look at the audience vs. the screen

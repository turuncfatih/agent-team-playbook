# Handoff: `content-writer` → `frontend-dev`

## Fixed

```
Format          Markdown, keyed by slot — one slot per line
Slots           hero.heading · hero.subheading · hero.cta
                section.<n>.heading · section.<n>.body
                state.empty · state.error
                meta.title (≤ 60 chars) · meta.description (≤ 155 chars)
Voice           Set by the brand inputs; not open to adjustment in markup
Heading order   The copy file's heading levels are the page's heading levels
```

## Open

- Which markup element carries each slot, as long as heading level is preserved
- Where line breaks fall in rendered text
- Whether long body copy is split across elements

## Forbidden

- **Rewriting copy to fit the layout.** If it does not fit, report it — the copy
  is too long or the layout is too tight, and silently trimming hides which.
- **Leaving a state unwritten.** `state.empty` and `state.error` are supplied.
  If a state exists in the design and not in the copy file, that is a gap to
  report, not a sentence to invent.
- **Changing heading levels** to suit styling. Style the level; do not change it.
- **Truncating `meta.description` in markup.** If it is too long, it came in too
  long — report it.

## Acceptance

Run by `content-writer` before handing over:

- [ ] Every slot the design references is filled
- [ ] `state.empty` and `state.error` written
- [ ] `meta.title` ≤ 60, `meta.description` ≤ 155
- [ ] No claim present that the inputs do not support
- [ ] One line of reasoning per non-obvious heading choice

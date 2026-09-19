# Handoff: `designer` → `frontend-dev`

The seam that fails most often. Everything below is here because something went
wrong once.

## Fixed

```
Type scale      14 / 16 / 20 / 28 / 40   (1.25 ratio, 16 base)
Spacing         4px rhythm
                section padding 64px desktop / 32px mobile
Colour          Token names only:
                surface · surface-raised · text · text-muted
                accent · accent-contrast · border · danger
Breakpoints     360 / 768 / 1200
Layout          12-column desktop, 4-column mobile, 1200px max content width
Motion          150ms ease-out on state change; nothing animates on load
Focus           2px accent outline, 2px offset, never removed
```

Hex values never appear in a handoff. A hex value means the token set is
incomplete, and that is a finding, not a workaround.

## Open

- Which HTML element realises each block, as long as heading order is kept
- Whether a section becomes a component or stays inline markup
- CSS technique — grid, flex, utility classes. The rendered result is judged
- Loading presentation — skeleton or spinner
- How the 12-column grid collapses between 768 and 1200

## Forbidden

- **Inventing a colour.** If a state has no token, stop and report it. Do not
  pick something close — a near-miss colour is invisible in review and wrong
  forever.
- **Changing the type scale to make text fit.** Either the copy is too long or
  the layout is wrong. Shrinking type hides both. Report it.
- **Adding a library** to solve a layout the spec already describes in CSS.
- **Shipping only the happy path.** All six states below, every time.
- **Removing focus outlines.** Ever. If it looks wrong, the outline style is a
  design finding.

## The six states

Every component, every time:

| State | Must specify |
|---|---|
| Empty | First run, no data — blank box or useful prompt? |
| Loading | Skeleton, spinner, or nothing — and for how long before it reads as broken |
| Error | What the user sees, and what they can do next |
| Too long | One item, 200-character title — wrap, truncate or scroll |
| Too many | 500 items — paginate, virtualise or cap |
| Partial | Some fields missing — hide the row or show a placeholder |

## Acceptance

Run by `designer` before handing over:

- [ ] All six spec sections present
- [ ] Every colour is a token name; no hex anywhere
- [ ] All six states specified
- [ ] Every token referenced actually exists in the brand set
- [ ] Layout described at all three breakpoints
- [ ] The "not templated" paragraph names a decision, not an adjective

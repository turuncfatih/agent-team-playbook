# 5. Handoff contracts

A team's quality is decided at its seams. Roles are easy to write; handoffs are
where teams actually fail, because a vague handoff forces the receiving agent to
invent the missing half — confidently, and differently every time.

> **"Make it look nice"** is not a handoff.
> **"Here is the type scale, the spacing rhythm and the four states"** is.

## The four blocks

Every handoff contains exactly these. The blank template is in
[`templates/HANDOFF.template.md`](../templates/HANDOFF.template.md).

### 1. Fixed — decided, not open for reinterpretation

What the receiver must treat as settled. If the receiver disagrees, that is a
finding to raise, not a decision to make.

### 2. Open — genuinely the receiver's call

Say this explicitly. Without it, a careful agent asks about everything and a
confident one decides everything, and you cannot tell which you will get.

### 3. Forbidden — the trap doors

The specific wrong turns available at this seam. These are learned from real
failures, so this block grows over time. It is the most valuable part of a
mature handoff.

### 4. Acceptance — how the receiver knows it is done

A checklist the receiver can run *before* handing on. If the next role is the
first to discover the work is incomplete, the contract failed.

---

## Worked example: designer → frontend-dev

This is the seam that goes wrong most often, so it is worth seeing in full.

### Fixed

```
Type scale      14 / 16 / 20 / 28 / 40  (1.25 ratio, 16 base)
Spacing         4px rhythm; section padding 64px desktop, 32px mobile
Colour          Token names only: surface, surface-raised, text, text-muted,
                accent, accent-contrast, border, danger
                (never hex values — hex in a handoff means the token set is incomplete)
Breakpoints     360 / 768 / 1200
Layout          12-column desktop, 4-column mobile, 1200px max content width
Motion          150ms ease-out for state changes; nothing animates on load
```

### Open

```
- Which HTML element realises each block, as long as the heading order is kept
- Whether a section is a component or inline markup
- CSS technique: grid, flex or a utility class — the result is what is judged
- Where to place loading state: skeleton or spinner
```

### Forbidden

```
- Inventing a colour that is not in the token set.
  If a state has no token, stop and report it — do not pick something close.
- Changing the type scale to make text fit.
  The copy is wrong, or the layout is wrong; silently shrinking type hides both.
- Adding a library to solve a layout the spec already describes in CSS.
- Shipping only the happy path. See the state checklist below.
```

### Acceptance

```
- [ ] Renders at 360, 768 and 1200 with no horizontal scroll
- [ ] Every colour resolves to a token; no hex in the diff
- [ ] All six states below are implemented and reachable
- [ ] Heading order is sequential; no level is skipped
- [ ] Keyboard focus is visible on every interactive element
- [ ] Reduced-motion preference is honoured
```

---

## The state checklist

The single highest-value item in any UI handoff. Designs are drawn full of
perfect content; reality is not. Every component handoff should name what
happens for:

| State | The question it forces |
|---|---|
| **Empty** | First run, no data yet — is this a blank box or a useful prompt? |
| **Loading** | Skeleton, spinner or nothing? For how long before it looks broken? |
| **Error** | What does the user see, and what can they do next? |
| **Too long** | One item with a 200-character title — wrap, truncate or scroll? |
| **Too many** | 500 items — paginate, virtualise or cap? |
| **Partial** | Some fields missing — hide the row, or show a placeholder? |

Six lines in a handoff. They prevent the most common review comment there is:
*"what happens when it's empty?"*

## Worked example: API contract → implementer

The same four blocks, a different seam.

| Block | Content |
|---|---|
| **Fixed** | Path and method · request/response schema · status codes · error taxonomy · idempotency key semantics · pagination style |
| **Open** | Internal layering · which library · how validation errors are assembled, as long as the shape matches |
| **Forbidden** | Adding an undocumented field "because it was useful" · returning 200 with an error body · changing a status code to make a test pass |
| **Acceptance** | Contract tests pass · every documented error is reachable · replaying the same idempotency key produces one effect |

## Rules for writing handoffs

1. **Write them at the seam, not in the role.** A handoff belongs to the pair.
   Duplicating it into both agent specs guarantees the copies will drift.
2. **Grow the Forbidden block from real failures.** Every "why did it do that?"
   becomes a line. This is where a mature team stores its scar tissue.
3. **Acceptance must be checkable by the sender.** Otherwise the receiver is
   your quality gate, which is late and expensive.
4. **If a handoff exceeds two screens, the roles are cut wrong.** A seam that
   needs that much explanation is a seam that should not exist —
   see [chapter 2](02-cutting-a-project-into-roles.md).

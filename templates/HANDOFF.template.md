# Handoff: `<sending-role>` → `<receiving-role>`

> A handoff belongs to the **pair**, not to either role. Keep one copy here;
> duplicating it into both agent specs guarantees the copies will drift.
> See [docs/05-handoff-contracts.md](../docs/05-handoff-contracts.md).

## Fixed

<Decided upstream. If the receiver disagrees, that is a finding to raise, not a
decision to make.>

```
<key>    <value>
<key>    <value>
```

## Open

<Genuinely the receiver's call. State this explicitly — without it, a careful
agent asks about everything and a confident one decides everything.>

- <decision left to the receiver>
- <decision left to the receiver>

## Forbidden

<The specific wrong turns available at this seam. Grow this block from real
failures: every "why did it do that?" becomes a line. This is where a mature
team stores its scar tissue.>

- Do not <...>. If <condition>, stop and report — do not <the tempting shortcut>.
- Do not <...>

## Acceptance

<A checklist the **sender** runs before handing over. If the receiver is the
first to discover the work is incomplete, this contract failed.>

- [ ] <checkable>
- [ ] <checkable>

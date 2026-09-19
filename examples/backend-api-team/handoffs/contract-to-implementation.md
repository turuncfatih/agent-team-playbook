# Handoff: `api-designer` → `implementer` and `test-engineer`

One contract, two receivers, two acceptance lists. Both read this document;
neither reads the other's output.

> This is what makes the parallelism real. If `test-engineer` read the
> implementation, the tests would describe what was built rather than what was
> promised — and a green suite would hide a broken endpoint.

## Fixed

```
Path & method      Exactly as written. No trailing-slash variants.
Request schema     Field names, types, required/optional — all fixed
Response schema    Per status code, fixed
Status codes       The complete set. If it is not listed, it must not occur.
Error shape        { code, message, details? } — same for every error, everywhere
Auth               Who may call, and on what basis
Idempotency        The key, and what a replay does
Pagination         Style, page size limits, cursor or offset semantics
Concurrency        Stated behaviour when two callers race
```

## Open

**For `implementer`:**
- Internal layering, module boundaries, naming
- Library choice, persistence approach
- How validation errors are assembled, as long as the shape matches
- Migration technique, as long as it is reversible

**For `test-engineer`:**
- Test framework layout and fixture strategy
- Whether a case is a unit or integration test
- How the race in the concurrency clause is provoked

## Forbidden

- **Adding an undocumented field**, request or response, "because it was
  useful". Every field is a promise you cannot withdraw.
- **Returning 200 with an error body.** If the operation failed, the status says so.
- **Changing a status code to make a test pass**, or changing a test to match an
  unexpected status. Either the contract is wrong — report it — or the code is.
- **`test-engineer` reading `src/`** to decide expected behaviour. The contract
  is the source of truth; if it is silent, that is a gap to report, not a
  behaviour to enshrine.
- **`implementer` writing `tests/`**, or `test-engineer` writing `src/`. The
  directory boundary is the whole reason both roles exist.
- **An irreversible migration** without it being stated explicitly in the summary
  and approved in the plan.

## Acceptance

Run by `api-designer` before handing over:

- [ ] Every status code the endpoint can return is listed, with its cause
- [ ] Error shape identical to the rest of the surface
- [ ] Idempotency stated — including "not idempotent", if that is the truth
- [ ] Concurrent-caller behaviour stated
- [ ] Auth requirement stated per endpoint, not per group
- [ ] Nothing in the contract requires a data-model change the plan did not authorise

Run by each receiver before handing on:

**`implementer`** — every listed status reachable · validation matches ·
idempotency behaves as written · migration rolls back · build green

**`test-engineer`** — one test per listed status · a negative authorization case
exists · idempotency tested by replay · no assertion reads implementation
internals

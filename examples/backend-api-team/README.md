# Team: backend / API team

A service with a public HTTP contract and a database behind it.

Read this **after** the [web product team](../web-product-team/). The value here
is the contrast: same method, different answers, because the work has a
different reversibility profile.

## Why a team at all

| Test | Verdict |
|---|---|
| **Artifact** | ✅ Plan · API contract · implementation · security findings · test suite · pass/fail report |
| **Veto** | ✅ Two — `security-reviewer` (judgment) and `verifier` (fact) |
| **Parallelism** | ✅ `implementer` and `test-engineer` both work from the contract, not from each other |
| **Reversibility** | ✅ **Strongly.** A published API contract has consumers; a migration is hard to undo; an authorization gap ships |

The fourth test is the one that changes everything. On the web team it was a
qualified yes; here it is an emphatic one, and that single difference justifies
every structural difference below.

## What changed from the web team, and why

| | Web team | Backend team | Why |
|---|---|---|---|
| Writers | 1 | **2** (directory-scoped) | Tests and source are different artifacts with different review criteria |
| Vetoes | 1 (fact) | **2** (judgment + fact) | An authorization gap that ships cannot be fixed by an edit |
| Highest-tier role | designer | **api-designer** | The contract is the irreversible decision here, not the appearance |
| Rework limit | 2 | **3** | Security findings often need two attempts; the cost of shipping one is higher than the cost of a third round |

The method did not change. The inputs to it did.

## The roster

| Role | Artifact | Writes? | Tier | Veto |
|---|---|:---:|---|:---:|
| [`tech-lead`](agents/tech-lead.md) | The plan | ✗ | high | ✗ |
| [`api-designer`](agents/api-designer.md) | API contract | ✗ | high | ✗ |
| [`implementer`](agents/implementer.md) | Implementation | ✅ `src/` | mid–high | ✗ |
| [`test-engineer`](agents/test-engineer.md) | Test suite | ✅ `tests/` | mid | ✗ |
| [`security-reviewer`](agents/security-reviewer.md) | Findings | ✗ | high | ✅ judgment |
| [`verifier`](agents/verifier.md) | Pass/fail report | ✗ | mid | ✅ fact |

### On having two writers

[Chapter 6](../../docs/06-permissions-and-veto.md) says one writer is the
target, and two are workable **when the boundary is a directory, not a
convention**. That condition is met here:

- `implementer` writes `src/` and `migrations/`. Never `tests/`.
- `test-engineer` writes `tests/`. Never `src/`.

The boundary is enforceable by a path check, so it cannot erode quietly. And it
buys something real: an implementer that writes its own tests writes tests that
pass, which is not the same as tests that are correct.

If your project cannot draw that line by directory, use one writer.

### On having two vetoes

Also an exception, also a stated one. The two vetoes are different in kind and
cannot deadlock each other:

| | `security-reviewer` | `verifier` |
|---|---|---|
| Basis | Expertise | Tool output |
| Blocks on | "Unsafe to ship", with evidence | Red build, failing test |
| Overridable | By a human, on the record | No — fix it |

A third veto would deadlock the team. There is no architecture reviewer here for
exactly that reason.

## The flow

```
tech-lead plans
      ▼
api-designer  ── the contract: paths, schemas, errors, idempotency
      ▼
   ┌──┴───────────────┐   (parallel — both read the contract, not each other)
   ▼                  ▼
implementer      test-engineer
   └──────┬───────────┘
          ▼
   ┌──────┴──────────────────┐
   ▼                         ▼
security-reviewer        verifier
  (judgment VETO)        (fact VETO)
   └──────┬──────────────────┘
          ▼
   blocked? ─> rework (max 3) ─> human
   clear?   ─> ship
```

## The one-line version

> *"The **tech-lead** plans; the **api-designer** fixes the contract; the
> **implementer** and **test-engineer** work from it in parallel; the
> **security-reviewer** and **verifier** can each stop the release."*

## Handoffs

| Seam | Contract |
|---|---|
| `api-designer` → `implementer` | [contract-to-implementation.md](handoffs/contract-to-implementation.md) |
| `api-designer` → `test-engineer` | Same contract, different acceptance — see the handoff's Acceptance section |

## Rework and escalation

**Rework limit:** 3 rounds, then escalate to a human.

**Escalate immediately when:** a finding requires a breaking change to a
published contract · a migration is not reversible · the fix requires a
credential or permission the team does not have.

## Roles deliberately not created

| Not created | Why |
|---|---|
| `db-migrator` | Migrations are part of the change that needs them. A separate role would split one artifact across two authors. |
| `architecture-reviewer` | Would be a third veto, and would deadlock the team. Architecture concerns are findings for `tech-lead`. |
| `performance-reviewer` | No distinct failure mode at this size — folded into the verifier's acceptance criteria. |
| `docs-writer` | The contract *is* the documentation. A second description of the same thing drifts from it. |

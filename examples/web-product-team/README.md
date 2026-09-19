# Team: web product team

A marketing or product website: pages that have to look considered, read well,
be findable, and actually run.

## Why a team at all

| Test | Verdict |
|---|---|
| **Artifact** | ✅ Plan · design spec · page copy · working pages · audit report · pass/fail report — six distinct artifacts |
| **Veto** | ✅ `verifier` holds a fact veto: nothing ships that does not build and render |
| **Parallelism** | ✅ `designer` and `content-writer` never read each other's output |
| **Reversibility** | ⚠️ Partly. Published pages are cheap to fix, but a site that ships broken or ugly costs trust, and SEO damage compounds |

Four for four on the first three, and enough on the fourth. A team is justified.

## The roster

| Role | Artifact | Writes? | Tier | Veto |
|---|---|:---:|---|:---:|
| [`tech-lead`](agents/tech-lead.md) | The plan | ✗ | high | ✗ |
| [`designer`](agents/designer.md) | Design spec | ✗ | high | ✗ |
| [`content-writer`](agents/content-writer.md) | Page copy | ✗ | mid | ✗ |
| [`frontend-dev`](agents/frontend-dev.md) | Working pages | ✅ | mid–high | ✗ |
| [`seo-auditor`](agents/seo-auditor.md) | Audit report | ✗ | low | ✗ |
| [`verifier`](agents/verifier.md) | Pass/fail report | ✗ | mid | ✅ fact |

One writer. One veto. Two parallel roles.

## The flow

```
tech-lead plans
   ├─ designer ───────┐   (parallel — neither reads the other)
   └─ content-writer ─┤
                      ▼
                 frontend-dev  (the only role that touches the repo)
                      ▼
   ┌──────────────────┴──────────────────┐
   ▼                                     ▼
seo-auditor (findings)              verifier (VETO)
   └──────────────────┬──────────────────┘
                      ▼
              red? ─> rework (max 2) ─> human
              green? ─> ship
```

`seo-auditor` and `verifier` both run after the build, in parallel. Only the
verifier can stop the release; SEO findings are recorded and scheduled.

## The one-line version

> *"The **tech-lead** plans; the **designer** and **content-writer** work in
> parallel; the **frontend-dev** builds; the **seo-auditor** reports; the
> **verifier** can stop the release."*

## Handoffs

| Seam | Contract |
|---|---|
| `designer` → `frontend-dev` | [design-to-frontend.md](handoffs/design-to-frontend.md) |
| `content-writer` → `frontend-dev` | [content-to-frontend.md](handoffs/content-to-frontend.md) |

## Rework and escalation

**Rework limit:** 2 rounds, then escalate to a human.

**Escalate immediately when:** brand tokens are missing or contradictory · the
brief asks for a page type the design system has no pattern for · the same
verifier failure recurs after one fix attempt.

## Roles deliberately not created

| Not created | Why |
|---|---|
| `react-dev` + `css-dev` | Same write permission, same artifact. One role. |
| `image-optimiser` | Deterministic. A build step. |
| `deployer` | Deterministic. A CI job. |
| `researcher` | Produced notes only the writer read. That is a prompt section, not an artifact. |
| `accessibility-reviewer` | Its checks are in the verifier's definition of done. A second reviewer here would be a second veto and would deadlock the team. |

# Team: <project or product name>

> One page describing the whole team. Written **after** working through
> [docs/01](../docs/01-when-not-to-build-a-team.md) and
> [docs/02](../docs/02-cutting-a-project-into-roles.md).

## The brief

<What this team delivers, in two or three sentences.>

## Why a team at all

| Test | Verdict |
|---|---|
| **Artifact** — does every role produce a distinct artifact? | <yes/no + note> |
| **Veto** — can at least one role say no? | <yes/no + which role> |
| **Parallelism** — do two roles not need each other's output? | <yes/no + which> |
| **Reversibility** — are mistakes expensive to undo? | <yes/no + why> |

<If fewer than three pass, do not build this team.>

## The roster

| Role | Artifact | Writes? | Tier | Veto |
|---|---|:---:|---|:---:|
| `<role>` | <artifact> | ✗ | high | ✗ |
| `<role>` | <artifact> | ✅ | mid | ✗ |
| `<role>` | <artifact> | ✗ | mid | ✅ |

## The flow

```
<role> plans
   ├─ <role> ─┐   (parallel)
   └─ <role> ─┤
              ▼
         <gate role>  ── blocks ──> rework (max N) ──> human
              │
              ▼
          <reporter>
```

## The one-line version

> *"The `<role>` plans; `<role>` and `<role>` work in parallel; `<role>` builds;
> `<role>` can stop the release."*

<If this sentence needs an "and also", or a role has no verb, the cut is wrong.>

## Handoffs

| Seam | Contract |
|---|---|
| `<a>` → `<b>` | `handoffs/<a>-to-<b>.md` |

## Rework and escalation

**Rework limit:** <N> rounds, then escalate to a human.

**Escalate immediately when:** <conditions that skip the loop entirely>

## Roles deliberately not created

| Not created | Why |
|---|---|
| `<role>` | <merged into X / this is a script / no distinct failure mode> |

# 8. Is your team working?

A team that produces output is not necessarily a team that is working. Five
numbers tell you more than reading transcripts, and all five are cheap to
collect.

## The five numbers

### 1. Rework rate — per role

> Of the rounds that were sent back, which role's output caused it?

This is the most diagnostic number in the system, because it localises the
problem instead of describing it.

| Reading | Means |
|---|---|
| One role causes most rework | That role's spec or tier is wrong — not the team |
| Rework is spread evenly | The **handoffs** are vague, not the roles ([chapter 5](05-handoff-contracts.md)) |
| Almost no rework | Either genuinely good, or the gate is decoration — check number 2 |

### 2. Veto rate

> What fraction of rounds does the gate block?

| Rate | Verdict |
|---|---|
| 0% | The gate is decoration. Severity is miscalibrated, or the reviewer lacks context |
| 10–30% | Healthy. It catches real things without stalling delivery |
| >50% | The bar is wrong, or upstream roles are underspecified |

Zero is the dangerous one, because it looks like success.

### 3. Cost per delivered artifact

Not cost per run — cost per thing that actually shipped. Escalated and abandoned
runs are part of the numerator. This is the number that survives contact with a
manager.

Track its **distribution**, not its average. One run at twenty times the median
usually means a silent retry loop ([anti-pattern 10](07-anti-patterns.md)).

### 4. Escalation rate

> How often does a human have to step in?

| Rate | Verdict |
|---|---|
| ~0% | Either the work is easy, or the limits are too loose and bad output ships |
| 5–15% | Healthy. The team knows what it cannot do |
| >30% | The team is not autonomous enough to be worth its overhead |

Escalation is a **feature**. A team that never escalates is a team that never
notices it is stuck.

### 5. Invocation count — per role

> How often is each role actually used?

A role invoked on 5% of tasks is not a role. Either merge it, or turn it into a
conditional step. This single number finds dead weight faster than any review.

## Red flags that do not show up in metrics

- **Output has stopped improving between rounds.** The reviewer's findings are
  not actionable. Check the handoff, not the reviewer.
- **The same finding recurs across deliveries.** It belongs in the Forbidden
  block of a handoff, or in an anti-goal — not in a review every time.
- **You cannot explain a decision from the log.** The trail is incomplete, and
  the first audit will be unpleasant.
- **Adding a role made things worse.** Trust that. Remove it.
- **Everyone praises everyone.** Reviewers with nothing to say are reviewers
  without enough context, or without a stated bar.

## Reviewing a team

Every few weeks, per role, in this order:

1. **Invocation count** — if near zero, delete or merge, and stop here
2. **Rework caused** — if high, is the spec wrong, or the tier?
3. **Anti-goals** — did it drift into a neighbour's territory? Add a line
4. **Tier** — could it move down? Most teams are over-provisioned in two roles
5. **Handoffs out of it** — did a recurring correction earn a Forbidden line?

A team is a living configuration. Cut it once and never revisit it, and you will
be paying frontier prices to reformat JSON six months from now.

## The one-question version

If you keep nothing else from this chapter:

> **When the team last shipped something wrong — which role should have caught
> it, and why didn't it?**

If the answer is "no role was supposed to catch it", you have a missing role.
If it is "that role exists but had no context", you have a handoff problem.
If it is "that role caught it and was overruled", you have a veto problem.

Three questions in one, and it works on any team.

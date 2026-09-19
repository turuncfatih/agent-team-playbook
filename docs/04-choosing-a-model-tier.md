# 4. Choosing a model tier

One rule generates almost every correct answer here:

> ### Reasoning scales with the *irreversibility* of the decision, not with the prestige of the task.

The instinct is to put the strongest model on the work that feels most
impressive — the code, the architecture, the clever bit. The correct instinct is
to put it where a mistake is **hardest to undo**.

A plan that is wrong wastes an entire round. A paragraph that is wrong gets
rewritten in ten seconds. Those two facts should decide your spending, and they
usually do not.

## Why tiers, not model names

This chapter deliberately does not name models. Names go stale within months;
the *shape* of the decision does not. Every provider offers roughly three tiers,
and your job is to map your roles onto them.

| Tier | Characteristics | Costs roughly |
|---|---|---|
| **High** | Strongest reasoning, best judgment, highest latency | 10–30× low |
| **Mid** | Solid instruction-following, good writing, fast enough | 3–8× low |
| **Low** | Fast, cheap, reliable on narrow well-specified tasks | 1× |

Write the tier in the agent spec, and keep the concrete model in one place —
project config, not scattered across six agent files.

## What belongs in each tier

### High — irreversible, ambiguous, or taste-driven

- **Planning and routing.** A wrong plan is the most expensive error in the
  system: it wastes every downstream role.
- **Architecture and API contract decisions.** Expensive to reverse once built on.
- **Security and compliance review.** A missed finding ships.
- **Visual design direction.** Taste does not survive downgrading; cheap models
  produce work that reads as generated, which is the exact failure the role exists
  to prevent.
- **Code review with judgment** — "is this the right abstraction", not "does this compile".

### Mid — real work, cheap to correct

- **Implementation from a clear spec.** When the contract is precise, the hard
  thinking already happened upstream.
- **Content and copy.** Wrong copy is caught in one read and rewritten in seconds.
- **Test case derivation** from stated acceptance criteria.
- **Summarising and reporting** over material that is already correct.

### Low — narrow, specified, verifiable

- **Classification and routing** into a fixed set of labels.
- **Extraction** into a known schema.
- **Formatting and normalising.**
- **Reading tool output and reporting it** — the tool did the work; the model
  only narrates.

> If a low-tier task is *also* deterministic, it is a script, not an agent.
> See the checklist test in [chapter 1](01-when-not-to-build-a-team.md).

## The mapping, by role archetype

| Archetype | Tier | Why |
|---|---|---|
| Orchestrator / tech-lead | **High** | A wrong plan wastes every other role |
| Designer | **High** | Taste is the deliverable; it does not survive a downgrade |
| API / contract designer | **High** | Expensive to reverse once implemented against |
| Implementer | **Mid–High** | High when the spec is thin, mid when it is precise |
| Content writer | **Mid** | Mistakes are visible and cheap |
| Test engineer | **Mid** | Derivation from stated criteria |
| Security reviewer | **High** | A missed finding ships |
| Auditor over tool output (SEO, lint, a11y) | **Low** | The tool decides; the model explains |
| Verifier (build, run, check) | **Mid** | Tool-heavy, but must judge whether output means failure |

Two things worth noticing in that table.

**The implementer is not automatically your top tier.** With a precise output
contract from an upstream designer, mid does the job. The spending moved
upstream, to where the irreversible decision actually is.

**The auditor is low tier on purpose.** If a role's job is to run a checker and
report, the model is a narrator. Paying frontier prices for narration is the
single most common waste in agent teams.

## Escalation: when to move a role up mid-run

Tier is a default, not a life sentence. Escalate when:

1. **The input is ambiguous or self-contradictory.** Cheap models paper over
   contradictions; expensive ones notice them.
2. **The same step has failed twice.** A third identical attempt is waste. Change
   something, and tier is the cheapest thing to change.
3. **The blast radius grew.** A change that started as one component now touches
   the data model — the decision became less reversible mid-flight.
4. **A reviewer disagrees with a writer twice.** Either the spec is bad or the
   tier is too low; both are worth one expensive opinion.

Escalation should be a **named, logged event**, not an ambient retry. If nobody
can see that it happened, nobody can tell why the run cost triple.

## De-escalation: when to move down

Less discussed, and where most of the savings are.

- **The task repeats with the same shape.** Once the first few runs are right,
  the reasoning is in the prompt, not the model.
- **The output is checked by a script anyway.** A verifier that catches the error
  makes an upstream downgrade safe.
- **The role only narrates tool output.**
- **Latency matters more than nuance** — anything a human waits on.

## The cost reality

The distribution matters more than any single choice. A typical five-role team,
per delivery:

| Role | Tier | Share of spend |
|---|---|---|
| tech-lead | high | ~15% |
| designer | high | ~25% |
| frontend-dev | mid | ~35% |
| content-writer | mid | ~15% |
| verifier | mid | ~10% |

Two structural facts:

- **The whole team on high tier costs 4–6× the mixed team**, for output that is
  better in two roles and identical in three.
- **Rework dominates everything.** One avoided rework round pays for a dozen
  upgrades. Spend on the roles that *prevent* rework — the planner and the
  reviewer — before you spend on the ones that do the work.

## Anti-patterns

| Anti-pattern | Why it is wrong |
|---|---|
| Top tier everywhere, "to be safe" | 4–6× the cost, and the plan was never the bottleneck |
| Cheapest tier everywhere, "it's fine" | It is fine until the plan is wrong, and then nothing is fine |
| Tier chosen by how impressive the task sounds | Prestige is not irreversibility |
| Tier not written in the spec | Nobody can revisit a decision they cannot find |
| Model names hardcoded in six agent files | Model names change; keep them in one place |

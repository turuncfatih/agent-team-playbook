# 3. The agent spec

An agent definition is a contract, not a personality. This chapter is the
contract, field by field: what each field is for, and what breaks without it.

The blank template is in [`templates/AGENT.template.md`](../templates/AGENT.template.md).
Filled-in examples are in [`examples/`](../examples/).

## The ten fields

| # | Field | Skipping it causes |
|---|---|---|
| 1 | Role | Two agents quietly doing the same job |
| 2 | Invoke / do not invoke | The agent gets called for everything, or never |
| 3 | Inputs | Context bloat, and worse output |
| 4 | Output contract | The next agent cannot consume the result |
| 5 | Tools | Privilege creep |
| 6 | Model tier | Paying frontier prices to reformat JSON |
| 7 | Definition of done | Nobody can say whether it worked |
| 8 | Veto | Either nothing ships, or nothing is ever blocked |
| 9 | Failure & escalation | Silent retries, burned budget, no signal |
| 10 | Anti-goals | Scope creep into the next agent's territory |

Fields 9 and 10 are the ones nearly everyone skips, and they are the two that do
the most work in practice.

---

### 1. Role — one sentence, one noun

> *"Produces the visual design spec for a page or component."*

Not *"helps with design"*. If the sentence needs an "and", you have two roles.
The noun at the end is the artifact, and it must match field 4.

### 2. Invoke / do not invoke

Both halves are required. The negative half is what stops an orchestrator
reaching for the most capable-sounding agent every time.

> **Invoke when:** a new page or component needs a visual direction.
> **Do not invoke when:** the change is copy-only, or an existing component is
> being reused unchanged. Route those to `content-writer` / `frontend-dev`.

Naming the alternative is the point. "Do not invoke for X" without saying who
*does* handle X just moves the problem.

### 3. Inputs — what it needs, and nothing more

List the context this role requires. Be specific, and be stingy: context is the
scarcest resource in the system, and irrelevant context measurably degrades
output.

> Brand tokens · target audience · the page's single goal · existing components
> it must stay consistent with

If an input appears in every agent's list, it belongs in shared project context,
not in the agent spec.

### 4. Output contract — the shape, not the vibe

This is what the next role consumes, so it must be precise enough to be checked.

> A markdown design spec containing: layout at 3 breakpoints · type scale ·
> colour roles (not hex values — token names) · spacing rhythm · component
> states · one paragraph on what makes this page *not* look templated.

"A design" is not an output contract. "A markdown file with these six sections"
is. If you cannot write a checklist that verifies the output, rewrite the field.

### 5. Tools — allow-list, plus explicit denials

Grant the minimum. Then state the interesting denials explicitly, because a
reader's first question is always "wait, can it edit files?"

> **Allowed:** `Read`, `Glob`, `Grep`
> **Explicitly not granted:** `Write`, `Edit`, `Bash` — the designer never
> touches the repository. Design decisions reach the code through
> `frontend-dev`, so every change has one author.

### 6. Model tier — and the reason

State the tier *and* why. The reason is what lets someone revisit the choice
later without guessing. See [chapter 4](04-choosing-a-model-tier.md).

> **Tier:** high. Visual judgment is the whole job, and a cheaper model produces
> work that reads as generated — which is precisely the failure this role exists
> to prevent.

### 7. Definition of done — checkable by someone else

Written so that a different role can verify it without re-doing the work.

> - Every section of the output contract is present
> - Every colour is a token name, not a hex value
> - Empty, loading, error and overflow states are each specified
> - The "why this is not templated" paragraph names a specific decision

"High quality" is not a definition of done. A list someone else can tick is.

### 8. Veto — can this role stop the work?

Most roles: **no.** A team with two or three vetoes stalls.

If yes, say what it may block on and what it may not:

> **Veto:** yes, on a red build or a failing acceptance case only. **Not** on
> style, naming or architecture preferences — those are findings, not blocks.

A veto without a stated scope becomes a veto on everything the role has an
opinion about. See [chapter 6](06-permissions-and-veto.md).

### 9. Failure & escalation

What this role does when it *cannot* do its job. Without this, agents guess,
and a guess presented confidently is worse than a stop.

> If the brand tokens are missing or contradictory, stop and report what is
> missing. Do not invent tokens. Escalate to `tech-lead`, which decides whether
> to ask the human or proceed with documented defaults.

Three things to specify: **what triggers a stop**, **what it must not do
instead**, and **who it hands to**.

### 10. Anti-goals — the sentences that keep a team separate

The most valuable field, and the one that is almost always missing. Every role
drifts towards the adjacent role's work, because adjacent work is visible and
looks helpful.

> - Do not write code, not even a snippet "for clarity"
> - Do not write user-facing copy — that is `content-writer`
> - Do not choose a component library — that is an architecture decision
> - Do not approve your own spec

Write anti-goals *after* the team is cut, and write them at the boundaries: each
one should name the neighbour whose territory is being protected.

---

## The frontmatter

The body is the contract; the frontmatter is what a runtime reads. This
playbook uses the format Claude Code expects, so the examples are directly
usable:

```markdown
---
name: designer
description: Produces the visual design spec for a page or component. Use before any new page or component is built.
tools: Read, Glob, Grep
---
```

`description` is how an orchestrator decides whether to route work here, so it
should read like field 2, not like field 1. Describing what the agent *is* helps
nobody; describing **when to reach for it** is the whole job.

## Length

A good agent spec is one to two screens. If it is longer, one of these is true:

- The role is actually two roles ([chapter 2](02-cutting-a-project-into-roles.md))
- Project-wide context has leaked into a single agent's file
- The prompt is compensating for a missing tool or a missing script

---
name: <kebab-case-role-name>
description: <When to reach for this agent — a routing hint, not a self-portrait. One or two sentences.>
tools: <comma-separated allow-list, or omit the field for no tools>
---

# <Role name>

> Copy this file into your project's agent directory and fill every section.
> A section you cannot fill is a signal, not an inconvenience — see
> [docs/03-the-agent-spec.md](../docs/03-the-agent-spec.md).

## Role

<One sentence, ending in the noun this role produces. If it needs an "and",
you have two roles.>

## Invoke / do not invoke

**Invoke when:** <the trigger condition>

**Do not invoke when:** <the near-miss cases — and name the role that handles
each instead>

## Inputs

<What context this role needs, and nothing more. Be stingy: irrelevant context
degrades output. If an input appears in every role's list, it belongs in shared
project context.>

- <input>
- <input>

## Output contract

<The exact shape of what is produced — precise enough that a checklist can
verify it. "A design" is not a contract; "a markdown file with these six
sections" is.>

## Tools

**Allowed:** <minimum set>

**Explicitly not granted:** <the notable denials, with the one-line reason a
reader will want>

## Model tier

**Tier:** <low | mid | high>

**Why:** <one sentence tied to irreversibility — see
[docs/04-choosing-a-model-tier.md](../docs/04-choosing-a-model-tier.md)>

## Definition of done

<A checklist another role can verify without redoing the work.>

- [ ] <checkable item>
- [ ] <checkable item>

## Veto

**Can this role stop the work?** <no | yes>

<If yes: state what it may block on, and what it may not. A veto without a
scope becomes a veto on everything the role has an opinion about.>

## Failure & escalation

**Stop when:** <the condition that means this role cannot do its job>

**Do not:** <the tempting wrong move — usually "invent the missing input">

**Hand to:** <role or human>

## Anti-goals

<Write these after the team is cut. Each one should name the neighbouring role
whose territory is being protected.>

- Do not <...> — that is `<other-role>`
- Do not <...>
- Do not approve your own output
- Do not create files the task did not ask for — no SUMMARY.md, no NOTES.md
- Do not comment what the code says; comment only why it is not obvious
- Do not end with a recap of what you just did; the diff is the report

# 1. When *not* to build an agent team

Start here, because most teams should not exist.

An agent team is not free. Every boundary between two agents is a place where
context is lost, cost is duplicated and a handoff can be misread. A single
well-specified agent with a good prompt outperforms a five-agent team on most
tasks, and it does so faster and for a tenth of the price.

So the first question is never "which agents do I need?" It is **"does this work
justify a team at all?"**

## The four tests

Run all four. Pass fewer than three, and you want one agent — or a script.

### 1. The artifact test

> Can you name the distinct artifact each role produces, in one noun phrase?

`designer → a design spec`, `frontend-dev → a working component`,
`verifier → a pass/fail report`. If two roles produce the same artifact, they
are one role wearing two hats. If a role's artifact is "help" or "advice", it is
not a role.

### 2. The veto test

> Is there at least one role that can say **no**?

A team where everyone contributes and nobody can stop the work is a relay race.
Relay races do not need coordination — they need an ordered list. The moment one
role can block, you need a plan, a rework path and an escalation rule. That is
when a team becomes worth its overhead.

### 3. The parallelism test

> Do at least two roles *not* need each other's output?

If every step depends on the one before it, you have a pipeline, and a pipeline
is a function call chain. Teams earn their coordination cost when work fans out.

### 4. The reversibility test

> Would a mistake here be expensive to undo?

Cheap mistakes do not need gates. A blog post draft can be wrong; a database
migration, a pricing change or a public API contract cannot. Gates, rework
loops and reviewers are all machinery for making irreversible mistakes less
likely — and they are wasted on reversible ones.

## The checklist test

Before writing any agent, ask:

> Could a deterministic script do this?

Counting words, validating a schema, checking that every image has alt text,
diffing two files, running a build — these are scripts. Wrapping a script in an
agent makes it slower, more expensive and less reliable, and it will sometimes
disagree with itself.

The right shape is usually: **a script does the checking, an agent explains the
result and decides what to do about it.**

## What to build instead

| Situation | Build this |
|---|---|
| One artifact, cheap mistakes | One agent, one good prompt |
| One artifact, expensive mistakes | One agent + one reviewer with veto |
| Deterministic verification | A script, invoked by an agent |
| Several artifacts, no dependencies | Parallel single agents, no orchestrator |
| Several artifacts, a gate, rework | **A team.** Continue to [chapter 2](02-cutting-a-project-into-roles.md). |

## The honest version

Most agent teams published as examples fail test 2 and test 4. They are five
agents taking turns at work one agent could do, with a coordinator added because
coordination looks like architecture.

A team is a cost you pay to make a specific failure less likely. If you cannot
name the failure, you are not buying anything.

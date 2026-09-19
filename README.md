# Agent Team Playbook

**How to design an agent team for a real project — role cuts, task contracts, model tiers, and the failures to design around.**

[![check](https://github.com/turuncfatih/agent-team-playbook/actions/workflows/check.yml/badge.svg)](https://github.com/turuncfatih/agent-team-playbook/actions/workflows/check.yml)
[![licence](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)

🇬🇧 English · [🇹🇷 Türkçe](README.tr.md)

Most agent teams fail before the first prompt is written, because the roles were
cut along the wrong lines. This playbook is the method for cutting them well:
how to decide a team is even justified, where the boundaries go, what every
agent definition must contain, which model tier each role gets and why, and what
one agent must hand the next.

It ships two complete worked examples — a **web product team** and a
**backend/API team** — with copy-paste-ready agent definitions, and the
reasoning for every decision, including the ones that went the other way.

```
8 chapters · 3 templates · 2 worked teams · 12 agent definitions · 3 handoff contracts
```

> **Companion repository.** [AgentForge](https://github.com/turuncfatih/agentforge) is the same subject from the
> engineering side: a .NET implementation of the orchestrator,
> the gate, the budget and the audit trail described here. This repo is the
> judgment; that one is the machinery.

---

## The thesis

Three claims, and everything here follows from them.

**1. Most agent teams should not exist.** A single well-specified agent beats a
five-agent team on most tasks — faster, cheaper, and with less context lost at
the seams. A team is a cost you pay to make a *specific* failure less likely. If
you cannot name that failure, you are not buying anything.

**2. Roles are cut along permissions and failure modes, not job titles.**
`frontend-dev` is a role because it is the only one allowed to write to the
repository — not because your company employs frontend developers.

**3. Capability comes from configuration, never from a prompt.** "Only you may
block delivery" is a request. Not granting the `Write` tool is a control.

---

## Start here

| If you are… | Read |
|---|---|
| Wondering whether you need a team at all | [1. When *not* to build a team](docs/01-when-not-to-build-a-team.md) |
| Sure you need one, unsure how to split it | [2. Cutting a project into roles](docs/02-cutting-a-project-into-roles.md) |
| Writing an agent definition right now | [3. The agent spec](docs/03-the-agent-spec.md) + [template](templates/AGENT.template.md) |
| Deciding which model goes where | [4. Choosing a model tier](docs/04-choosing-a-model-tier.md) |
| Debugging a team that produces bad output | [5. Handoff contracts](docs/05-handoff-contracts.md) |
| Debugging a team that ships broken work | [6. Permissions and veto](docs/06-permissions-and-veto.md) |
| Suspicious that something is off | [7. Anti-patterns](docs/07-anti-patterns.md) |
| Wanting to know if it is working | [8. Is your team working?](docs/08-is-your-team-working.md) |
| Just wanting a team to copy | [examples/](examples/) — but read chapter 2 first |

---

## The method, in one page

### Step 1 — Should this be a team at all?

Four tests. Pass fewer than three, and you want one agent, or a script.

| Test | Question |
|---|---|
| **Artifact** | Can you name the distinct artifact each role produces? |
| **Veto** | Can at least one role say *no*? |
| **Parallelism** | Do at least two roles not need each other's output? |
| **Reversibility** | Would a mistake here be expensive to undo? |

### Step 2 — Where do the cuts go?

Cut along these lines:

| Cut by | Not by |
|---|---|
| **Write permission** — who may change the repo | Job title |
| **Type of judgment** — taste / correctness / compliance | Seniority |
| **Failure mode caught** — name it, or the role is decoration | Technology |
| **Context needed** — wildly different context, separate roles | Task |

Target **3–6 roles**, **one writer**, **one or two vetoes**.

### Step 3 — Specify each role

Ten fields. The two everyone skips are the two that matter most:

```
Role · Invoke/don't invoke · Inputs · Output contract · Tools
Model tier · Definition of done · Veto · Failure & escalation · Anti-goals
                                        └──────── these two ────────┘
```

### Step 4 — Pick the tier

> **Reasoning scales with the irreversibility of the decision, not with the prestige of the task.**

| Tier | Belongs there |
|---|---|
| **High** | Planning · architecture & contracts · security review · visual design |
| **Mid** | Implementation from a clear spec · content · tests · verification |
| **Low** | Classification · extraction · formatting · narrating tool output |

The implementer is usually **not** your top tier. With a precise spec upstream,
the irreversible thinking already happened.

### Step 5 — Write the handoffs

Four blocks per seam: **Fixed** · **Open** · **Forbidden** · **Acceptance**.
The Forbidden block grows from real failures — it is where a mature team stores
its scar tissue.

### Step 6 — Measure

| Number | Healthy |
|---|---|
| Veto rate | 10–30%. Zero means the gate is decoration |
| Escalation rate | 5–15%. Zero means bad work is shipping |
| Rework by role | Concentrated → fix that role. Spread → fix the handoffs |
| Invocations by role | Near zero → delete the role |

---

## The two worked teams

Same method, different answers — because the work has a different
reversibility profile. **The contrast is the point.**

### [Web product team](examples/web-product-team/)

`tech-lead` · `designer` · `content-writer` · `frontend-dev` · `seo-auditor` · `verifier`

```
tech-lead plans
   ├─ designer ───────┐   (parallel)
   └─ content-writer ─┤
                      ▼
                 frontend-dev  ← the only writer
                      ▼
        seo-auditor ──┴── verifier (VETO)
                      ▼
              red? → rework (max 2) → human
```

### [Backend / API team](examples/backend-api-team/)

`tech-lead` · `api-designer` · `implementer` · `test-engineer` · `security-reviewer` · `verifier`

```
tech-lead plans
      ▼
api-designer  ← the contract is the irreversible decision
      ▼
   ┌──┴───────────────┐   (parallel — both read the contract, never each other)
   ▼                  ▼
implementer      test-engineer
   └──────┬───────────┘
          ▼
security-reviewer ──┴── verifier
  (judgment VETO)       (fact VETO)
          ▼
   blocked? → rework (max 3) → human
```

### What changed, and why

| | Web team | Backend team | Why |
|---|---|---|---|
| Writers | 1 | **2**, split by directory | Tests and source are different artifacts with different review criteria — and an implementer who writes their own tests writes tests that pass, not tests that are correct |
| Vetoes | 1 (fact) | **2** (judgment + fact) | An authorization gap that ships cannot be fixed by an edit |
| Top-tier role | `designer` | `api-designer` | The contract is what is irreversible here, not the appearance |
| Rework limit | 2 | **3** | Security findings often need two attempts, and shipping one costs more than a third round |

Both teams also document the roles they **deliberately did not create** — and why.

---

## Two kinds of veto

The distinction that most teams miss, and the reason two gates can coexist
without deadlocking:

| | Judgment veto | Fact veto |
|---|---|---|
| Example | `security-reviewer` | `verifier` |
| Basis | Expertise | Tool output |
| Needs evidence | **Yes, mandatory** — a block without a citation is an opinion | It *is* evidence |
| Can be overridden | By a human, on the record | No — fix it |
| Miscalibration looks like | Blocks everything, or nothing | Flaky, then ignored |

A third veto deadlocks the team. Both examples state which role was *not* given
one, and why.

---

## Templates

| Template | For |
|---|---|
| [`AGENT.template.md`](templates/AGENT.template.md) | One agent definition — all ten fields, with prompts for each |
| [`HANDOFF.template.md`](templates/HANDOFF.template.md) | One seam — Fixed / Open / Forbidden / Acceptance |
| [`TEAM.template.md`](templates/TEAM.template.md) | The whole team on one page, including the four justification tests |

Agent definitions use the Claude Code `.claude/agents/*.md` frontmatter format,
so the examples drop straight into a project. The method is
runtime-agnostic — only the frontmatter is specific.

---

## The twelve anti-patterns

Each one in [chapter 7](docs/07-anti-patterns.md) with symptom, cause and fix.

| | | |
|---|---|---|
| The committee | No verifier | The author approves their own work |
| Everyone has every tool | The decorative veto | The infinite loop |
| "Be helpful" | Context stuffing | The agent that should be a script |
| Silent retry | The orchestrator that does the work | Copying a team you found |

If you are debugging a team right now, the fastest three checks are:
**is there a verifier?** · **does the veto ever fire?** · **is any role invoked
almost never?**

---

## The one question

If you keep nothing else from this playbook:

> **When your team last shipped something wrong — which role should have caught
> it, and why didn't it?**

- *"No role was supposed to catch it"* → a missing role
- *"That role exists but had no context"* → a handoff problem
- *"That role caught it and was overruled"* → a veto problem

Three diagnoses in one question, and it works on any team.

---

## Contents

```
docs/
  01-when-not-to-build-a-team.md      four tests, and the checklist test
  02-cutting-a-project-into-roles.md  where the boundaries go
  03-the-agent-spec.md                ten fields, field by field
  04-choosing-a-model-tier.md         irreversibility, not prestige
  05-handoff-contracts.md             Fixed / Open / Forbidden / Acceptance
  06-permissions-and-veto.md          least privilege, two kinds of veto
  07-anti-patterns.md                 twelve, with fixes
  08-is-your-team-working.md          five numbers
templates/
  AGENT.template.md · HANDOFF.template.md · TEAM.template.md
examples/
  web-product-team/     6 agents, 2 handoffs, full reasoning
  backend-api-team/     6 agents, 1 handoff, full reasoning
```

---

**Licence** · MIT — copy the templates, copy the teams, copy the method.

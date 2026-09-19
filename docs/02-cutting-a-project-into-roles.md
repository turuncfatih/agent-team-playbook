# 2. Cutting a project into roles

You decided a team is justified. Now the only question that matters:

> **Where do the cuts go?**

Most teams are cut badly, and a badly cut team cannot be fixed by better
prompts. It has to be re-cut.

## The wrong cuts

### Cut by job title

The most common mistake, because it feels natural. Your company has a frontend
developer and a backend developer, so your team has a `frontend-agent` and a
`backend-agent`.

Job titles exist for hiring, career progression and payroll. None of those are
reasons to split a system. A title is a *bundle* of responsibilities that made
sense for a human with a career — an agent has neither.

### Cut by seniority

`senior-dev` and `junior-dev` produce the same artifact with the same
permissions. That is one role with a model-tier decision attached
(see [chapter 4](04-choosing-a-model-tier.md)), not two roles.

### Cut by technology

`react-agent`, `css-agent`, `typescript-agent`. Same write permission, same
artifact, same failure mode, same context. One role.

### Cut by task

One agent per thing to do. This is how teams grow to nine agents and start
losing more to handoffs than they gain from specialisation.

## The right cuts

Cut along the four lines where a boundary actually buys you something.

### 1. Write permission

**Who is allowed to change the repository?**

This is the most important line in the whole design. An agent that can write and
an agent that can only read are fundamentally different risks, and they should
never be the same role. In a well-cut team, usually **one or two** roles can
write. Everyone else reads and reports.

### 2. Type of judgment

| Judgment | Question it answers |
|---|---|
| Taste | "Is this good?" |
| Correctness | "Does this work?" |
| Compliance | "Is this allowed?" |

These three need different context, different prompts and — genuinely —
different model tiers. A role that mixes them will be mediocre at all three,
because the prompt has to hedge.

### 3. Failure mode caught

Every reviewer exists to catch **one kind of mistake**. Name it:

- `security-reviewer` catches "this is unsafe to ship"
- `verifier` catches "this does not actually run"
- `seo-auditor` catches "this will not be found"

If you cannot name the failure mode a role catches, that role is decoration.
Two roles that catch the same failure are one role.

### 4. Context need

Roles that need wildly different context should be separate, because context is
the scarcest resource in the system. A content writer needs brand voice and
audience. An implementer needs file structure and conventions. Merging them
means every invocation carries both, and both get worse.

## A worked example

**Brief:** build a marketing site for a local service business.

### The bad cut — nine agents

```
planner · researcher · copywriter · seo-specialist · designer
react-developer · css-developer · image-optimiser · deployer
```

What is wrong:

- `react-developer` and `css-developer` — same write permission, same artifact. **Merge.**
- `image-optimiser` — deterministic. **This is a script.**
- `deployer` — deterministic. **A script, or a CI step.**
- `researcher` and `copywriter` — researcher produces notes that only the
  copywriter reads. That is not an artifact, it is a paragraph in a prompt. **Merge.**
- `seo-specialist` — catches a real, distinct failure mode. **Keep.**
- No role can say no. **Nothing here is a gate.**

Nine roles, four of them fictional, and it fails the veto test.

### The good cut — five agents

| Role | Artifact | Writes? | Judgment | Catches |
|---|---|:---:|---|---|
| `tech-lead` | The plan | ✗ | — | wrong shape of work |
| `designer` | Design spec | ✗ | taste | "this looks generic" |
| `content-writer` | Page copy | ✗ | taste | "this says nothing" |
| `frontend-dev` | Working pages | ✅ | correctness | — |
| `verifier` | Pass/fail report | ✗ | correctness | **"this does not actually run"** |

Five roles. One writer. One veto. Two roles (`designer`, `content-writer`) that
can work in parallel. Passes all four tests from [chapter 1](01-when-not-to-build-a-team.md).

`seo-auditor` is a legitimate sixth — it catches a distinct failure mode — and
is added in the [web product team example](../examples/web-product-team/).

## Sizing

| Agents | Verdict |
|---|---|
| 1–2 | Usually right. Do not add more without a reason you can name. |
| 3–6 | The useful range. Most real teams live here. |
| 7+ | Almost always a bad cut. Look for merged artifacts and fictional roles. |

The limit is not a style preference. Every additional role is another handoff,
another prompt to keep consistent, another place for context to be dropped, and
another invocation to pay for.

## The final check

Write the team as a one-line sentence:

> *"The **tech-lead** plans; the **designer** and **content-writer** work in
> parallel; the **frontend-dev** builds; the **verifier** can stop the release."*

If that sentence needs an "and also", or a role has no verb, the cut is wrong.

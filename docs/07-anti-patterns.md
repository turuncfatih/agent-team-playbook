# 7. Anti-patterns

A catalogue. Each entry: how it looks from outside, why it happened, and the fix.

---

## 1. The committee

**Symptom.** Nine agents. Every one is invoked on every task. Runs are slow,
expensive, and the output is blander than a single agent would produce.

**Why.** The team was cut by task rather than by boundary
([chapter 2](02-cutting-a-project-into-roles.md)). Adding a role feels like
progress; it is measurable, and it looks like architecture.

**Fix.** Apply the artifact test. Merge every pair producing the same artifact.
Delete every role that produces "input for the next agent" rather than an
artifact. Expect to land at four or five.

---

## 2. No verifier

**Symptom.** The team reports success. The build is broken. Nobody noticed
because nobody ran it.

**Why.** Every role in the team *produces* something. Producing feels like the
work; checking feels like overhead. So the checking role is the one that never
gets written.

**Fix.** Add a verifier with a fact veto. It builds, runs and reports. It writes
nothing. If you add exactly one role to a struggling team, add this one — it is
the highest-value role in this playbook.

---

## 3. The author approves their own work

**Symptom.** The implementer finishes, declares it correct, and it ships. Review
findings are suspiciously rare.

**Why.** It is one fewer handoff, and the implementer has the most context, so
it seems efficient.

**Fix.** Separate write from approve, structurally. The reviewer must be a role
that did not produce the artifact, and the orchestrator must not accept an
approval from the author. See [chapter 6](06-permissions-and-veto.md).

---

## 4. Everyone has every tool

**Symptom.** Every agent's spec lists the full tool set, "just in case".

**Why.** Copy-paste from the first agent that needed them, plus a reluctance to
debug a blocked call later.

**Fix.** Grant the minimum per role, and state the notable denials out loud. The
permission table should look lopsided — usually one writer. A designer with
`Write` will eventually edit a file, and then two roles own the same code.

---

## 5. The decorative veto

**Symptom.** A security reviewer has run for two months and never blocked
anything. Or it blocks every single round.

**Why.** Severity was never calibrated. Without an explicit bar, a model either
reserves the top level for catastrophe (never fires) or applies it to everything
it dislikes (always fires).

**Fix.** Define the blocking level in one sentence — "unsafe to ship, with
evidence" — and require a citation for every block. Then watch the rate: 10–30%
of rounds is healthy. Zero means it is decoration; most rounds means the bar is
wrong.

---

## 6. The infinite loop

**Symptom.** Reviewer blocks, writer revises, reviewer blocks again. Round six.
The budget is gone and the objection has not changed.

**Why.** The rework path was designed; the limit was not.

**Fix.** Cap rework at two or three rounds, then escalate to a human.
Escalation is a legitimate outcome, not a failure. A loop that has not converged
in three rounds will not converge in six.

---

## 7. "Be helpful"

**Symptom.** Agent specs read like personality descriptions. *"You are an
experienced senior developer who cares deeply about quality."*

**Why.** Prompt-writing habits from chat, carried into system design.

**Fix.** Replace each adjective with a checkable clause. "Cares about quality"
becomes a definition of done someone else can verify
([chapter 3](03-the-agent-spec.md)). Experience is not a specification.

---

## 8. Context stuffing

**Symptom.** Every agent receives the entire project context. Output quality
drops as the project grows, and nobody can see why.

**Why.** It is easier to pass everything than to decide what each role needs,
and irrelevant context does not throw an error.

**Fix.** Per-role input lists. If an input appears in every role's list, it is
project context, not agent context. Removing irrelevant context measurably
improves output — this is the cheapest quality win available.

---

## 9. The agent that should be a script

**Symptom.** An agent counts words, validates a schema, or checks every image
has alt text. It is slow, costs money, and occasionally disagrees with itself.

**Why.** Once a team exists, every task looks like an agent-shaped task.

**Fix.** Deterministic work is a script. Keep the agent for the part that needs
judgment: **the script checks, the agent explains the result and decides what to
do about it.**

---

## 10. Silent retry

**Symptom.** A run cost three times the usual and nobody can say why.

**Why.** A failure was retried inside the agent, or a tier was escalated
implicitly, and neither was recorded.

**Fix.** Retries and escalations are events. Log them, count them, and carry the
cost of failed attempts into the total — otherwise the most expensive run looks
like the cheapest one.

---

## 11. The orchestrator that does the work

**Symptom.** The tech-lead role has grown tools, and now plans *and* implements
"the simple parts".

**Why.** Routing a trivial change feels wasteful, so the orchestrator handles it
"just this once", and once generalises.

**Fix.** The orchestrator plans and routes. It holds no tools. If routing a
trivial change is genuinely too expensive, the answer is a rule that skips the
team entirely — not an orchestrator with side effects.

---

## 12. Copying a team you found

**Symptom.** A team of roles that do not match the actual work, with two roles
that are never invoked.

**Why.** A published example looked complete.

**Fix.** Copy the *method*, not the roster. The examples in this repository are
worked answers to specific briefs — including the reasoning for each cut, so you
can redo the reasoning for yours. Start from [chapter 1](01-when-not-to-build-a-team.md).

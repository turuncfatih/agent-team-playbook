#!/usr/bin/env python3
"""Repository hygiene checks.

Two things a documentation repository cannot afford to get wrong:

  1. A broken internal link.
  2. An example that does not obey the spec the repository itself defines.

Both are checked here and enforced in CI.
"""

from __future__ import annotations

import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent

REQUIRED_SECTIONS = [
    "## Role",
    "## Invoke / do not invoke",
    "## Inputs",
    "## Output contract",
    "## Tools",
    "## Model tier",
    "## Definition of done",
    "## Veto",
    "## Failure & escalation",
    "## Anti-goals",
]


def markdown_files() -> list[pathlib.Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def check_links() -> list[str]:
    """Every relative link must resolve to a file that exists."""
    problems, checked = [], 0

    for md in markdown_files():
        for match in re.finditer(r"\[([^\]]*)\]\(([^)]+)\)", md.read_text()):
            target = match.group(2).split("#")[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue

            checked += 1
            resolved = (md.parent / urllib.parse.unquote(target)).resolve()
            if not resolved.exists():
                problems.append(f"{md.relative_to(ROOT)} -> {target}")

    print(f"links:  {checked} relative links checked, {len(problems)} broken")
    return problems


def check_agent_specs() -> list[str]:
    """Each example agent must satisfy the ten-field spec from docs/03."""
    problems = []
    files = sorted(ROOT.glob("examples/*/agents/*.md"))

    for agent in files:
        text = agent.read_text()
        where = agent.relative_to(ROOT)

        if not text.startswith("---\n"):
            problems.append(f"{where}: no frontmatter")
            continue

        frontmatter = text.split("---\n")[1]

        name = re.search(r"^name:\s*(\S+)", frontmatter, re.M)
        if name is None:
            problems.append(f"{where}: frontmatter has no 'name'")
        elif name.group(1) != agent.stem:
            problems.append(f"{where}: name '{name.group(1)}' does not match the filename")

        if not re.search(r"^description:\s*\S", frontmatter, re.M):
            problems.append(f"{where}: frontmatter has no 'description'")

        for section in REQUIRED_SECTIONS:
            if section not in text:
                problems.append(f"{where}: missing '{section}'")

    print(f"agents: {len(files)} agent specs checked, {len(problems)} problems")
    return problems


def main() -> int:
    problems = check_links() + check_agent_specs()

    if problems:
        print("\nFAILED:")
        for problem in problems:
            print(f"  {problem}")
        return 1

    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

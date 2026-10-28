# CLAUDE.md

## Session start

When working in a local checkout of this repo, start every session by pulling from origin (`git pull origin main`) so you work on the latest skills.

## Plugin

The repo is also a Claude Code plugin (`vaimo-skills`) and its own marketplace, in `.claude-plugin/`. The skill folders stay at the root because project repos mount this repo as the `.claude/skills` submodule. When you add, rename or remove a skill folder, update the `skills` list in `.claude-plugin/plugin.json` and bump its `version`, then run `claude plugin validate .`.

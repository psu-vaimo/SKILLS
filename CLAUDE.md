# CLAUDE.md

## Session start

When working in a local checkout of this repo, start every session by pulling from origin (`git pull origin main`) so you work on the latest skills.

## Layout

This repo is a Claude Code marketplace (`psu-vaimo`, in `.claude-plugin/marketplace.json`) with its plugins under `plugins/`. The `vaimo-skills` plugin has its manifest in `plugins/vaimo-skills/.claude-plugin/plugin.json` and one folder per skill in `plugins/vaimo-skills/skills/`.

- A new skill is a new folder `plugins/vaimo-skills/skills/<name>/` with a `SKILL.md`. Skills in that folder are picked up without listing them.
- Bump `version` in `plugin.json` with every change to the plugin, or installed copies won't update.
- A new plugin gets its own folder under `plugins/` and an entry in `marketplace.json`.
- Run `claude plugin validate .` and `claude plugin validate plugins/<name>` before committing.

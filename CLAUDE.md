# CLAUDE.md

## Session start

When working in a local checkout of this repo, start every session by pulling from origin (`git pull origin main`) so you work on the latest skills.

## Layout

This repo is a Claude Code marketplace (`pontus`, in `.claude-plugin/marketplace.json`) with its plugins under `plugins/`:

- `routine`: the project working routine (daily, worklog, jira, pen, ord, proj).
- `pxm`: product information consulting (abilities, data-audit, data-model, discovery-report).

Each plugin has its manifest in `plugins/<plugin>/.claude-plugin/plugin.json` and one folder per skill in `plugins/<plugin>/skills/`.

- A new skill is a new folder `plugins/<plugin>/skills/<name>/` with a `SKILL.md`. Skills in that folder are picked up without listing them.
- Bump `version` in the plugin's `plugin.json` with every change to it, or installed copies won't update.
- A new plugin gets its own folder under `plugins/` and an entry in `marketplace.json`.
- Run `claude plugin validate .` and `claude plugin validate plugins/<plugin>` before committing.

# SKILLS

Pontus Sundén's shared Claude Code skills, published as the `psu-vaimo` plugin marketplace.

## Plugins

- **vaimo-skills**: the project working routine. `daily` (start and end of day), `worklog` (rebuild and log the day's time), `jira`, `pen` (notes in the NOTES repo), `ord` (the Ord note format) and `proj` (how projects are organised).

## Install

```bash
claude plugin marketplace add psu-vaimo/SKILLS
claude plugin install vaimo-skills@psu-vaimo
```

Skills are then available as `/vaimo-skills:daily` and so on. Update with:

```bash
claude plugin marketplace update psu-vaimo
claude plugin update vaimo-skills@psu-vaimo
```

New skills and changes take effect in the next session.

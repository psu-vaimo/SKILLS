# claude

Pontus Sundén's Claude Code plugins, published as the `pontus` plugin marketplace.

## Plugins

- **routine**: the project working routine. `daily` (start and end of day), `worklog` (rebuild and log the day's time), `jira`, `pen` (notes in the NOTES repo), `ord` (the Ord note format) and `proj` (how projects are organised).
- **pxm**: product information (PX/PXM/PIM) consulting. `px-analyst` (discovery analysis and the ability model), `px-data-audit` (profiling client exports), `px-data-model` (designing the product data model) and `vaimo-pim-discovery-report` (writing the discovery report).

## Install

```bash
claude plugin marketplace add psu-vaimo/claude
claude plugin install routine@pontus
claude plugin install pxm@pontus
```

Skills are then available as `/routine:daily`, `/pxm:px-data-audit` and so on. Update with:

```bash
claude plugin marketplace update pontus
claude plugin update routine@pontus
claude plugin update pxm@pontus
```

New skills and changes take effect in the next session.

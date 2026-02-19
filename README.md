# Modframe — Structural Map of Federal Power

A structural and mechanical map of how Washington DC federal government power actually works.

**14 sections. 230 modules. 147 built.**

## What this maps

| Section | Topic | Modules | Status |
|---------|-------|---------|--------|
| 01 | Electoral Power Structures | 17 | Built |
| 02 | Congressional Power Mechanics | 25 | Built |
| 03 | Executive Branch Incentives | 23 | Built |
| 04 | Revolving Door and Influence | 23 | Built |
| 05 | Media Ecosystem and Information Architecture | 19 | Built |
| 06 | Judicial Power Structure | 20 | Built |
| 07 | State-Level Power Laboratories | 20 | Built |
| 08 | Money and Industry Influence | 17 | Scaffold |
| 09 | Crisis Governance | 15 | Scaffold |
| 10 | Structural Incentives Behind Polarization | 6 | Scaffold |
| 11 | Accountability and Transparency Gaps | 15 | Scaffold |
| 12 | Foreign Influence and Global Intersections | 10 | Scaffold |
| 13 | Meta-Incentive Structures | 10 | Scaffold |
| 14 | Emerging and Overlooked Structures | 10 | Scaffold |

See `docs/SECTION_AND_MODULE_MAP.md` for the full module listing and future expansion roadmap (~380 financial system module ideas, 45 domain-applied sections).

## What each module contains

Each built module includes:
- **Summary** — what the mechanism is and why it matters
- **Mechanism in one sentence** — the operational lever
- **Actors and roles** — who exercises power, tagged by type
- **Process map** — step-by-step how it works
- **Where power concentrates** — structural bottlenecks
- **Common failure modes** — how accountability breaks down
- **Evidence tests** — `[Observed]`, `[Inferred]`, `[Hypothesis]` with citations
- **Suggested sources** — statutes, cases, datasets, agency records
- **Episode outline** — 6-part structure for media activation

## Repository structure

- `topics/` — one folder per section, one subfolder per module
- `docs/` — contribution standards, module template, content agent guide, prompts, schemas
- `scripts/` — validators, index builders, queue generator

## How to use this

Browse `topics/` by section number. Each module folder contains `README.md` (metadata) and `outline.md` (the full explainer).

## Principles

- **Structural, not partisan** — explain mechanics, incentives, and constraints
- **Citation-forward** — every factual claim tagged and traceable
- **Composable** — modules stand alone and combine for event coverage

## License

Content is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
See `LICENSE`.

## Contributing

Start with `docs/CONTRIBUTING.md` and `docs/MODULE_TEMPLATE.md`.

## Quality checks

```bash
python3 scripts/validate_metadata.py
python3 scripts/validate_completeness.py --warn-only
python3 scripts/build_indexes.py
```

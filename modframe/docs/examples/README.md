# Golden Examples

This folder holds reference modules showing what `sourced`-quality content looks like.
Use these when calibrating drafts, running neutrality passes, or onboarding new contributors.

## Current examples

| Module | Section | Status | Sources |
| ------- | --------- | ------- | ------- |
| [001_Campaign_Finance_Architecture](001_Campaign_Finance_Architecture/outline.md) | 01 Electoral | sourced | 7 (FECA, Buckley, Citizens United, McCutcheon, OpenSecrets, FEC stats, CRS) |
| [002_Primaries_and_Candidate_Gatekeeping](002_Primaries_and_Candidate_Gatekeeping/outline.md) | 01 Electoral | sourced | 7 (CA Dem v. Jones, NCSL, Ballotpedia, Hall 2019, Brookings, DNC/RNC rules) |
| [003_Gerrymandering_Systems](003_Gerrymandering_Systems/outline.md) | 01 Electoral | sourced | 7 (Rucho, VRA §10301, Allen v. Milligan, Stephanopoulos/McGhee, NCSL, Princeton GP, Dave's) |

These are copies of their counterparts in `topics/`. When the topic versions advance to
`reviewed` or `published`, update the copies here.

## What to use them for

- **Calibration before drafting** — read an example before filling `draft_module.md`
  prompt variables; notice how claim labels are applied, how process steps are scoped,
  how sources are formatted
- **Prompt grounding** — paste an example outline as context when instructing a model
  to draft a new module in the same style
- **Reviewer reference** — when running `neutrality_pass.md`, compare the candidate
  module's tone and structure to the examples

## Metadata expectation (MVP)

Golden examples should also demonstrate README metadata completeness:

- `Related modules`
- `Last reviewed`
- `Actors`
- `Statutes`
- `Cases`

Use `python scripts/validate_metadata.py --status sourced --warn-only` before promoting
an example copy.

## Selection criteria for future examples

A module should replace or join this set when it:

1. Is `reviewed` or `published` status
2. Has ≥ 5 real citations, all tier-1 or tier-2 (see `docs/CITATIONS.md`)
3. Has passed both the neutrality and final polish passes
4. Covers a different section than existing examples (aim for cross-section diversity)

## File structure

```text
docs/examples/
  NNN_Topic_Name/
    README.md    (copied from topics/ at time of promotion)
    outline.md   (copied from topics/ at time of promotion)
```

# Modframe Wall Street (Stub)

A focused variant of the Modframe approach for financial-system power mechanics.

## Core idea

Translate the Modframe methodology (mechanism-first, actor/incentive mapping, citation-forward explainers) into a Wall Street / market-structure domain.

## What this project will explain

- How power concentrates across capital markets, banking, asset management, and market infrastructure
- Which actors control access, pricing, information, and enforcement pathways
- Where structural bottlenecks and veto points emerge
- What datasets, filings, statutes, and case law can validate each claim

## Scope (initial)

- Nonpartisan, structural analysis
- U.S.-focused first, optional international comparisons later
- Modular topic library format (one mechanism per module)

## Candidate section map (v0)

1. Market Structure & Plumbing
2. Banking Power Channels
3. Asset Management & Passive Concentration
4. Regulatory Architecture & Capture Risks
5. Corporate Governance Control Systems
6. Information Asymmetry & Data Power
7. Crisis Liquidity & Backstop Mechanisms

## Intended output format

Each module should include:

- Summary
- Mechanism in one sentence
- Actors and roles
- Process map
- Where power concentrates
- Common failure modes
- Evidence tests
- Suggested sources
- Episode outline

## Source priority (draft)

1. Primary legal/regulatory sources (SEC, CFTC, OCC, FRB, FDIC, FINRA, statutes, rules)
2. Official datasets/filings (EDGAR, call reports, Form ADV, 13F, TRACE where available)
3. Court opinions, enforcement actions, inspector reports
4. High-quality investigative/academic secondary sources

## What this repository contains

- `topics/` — the skeletal map: one folder per section, containing topic modules
- `docs/` — contribution standards, module template, governance, style constraints, and the full section/module map
- `scripts/` — validators, queue generator, index builder, and other tooling

## How to use this

- Browse `topics/` by section.
- Each topic module should contain:
  - `README.md` (what this module is)
  - `outline.md` (structured explainer outline + source targets)
  - optional `figures/` for visuals
- See `docs/SECTION_AND_MODULE_MAP.md` for the full unabridged list of candidate modules.

## Local quality checks

Run these before opening a PR:

- `python scripts/validate_topic_names.py`
- `npx markdownlint-cli2 "**/*.md"`

## Next setup steps

- Finalize module list, assign IDs, and create topic folder scaffolds
- Build one golden example module before scaling
- Port CI workflow

## Naming note

Current working name: `modframe_wallstreet`.
Alternatives: `modframe_dc_wallstreet`, `modframe_markets`, or `modframe_finance`.

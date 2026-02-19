# MVP Branch Plan — Metadata-Aware Module Factory

This plan adds machine-readable metadata to the existing content workflow without
breaking current authoring velocity.

## Branch objective

Upgrade the module pipeline from prose-only outputs to prose + structured metadata,
while preserving the current `CONTENT_AGENT.md` loop.

## Phase 1 (this MVP)

1. Add metadata contract to schemas and templates
2. Add metadata validator script
3. Integrate metadata signal into queue prioritization
4. Add non-blocking CI metadata check (`--warn-only`)
5. Update prompts and `CONTENT_AGENT.md` so coder LLMs emit metadata by default

### Phase 1 acceptance criteria

- Metadata fields documented in `docs/schemas/readme_schema.json`
- `python scripts/validate_metadata.py` runs across all topics
- `python scripts/generate_queue.py` includes metadata completeness penalty
- CI includes metadata validation in warn-only mode
- `docs/MODULE_TEMPLATE.md`, `docs/prompts/*.md`, and `docs/CONTENT_AGENT.md`
  include explicit metadata production steps

## Phase 2 (next)

1. Add `scripts/build_indexes.py` to generate:
   - `docs/indexes/actors.json`
   - `docs/indexes/statutes.json`
   - `docs/indexes/cases.json`
   - `docs/indexes/related_modules.json`
2. Add strict CI mode for `sourced+` modules once metadata coverage > 80%
3. Add metadata examples to `docs/examples/`

## Phase 3 (next)

1. Add staleness queue (`last_reviewed` + legal citation volatility)
2. Add auto-suggest links (`related_modules`) based on citations and actor overlap
3. Add API-ready export (`queue.json` + index bundle)

## Implementation status (2026-02)

- Phase 1: implemented
- Phase 2: implemented (index builder, prompt/template updates, metadata examples)
- Phase 3: implemented MVP slice (staleness queue, related-module suggester, API-ready queue/index outputs)

## Operational model (coder LLM)

The coder LLM continues to be instructed by `docs/CONTENT_AGENT.md`.
The only behavior change: after citation pass, it must add/update README metadata
and run metadata validation before setting/keeping `Status: sourced`.

## Risk controls

- Keep metadata CI in warn-only mode initially
- Do not fail `draft` creation on metadata completeness
- Enforce strict mode later by status gate (`sourced+`)

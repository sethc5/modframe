# Governance

Goal: keep the library broadly trusted and difficult to capture ideologically.

## Editorial principles

- Structural mechanics first.
- Prefer primary sources.
- Make uncertainty explicit.

## Module lifecycle

Each module progresses through defined states. The current state is tracked in the
`Status:` field of `README.md`. Valid values are enforced by `scripts/validate_completeness.py`.

| State | Definition | Who can advance it |
| ----------- | ------------------------------------------------- | ------------------- |
| `empty` | Folder and template files exist; no real content | Any contributor |
| `scaffolded` | Placeholder prose replaced with intent notes | Any contributor |
| `draft` | All sections have substantive prose; all claims carry `[Observed]`/`[Inferred]`/`[Hypothesis]` labels | Any contributor |
| `sourced` | Every `[Observed]` claim has a matching entry in Suggested Sources | Any contributor |
| `reviewed` | A second contributor (not the draft author) has verified tone and sourcing | Reviewer |
| `published` | Module is considered stable; material changes require a new PR | Maintainer merge |

### Transition rules

- Any contributor may move a module forward through `empty` → `sourced` in a single PR if they complete all required work.
- `reviewed` requires a PR approval from a contributor who did not author the current draft content.
- `published` requires maintainer merge (see `docs/MAINTAINERS.md`).
- Modules may move backward (e.g., `published` → `sourced`) if a factual correction requires removing a claim that lacks a valid source.

### Completeness gates

The CI workflow runs `scripts/validate_completeness.py --warn-only` on every PR.
Remove `--warn-only` once a meaningful fraction of modules are in `draft` or later —
at that point the check becomes a hard gate.

## Change control

- Major structural changes (taxonomy, naming, numbering) must be proposed in a PR with rationale.
- Module content can be iterated freely, but the PR description must note what changed and why.
- New sections (numbered folders under `topics/`) require maintainer approval.

## Conflicts of interest

Contributors must disclose relevant conflicts of interest (employment, financial ties,
advocacy affiliations) when working on modules where it matters. Include the disclosure
in the PR description under "Conflict of interest". "None" is a complete and acceptable answer.

## Anti-capture measures

- No module may advocate for a policy outcome. Describing a failure mode is allowed;
  prescribing a remedy is not (except in the "Levers" episode outline section, which
  describes existing reform mechanisms neutrally).
- If a section of the taxonomy persistently lacks contributions from one political
  tendency's perspective, maintainers should flag it and seek balance.
- The claim type system (`[Observed]`, `[Inferred]`, `[Hypothesis]`) is the primary
  technical defense against unsupported assertions entering the library.

## Golden examples

Three fully-complete modules should be maintained in `docs/examples/` as reference outputs.
These serve as the ground truth for what `published` looks like. See `docs/examples/README.md`
for selection criteria.

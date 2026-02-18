# Golden Examples

This folder holds 3 fully-complete, `published`-status modules that serve as the
reference standard for all content work. When in doubt about what a finished module
looks like, use these.

## Purpose

- **Ground truth** for what `published` means in practice
- **Training material** for contributors and model prompts
- **Calibration** for the neutrality and citation passes

## Selection criteria

A golden example module must:

1. Cover a mechanism that is well-documented in primary sources (not contested or data-sparse)
2. Have ≥ 5 real citations, all tier-1 or tier-2 (see `docs/CITATIONS.md`)
3. Have passed both the neutrality pass and final polish pass
4. Have been reviewed by at least two contributors
5. Represent different sections of the taxonomy (not all from the same section)

## Status

No golden examples have been designated yet. The first three modules to reach `reviewed`
status and be approved by a maintainer will be copied here (or symlinked) and designated
as golden examples.

Candidates for first golden examples (high source availability, well-documented mechanisms):

- `001_Campaign_Finance_Architecture` (01 Electoral)
- `028_Congressional_Committee_Power` or similar (02 Congressional)
- `056_Revolving_Door_Mechanics` or similar (04 Revolving Door)

## File structure

Each golden example lives in its own subfolder mirroring the topic structure:

```text
docs/examples/
  001_Campaign_Finance_Architecture/
    README.md       (copy from topics/, Status: published)
    outline.md      (fully drafted, sourced, reviewed)
  ...
```

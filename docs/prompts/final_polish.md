# Prompt Pack: Final Polish

**Task type:** Prose quality and consistency pass
**Moves module from:** `reviewed` → `published`
**Input variables:** Replace all `{{VARIABLE}}` blocks before sending.
**Note:** Run after neutrality pass is complete. Do not run on modules still in `draft` or `sourced`.

---

## How to use this prompt

1. Run `python scripts/generate_queue.py --status reviewed` to find reviewed-stage topics.
2. Copy the topic's `outline.md` into `{{OUTLINE_MD}}` below.
3. Fill `{{TOPIC_NAME}}`.
4. Send to the model.
5. Apply revisions. Do a final human read.
6. Set `Status: published` in `README.md`.

---

## Prompt

You are doing a final polish pass on a module that has already passed content, citation, and neutrality review. Your job is prose quality and internal consistency — not content changes. Do not alter claim types, remove sources, restructure sections, or change the substance of any claim.

**Topic:** {{TOPIC_NAME}}

---

### What to fix

**A. Prose clarity**
- Replace jargon with plain equivalents where possible (without losing precision).
- Break sentences longer than 35 words into two.
- Ensure each bullet point in bulleted sections starts with a concrete subject (not "It" or "This").

**B. Consistency**
- Actor names used consistently throughout (e.g., don't alternate "FEC" and "the Commission").
- Claim type labels (`[Observed]`, `[Inferred]`, `[Hypothesis]`) formatted exactly as specified — square brackets, title case.
- Tense is consistent within each section (present tense preferred for describing ongoing structures).

**C. Summary and mechanism sentence**
- Summary must be 3–5 sentences, no longer.
- Mechanism sentence must be ≤ 30 words and self-contained (readable without context).
- Neither should repeat verbatim from the other.

**D. Episode outline**
- Each of the 6 parts should be 1–3 sentences describing what content goes in that segment.
- Part 3 (Example) should name a real, specific case study — not a generic placeholder.
- Part 5 (Levers) should name at least two concrete accountability or reform mechanisms.

**E. Glossary alignment**
- Terms that appear in `docs/GLOSSARY.md` should be used with their glossary definitions.
- Do not introduce new technical terms without defining them inline.

---

### Output format

Return the complete, polished `outline.md` in Markdown. After the document, append a brief change log:

```
---
## Changes made
- [Brief list of what was changed and why]
```

**Current outline.md:**

```
{{OUTLINE_MD}}
```

---

## Pre-publish checklist

- [ ] Summary is 3–5 sentences, original, not copied verbatim from any source
- [ ] Mechanism sentence is ≤ 30 words and self-contained
- [ ] Episode outline Part 3 names a real case study
- [ ] Episode outline Part 5 names ≥ 2 concrete levers
- [ ] No sentences > 35 words
- [ ] All claim labels formatted correctly
- [ ] `Status: published` set in README.md
- [ ] PR description includes change log

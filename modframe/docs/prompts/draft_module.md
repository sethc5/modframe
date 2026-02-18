# Prompt Pack: Draft Module

**Task type:** Initial content draft
**Moves module from:** `scaffolded` → `draft`
**Input variables:** Replace all `{{VARIABLE}}` blocks before sending.

---

## How to use this prompt

1. Run `python scripts/generate_queue.py --next 1` to get the next topic to draft.
2. Copy the topic's `outline.md` into `{{OUTLINE_MD}}` below.
3. Fill `{{TOPIC_NAME}}`, `{{TOPIC_ID}}`, `{{SECTION_NAME}}`.
4. Send the completed prompt to the model.
5. Paste the model's output back into `outline.md`.
6. Set `Status: draft` in `README.md`.

---

## Prompt

You are drafting content for a nonpartisan, citation-forward library that explains political power mechanics in the United States. This is structural analysis, not opinion. Your job is to explain *how* systems work, *where* power concentrates, and *what incentives* drive behavior — not to evaluate whether outcomes are good or bad.

**Topic:** {{TOPIC_NAME}} (ID: {{TOPIC_ID}})
**Section:** {{SECTION_NAME}}

---

### Non-negotiable style rules

1. **Institutional, descriptive voice.** Write as a congressional research analyst would. No partisan language, no moralizing adjectives (e.g., avoid: corrupt, broken, radical, extreme, dangerous, failed).

2. **Explicit claim types.** Every factual claim must carry one of:
   - `[Observed]` — documented in primary sources (statutes, agency records, court opinions, GAO/OIG reports, official data). Attach a citation stub: `[Observed — source: TBD]` if you don't have the exact citation yet.
   - `[Inferred]` — follows logically from observed facts but is not directly documented. State the reasoning.
   - `[Hypothesis]` — plausible but unverified. State what evidence would confirm or refute it.

3. **No unsourced generalizations.** If you cannot label a claim, do not make it.

4. **Word count targets:**
   - Summary: 3–5 sentences (60–100 words)
   - Mechanism sentence: 1 sentence, ≤30 words
   - Actors and roles: 100–250 words total
   - Process map: minimum 4 steps, each 10–30 words
   - All other sections: 80–200 words each

---

### Your task

Fill in the outline below with real, substantive content. Replace every placeholder line. Do not add, remove, or rename any section headings — preserve the exact structure.

**Current outline.md:**

```
{{OUTLINE_MD}}
```

**Output:** Return the complete, filled `outline.md` in Markdown. Output only the document — no preamble, commentary, or explanation outside the document.

---

## Post-draft checklist (run before updating Status)

- [ ] No placeholder text remains (no "Step 1", "Briefly explain", etc.)
- [ ] All claims carry `[Observed]`, `[Inferred]`, or `[Hypothesis]` labels
- [ ] Summary is 3–5 original sentences
- [ ] Process map has ≥ 4 steps
- [ ] Suggested sources lists ≥ 3 entries (stubs are OK at this stage)
- [ ] No partisan or moralizing language

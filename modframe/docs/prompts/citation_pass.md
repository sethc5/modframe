# Prompt Pack: Citation Pass

**Task type:** Citation review and enrichment
**Moves module from:** `draft` → `sourced`
**Input variables:** Replace all `{{VARIABLE}}` blocks before sending.

---

## How to use this prompt

1. Run `python scripts/generate_queue.py --status draft` to find draft-stage topics.
2. Copy the topic's `outline.md` into `{{OUTLINE_MD}}` below.
3. Fill `{{TOPIC_NAME}}`.
4. Send the completed prompt to the model.
5. Paste the model's output back into `outline.md`.
6. Verify at least 3 real sources exist and all `[Observed]` claims have a matching citation.
7. Set `Status: sourced` in `README.md`.

---

## Prompt

You are doing a citation pass on a draft module for a nonpartisan political power library. Your job is to find real, specific sources and attach them to claims. Do not change any prose or claim types unless the claim is demonstrably wrong — if so, flag it, do not silently alter it.

**Topic:** {{TOPIC_NAME}}

---

### Citation format (required for every entry in Suggested sources)

```
- [Full document title]. [Issuing body], [Month Year]. [URL or identifier].
```

Examples:
```
- Bipartisan Campaign Reform Act of 2002. 107th Congress, Pub. L. 107-155, 2002. https://www.congress.gov/107/plaws/publ155/PLAW-107publ155.pdf
- Campaign Finance Law Quick Reference. Federal Election Commission, 2023. https://www.fec.gov/legal-resources/
- Dark Money: The Hidden World of Tax-Exempt Groups. ProPublica, 2018. https://www.propublica.org/series/dark-money
```

---

### Source hierarchy (prefer earlier tiers)

1. **Primary (strongest):** U.S.C., C.F.R., Federal Register, court opinions (SCOTUS, circuit), agency guidance documents, GAO/OIG/CRS reports, official datasets (FEC, FARA, USASpending, Data.gov).
2. **Secondary (acceptable):** Reputable primary-source journalism (ProPublica, Reuters, AP, Bloomberg); peer-reviewed academic work with original data.
3. **Avoid:** Opinion pieces, advocacy reports (unless they cite tier-1 sources), Wikipedia, paywalled-only sources without free version noted.

---

### Your task

1. Review the outline below for every `[Observed]` claim.
2. For each `[Observed]` claim, add or improve the matching entry in **Suggested sources**.
3. If you cannot find a real tier-1 or tier-2 source for a claim:
   - Change `[Observed]` → `[Inferred]` or `[Hypothesis]` with a brief note explaining the downgrade.
   - Do not invent citations.
4. Ensure **Suggested sources** has at least 3 real, specific entries (not generic category headers).
5. Do not change headings, restructure sections, or alter prose beyond claim-type labels.

**Current outline.md:**

```
{{OUTLINE_MD}}
```

**Output:** Return the complete updated `outline.md` in Markdown. Output only the document — no preamble or commentary.

---

## Post-citation-pass checklist

- [ ] Every `[Observed]` claim has a matching source entry
- [ ] All source entries include: title, issuing body, date, and link/identifier
- [ ] No invented or unverifiable citations
- [ ] At least 3 sources in Suggested sources
- [ ] Any downgraded claims (Observed → Inferred/Hypothesis) are annotated with a reason

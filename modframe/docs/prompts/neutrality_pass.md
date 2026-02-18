# Prompt Pack: Neutrality Pass

**Task type:** Tone and framing review
**Moves module from:** `sourced` → `reviewed` (first gate)
**Input variables:** Replace all `{{VARIABLE}}` blocks before sending.
**Note:** This pass is ideally done by a contributor who did not write the draft (see GOVERNANCE.md).

---

## How to use this prompt

1. Run `python scripts/generate_queue.py --status sourced` to find sourced-stage topics.
2. Copy the topic's `outline.md` into `{{OUTLINE_MD}}` below.
3. Fill `{{TOPIC_NAME}}`.
4. Send to the model.
5. Review the model's flagged items and revise accordingly.
6. If no material issues found, set `Status: reviewed` in `README.md`.

---

## Prompt

You are doing a neutrality and framing review on a module for a nonpartisan political power library. The library's credibility depends on being usable by readers across the ideological spectrum. Your job is to identify framing, word choices, or structural imbalances that would cause a careful reader to perceive ideological bias.

**Topic:** {{TOPIC_NAME}}

---

### What to flag (be specific, quote the text)

**A. Partisan or loaded language**
Flag words or phrases that carry political valence beyond their descriptive content.
Examples to flag: "captured", "weaponized", "radical", "extreme", "protect", "exploit", "undermine" (when used evaluatively, not descriptively).
Examples that are fine: "conflict of interest", "principal-agent problem", "enforcement gap", "regulatory capture" (technical terms defined in GLOSSARY.md).

**B. Asymmetric treatment**
Flag if the module focuses on abuses or failure modes by actors associated with one political tendency while ignoring structurally similar behavior by others. The standard is: would a careful reader from the other side of the political spectrum find the framing balanced?

**C. Unsupported causal claims**
Flag any claim that asserts causation without evidence — especially when the claim implies blame or wrongdoing.

**D. Missing structural counterweights**
Flag if a section describes a mechanism that concentrates power without noting the formal checks, oversight mechanisms, or reform levers that exist (even if imperfect).

**E. Moralizing without evidence**
Flag language that implies the system *should* work differently rather than describing how it *does* work. Exception: "Episode outline — Levers" section may describe reform mechanisms neutrally.

---

### Output format

Return a structured review in this format:

```
## Neutrality Review: {{TOPIC_NAME}}

### Flagged items

**Item 1**
- Location: [section name, approximate line]
- Quoted text: "[exact quote]"
- Issue type: [A / B / C / D / E]
- Issue: [brief explanation]
- Suggested revision: [alternative phrasing, or "needs evidence"]

**Item 2**
...

### Overall assessment

[One paragraph: Is the module broadly neutral? What is the most important issue to address before marking as reviewed?]

### Verdict

[ ] Ready to mark as `reviewed` (no material issues)
[ ] Needs revision before `reviewed` (see flagged items above)
```

If no issues are found, say so explicitly and give the ready verdict.

**Current outline.md:**

```
{{OUTLINE_MD}}
```

---

## Post-neutrality-pass checklist

- [ ] All flagged items resolved or documented as accepted with rationale
- [ ] No language that implies partisan intent or moral judgment without evidence
- [ ] Failure modes section does not focus asymmetrically on one political tendency
- [ ] Episode outline — Levers section describes reform options neutrally

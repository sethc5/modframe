# Module Template

Copy this structure into a topic folder. See `docs/GOVERNANCE.md` for the full lifecycle
and `docs/prompts/` for prompts that drive each production stage.

---

## README.md

```text
# [Topic Name]

Purpose: [One sentence — what mechanic or structure this module explains.]

Status: empty

Tags: [comma-separated; see docs/schemas/readme_schema.json for recommended values]

Outline: see `outline.md`

Contributors: [names / links]

Related modules: [comma-separated 3-digit IDs, e.g., 001, 013, 017]
Last reviewed: [YYYY-MM]

Actors:
	- name: [Actor name]
		type: [regulatory_body | political_entity | institution | court | committee | office | dataset_owner]

Statutes:
	- [e.g., 52 U.S.C. § 30118]

Cases:
	- [e.g., Citizens United v. FEC, 558 U.S. 310 (2010)]

Case study:
	name: [specific event or package]
	date: [YYYY-MM or YYYY]
	actors:
		- [Actor A]
		- [Actor B]
	outcome: [one-sentence structural outcome]

Reform proposals:
	- name: [proposal name]
	  bill: [bill number or N/A]
	  congress: [e.g., 118th]
	  status: [introduced|committee|passed chamber|enacted|not advanced]
	  addresses_failure_mode: [which failure mode and how]

Data sources:
	- source: [dataset or reporting system]
	  format: [csv|json|api|pdf]
	  update_frequency: [daily|monthly|quarterly|annual|ad hoc]
	  url: [https://...]
	  accessibility: [open|registration|restricted]

How to contribute:

- Use docs/prompts/draft_module.md to generate initial content
- Add citations under "Suggested sources" in outline.md
- Propose visuals in figures/ and link from here
```

**Status field — controlled vocabulary** (see `docs/GOVERNANCE.md` for transition rules):

| Value | Meaning |
| ------- | --------- |
| `empty` | Folder exists; files are pure template |
| `scaffolded` | Headings present; intent notes replace placeholders |
| `draft` | All sections have substantive prose; claims labeled |
| `sourced` | All `[Observed]` claims have citations |
| `reviewed` | Second contributor verified tone and sourcing |
| `published` | Stable; changes tracked in PR descriptions |

---

## outline.md

```markdown
# [Topic Name]

**Summary:** 3–5 sentences explaining what this mechanism is, why it exists,
and why it matters for understanding financial-system power. Institutional, descriptive
voice — no partisan framing, no moral evaluation.

**Mechanism in one sentence:** ≤ 30 words. How the lever of power operates.

### Actors and roles

- [Actor A] — [role]; incentive: [what they gain]; constraint: [what limits them]
- [Actor B] — [role]; incentive: [what they gain]; constraint: [what limits them]
- [Oversight actor] — [role]; constraint: [what limits enforcement]

### Process map (bulleted)

- Step 1: [concrete action — who does it, what triggers it]
- Step 2: [next concrete action]
- Step 3: [next concrete action]
- Step 4: [outcome or next stage]

### Where power concentrates

- **Gatekeepers:** [who controls access or flow]
- **Bottlenecks:** [where delays or blockages occur structurally]
- **Veto points:** [who can stop or reverse the process]

### Common failure modes

- [Mode 1] — [Observed/Inferred/Hypothesis] — [explanation]
- [Mode 2] — [Observed/Inferred/Hypothesis] — [explanation]
- [Mode 3] — [Observed/Inferred/Hypothesis] — [explanation]

### What evidence would prove/disprove key claims

- [Dataset, audit, or record type that would confirm or refute the main claims]
- [What a contrary finding would look like]

### Suggested sources

- [Full title]. [Issuing body], [Date]. [URL or identifier].
- [Full title]. [Issuing body], [Date]. [URL or identifier].
- [Full title]. [Issuing body], [Date]. [URL or identifier].

### Episode outline (6 parts)

1. **Structure** — [1–2 sentences: what this mechanism is]
2. **Incentive** — [1–2 sentences: why actors behave as they do]
3. **Example** — [1–2 sentences: a specific, real case study — name it]
4. **Evidence** — [1–2 sentences: primary sources or data to show]
5. **Levers** — [1–2 sentences: ≥ 2 concrete accountability or reform mechanisms]
6. **Takeaway** — [1–2 sentences: what a reader should remember]
```

---

## Claim type labels

Every factual assertion must carry one of:

- `[Observed]` — documented in a primary source listed in Suggested sources
- `[Inferred]` — follows logically from observed facts; state the reasoning
- `[Hypothesis]` — plausible but unverified; state what would confirm or refute it

---

## Production workflow

1. `python scripts/generate_queue.py --next 1` — get next topic to draft
2. `docs/prompts/draft_module.md` — generate initial outline.md content
3. `docs/prompts/citation_pass.md` — verify and enrich sources
4. `docs/prompts/metadata_pass.md` — populate/normalize structured README metadata
5. `docs/prompts/linking_pass.md` — choose 3–6 high-confidence related module links
6. `python scripts/validate_metadata.py --status sourced --warn-only` — metadata quality check
7. `docs/prompts/neutrality_pass.md` — check for framing issues
8. `docs/prompts/final_polish.md` — prose quality pass
9. Open PR using `.github/PULL_REQUEST_TEMPLATE.md` checklist

# Prompt Pack: Metadata Pass

**Task type:** Structured metadata extraction and normalization  
**Runs after:** `citation_pass.md` and before setting `Status: sourced`  
**Input variables:** Replace all `{{VARIABLE}}` blocks before sending.

---

## How to use this prompt

1. Copy the module `README.md` into `{{README_MD}}`.
2. Copy the module `outline.md` into `{{OUTLINE_MD}}`.
3. Fill `{{TOPIC_NAME}}` and `{{TOPIC_ID}}`.
4. Send the completed prompt to the model.
5. Replace `README.md` with the returned output.
6. Run `python3 scripts/validate_metadata.py --status sourced --warn-only`.

---

## Prompt

You are extracting machine-readable metadata for a nonpartisan U.S. political power module.
Do not rewrite module prose. Only normalize and complete README metadata from evidence in the outline.

**Topic:** {{TOPIC_NAME}} (ID: {{TOPIC_ID}})

### Metadata format requirements

Return README with these fields present and valid:

- `Related modules:` comma-separated 3-digit IDs (3–6 entries, highest-confidence links)
- `Last reviewed:` `YYYY-MM`
- `Actors:` YAML-like list of objects:
  - `name`
  - `type` (`regulatory_body | political_entity | institution | court | committee | office | dataset_owner`)
- `Statutes:` YAML-like list of normalized legal identifiers
- `Cases:` YAML-like list of normalized case citations

Optional fields (include when evidence is present):

- `Case study:`
  - `name`
  - `date`
  - `actors` (list)
  - `outcome`
- `Reform proposals:` list of objects:
  - `name`
  - `bill`
  - `congress`
  - `status`
  - `addresses_failure_mode`
- `Data sources:` list of objects:
  - `source`
  - `format`
  - `update_frequency`
  - `url`
  - `accessibility`

### Rules

1. Prefer metadata directly supported by `outline.md` claims and Suggested sources.
2. Do not invent statutes, cases, actors, or bill IDs.
3. Keep entries concise and normalized.
4. Preserve all existing README fields and headings.
5. Do not change `Status` value in this pass.

**Current README.md:**

```markdown
{{README_MD}}
```

**Current outline.md:**

```markdown
{{OUTLINE_MD}}
```

**Output:** Return full updated `README.md` only.

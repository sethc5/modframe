# Prompt Pack: Linking Pass

**Task type:** Related-module graph linking  
**Runs after:** `metadata_pass.md`  
**Input variables:** Replace all `{{VARIABLE}}` blocks before sending.

---

## How to use this prompt

1. Copy the module `README.md` into `{{README_MD}}`.
2. Provide candidate module summaries in `{{CANDIDATE_MODULES}}` (from queue/index/search).
3. Fill `{{TOPIC_NAME}}` and `{{TOPIC_ID}}`.
4. Send the completed prompt to the model.
5. Update only the `Related modules:` line in README with returned IDs.

---

## Prompt

You are selecting high-confidence cross-links for a nonpartisan U.S. political power module.
Pick the best related modules by structural mechanism overlap, not by partisan framing.

**Topic:** {{TOPIC_NAME}} (ID: {{TOPIC_ID}})

### Selection criteria

Rank candidates by:

1. Shared actors and institutions
2. Shared legal authorities (statutes/cases)
3. Shared process mechanics and veto points
4. Distinct but adjacent explanatory value (avoid duplicates)

### Output requirements

- Return exactly 3 to 6 topic IDs
- IDs must be 3 digits
- Prefer cross-section diversity when confidence is similar
- No commentary; output a single comma-separated line

**Current README.md:**

```markdown
{{README_MD}}
```

**Candidate modules:**

```text
{{CANDIDATE_MODULES}}
```

**Output format example:**

```text
013, 018, 032, 071
```

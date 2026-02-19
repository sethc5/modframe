#!/usr/bin/env python3
"""Add 5th actor bullet to modules 019-032 and 4th failure-mode bullet to 019-030."""

import pathlib, re

BASE = pathlib.Path(__file__).resolve().parent.parent / "topics" / "02_Congressional_Power_Mechanics"

# 5th actor bullets for 019-032
FIFTH_ACTORS = {
    "019": "- Rank-and-file members use position-taking, coalition defection leverage, and public signaling to push back against centralized scheduling when leadership priorities diverge from district or policy priorities. [Observed]",
    "020": "- Congressional Budget Office scoring and Joint Committee on Taxation estimates constrain procedural packaging choices by determining what qualifies under reconciliation or budget-point-of-order protections. [Observed]",
    "021": "- Congressional Research Service and advocacy organizations supply analysis and pressure that shape subcommittee priorities, though their influence is indirect relative to formal allocators. [Inferred]",
    "022": "- Outside advocacy organizations and media amplify petition campaigns by applying constituency pressure to uncommitted signers, shifting the cost-benefit calculus for visible support. [Inferred]",
    "023": "- Whip teams monitor suspension outcomes and advise leadership on two-thirds threshold feasibility, incorporating party-discipline signals and policy-risk assessments into scheduling decisions. [Observed]",
    "024": "- Issue-advocacy groups and media outlets amplify cloture dynamics by framing obstruction narratives, influencing electoral cost-benefit calculations for senators considering procedural cooperation. [Inferred]",
    "025": "- Advocacy coalitions, defense and domestic program constituencies, and fiscal-policy think tanks supply analysis and pressure that shapes public perception and legislative bargaining positions around cap levels. [Inferred]",
    "026": "- Rating agencies and international finance institutions amplify sovereign-risk narratives that intersect with domestic political pressure, adding external accountability signals to congressional negotiation. [Observed]",
    "027": "- Donor networks and bundlers supply not only funds but also intelligence on competitive dynamics, reinforcing feedback loops between fundraising access and legislative agenda awareness. [Inferred]",
    "028": "- Media and public commentators amplify bloc identity and framing, affecting perceived leverage and electoral salience of caucus positions in public discourse. [Inferred]",
    "029": "- Whistleblowers and former staff can surface misconduct evidence but face retaliation risk and limited formal protection channels within the legislative branch ethics framework. [Observed]",
    "030": "- Conference committees and bicameral negotiation teams bridge structural asymmetries by producing compromise texts whose procedural origins reflect each chamber's distinct leverage environment. [Observed]",
    "031": "- CBO and Joint Committee on Taxation scoring staff interact with draft text early, creating iterative feedback loops that constrain or reopen drafting options before formal committee action. [Observed]",
    "032": "- Congressional leadership and appropriations actors can amplify or sideline GAO recommendations through hearing focus, report-language directives, and funding conditions in subsequent cycles. [Observed]",
}

# 4th failure-mode bullets for 019-030 (031-032 already have 4)
FOURTH_FAILURES = {
    "019": "- Leadership turnover or factional challenges can destabilize established procedural expectations, creating transition periods where scheduling becomes less predictable and caucus bargaining more fluid. [Observed]",
    "020": "- Public understanding of procedural actions often lags institutional complexity, weakening electoral feedback loops for strategic lever use. [Observed]",
    "021": "- Continuing resolutions and government shutdowns can become normalized negotiating tools, reducing institutional pressure to complete regular-order appropriations. [Observed]",
    "022": "- Historical success rates for discharge petitions are low enough that the tool may function primarily as a signaling device rather than a reliable path to floor consideration. [Observed]",
    "023": "- Repeated use of suspension for time-sensitive measures can create precedent expectations that reduce leadership flexibility in future scheduling decisions. [Inferred]",
    "024": "- Abolition or modification of the filibuster under changed precedent can produce rapid norm shifts that are difficult to reverse once established. [Observed]",
    "025": "- Repeated expiration-and-renewal cycles can erode long-term planning capacity for agencies and stakeholders dependent on stable discretionary funding trajectories. [Observed]",
    "026": "- Post-resolution spending trajectories may not match pre-resolution rhetoric, weakening the credibility of concessions extracted under deadline pressure. [Inferred]",
    "027": "- New members may internalize fundraising norms as central legislative work before fully developing policy or oversight capacity, affecting long-term institutional expertise development. [Inferred]",
    "028": "- Leadership may co-opt caucus labels for strategic positioning without delivering substantive policy changes, diluting caucus brand credibility over time. [Inferred]",
    "029": "- Institutional memory loss through member turnover can weaken cross-cycle consistency in ethics enforcement standards and procedural interpretation. [Inferred]",
    "030": "- Reform proposals that address one chamber's pathologies may worsen coordination problems with the other, given asymmetric rule-change procedures and incentive structures. [Hypothesis]",
}


def insert_bullet_after_section(text: str, section_header_re: str, new_bullet: str) -> str:
    """Insert new_bullet as the last bullet in the section identified by section_header_re."""
    # Find the section
    pattern = re.compile(rf"(### {section_header_re}.*?\n)((?:- .+\n(?:.*\[(?:Observed|Inferred|Hypothesis)\]\s*\n)?)*)", re.DOTALL)
    
    # Simpler approach: find all lines belonging to the section
    lines = text.split("\n")
    in_section = False
    last_bullet_idx = -1
    section_start = -1
    
    for i, line in enumerate(lines):
        if re.match(rf"^### {section_header_re}", line):
            in_section = True
            section_start = i
            continue
        if in_section:
            if line.startswith("### ") or (line.startswith("## ") and i > section_start):
                break
            if line.startswith("- "):
                last_bullet_idx = i
    
    if last_bullet_idx == -1:
        print(f"  WARNING: Could not find bullets in section '{section_header_re}'")
        return text
    
    # Insert after last bullet line
    lines.insert(last_bullet_idx + 1, new_bullet)
    return "\n".join(lines)


changed = 0
for mod_dir in sorted(BASE.iterdir()):
    if not mod_dir.is_dir():
        continue
    num = mod_dir.name[:3]
    outline = mod_dir / "outline.md"
    if not outline.exists():
        continue
    
    text = outline.read_text()
    modified = False
    
    if num in FIFTH_ACTORS:
        new_text = insert_bullet_after_section(text, "Actors and roles", FIFTH_ACTORS[num])
        if new_text != text:
            text = new_text
            modified = True
    
    if num in FOURTH_FAILURES:
        new_text = insert_bullet_after_section(text, "Common failure", FOURTH_FAILURES[num])
        if new_text != text:
            text = new_text
            modified = True
    
    if modified:
        outline.write_text(text)
        changed += 1
        a = len(re.findall(r"^- ", text[text.find("### Actors"):text.find("### Process")], re.MULTILINE)) if "### Actors" in text and "### Process" in text else "?"
        f_section = text[text.find("### Common fail"):text.find("### What evidence")] if "### Common fail" in text and "### What evidence" in text else ""
        f = len(re.findall(r"^- ", f_section, re.MULTILINE))
        print(f"  patched {num}: actors={a} failures={f}")

print(f"\nDone: {changed} outlines updated")

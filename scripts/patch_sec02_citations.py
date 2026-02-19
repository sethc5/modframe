#!/usr/bin/env python3
"""Patch section 02 READMEs (018-030): add 2nd statute and/or 2nd case to reach 2+ each."""

import re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent / "topics" / "02_Congressional_Power_Mechanics"

# For modules that need a 2nd case (018-030).
# Modules 018-020 already have 2 statutes, only need 2nd case.
# Modules 021-030 need both a 2nd statute AND 2nd case.
ADDITIONS = {
    "018": {
        "add_statutes": [],  # already 2
        "add_cases": ["Watkins v. United States, 354 U.S. 178 (1957)"],
    },
    "019": {
        "add_statutes": [],  # already 2
        "add_cases": ["Gravel v. United States, 408 U.S. 606 (1972)"],
    },
    "020": {
        "add_statutes": [],  # already 2
        "add_cases": ["United States v. Ballin, 144 U.S. 1 (1892)"],
    },
    "021": {
        "add_statutes": ["31 U.S.C. § 1105 (President's budget submission)"],
        "add_cases": ["Clinton v. City of New York, 524 U.S. 417 (1998)"],
    },
    "022": {
        "add_statutes": ["U.S. Const. art. I, § 5, cl. 2 (chamber rulemaking authority)"],
        "add_cases": ["Christoffel v. United States, 338 U.S. 84 (1949)"],
    },
    "023": {
        "add_statutes": ["U.S. Const. art. I, § 5, cl. 2 (chamber rulemaking authority)"],
        "add_cases": ["Field v. Clark, 143 U.S. 649 (1892)"],
    },
    "024": {
        "add_statutes": ["U.S. Const. art. I, § 5, cl. 2 (Senate rulemaking authority)"],
        "add_cases": ["United States v. Ballin, 144 U.S. 1 (1892)"],
    },
    "025": {
        "add_statutes": ["2 U.S.C. § 901 (discretionary spending caps)"],
        "add_cases": ["Clinton v. City of New York, 524 U.S. 417 (1998)"],
    },
    "026": {
        "add_statutes": ["U.S. Const. amend. XIV, § 4 (public-debt clause)"],
        "add_cases": ["Ashwander v. TVA, 297 U.S. 288 (1936)"],
    },
    "027": {
        "add_statutes": ["2 U.S.C. § 1604 (lobbying disclosure/fundraising nexus)"],
        "add_cases": ["Randall v. Sorrell, 548 U.S. 230 (2006)"],
    },
    "028": {
        "add_statutes": ["2 U.S.C. § 29d (Congressional Member Organization funding rules)"],
        "add_cases": ["Bond v. Floyd, 385 U.S. 116 (1966)"],
    },
    "029": {
        "add_statutes": ["House Rule XI (ethics committee jurisdiction and procedures)"],
        "add_cases": ["Gravel v. United States, 408 U.S. 606 (1972)"],
    },
    "030": {
        "add_statutes": ["U.S. Const. art. I, § 3 (Senate composition and powers)"],
        "add_cases": ["INS v. Chadha, 462 U.S. 919 (1983)"],
    },
}


def patch_readme(readme_path: pathlib.Path, add_statutes: list[str], add_cases: list[str]) -> bool:
    text = readme_path.read_text()
    changed = False

    for statute in add_statutes:
        # Append after last statute line
        # Find the Cases: line and insert before it
        if statute not in text:
            text = re.sub(
                r"(Statutes:\n(?:\t- [^\n]+\n)+)",
                lambda m: m.group(0).rstrip("\n") + f"\n\t- {statute}\n",
                text,
            )
            changed = True

    for case in add_cases:
        if case not in text:
            text = re.sub(
                r"(Cases:\n(?:\t- [^\n]+\n)+)",
                lambda m: m.group(0).rstrip("\n") + f"\n\t- {case}\n",
                text,
            )
            changed = True

    if changed:
        readme_path.write_text(text)
    return changed


patched = 0
for mod_dir in sorted(BASE.iterdir()):
    if not mod_dir.is_dir():
        continue
    num = mod_dir.name[:3]
    if num not in ADDITIONS:
        continue
    info = ADDITIONS[num]
    readme = mod_dir / "README.md"
    if patch_readme(readme, info["add_statutes"], info["add_cases"]):
        patched += 1
        print(f"  patched {num}")

print(f"\nDone: {patched} READMEs updated")

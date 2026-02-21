#!/usr/bin/env python3
"""Patch section 01 READMEs: replace placeholder citations with topically relevant ones, ensure 2+ statutes and 2+ cases each."""

import re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent / "topics" / "01_Electoral_Power_Structures"

# Map module number -> (statutes_list, cases_list)
# Each module gets exactly what it needs to reach 2+ of each.
CITATIONS = {
    "001": {
        "statutes": [
            "52 U.S.C. §§ 30101–30145 (Federal Election Campaign Act)",
            "26 U.S.C. § 527 (tax-exempt political organizations)",
        ],
        "cases": [
            "Buckley v. Valeo, 424 U.S. 1 (1976)",
            "Citizens United v. FEC, 558 U.S. 310 (2010)",
        ],
    },
    "002": {
        "statutes": [
            "52 U.S.C. § 10301 (Voting Rights Act Section 2, primary access)",
            "Cal. Elec. Code § 5100 et seq. (top-two primary system)",
        ],
        "cases": [
            "California Democratic Party v. Jones, 530 U.S. 567 (2000)",
            "Tashjian v. Republican Party of Connecticut, 479 U.S. 208 (1986)",
        ],
    },
    "003": {
        "statutes": [
            "52 U.S.C. § 10301 (Voting Rights Act Section 2)",
            "2 U.S.C. § 2c (single-member congressional districts)",
        ],
        "cases": [
            "Rucho v. Common Cause, 588 U.S. 684 (2019)",
            "Allen v. Milligan, 599 U.S. 1 (2023)",
        ],
    },
    "004": {
        "statutes": [
            "52 U.S.C. §§ 20501–20511 (National Voter Registration Act)",
            "52 U.S.C. §§ 10301–10308 (Voting Rights Act of 1965)",
        ],
        "cases": [
            "Shelby County v. Holder, 570 U.S. 529 (2013)",
            "Crawford v. Marion County Election Board, 553 U.S. 181 (2008)",
        ],
    },
    "005": {
        "statutes": [
            "Cal. Const. art. II, § 8 (California initiative provisions)",
            "Colo. Const. art. V, § 1 (Colorado initiative and referendum)",
        ],
        "cases": [
            "Meyer v. Grant, 486 U.S. 414 (1988)",
            "Buckley v. American Constitutional Law Foundation, 525 U.S. 182 (1999)",
        ],
    },
    "006": {
        "statutes": [
            "Alaska Stat. § 15.15.350 (Alaska ranked-choice voting)",
            "Me. Rev. Stat. tit. 21-A, § 723-A (Maine ranked-choice voting)",
        ],
        "cases": [
            "Dudum v. Arntz, 640 F.3d 1098 (9th Cir. 2011)",
            "Baber v. Dunlap, 349 F. Supp. 3d 68 (D. Me. 2018)",
        ],
    },
    "007": {
        "statutes": [
            "3 U.S.C. §§ 1–21 (Electoral Count Reform Act of 2022)",
            "U.S. Const. art. II, § 1, cl. 2 (state appointment of electors)",
        ],
        "cases": [
            "Chiafalo v. Washington, 591 U.S. 578 (2020)",
            "Bush v. Gore, 531 U.S. 98 (2000)",
        ],
    },
    "008": {
        "statutes": [
            "3 U.S.C. § 5 (safe-harbor deadline for state certification)",
            "3 U.S.C. § 6 (governor's certificate of ascertainment)",
        ],
        "cases": [
            "Bush v. Gore, 531 U.S. 98 (2000)",
            "Texas v. Pennsylvania, 592 U.S. ___ (2020)",
        ],
    },
    "009": {
        "statutes": [
            "52 U.S.C. § 30104 (FEC disclosure and reporting requirements)",
            "11 C.F.R. § 109.21 (coordination with vendors)",
        ],
        "cases": [
            "Bluman v. FEC, 800 F. Supp. 2d 281 (D.D.C. 2011)",
            "FEC v. Beaumont, 539 U.S. 146 (2003)",
        ],
    },
    "010": {
        "statutes": [
            "52 U.S.C. § 20507 (NVRA voter-file maintenance and access)",
            "Cal. Civ. Code §§ 1798.100–1798.199 (CCPA data-broker provisions)",
        ],
        "cases": [
            "Spokeo, Inc. v. Robins, 578 U.S. 330 (2016)",
            "AFL-CIO v. FEC, 333 F.3d 168 (D.C. Cir. 2003)",
        ],
    },
    "011": {
        "statutes": [
            "52 U.S.C. § 30101(14) (FEC definition of national party)",
            "11 C.F.R. § 9008.3 (convention financing and platform activities)",
        ],
        "cases": [
            "Eu v. San Francisco County Democratic Central Committee, 489 U.S. 214 (1989)",
            "Democratic Party of U.S. v. Wisconsin ex rel. La Follette, 450 U.S. 107 (1981)",
        ],
    },
    "012": {
        "statutes": [
            "52 U.S.C. § 30101(14) (party definition and convention framework)",
            "11 C.F.R. § 9008.7 (convention expenditure requirements)",
        ],
        "cases": [
            "Democratic Party of U.S. v. Wisconsin ex rel. La Follette, 450 U.S. 107 (1981)",
            "Cousins v. Wigoda, 419 U.S. 477 (1975)",
        ],
    },
    "013": {
        "statutes": [
            "52 U.S.C. §§ 30101–30126 (FECA independent expenditure rules)",
            "11 C.F.R. § 109.21 (FEC coordination standard)",
        ],
        "cases": [
            "SpeechNow.org v. FEC, 599 F.3d 686 (D.C. Cir. 2010)",
            "Citizens United v. FEC, 558 U.S. 310 (2010)",
        ],
    },
    "014": {
        "statutes": [
            "52 U.S.C. § 30116 (contribution limits, state/national party)",
            "11 C.F.R. § 109.32 (coordinated party expenditures)",
        ],
        "cases": [
            "McConnell v. FEC, 540 U.S. 93 (2003)",
            "Colorado Republican Federal Campaign Committee v. FEC, 518 U.S. 604 (1996)",
        ],
    },
    "015": {
        "statutes": [
            "52 U.S.C. § 10301 (Voting Rights Act Section 2, litigation basis)",
            "42 U.S.C. § 1983 (civil rights actions in election cases)",
        ],
        "cases": [
            "Purcell v. Gonzalez, 549 U.S. 1 (2006)",
            "Bush v. Gore, 531 U.S. 98 (2000)",
        ],
    },
    "016": {
        "statutes": [
            "Fla. Stat. § 102.166 (Florida recount procedures)",
            "Minn. Stat. § 204C.35 (Minnesota automatic recount provisions)",
        ],
        "cases": [
            "Bush v. Gore, 531 U.S. 98 (2000)",
            "Coleman v. Franken, 767 N.W.2d 453 (Minn. 2009)",
        ],
    },
    "017": {
        "statutes": [
            "52 U.S.C. §§ 30101–30116 (FECA PAC registration and limits)",
            "11 C.F.R. § 109.21 (coordination with PACs)",
        ],
        "cases": [
            "SpeechNow.org v. FEC, 599 F.3d 686 (D.C. Cir. 2010)",
            "FEC v. Wisconsin Right to Life, Inc., 551 U.S. 449 (2007)",
        ],
    },
}


def rebuild_citations(readme_text: str, statutes: list[str], cases: list[str]) -> str:
    """Replace the Statutes: and Cases: blocks, using tab indentation (sec 03 standard)."""
    # Build new blocks
    stat_block = "Statutes:\n" + "\n".join(f"\t- {s}" for s in statutes)
    case_block = "Cases:\n" + "\n".join(f"\t- {c}" for c in cases)

    # Replace Statutes block
    readme_text = re.sub(
        r"Statutes:\n(?:[ \t]+- [^\n]+\n?)+",
        stat_block + "\n",
        readme_text,
    )
    # Replace Cases block
    readme_text = re.sub(
        r"Cases:\n(?:[ \t]+- [^\n]+\n?)+",
        case_block + "\n",
        readme_text,
    )
    return readme_text


def normalize_actor_indent(readme_text: str) -> str:
    """Convert space-indented actor YAML to tab-indented (sec 03 standard)."""
    lines = readme_text.split("\n")
    out = []
    in_actors = False
    for line in lines:
        if line.startswith("Actors:"):
            in_actors = True
            out.append(line)
            continue
        if in_actors:
            if line.strip() == "" or (not line[0].isspace() and not line.startswith("\t")):
                in_actors = False
                out.append(line)
                continue
            # Convert leading spaces to a single tab
            stripped = line.lstrip()
            if stripped.startswith("- name:") or stripped.startswith("type:"):
                out.append("\t" + stripped)
            else:
                out.append(line)
            continue
        out.append(line)
    return "\n".join(out)


changed = 0
for mod_dir in sorted(BASE.iterdir()):
    if not mod_dir.is_dir():
        continue
    num = mod_dir.name[:3]
    if num not in CITATIONS:
        continue
    readme = mod_dir / "README.md"
    text = readme.read_text()
    new_text = rebuild_citations(text, CITATIONS[num]["statutes"], CITATIONS[num]["cases"])
    new_text = normalize_actor_indent(new_text)
    if new_text != text:
        readme.write_text(new_text)
        changed += 1
        print(f"  patched {num}")

print(f"\nDone: {changed} READMEs updated")

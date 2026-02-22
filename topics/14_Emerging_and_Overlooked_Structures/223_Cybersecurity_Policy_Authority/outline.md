# Cybersecurity Policy Authority

**Summary:** Federal cybersecurity authority is fragmented across more than two dozen agencies with overlapping and sometimes conflicting jurisdictions: CISA leads civilian federal network defense, NSA leads offensive operations and intelligence collection, Cyber Command leads military cyber operations, and the FBI leads domestic cybercrime investigation — with no unified command authority for coordinating responses during major incidents. [Observed] The Cybersecurity and Infrastructure Security Agency Act (2018) elevated CISA to the lead civilian cybersecurity agency, but CISA's authorities over federal contractor networks, private critical infrastructure, and state/local governments remain advisory rather than directive. [Observed] The SolarWinds intrusion (discovered December 2020) demonstrated that the fragmented agency structure created detection and response gaps: the breach was discovered by a private firm (FireEye), and the government's response required ad hoc coordination among CISA, NSA, FBI, and the intelligence community without a pre-established command structure. [Observed] The structural result is a cybersecurity governance architecture designed for a government computing environment of the 1990s — with agency-specific networks and clear public/private boundaries — that is misconfigured for an integrated cloud and shared-services environment where that boundary has largely dissolved. [Inferred]

**Mechanism in one sentence:** Federal cybersecurity authority is split among dozens of agencies with overlapping, uncoordinated jurisdictions and no unified command, creating structural detection and response gaps during major cyber incidents affecting government and critical infrastructure. [Observed]

### Actors and roles

- **Cybersecurity and Infrastructure Security Agency (CISA, DHS)** — lead civilian federal cybersecurity agency; responsible for federal civilian network defense (.gov), critical infrastructure sector coordination, and state/local government assistance; directive authority over contractors is limited. [Observed]
- **National Security Agency (NSA)** — leads foreign signals intelligence and offensive cyber operations; provides technical assistance to CISA through the Cybersecurity Collaboration Center; operates under Title 50 intelligence authorities. [Observed]
- **U.S. Cyber Command (CYBERCOM)** — military cyber operations command; coordinates with NSA (dual-hatted commander); responsible for defending military networks (DoD Information Network) and conducting offensive military cyber operations. [Observed]
- **Federal Bureau of Investigation (FBI)** — leads domestic cybercrime investigation and attribution; coordinates with CISA on major incidents under the National Cyber Incident Response Plan. [Observed]
- **Office of the National Cyber Director (ONCD)** — established 2021 within EOP; coordinates national cybersecurity strategy and interagency cybersecurity policy; advisory role, not operational. [Observed]
- **Sector-specific agencies (FERC for energy, FDA for health, TSA for transportation)** — regulate cybersecurity within their sectors with varying statutory authority; FERC has mandatory reliability standards (NERC CIP); FDA has guidance-based authority. [Observed]
- **Private critical infrastructure operators** — own and operate most U.S. critical infrastructure; relationship with CISA is voluntary information-sharing rather than directive. [Observed]

### Process map (bulleted)

- A significant cyber incident is detected, either by a private firm, an affected agency, or intelligence community monitoring. [Observed]
- CISA activates the National Cyber Incident Response Plan (NCIRP), theoretically coordinating across Threat (FBI), Asset (CISA), Intelligence (NSA/ODNI), and Affected Entity response roles. [Observed]
- In practice, coordinate across agencies requires ad hoc inter-agency working groups without a clear command hierarchy; each agency operates under separate authorities that may impose different classification, information-sharing, and disclosure requirements. [Observed]
- Private sector operators who are victims of a cyber incident are not legally required (in most sectors) to report to CISA or other agencies; voluntary reporting is the norm, limiting the government's situational awareness. [Observed]
- Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA, 2022) mandates reporting requirements for critical infrastructure operators, but implementing regulations were not finalized as of early 2026. [Observed]
- Attribution and attribution disclosure decisions involve NSA (intelligence equities), FBI (law enforcement), and State Department (diplomatic implications), requiring interagency consensus that can slow the response. [Observed]

### Where power concentrates

- **Gatekeepers:** CISA holds the nominal lead for civilian incident response but lacks directive authority over most of the entities (private contractors, critical infrastructure operators) that must participate in effective defense. [Observed]
- **Bottlenecks:** The intelligence community's signals intelligence on adversary cyber operations is governed by classification rules that limit information sharing with private-sector defenders who most need it. [Observed]
- **Veto points:** The NSA's equities review process (protecting intelligence sources and methods) can delay disclosure of known vulnerabilities to affected system owners, creating a structural tension between offense (exploiting vulnerabilities) and defense (disclosing them). [Observed]

### Common failure modes

- The Vulnerabilities Equities Process (VEP), which governs NSA decisions about whether to disclose or retain discovered vulnerabilities, is conducted with limited transparency and congressional oversight. [Observed]
- Agency-specific budget and personnel structures create incentives for each agency to protect its cybersecurity turf rather than integrate with CISA coordination mechanisms. [Inferred]
- Federal contractor network security requirements were tightened by Executive Order 14028 (2021), but implementation across the contractor base — including tens of thousands of small contractors — is highly uneven. [Observed]
- The absence of mandatory reporting requirements for most sectors (pending CIRCIA implementation) means CISA routinely learns about major incidents from news coverage rather than from the affected entities. [Observed]

### What evidence would prove/disprove key claims

- GAO reports on federal cybersecurity maturity (FISMA annual reports to Congress) document agency-by-agency compliance with federal security standards. [Observed]
- CISA's annual "Known Exploited Vulnerabilities" catalog documents which vulnerabilities have been actively exploited; cross-reference with disclosure timelines to measure NSA equities review delays. [Observed]
- Congressional testimony and post-incident reports on SolarWinds, Microsoft Exchange server breach, and Colonial Pipeline demonstrate the coordination failure pattern. [Observed]
- CIRCIA implementation docket at CISA provides evidence of the rulemaking process for mandatory reporting requirements. [Observed]

### Suggested sources

- Cybersecurity and Infrastructure Security Agency Act of 2018, Pub. L. 115-278.
- Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA), Pub. L. 117-103 (2022).
- Executive Order 14028, *Improving the Nation's Cybersecurity.* May 12, 2021. 86 Fed. Reg. 26633.
- National Cyber Incident Response Plan (NCIRP). CISA, 2016 (update in progress). URL: https://www.cisa.gov
- Government Accountability Office. *Cybersecurity: Federal Agencies Need to Fully Implement Key Practices* (multiple reports). URL: https://www.gao.gov
- Nakashima, Ellen. "The SolarWinds Hack Was All But Inevitable." *Washington Post*, December 2020.

### Episode outline (6 parts)

1. **Structure:** Map the federal cybersecurity agency landscape — CISA, NSA, CYBERCOM, FBI, ONCD, and sector-specific regulators — their respective authorities, and the information-sharing and coordination mechanisms (NCIRP) that theoretically integrate them. [Observed]
2. **Incentive:** Explain why fragmentation persists — agency turf protection, classification barriers to information sharing, intelligence community equities interests in retaining offensive capabilities, and the political difficulty of consolidating authorities. [Inferred]
3. **Example:** Trace the SolarWinds incident — breach discovery by a private firm, ad hoc government response, gaps in detection and coordination — as a demonstration of the fragmented authority structure's operational consequences. [Observed]
4. **Evidence:** Present GAO FISMA compliance data; CIRCIA implementation timeline; NSA vulnerability disclosure record; CISA budget relative to the scale of the defended network. [Observed]
5. **Levers:** Evaluate CISA directive authority expansion, unified incident command structures, mandatory ISAC participation for critical infrastructure, and CIRCIA full implementation as structural improvements. [Hypothesis]
6. **Takeaway:** Federal cybersecurity authority is architecturally misaligned — split among agencies whose authorities, classification regimes, and turf interests create gaps at exactly the points where adversaries operate; the result is a defensive posture that is structurally weaker than the fragmented agency map would suggest. [Inferred]

# Campaign Finance Architecture

**Summary:** The federal campaign finance system structures how money is raised,
reported, and spent in elections through contribution limits, disclosure requirements,
and spending rules. [Observed] Court decisions over several decades expanded
constitutional protection for certain political expenditures, creating parallel funding
channels with different legal constraints. [Observed] The resulting architecture combines
direct, contribution-limited support with large independent-spending pathways. [Observed]
Mapping how money moves across those pathways is central to analyzing access,
agenda-setting, and enforcement capacity in elections. [Inferred]

**Mechanism in one sentence:** Federal law caps direct contributions to candidates while
court rulings permit unlimited independent expenditures, creating two parallel money tracks
with different disclosure requirements and different points of structural leverage. [Observed]

### Actors and roles

- **Candidates and campaigns** — raise and spend funds subject to FECA contribution
  limits; must disclose donors above $200 per-cycle threshold; incentive: maximize
  fundraising within legal channels while benefiting from aligned outside spending they
  cannot legally coordinate; constraint: hard contribution limits per election. [Observed
  — source: 52 U.S.C. § 30116]

- **Political party committees** (DNC, RNC, DSCC, DCCC, NRCC, NRSC) — may make
  limited coordinated expenditures with candidates; operate separate accounts for
  unlimited independent expenditures; incentive: concentrate resources in competitive
  races; constraint: coordinated spending limits scale with the office sought. [Observed
  — source: 52 U.S.C. § 30116(d)]

- **Political Action Committees (PACs)** — aggregate contributions from members,
  employees, or shareholders; may give directly to candidates within limits ($5,000 per
  election per candidate); may also make independent expenditures; incentive: advance
  organizational policy interests; constraint: contribution limits and disclosure
  requirements apply. [Observed — source: 52 U.S.C. § 30118]

- **Super PACs (independent expenditure-only committees)** — may raise unlimited funds
  from individuals, corporations, and unions; cannot contribute to or coordinate with
  candidates; must disclose donors to FEC; incentive: concentrated influence over
  election outcomes without contribution limits; constraint: coordination prohibition.
  [Observed — source: SpeechNow.org v. FEC, 599 F.3d 686 (D.C. Cir. 2010); FEC
  Advisory Opinion 2010-11]

- **501(c)(4) "dark money" organizations** — tax-exempt social welfare nonprofits that
  may engage in political activity provided it is not their primary purpose; not required
  to disclose donors publicly; frequently fund super PACs without triggering disclosure
  of the 501(c)(4)'s underlying contributors; incentive: allow donors to influence
  elections anonymously; constraint: political activity must remain below the
  primary-purpose threshold, though IRS enforcement has been minimal. [Observed —
  source: 26 U.S.C. § 501(c)(4); IRS Revenue Ruling 2004-6]

- **Federal Election Commission (FEC)** — six presidentially-appointed,
  Senate-confirmed commissioners; by statute no more than three may be from the same
  party; enforces FECA, issues advisory opinions, maintains public disclosure database;
  constraint: enforcement actions require a four-vote majority, producing frequent 3-3
  partisan deadlocks that effectively dismiss complaints. [Observed — source: 52 U.S.C.
  § 30106; FEC enforcement statistics]

- **Federal courts** — review challenges to campaign finance statutes on First Amendment
  grounds; have progressively narrowed permissible contribution limits and disclosure
  requirements since *Buckley* (1976); constraint: courts act only on cases brought
  before them and cannot initiate enforcement. [Observed — source: Buckley v. Valeo,
  424 U.S. 1 (1976); Citizens United v. FEC, 558 U.S. 310 (2010); McCutcheon v. FEC,
  572 U.S. 185 (2014)]

### Process map (bulleted)

- **Step 1 — Fundraising:** Candidate committees, party committees, and PACs solicit
  contributions within applicable per-election and aggregate limits; 501(c)(4)s solicit
  from corporations, unions, and individuals without triggering FEC donor disclosure.
  [Observed — source: 52 U.S.C. §§ 30116, 30118]

- **Step 2 — Disclosure filing:** Registered committees file periodic reports with the
  FEC listing contributions above $200 and itemizing expenditures; super PACs file
  separately and disclose their donors; 501(c)(4)s file IRS Form 990, which does not
  publicly list donors. [Observed — source: 52 U.S.C. § 30104; IRS Form 990 instructions]

- **Step 3 — Routing through the dark money pass-through:** 501(c)(4)s transfer funds to
  super PACs; the super PAC's donor report lists the 501(c)(4) entity as the source, not
  its underlying contributors, creating an effective donor anonymization layer. [Observed
  — source: FEC advisory opinions; Campaign Legal Center analysis]

- **Step 4 — Independent spending:** Super PACs and 501(c)(4)s run advertising and voter
  contact independently; campaigns cannot legally direct this activity; "general public
  communications" regulatory exceptions and former-staffer-run super PACs are common
  coordination-adjacent structures. [Observed — source: 11 C.F.R. § 109.21; Inferred —
  coordination-adjacent patterns documented in press reporting but rarely proven legally]

- **Step 5 — Enforcement:** FEC staff investigate complaints and recommend action;
  recommendations require a four-vote commission majority to proceed; tied votes close
  the matter without enforcement; criminal referrals to DOJ also require a commission
  vote. [Observed — source: 52 U.S.C. § 30109; FEC enforcement statistics]

### Where power concentrates

- **Gatekeepers:** Major donors funding 501(c)(4)s and super PACs, whose identities may
  not be publicly disclosed; party campaign committees selecting which candidates receive
  coordinated support; professional bundlers who aggregate individual contributions above
  the individual cap. [Inferred — influence patterns visible in FEC data; causal access
  claims inferred from documented access patterns in prior research, not direct evidence]

- **Bottlenecks:** The FEC disclosure database is the only comprehensive public record of
  most campaign money, but its coverage ends at the 501(c)(4) boundary; the IRS Form 990
  is the only public 501(c)(4) filing and does not include donor lists. [Observed —
  source: FEC.gov/data; IRS Form 990]

- **Veto points:** The FEC four-vote enforcement threshold, enabling 3-3 partisan
  deadlock; federal courts reviewing constitutional challenges, which have blocked
  multiple contribution limits and disclosure requirements. [Observed — source: 52 U.S.C.
  § 30106; McCutcheon v. FEC, 572 U.S. 185 (2014)]

### Common failure modes

- **Enforcement paralysis** — [Observed] The FEC's four-vote requirement enables partisan
  deadlock that terminates complaints without action. In fiscal year 2021, the commission
  deadlocked on 31 enforcement matters, the highest recorded total. Former commissioners
  from both parties have publicly described the commission as institutionally
  dysfunctional. [Source: FEC FY2021 Enforcement Statistics; former commissioner public
  statements]

- **Coordination prohibition erosion** — [Inferred] The formal prohibition on super PAC
  coordination with campaigns is undermined by FEC "general public communications"
  exceptions (11 C.F.R. § 109.21) and the practice of former campaign staff leading
  aligned super PACs. Proving coordination requires evidence of direct communication,
  which investigators rarely obtain without subpoena power.

- **Dark money disclosure gap** — [Observed] 501(c)(4) organizations may transfer funds
  to super PACs without triggering disclosure of the 501(c)(4)'s donors. Total spending
  from nonprofits that did not disclose their donors reached approximately $1 billion in
  the 2020 election cycle. [Source: OpenSecrets dark money tracking, 2020 cycle]

- **Contribution limit circumvention** — [Observed] Limits on direct candidate
  contributions have become structurally less binding as unlimited outside spending has
  grown. Total outside spending by non-party groups grew from approximately $143 million
  in 2004 to over $3 billion in 2020. [Source: OpenSecrets, Outside Spending by Election
  Cycle]

### What evidence would prove/disprove key claims

- FEC enforcement records (vote-by-vote deadlock rates, complaint-to-penalty ratios by
  year) would quantify and track the severity of enforcement paralysis over time
- Cross-referencing 501(c)(4) IRS Form 990 expense lines with super PAC FEC receipts
  would document the dark money pass-through mechanism and estimate total anonymized flows
- Coordination case outcomes (criminal referrals made vs. declined, civil penalties
  assessed vs. deadlocked) would indicate deterrent effect of coordination rules
- Longitudinal outside spending data (FEC + OpenSecrets) vs. disclosed direct
  contributions tracks the structural shift in money flows since Citizens United

### Suggested sources

- Federal Election Campaign Act, as amended. 52 U.S.C. §§ 30101–30145. U.S. House of
  Representatives Office of Law Revision Counsel.
  https://uscode.house.gov/view.xhtml?path=/prelim@title52/subtitle3/chapter301&edition=prelim

- *Buckley v. Valeo*, 424 U.S. 1 (1976). Supreme Court of the United States.
  https://supreme.justia.com/cases/federal/us/424/1/

- *Citizens United v. Federal Election Commission*, 558 U.S. 310 (2010). Supreme Court
  of the United States.
  https://supreme.justia.com/cases/federal/us/558/310/

- *McCutcheon v. Federal Election Commission*, 572 U.S. 185 (2014). Supreme Court of the
  United States.
  https://supreme.justia.com/cases/federal/us/572/185/

- Outside Spending by Election Cycle. OpenSecrets (Center for Responsive Politics),
  updated 2024.
  https://www.opensecrets.org/outside-spending

- FEC Enforcement Statistics. Federal Election Commission, updated annually.
  https://www.fec.gov/legal-resources/enforcement/enforcement-statistics/

- Campaign Finance Law: A Summary and Guide. Congressional Research Service, Report
  RL30965, updated 2022.
  https://crsreports.congress.gov/product/pdf/RL/RL30965

### Episode outline (6 parts)

1. **Structure** — The US campaign finance system has two parallel tracks: a disclosed,
   contribution-limited track for direct giving to candidates and parties, and an
   effectively unlimited, partially undisclosed track for independent expenditures
   through super PACs and 501(c)(4) organizations — created by a combination of FECA
   and three decades of Supreme Court rulings.

2. **Incentive** — Candidates need money to compete; donors may seek access or policy
   outcomes; the legal asymmetry between the two tracks creates structural incentives to
   route resources through outside groups that face fewer limits and, in the case of
   501(c)(4)s, no donor disclosure requirements.

3. **Example** — In the 2012 election, 501(c)(4) Crossroads GPS raised over $70 million
   without publicly disclosing its donors and transferred funds to super PAC American
   Crossroads, which spent independently on presidential and Senate races. This was the
   first large-scale deployment of the dark money pass-through mechanism in a presidential
   cycle. [Observed — source: OpenSecrets; FEC filings; IRS Form 990 records]

4. **Evidence** — FEC public disclosure database (FEC.gov/data); OpenSecrets outside
   spending and dark money tracking; IRS Form 990 filings for 501(c)(4)s (available via
   ProPublica Nonprofit Explorer); FEC enforcement statistics and vote records.

5. **Levers** — The DISCLOSE Act (proposed multiple sessions of Congress) would require
   501(c)(4)s to disclose donors above a threshold amount; FEC restructuring proposals
   include replacing the six-member commission with an odd-numbered body to break
   enforcement deadlocks; state-level small-donor matching fund programs (New York City
   model) demonstrate alternative architectures that amplify small donors relative to
   large ones.

6. **Takeaway** — The campaign finance architecture determines not just who funds
   elections but whose funding is publicly visible; the structural gap between the
   disclosed and undisclosed tracks is the primary transparency deficit in the system
   and is maintained by both statutory design and judicial interpretation of the First
   Amendment.

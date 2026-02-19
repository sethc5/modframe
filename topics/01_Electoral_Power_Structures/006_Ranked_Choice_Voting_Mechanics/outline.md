# Ranked Choice Voting Mechanics

**Summary:** Ranked choice voting (RCV) counts ballots through sequential elimination and
redistribution until a candidate reaches a majority of active votes. [Observed] It is used
in selected federal and local jurisdictions as an alternative to plurality systems.
[Observed] RCV changes campaign strategy incentives and election-administration workflows,
especially tabulation, certification timing, and equipment requirements. [Inferred]

**Mechanism in one sentence:** Voters rank candidates, lower-performing candidates are
eliminated in rounds, and ballots transfer until one candidate holds a majority of active
votes. [Observed]

### Actors and roles

- **State and local governments** — adopt RCV by statute, constitutional amendment, or
  city charter amendment; most adoptions have occurred via voter-approved ballot
  initiative rather than legislative action; incentive varies by political context —
  parties that benefit from vote-splitting in the current plurality system may oppose
  adoption; constraint: voting system changes must comply with state and federal election
  law. [Observed — source: NCSL RCV survey; FairVote adoption tracker]

- **Election administrators** (Secretaries of State, county election directors) —
  implement RCV tabulation, conduct voter education, procure or configure counting
  equipment or software; incentive: accurate and timely results; constraint: existing
  voting equipment may not support RCV tabulation without recertification or replacement;
  state certification of voting systems is a material bottleneck. [Observed — source:
  Alaska Division of Elections, 2022 Special Election administration report; Maine
  Secretary of State RCV implementation documentation]

- **Voting equipment vendors and state certification authorities** — voting systems used
  in federal and state elections must be certified by state authorities (following EAC
  guidelines); some certified voting systems do not support RCV tabulation, limiting
  jurisdictions' ability to adopt RCV without equipment replacement; incentive for
  vendors: maintain certification and market position; constraint: EAC Voluntary Voting
  System Guidelines do not currently include RCV-specific certification standards.
  [Observed — source: EAC VVSG documentation; NCSL voting system certification overview]

- **Candidates** — under RCV, candidates have a structural incentive to campaign broadly
  and seek second-choice votes from supporters of other candidates, rather than only
  mobilizing their own base; candidates who run highly negative campaigns risk alienating
  potential second-choice voters; incentive: maximize ranked preferences across the
  electorate; constraint: strategic behavior may still favor base mobilization in
  low-turnout primaries. [Inferred — incentive logic is structural; empirical evidence
  on whether candidate behavior changes is mixed; see Donovan et al. (2019)]

- **Voters** — must rank candidates rather than selecting one; ranking is optional in
  most implementations (voters may rank as many or as few as they wish); voters who
  rank fewer candidates than there are rounds risk "ballot exhaustion" (their ballot
  has no valid ranking when it matters); voter education requirements are higher than
  for plurality elections. [Observed — source: FairVote ballot exhaustion data; Alvarez,
  Hall, and Levin, "Voter Attitudes About Ranked Choice Voting" (2018)]

- **Advocacy organizations** — FairVote (primary national advocate for RCV) and
  affiliated state organizations campaign for adoption; opposition comes from some
  incumbent parties and traditional election administrators wary of complexity; both
  sides conduct public campaigns and legislative testimony. Note: FairVote is an advocacy
  organization and its data should be cross-checked against independent sources.
  [Observed — source: FairVote mission statement; NCSL legislative testimony records]

### Process map (bulleted)

- **Step 1 — Ballot design:** Voters receive a ballot listing candidates with ranking
  columns (rank 1, 2, 3, etc.); jurisdictions vary in whether they allow unlimited
  ranking or cap the number of choices (e.g., "vote for up to 5"); ballot design
  affects both voter error rates and ballot exhaustion. [Observed — source: Alaska 2022
  ballot design; FairVote ballot design guidance]

- **Step 2 — First-round count:** All ballots are tallied for each voter's first-choice
  candidate; if any candidate exceeds the threshold (typically 50% +1 in single-winner
  elections; a Droop quota in multi-winner elections), that candidate is declared a
  winner immediately. [Observed — source: Maine RCV statute; Alaska Ballot Measure 2
  (2020) implementing statute]

- **Step 3 — Elimination:** If no candidate meets the threshold, the candidate with the
  fewest votes is eliminated; all ballots that had that candidate as their active choice
  are transferred to each ballot's next-ranked active candidate. [Observed — source:
  Alaska election code; Maine election code]

- **Step 4 — Successive rounds:** Steps 2–3 repeat with the reduced candidate field;
  ballots whose next-ranked candidate has also been eliminated skip to the next active
  ranking; ballots with no remaining active candidate are "exhausted" and are no longer
  counted in subsequent rounds. [Observed — source: RCV tabulation specifications; FEC
  guidance on RCV reporting]

- **Step 5 — Results tabulation and reporting:** Final results require reporting both
  first-choice totals and round-by-round transfers; tabulation takes longer than
  plurality counting, particularly when ballots must be physically transported to a
  central location for ranked-choice counting; Maine mails ballots to Augusta for
  central tabulation; Alaska uses software-based tabulation. [Observed — source: Maine
  Secretary of State RCV administration; Alaska Division of Elections 2022 Special
  Election timeline]

### Where power concentrates

- **Gatekeepers:** State legislatures and local governments that decide whether to adopt
  RCV; state certification authorities whose approved equipment list constrains adoption;
  election administrators who design voter education and ballot layout. [Observed —
  source: NCSL voting system certification process; FairVote adoption tracker]

- **Bottlenecks:** Voting equipment certification is a structural bottleneck — if
  certified machines do not support RCV, adoption requires either legislative equipment
  replacement mandates or manual/central tabulation workarounds; voter education gaps
  create a participation bottleneck, with lower-information voters more likely to rank
  fewer candidates and risk ballot exhaustion. [Observed — source: EAC VVSG; FairVote
  ballot exhaustion analysis]

- **Veto points:** State legislatures may preempt local RCV adoptions (as has occurred
  in several states); courts may review RCV implementations for compliance with state
  constitutional one-person-one-vote requirements; voters may repeal RCV by initiative
  if they are dissatisfied with results. [Observed — source: Burlington, VT repeal
  (2010); Tennessee and other state preemption statutes; Arkansas state court challenge]

### Common failure modes

- **Ballot exhaustion** — [Observed] When voters do not rank enough candidates, their
  ballots become exhausted before a winner is determined; the winning candidate may be
  elected by a majority of non-exhausted ballots but not of all ballots cast. In the
  2020 Democratic presidential primary in Alaska using RCV, approximately 10% of ballots
  were exhausted. FairVote tracks exhaustion rates across jurisdictions; rates vary
  significantly based on ballot design and the number of candidates. [Source: FairVote,
  "Ballot Exhaustion in RCV Elections"; Burnett and Kogan (2015)]

- **Tabulation delay and result uncertainty** — [Observed] RCV tabulation requires more
  processing than plurality counting, and in jurisdictions using mail ballots (Maine,
  Alaska), late-arriving ballots must be received before final tabulation can begin;
  the 2018 Maine 2nd Congressional District RCV election took approximately one week to
  finalize, extending the period of uncertainty about the outcome. [Source: Maine
  Secretary of State, 2018 election certification timeline; Associated Press reporting]

- **Equipment certification barrier to adoption** — [Observed] Many jurisdictions that
  wish to implement RCV find that their existing certified voting equipment does not
  support RCV tabulation, requiring either costly equipment replacement or central manual
  tabulation; the absence of RCV-specific EAC certification standards means
  jurisdictions must navigate state-by-state certification processes. [Source: Verified
  Voting Foundation, "Voting Equipment and Ranked Choice Voting" (2021)]

- **Legislative preemption of local adoption** — [Observed] Several states have enacted
  statutes prohibiting localities from using voting methods other than plurality,
  overriding local charter amendments or referenda adopting RCV; as of 2024, Tennessee,
  Arkansas, and several other states have enacted RCV preemption statutes. [Source: NCSL
  preemption statute tracking; FairVote state preemption tracker]

### What evidence would prove/disprove key claims

- Ballot exhaustion rates across jurisdictions and election types would test whether RCV
  produces majority winners in practice or shifts the effective threshold to exhausted-
  ballot-adjusted majorities
- Candidate campaign tone and strategy comparisons (pre/post RCV adoption in the same
  jurisdiction) would test the "civility incentive" claim
- Turnout data pre- and post-RCV adoption in the same jurisdiction, controlling for
  other variables, would test whether RCV increases or decreases participation
- Voter error rate data (overvotes, invalid rankings) would measure implementation
  quality and education effectiveness

### Suggested sources

- Maine Ranked Choice Voting Implementation Act. Pub. L. 2017, ch. 316. Maine
  Legislature. https://legislature.maine.gov/legis/bills/bills_128th/chappdfs/PUBLIC316.pdf

- Alaska Ballot Measure 2 (2020) and implementing statutes. Alaska Division of Elections,
  updated 2024.
  https://www.elections.alaska.gov/RCV.php

- Where is RCV Used? FairVote, updated 2024. (Note: FairVote is an RCV advocacy
  organization; verify data against independent sources.)
  https://www.fairvote.org/where-is-ranked-choice-voting-used

- Ranked Choice Voting. National Conference of State Legislatures (NCSL), updated 2024.
  https://www.ncsl.org/elections-and-campaigns/ranked-choice-voting

- Alaska Division of Elections, 2022 Special Election Results and Administration.
  https://www.elections.alaska.gov/results/22SSPG/

- Burnett, Craig M., and Vladimir Kogan. "Ballot (and voter) 'exhaustion' under Instant
  Runoff Voting." *Electoral Studies* 37 (2015): 41–49.
  https://doi.org/10.1016/j.electstud.2014.11.006

- Donovan, Todd, Caroline Tolbert, and Kellen Gracey. "Campaign civility under
  preferential and plurality voting." *Electoral Studies* 42 (2016): 157–163.
  https://doi.org/10.1016/j.electstud.2016.02.009

### Episode outline (6 parts)

1. **Structure** — RCV is a ballot counting method in which voters rank candidates;
   losers are progressively eliminated and their voters' ballots redistributed until one
   candidate reaches a majority; it is used in federal elections in Maine and Alaska and
   in dozens of local jurisdictions, and is structurally distinct from both plurality
   voting and traditional runoff elections.

2. **Incentive** — Under plurality voting, a candidate can win with less than a majority
   in a multi-candidate field, creating a structural spoiler dynamic; RCV eliminates the
   spoiler incentive in theory because voters can safely rank a preferred minor-party
   candidate first without "wasting" their vote; candidates have structural incentive to
   seek second-choice support across traditional partisan lines.

3. **Example** — In the August 2022 Alaska special election to fill a vacant US House
   seat, Republican Sarah Palin led the first-round count with approximately 31% of the
   vote, Democrat Mary Peltola had 40%, and Republican Nick Begich had 29%; after Begich
   was eliminated in round 2, enough of his voters ranked Peltola second (rather than
   Palin) that Peltola won — the first RCV result in a federal general election in US
   history. [Observed — source: Alaska Division of Elections, 2022 Special Election
   certified results]

4. **Evidence** — Alaska Division of Elections round-by-round tabulation reports; Maine
   Secretary of State 2018 and 2020 RCV tabulation data; FairVote ballot exhaustion
   database (with advocacy-source caveat); NCSL jurisdiction adoption tracker; Burnett
   and Kogan (2015) academic analysis.

5. **Levers** — EAC updating Voluntary Voting System Guidelines to include RCV-specific
   certification standards would remove the equipment bottleneck; uniform state-level
   voter education requirements would reduce ballot exhaustion rates; removing state
   preemption statutes would allow local experimentation; requiring unlimited candidate
   rankings (not capping at 3 or 5) reduces exhaustion risk.

6. **Takeaway** — RCV changes the math of who wins a multi-candidate election by
   requiring majority rather than plurality support, but it introduces real implementation
   complexity — ballot exhaustion, tabulation delay, and equipment certification barriers
   — that affect both adoption and operational performance; the structural effects on
   candidate behavior and voter participation remain empirically contested.

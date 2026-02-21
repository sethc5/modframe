# Debt Issuance Structure

Purpose: How Treasury finances $26+ trillion in federal borrowing through a primary dealer auction system, where maturity composition decisions and an industry-only advisory committee concentrate consequential fiscal authority in a small number of actors.

Status: draft

Tags: mechanics, institutions, accountability, fiscal_policy, debt_management

Outline: see `outline.md`

Contributors: modframe content agent

Related modules: 152, 153, 159, 160, 161

Last reviewed: 2026-02

Actors:
	- name: Treasury Secretary
	  type: official
	- name: Office of Debt Management
	  type: institution
	- name: Treasury Borrowing Advisory Committee
	  type: advisory_body
	- name: Primary Dealers (~24 firms)
	  type: institution
	- name: Federal Reserve Bank of New York
	  type: institution
	- name: Congressional Budget Office
	  type: institution

Statutes:
	- 31 U.S.C. §§ 3101-3130 (public debt)
	- 31 C.F.R. Part 356 (Uniform Offering Circular)
	- 12 U.S.C. § 391 (FRBNY as fiscal agent)

Cases:
	- N/A (primary authority is statutory and regulatory)

Case study:
	name: March 2020 Treasury market disruption
	date: 2020-03
	actors:
		- Primary dealers
		- Federal Reserve
		- Treasury
	outcome: Massive sell-off overwhelmed primary dealer capacity, requiring Fed intervention with unlimited QE announcement on March 23, 2020, exposing concentration risk in the primary dealer model

Data sources:
	- source: Treasury Monthly Statement of the Public Debt
	  format: csv
	  update_frequency: monthly
	  url: https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt
	  accessibility: open
	- source: Treasury Auction Results
	  format: csv/xml
	  update_frequency: per auction
	  url: https://www.treasurydirect.gov/auctions/auction-query/results/
	  accessibility: open
	- source: TBAC Quarterly Materials
	  format: pdf
	  update_frequency: quarterly
	  url: https://home.treasury.gov/policy-issues/financing-the-government/quarterly-refunding
	  accessibility: open

How to contribute:

- Use docs/prompts/draft_module.md to generate initial content
- Add citations under "Suggested sources" in outline.md
- Propose visuals in figures/ and link from here

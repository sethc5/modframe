# Government Subsidy Design Mechanics

Purpose: How federal subsidy programs create self-reinforcing lobbying cycles where recipient industries shape the programs from which they benefit, making subsidy reduction one of the hardest structural problems in democratic governance.

Status: draft

Tags: mechanics, institutions, accountability, fiscal_policy, regulatory_capture, subsidies

Outline: see `outline.md`

Contributors: modframe content agent

Related modules: 157, 159, 164, 148, 149

Last reviewed: 2026-02

Actors:
	- name: House and Senate Authorizing Committees
	  type: committee
	- name: Appropriations Subcommittees
	  type: committee
	- name: USDA
	  type: institution
	- name: Department of Energy
	  type: institution
	- name: Congressional Budget Office
	  type: institution
	- name: Government Accountability Office
	  type: institution

Statutes:
	- Agriculture Improvement Act of 2018 (Farm Bill)
	- OMB Circular A-129 (federal credit programs)
	- Various program-specific authorizing statutes

Cases:
	- N/A

Case study:
	name: Farm Bill reauthorization cycle
	date: 2018-2024
	actors:
		- Senate and House Agriculture Committees
		- American Farm Bureau Federation
		- Commodity program recipients
		- Nutrition program advocates
	outcome: Commodity subsidies and crop insurance subsidies protected through legislative coalition linking agricultural payments to nutrition programs (SNAP), with benefit concentration among the largest operations

Data sources:
	- source: USASpending.gov
	  format: csv/api
	  update_frequency: daily
	  url: https://www.usaspending.gov
	  accessibility: open
	- source: EWG Farm Subsidy Database
	  format: html/csv
	  update_frequency: annual
	  url: https://farm.ewg.org
	  accessibility: open
	- source: GAO Duplication and Cost Savings Reports
	  format: pdf
	  update_frequency: annual
	  url: https://www.gao.gov/duplication-cost-savings
	  accessibility: open

How to contribute:

- Use docs/prompts/draft_module.md to generate initial content
- Add citations under "Suggested sources" in outline.md
- Propose visuals in figures/ and link from here

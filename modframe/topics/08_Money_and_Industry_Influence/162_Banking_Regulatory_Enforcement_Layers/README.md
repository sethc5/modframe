# Banking Regulatory Enforcement Layers

Purpose: How the fragmented multi-agency bank regulatory system produces regulatory competition, enforcement opacity, and penalty inadequacy through overlapping authorities where charter choice enables regulatory arbitrage.

Status: draft

Tags: mechanics, institutions, accountability, financial_regulation, regulatory_capture, enforcement

Outline: see `outline.md`

Contributors: modframe content agent

Related modules: 151, 152, 154, 155, 164

Last reviewed: 2026-02

Actors:
	- name: Office of the Comptroller of the Currency
	  type: regulatory_body
	- name: Federal Reserve
	  type: institution
	- name: Federal Deposit Insurance Corporation
	  type: regulatory_body
	- name: Consumer Financial Protection Bureau
	  type: regulatory_body
	- name: Financial Crimes Enforcement Network
	  type: institution
	- name: Department of Justice
	  type: institution

Statutes:
	- 12 U.S.C. § 1818 (enforcement powers)
	- 12 U.S.C. § 1820(d) (examination requirements)
	- 31 U.S.C. § 5311 et seq. (Bank Secrecy Act)
	- 12 U.S.C. §§ 5491-5603 (CFPB)

Cases:
	- United States v. Wells Fargo Bank, N.A. (DOJ consent order, 2020)

Case study:
	name: Wells Fargo fake accounts enforcement
	date: 2011-2020
	actors:
		- OCC
		- CFPB
		- Federal Reserve
		- DOJ
		- Wells Fargo
	outcome: Multi-agency fragmentation produced delayed enforcement; initial penalty of $185M (2016) scaled to $3B DOJ/SEC consent order (2020) and unprecedented Fed asset cap (2018), demonstrating how overlapping jurisdiction enables delayed, inadequate initial response for the largest institutions

Data sources:
	- source: OCC Enforcement Actions Database
	  format: html
	  update_frequency: ongoing
	  url: https://www.occ.treas.gov/topics/laws-and-regulations/enforcement-actions/index-enforcement-actions.html
	  accessibility: open
	- source: FDIC Enforcement Decisions and Orders
	  format: html
	  update_frequency: ongoing
	  url: https://www.fdic.gov/bank-examinations/enforcement-decisions-and-orders
	  accessibility: open
	- source: Federal Reserve Enforcement Actions
	  format: html
	  update_frequency: ongoing
	  url: https://www.federalreserve.gov/supervisionreg/enforcement-actions.htm
	  accessibility: open

How to contribute:

- Use docs/prompts/draft_module.md to generate initial content
- Add citations under "Suggested sources" in outline.md
- Propose visuals in figures/ and link from here

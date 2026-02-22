# Fundraising Incentives for Conflict

Purpose: short reference and outline for the "Fundraising Incentives for Conflict" module.

Status: sourced

Tags: mechanics, institutions, accountability

Outline: see `outline.md`

Contributors: add names and links here

Related modules: 027, 181, 183, 184, 001, 013

Last reviewed: 2026-02

Actors:
	- name: Members of Congress and candidates
		type: political_entity
	- name: ActBlue
		type: institution
	- name: WinRed
		type: institution
	- name: Democratic Congressional Campaign Committee (DCCC)
		type: political_entity
	- name: National Republican Congressional Committee (NRCC)
		type: political_entity
	- name: Democratic Senatorial Campaign Committee (DSCC)
		type: political_entity
	- name: National Republican Senatorial Committee (NRSC)
		type: political_entity
	- name: Federal Election Commission
		type: regulatory_body

Statutes:
	- Federal Election Campaign Act (52 U.S.C. §§ 30101–30146)

Cases:
	- Buckley v. Valeo, 424 U.S. 1 (1976)
	- Citizens United v. Federal Election Commission, 558 U.S. 310 (2010)

Case study:
	name: Kavanaugh Confirmation Fundraising Spikes (2018)
	date: 2018-09
	actors:
		- ActBlue
		- WinRed
		- DCCC
		- NRCC
		- Senate campaign committees
	outcome: FEC Q3 2018 receipts showed record small-dollar fundraising spikes on both platforms during and immediately after the September–October confirmation hearings, documented in FEC quarterly filings.

Reform proposals:
	- name: For the People Act small-donor matching program
		bill: H.R. 1
		congress: 116th
		status: passed House; not enacted
		addresses_failure_mode: Conflict amplification loop; reduces financial premium on conflict-triggered solicitation by increasing relative weight of non-conflict-motivated constituents

Data sources:
	- source: FEC Campaign Finance Bulk Data
		format: CSV/API
		update_frequency: quarterly
		url: https://www.fec.gov/data/
		accessibility: public
	- source: OpenSecrets Online Fundraising Analysis
		format: web/data download
		update_frequency: ongoing
		url: https://www.opensecrets.org
		accessibility: public
	- source: ActBlue FEC Committee Records
		format: FEC bulk data
		update_frequency: quarterly
		url: https://www.fec.gov/data/committee/C00401224/
		accessibility: public
	- source: WinRed FEC Committee Records
		format: FEC bulk data
		update_frequency: quarterly
		url: https://www.fec.gov/data/committee/C00694323/
		accessibility: public

How to contribute:

- Add citations to `outline.md` under "Suggested sources"
- Propose visuals in `figures/` and link from this README

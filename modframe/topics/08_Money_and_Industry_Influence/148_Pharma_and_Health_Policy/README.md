# Pharma and Health Policy

Purpose: How patent protection, FDA exclusivity, PBM intermediation, and fragmented congressional jurisdiction shape pharmaceutical pricing and health policy outcomes.

Status: draft

Tags: mechanics, institutions, accountability, regulatory_capture, lobbying

Outline: see `outline.md`

Contributors: modframe content agent

Related modules: 149, 150, 158, 164

Last reviewed: 2026-02

Actors:
	- name: Pharmaceutical manufacturers
	  type: industry
	- name: Food and Drug Administration
	  type: regulatory_body
	- name: Centers for Medicare and Medicaid Services
	  type: institution
	- name: Pharmacy Benefit Managers
	  type: industry
	- name: Senate Finance Committee
	  type: committee
	- name: House Energy and Commerce Committee
	  type: committee
	- name: PhRMA
	  type: trade_association

Statutes:
	- 21 U.S.C. §§ 355, 355a (Federal Food, Drug, and Cosmetic Act — drug approval and exclusivity)
	- 42 U.S.C. § 1395w-111 (Medicare Part D prescription drug benefit)
	- Inflation Reduction Act § 11001 (Medicare drug price negotiation)
	- 21 U.S.C. § 355(j)(5)(B)(iii) (Orange Book listing and 30-month stay)

Cases:
	- FTC v. Actavis, Inc., 570 U.S. 136 (2013)
	- Caraco Pharmaceutical Laboratories v. Novo Nordisk, 566 U.S. 399 (2012)

Case study:
	name: Inflation Reduction Act Medicare drug price negotiation
	date: 2022-08
	actors:
		- Centers for Medicare and Medicaid Services
		- Pharmaceutical manufacturers
		- PhRMA
	outcome: First direct federal negotiation channel for Medicare drug prices, initially covering 10 high-expenditure Part D drugs with phased expansion

Data sources:
	- source: OpenSecrets Pharmaceutical/Health Products Lobbying
	  format: csv
	  update_frequency: quarterly
	  url: https://www.opensecrets.org/industries/indus?ind=H04
	  accessibility: open
	- source: FDA Orange Book
	  format: database
	  update_frequency: monthly
	  url: https://www.accessdata.fda.gov/scripts/cder/ob/
	  accessibility: open
	- source: CBO Prescription Drug Pricing Analyses
	  format: pdf
	  update_frequency: ad hoc
	  url: https://www.cbo.gov
	  accessibility: open

How to contribute:

- Use docs/prompts/draft_module.md to generate initial content
- Add citations under "Suggested sources" in outline.md
- Propose visuals in figures/ and link from here

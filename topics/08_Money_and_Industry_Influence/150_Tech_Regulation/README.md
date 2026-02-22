# Tech Regulation

Purpose: How fragmented federal jurisdiction, broad liability shields, and absence of comprehensive legislation shape the regulatory environment for technology companies.

Status: sourced

Tags: mechanics, institutions, accountability, regulatory_capture, lobbying

Outline: see `outline.md`

Contributors: modframe content agent

Related modules: 083, 088, 091, 097, 103, 072

Last reviewed: 2026-02

Actors:
	- name: Federal Trade Commission
	  type: regulatory_body
	- name: Federal Communications Commission
	  type: regulatory_body
	- name: DOJ Antitrust Division
	  type: institution
	- name: Securities and Exchange Commission
	  type: regulatory_body
	- name: Senate Commerce Committee
	  type: committee
	- name: House Energy and Commerce Committee
	  type: committee
	- name: House Judiciary Committee
	  type: committee
	- name: Senate Judiciary Committee
	  type: committee

Statutes:
	- 15 U.S.C. §§ 41–58 (FTC Act)
	- 47 U.S.C. § 230 (CDA Section 230)
	- 15 U.S.C. §§ 1–7 (Sherman Act)
	- 15 U.S.C. §§ 12–27 (Clayton Act)
	- 47 U.S.C. §§ 151–614 (Communications Act)

Cases:
	- FTC v. Facebook, Inc., Case No. 1:20-cv-03590 (D.D.C. 2020)
	- SEC v. W.J. Howey Co., 328 U.S. 293 (1946)

Case study:
	name: FTC antitrust action against Meta
	date: 2020-12
	actors:
		- Federal Trade Commission
		- Meta Platforms Inc.
	outcome: Multi-year litigation demonstrating enforcement timeline lag against platform-scale companies

Data sources:
	- source: OpenSecrets Internet/Technology Sector Lobbying
	  format: csv
	  update_frequency: quarterly
	  url: https://www.opensecrets.org/industries/indus?ind=B13
	  accessibility: open
	- source: FTC Enforcement Actions
	  format: api
	  update_frequency: ad hoc
	  url: https://www.ftc.gov/legal-library/browse/cases-proceedings
	  accessibility: open

How to contribute:

- Use docs/prompts/draft_module.md to generate initial content
- Add citations under "Suggested sources" in outline.md
- Propose visuals in figures/ and link from here

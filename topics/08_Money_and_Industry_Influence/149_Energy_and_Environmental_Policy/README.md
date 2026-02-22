# Energy and Environmental Policy

Purpose: How fragmented federal jurisdiction over energy production, environmental regulation, and subsidy allocation creates multiple access points for industry influence over long-term energy and environmental outcomes.

Status: sourced

Tags: mechanics, institutions, accountability, regulatory_capture, lobbying

Outline: see `outline.md`

Contributors: modframe content agent

Related modules: 148, 150, 158, 159

Last reviewed: 2026-02

Actors:
	- name: Environmental Protection Agency
	  type: regulatory_body
	- name: Department of Energy
	  type: institution
	- name: Federal Energy Regulatory Commission
	  type: regulatory_body
	- name: Department of the Interior
	  type: institution
	- name: Fossil fuel industry
	  type: political_entity
	- name: Renewable energy industry
	  type: political_entity
	- name: Senate Energy and Natural Resources Committee
	  type: committee

Statutes:
	- 42 U.S.C. § 7401 et seq. (Clean Air Act)
	- 16 U.S.C. § 791a et seq. (Federal Power Act / FERC authority)
	- 42 U.S.C. § 4321 et seq. (National Environmental Policy Act)
	- Inflation Reduction Act §§ 13101–13702 (clean energy tax credits)

Cases:
	- West Virginia v. EPA, 597 U.S. 697 (2022)
	- Massachusetts v. EPA, 549 U.S. 497 (2007)

Case study:
	name: NEPA permitting delays on energy infrastructure
	date: 2020-01
	actors:
		- Department of the Interior
		- Federal Energy Regulatory Commission
		- Environmental organizations
	outcome: Multi-year environmental review timelines creating procedural leverage that affects project economics and energy transition speed regardless of project merit

Data sources:
	- source: OpenSecrets Energy/Natural Resources Lobbying
	  format: csv
	  update_frequency: quarterly
	  url: https://www.opensecrets.org/industries/indus?ind=E
	  accessibility: open
	- source: FERC Dockets and Ex Parte Logs
	  format: database
	  update_frequency: continuous
	  url: https://www.ferc.gov
	  accessibility: open
	- source: GAO Reports on NEPA Review Timelines
	  format: pdf
	  update_frequency: ad hoc
	  url: https://www.gao.gov
	  accessibility: open

How to contribute:

- Use docs/prompts/draft_module.md to generate initial content
- Add citations under "Suggested sources" in outline.md
- Propose visuals in figures/ and link from here

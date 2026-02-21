# Procurement Contracting Pathways

Purpose: How the federal government's ~$700 billion annual procurement system formally requires competition but structurally favors incumbent prime contractors through IDIQ vehicles, past performance advantages, and procedural complexity.

Status: draft

Tags: mechanics, institutions, accountability, procurement, regulatory_capture

Outline: see `outline.md`

Contributors: modframe content agent

Related modules: 048, 150, 158, 164

Last reviewed: 2026-02

Actors:
	- name: Contracting Officers
	  type: official
	- name: Office of Federal Procurement Policy
	  type: institution
	- name: General Services Administration
	  type: institution
	- name: Small Business Administration
	  type: institution
	- name: Government Accountability Office
	  type: institution

Statutes:
	- 41 U.S.C. § 3301 (competition requirements)
	- 10 U.S.C. § 3201 et seq. (defense procurement)
	- 48 C.F.R. Chapter 1 (Federal Acquisition Regulation)
	- 15 U.S.C. § 644 (small business set-asides)

Cases:
	- N/A (protests adjudicated at GAO and Court of Federal Claims)

Case study:
	name: Major IDIQ vehicle task order concentration
	date: ongoing
	actors:
		- GSA
		- Pre-qualified prime contractors
		- Agency contracting officers
	outcome: IDIQ vehicles route billions in spending through simplified competition among pre-qualified pools, creating competitive oligopolies that reduce the competitive pressure that the initial vehicle award was designed to produce

Data sources:
	- source: Federal Procurement Data System (FPDS-NG)
	  format: csv/xml
	  update_frequency: real-time
	  url: https://www.fpds.gov
	  accessibility: open
	- source: USASpending.gov
	  format: csv/api
	  update_frequency: daily
	  url: https://www.usaspending.gov
	  accessibility: open
	- source: SBA Small Business Procurement Scorecard
	  format: html
	  update_frequency: annual
	  url: https://www.sba.gov/document/support--small-business-procurement-scorecard
	  accessibility: open

How to contribute:

- Use docs/prompts/draft_module.md to generate initial content
- Add citations under "Suggested sources" in outline.md
- Propose visuals in figures/ and link from here

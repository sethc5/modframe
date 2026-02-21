# Fed Open Market Operations Structure

Purpose: How the Fed's Open Market Trading Desk translates FOMC interest rate decisions into actual financial conditions through a $7T+ balance sheet, ~24 primary dealer counterparties, and administered rate facilities — with profound effects on asset prices, wealth distribution, and fiscal outcomes that operate with delayed disclosure and limited democratic accountability.

Status: draft

Tags: mechanics, institutions, accountability, monetary_policy, financial_regulation

Outline: see `outline.md`

Contributors: modframe content agent

Related modules: 152, 153, 156, 160

Last reviewed: 2026-02

Actors:
	- name: Federal Open Market Committee
	  type: institution
	- name: Federal Reserve Bank of New York
	  type: institution
	- name: Open Market Trading Desk
	  type: institution
	- name: Primary Dealers (~24 firms)
	  type: institution
	- name: Board of Governors
	  type: institution

Statutes:
	- 12 U.S.C. § 355 (Federal Reserve Act § 14, OMO authority)
	- 12 U.S.C. § 225a (dual mandate)
	- 12 U.S.C. § 263 (FOMC composition)
	- Dodd-Frank § 1103 (GAO audit authority)

Cases:
	- N/A

Case study:
	name: 2020-2024 QE/QT cycle
	date: 2020-03 to 2024
	actors:
		- FOMC
		- Open Market Trading Desk
		- Primary dealers
	outcome: Balance sheet expanded from ~$4T to ~$9T via unlimited QE, then QT reduced to ~$7T but never returned to pre-COVID levels; Fed began accumulating deferred asset (net operating losses) in September 2022 as interest expense on reserves exceeded SOMA portfolio income

Data sources:
	- source: Federal Reserve H.4.1 Statistical Release
	  format: csv/html
	  update_frequency: weekly
	  url: https://www.federalreserve.gov/releases/h41/
	  accessibility: open
	- source: FOMC Statements, Minutes, and Transcripts
	  format: pdf/html
	  update_frequency: per meeting (minutes 3-week lag; transcripts 5-year lag)
	  url: https://www.federalreserve.gov/monetarypolicy/fomc.htm
	  accessibility: open
	- source: FRBNY Markets Data
	  format: csv/html
	  update_frequency: daily
	  url: https://www.newyorkfed.org/markets
	  accessibility: open

How to contribute:

- Use docs/prompts/draft_module.md to generate initial content
- Add citations under "Suggested sources" in outline.md
- Propose visuals in figures/ and link from here

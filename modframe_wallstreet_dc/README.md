# Modframe Wallstreet DC (Bridge Concept Stub)

A bridge project connecting `modframe` (political power mechanics) and `modframe_wallstreet` (financial-system power mechanics).

## Core purpose

Map how public power and market power interact:

- Policy design ↔ capital allocation
- Regulatory architecture ↔ market structure outcomes
- Enforcement capacity ↔ incentive behavior in firms and intermediaries
- Election/governance cycles ↔ risk-taking, liquidity, and concentration dynamics

## Bridge thesis

Political institutions and market institutions are co-governed systems.
This project explains cross-system mechanisms where decisions in one domain systematically shift power in the other.

## Priority mechanism families

1. Rulemaking and market adaptation loops
2. Oversight asymmetry and compliance arbitrage
3. Lobbying, disclosure, and agenda influence channels
4. Crisis backstop design and moral-hazard transmission
5. Procurement, contracting, and public-private dependency networks
6. Information control (data, ratings, benchmarks, platform access)

## Module format (same core structure)

Each bridge module should preserve Modframe compatibility:

- Summary
- Mechanism in one sentence
- Actors and roles (public + private)
- Process map
- Where power concentrates
- Common failure modes
- Evidence tests
- Suggested sources
- Episode outline

## Cross-project metadata requirements (draft)

- `Related modules`: include IDs from both upstream libraries when relevant
- `Actors`: tag actors by domain (`public`, `market`, `hybrid`)
- `Statutes` + `Cases`: include legal anchors on both regulatory and market sides
- `Data sources`: list datasets enabling cross-domain verification

## Suggested repository role

`modframe_wallstreet_dc` acts as an integration layer, not a replacement:

- Keep `modframe` and `modframe_wallstreet` independent and focused
- Use this bridge repo for cross-domain modules and synthesis indexes
- Optionally consume exports from both repos (queue/index bundles) for linking

## Initial launch plan

1. Define 12 bridge modules across 3 sections
2. Add schema + validator compatibility with both upstream repos
3. Build a small crosswalk index (`policy_to_market.json`, `market_to_policy.json`)
4. Publish 1 golden bridge example before scaling

## Naming note

Current name: `modframe_wallstreet_dc`.
Alternative: `modframe_bridge` or `modframe_public_markets`.

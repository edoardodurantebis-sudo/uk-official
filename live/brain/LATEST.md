# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T18:58:17.129102Z`  
Memory snapshots: **305**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3299 d1=2.0 d12=72.0 z=38.770670074074076
- **PERSISTENT_UP** `biomass_gen` value=3299 d1=2.0 d12=72.0 z=38.770670074074076
- **ROBUST_OUTLIER** `biomass_gen` value=3299 d1=2.0 d12=72.0 z=38.770670074074076
- **ROBUST_OUTLIER** `ind_demand` value=-1.191e+04 d1=0.0 d12=8.0 z=4.72142825
- **CHANGE_POINT** `margin` value=3.559e+04 d1=0.0 d12=-81.0 z=1.9977744023809523
- **CHANGE_POINT** `thermal_base` value=1.422e+04 d1=-2.0 d12=406.0 z=1.1167999228195011
- **CHANGE_POINT** `ccgt_gen` value=1.09e+04 d1=-5.0 d12=397.0 z=1.1162069641801549
- **CHANGE_POINT** `ps_gen` value=803 d1=-1.0 d12=65.0 z=0.9896029300781249
- **CHANGE_POINT** `interconnector_net` value=-1701 d1=-78.0 d12=-14.0 z=-0.8582845297003888
- **CHANGE_POINT** `imbalance` value=5739 d1=0.0 d12=-36.0 z=-0.41996531603773585
- **CHANGE_POINT** `ind_generation` value=2.486e+04 d1=0.0 d12=-36.0 z=-0.41996531603773585
- **PERSISTENT_DOWN** `margin` value=3.559e+04 d1=0.0 d12=-81.0 z=1.9977744023809523
- **REVERSAL** `wind_gen` value=9931 d1=24.0 d12=-293.0 z=-1.133075833126551
- **REVERSAL** `thermal_base` value=1.422e+04 d1=-2.0 d12=406.0 z=1.1167999228195011
- **REVERSAL** `ccgt_gen` value=1.09e+04 d1=-5.0 d12=397.0 z=1.1162069641801549

## Nearest historical live analogues

- `2026-09-15T17:50:55.506503Z` distance=0.062 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.062 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:59:22.215947Z` distance=0.062 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:03:35.364442Z` distance=0.062 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:22:30.581865Z` distance=0.151 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T18:49:51.656019Z`  
Memory snapshots: **303**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3299 d1=0.0 d12=93.0 z=38.770670074074076
- **PERSISTENT_UP** `biomass_gen` value=3299 d1=0.0 d12=93.0 z=38.770670074074076
- **ROBUST_OUTLIER** `biomass_gen` value=3299 d1=0.0 d12=93.0 z=38.770670074074076
- **ROBUST_OUTLIER** `ind_demand` value=-1.191e+04 d1=0.0 d12=9.0 z=5.395918
- **CHANGE_POINT** `margin` value=3.559e+04 d1=-65.0 d12=-81.0 z=1.9977744023809523
- **CHANGE_POINT** `ccgt_gen` value=1.085e+04 d1=0.0 d12=445.0 z=1.4239724780033138
- **CHANGE_POINT** `thermal_base` value=1.417e+04 d1=0.0 d12=448.0 z=1.4217613377672802
- **CHANGE_POINT** `ps_gen` value=803 d1=0.0 d12=296.0 z=0.989111333853354
- **CHANGE_POINT** `imbalance` value=5737 d1=0.0 d12=-38.0 z=-0.4454177594339623
- **CHANGE_POINT** `ind_generation` value=2.486e+04 d1=0.0 d12=-38.0 z=-0.4454177594339623
- **PERSISTENT_DOWN** `margin` value=3.559e+04 d1=-65.0 d12=-81.0 z=1.9977744023809523
- **ACCELERATION** `margin` value=3.559e+04 d1=-65.0 d12=-81.0 z=1.9977744023809523
- **PERSISTENT_UP** `ccgt_gen` value=1.085e+04 d1=0.0 d12=445.0 z=1.4239724780033138
- **PERSISTENT_UP** `thermal_base` value=1.417e+04 d1=0.0 d12=448.0 z=1.4217613377672802

## Nearest historical live analogues

- `2026-09-15T17:50:55.506503Z` distance=0.063 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.063 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:22:30.581865Z` distance=0.151 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:26:42.593420Z` distance=0.151 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:30:55.285075Z` distance=0.151 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

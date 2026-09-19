# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T17:39:26.231429Z`  
Memory snapshots: **1561**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=607 d1=-1.0 d12=1.0 z=24.95612075
- **REVERSAL** `biomass_gen` value=607 d1=-1.0 d12=1.0 z=24.95612075
- **ACCELERATION** `biomass_gen` value=607 d1=-1.0 d12=1.0 z=24.95612075
- **ROBUST_OUTLIER** `biomass_gen` value=607 d1=-1.0 d12=1.0 z=24.95612075
- **CHANGE_POINT** `ccgt_gen` value=6774 d1=78.0 d12=2265.0 z=6.015039188432836
- **CHANGE_POINT** `thermal_base` value=1.01e+04 d1=78.0 d12=2254.0 z=6.013290311643836
- **PERSISTENT_UP** `ccgt_gen` value=6774 d1=78.0 d12=2265.0 z=6.015039188432836
- **ROBUST_OUTLIER** `ccgt_gen` value=6774 d1=78.0 d12=2265.0 z=6.015039188432836
- **PERSISTENT_UP** `thermal_base` value=1.01e+04 d1=78.0 d12=2254.0 z=6.013290311643836
- **ROBUST_OUTLIER** `thermal_base` value=1.01e+04 d1=78.0 d12=2254.0 z=6.013290311643836
- **CHANGE_POINT** `margin` value=3.625e+04 d1=0.0 d12=-673.0 z=-2.4778130399305556
- **ROBUST_OUTLIER** `ps_gen` value=796 d1=-36.0 d12=-185.0 z=3.6495975780922434
- **ROBUST_OUTLIER** `ind_generation` value=1.682e+04 d1=0.0 d12=15.0 z=3.2038263125
- **ROBUST_OUTLIER** `residual_proxy` value=1.259e+04 d1=0.0 d12=0.0 z=-3.1556484732142858
- **PERSISTENT_DOWN** `nuclear_gen` value=3327 d1=0.0 d12=-11.0 z=-1.3489795

## Nearest historical live analogues

- `2026-09-19T11:50:05.858742Z` distance=0.174 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.178 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.178 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.178 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.178 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

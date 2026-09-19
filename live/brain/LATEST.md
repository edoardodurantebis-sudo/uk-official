# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T17:43:39.582352Z`  
Memory snapshots: **1562**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=608 d1=1.0 d12=2.0 z=21.920916875
- **PERSISTENT_UP** `biomass_gen` value=608 d1=1.0 d12=2.0 z=21.920916875
- **ACCELERATION** `biomass_gen` value=608 d1=1.0 d12=2.0 z=21.920916875
- **ROBUST_OUTLIER** `biomass_gen` value=608 d1=1.0 d12=2.0 z=21.920916875
- **CHANGE_POINT** `ccgt_gen` value=6805 d1=31.0 d12=2260.0 z=6.051160523883374
- **CHANGE_POINT** `thermal_base` value=1.014e+04 d1=36.0 d12=2256.0 z=6.011358709001233
- **PERSISTENT_UP** `ccgt_gen` value=6805 d1=31.0 d12=2260.0 z=6.051160523883374
- **ROBUST_OUTLIER** `ccgt_gen` value=6805 d1=31.0 d12=2260.0 z=6.051160523883374
- **PERSISTENT_UP** `thermal_base` value=1.014e+04 d1=36.0 d12=2256.0 z=6.011358709001233
- **ROBUST_OUTLIER** `thermal_base` value=1.014e+04 d1=36.0 d12=2256.0 z=6.011358709001233
- **CHANGE_POINT** `ind_generation` value=1.682e+04 d1=0.0 d12=15.0 z=3.2038263125
- **CHANGE_POINT** `margin` value=3.625e+04 d1=0.0 d12=-8.0 z=-2.4778130399305556
- **PERSISTENT_DOWN** `ps_gen` value=796 d1=0.0 d12=-186.0 z=3.8185798626681615
- **ROBUST_OUTLIER** `ps_gen` value=796 d1=0.0 d12=-186.0 z=3.8185798626681615
- **ROBUST_OUTLIER** `ind_generation` value=1.682e+04 d1=0.0 d12=15.0 z=3.2038263125

## Nearest historical live analogues

- `2026-09-19T11:50:05.858742Z` distance=0.174 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.178 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.178 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.178 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.178 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

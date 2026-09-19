# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T17:35:13.165368Z`  
Memory snapshots: **1560**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=608 d1=0.0 d12=1.0 z=29.452719083333335
- **PERSISTENT_UP** `biomass_gen` value=608 d1=0.0 d12=1.0 z=29.452719083333335
- **ROBUST_OUTLIER** `biomass_gen` value=608 d1=0.0 d12=1.0 z=29.452719083333335
- **CHANGE_POINT** `thermal_base` value=1.002e+04 d1=0.0 d12=2283.0 z=5.921648105889724
- **CHANGE_POINT** `ccgt_gen` value=6696 d1=0.0 d12=2289.0 z=5.899682788341646
- **PERSISTENT_UP** `thermal_base` value=1.002e+04 d1=0.0 d12=2283.0 z=5.921648105889724
- **ROBUST_OUTLIER** `thermal_base` value=1.002e+04 d1=0.0 d12=2283.0 z=5.921648105889724
- **PERSISTENT_UP** `ccgt_gen` value=6696 d1=0.0 d12=2289.0 z=5.899682788341646
- **ROBUST_OUTLIER** `ccgt_gen` value=6696 d1=0.0 d12=2289.0 z=5.899682788341646
- **CHANGE_POINT** `ind_generation` value=1.682e+04 d1=0.0 d12=15.0 z=3.2038263125
- **CHANGE_POINT** `margin` value=3.625e+04 d1=0.0 d12=-673.0 z=-2.4778130399305556
- **ACCELERATION** `ps_gen` value=832 d1=0.0 d12=-95.0 z=3.4805730610687022
- **ROBUST_OUTLIER** `ps_gen` value=832 d1=0.0 d12=-95.0 z=3.4805730610687022
- **PERSISTENT_UP** `ind_generation` value=1.682e+04 d1=0.0 d12=15.0 z=3.2038263125
- **ROBUST_OUTLIER** `ind_generation` value=1.682e+04 d1=0.0 d12=15.0 z=3.2038263125

## Nearest historical live analogues

- `2026-09-19T11:50:05.858742Z` distance=0.174 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.178 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.178 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.178 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.178 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T18:05:11.055248Z`  
Memory snapshots: **1908**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=2260 d1=0.0 d12=50.0 z=204.98356675000002
- **ROBUST_OUTLIER** `biomass_gen` value=2260 d1=0.0 d12=50.0 z=204.98356675000002
- **PERSISTENT_UP** `thermal_base` value=1.229e+04 d1=0.0 d12=1354.0 z=50.8769187005814
- **ROBUST_OUTLIER** `thermal_base` value=1.229e+04 d1=0.0 d12=1354.0 z=50.8769187005814
- **PERSISTENT_UP** `ccgt_gen` value=8951 d1=0.0 d12=1354.0 z=50.829861276162795
- **ROBUST_OUTLIER** `ccgt_gen` value=8951 d1=0.0 d12=1354.0 z=50.829861276162795
- **CHANGE_POINT** `margin` value=3.546e+04 d1=0.0 d12=-424.0 z=-15.657797767857144
- **ROBUST_OUTLIER** `margin` value=3.546e+04 d1=0.0 d12=-424.0 z=-15.657797767857144
- **PERSISTENT_UP** `imbalance` value=-5165 d1=0.0 d12=25.0 z=3.989360106707317
- **ROBUST_OUTLIER** `imbalance` value=-5165 d1=0.0 d12=25.0 z=3.989360106707317
- **CHANGE_POINT** `wind_gen` value=6609 d1=0.0 d12=-1131.0 z=-1.226366477145359
- **PERSISTENT_UP** `ps_gen` value=222 d1=0.0 d12=160.0 z=3.1441599115384617
- **ACCELERATION** `ps_gen` value=222 d1=0.0 d12=160.0 z=3.1441599115384617
- **ROBUST_OUTLIER** `ps_gen` value=222 d1=0.0 d12=160.0 z=3.1441599115384617
- **PERSISTENT_DOWN** `wind_gen` value=6609 d1=0.0 d12=-1131.0 z=-1.226366477145359

## Nearest historical live analogues

- `2026-09-20T14:49:59.741529Z` distance=0.041 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:24:12.719546Z` distance=0.046 → {'next30m_imbalance_delta': 81.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:28:27.793665Z` distance=0.046 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:32:40.592900Z` distance=0.046 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:36:50.929973Z` distance=0.046 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

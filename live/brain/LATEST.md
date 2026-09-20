# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T17:52:35.892709Z`  
Memory snapshots: **1905**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `biomass_gen` value=2259 d1=0.0 d12=124.0 z=225.41447445
- **PERSISTENT_UP** `thermal_base` value=1.218e+04 d1=40.0 d12=1711.0 z=71.33983322727273
- **ROBUST_OUTLIER** `thermal_base` value=1.218e+04 d1=40.0 d12=1711.0 z=71.33983322727273
- **PERSISTENT_UP** `ccgt_gen` value=8842 d1=39.0 d12=1714.0 z=67.3857415859375
- **ROBUST_OUTLIER** `ccgt_gen` value=8842 d1=39.0 d12=1714.0 z=67.3857415859375
- **CHANGE_POINT** `margin` value=3.546e+04 d1=-325.0 d12=-424.0 z=-15.657797767857144
- **PERSISTENT_DOWN** `margin` value=3.546e+04 d1=-325.0 d12=-424.0 z=-15.657797767857144
- **ACCELERATION** `margin` value=3.546e+04 d1=-325.0 d12=-424.0 z=-15.657797767857144
- **ROBUST_OUTLIER** `margin` value=3.546e+04 d1=-325.0 d12=-424.0 z=-15.657797767857144
- **ROBUST_OUTLIER** `imbalance` value=-5172 d1=0.0 d12=18.0 z=7.361983867021277
- **CHANGE_POINT** `wind_gen` value=6873 d1=-98.0 d12=-904.0 z=-1.1186819297178987
- **REVERSAL** `ps_gen` value=-11 d1=3.0 d12=-176.0 z=2.651918744027304
- **ACCELERATION** `ps_gen` value=-11 d1=3.0 d12=-176.0 z=2.651918744027304
- **REVERSAL** `interconnector_net` value=1.004e+04 d1=2.0 d12=-1604.0 z=1.5241969483888889
- **PERSISTENT_DOWN** `wind_gen` value=6873 d1=-98.0 d12=-904.0 z=-1.1186819297178987

## Nearest historical live analogues

- `2026-09-20T14:49:59.741529Z` distance=0.041 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:24:12.719546Z` distance=0.046 → {'next30m_imbalance_delta': 81.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:28:27.793665Z` distance=0.046 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:32:40.592900Z` distance=0.046 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:36:50.929973Z` distance=0.046 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

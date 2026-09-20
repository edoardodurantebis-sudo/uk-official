# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T11:14:40.539694Z`  
Memory snapshots: **1811**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=33.454691600000004
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=33.454691600000004
- **CHANGE_POINT** `ind_generation` value=1.536e+04 d1=0.0 d12=-668.0 z=15.726071176470588
- **ROBUST_OUTLIER** `ind_generation` value=1.536e+04 d1=0.0 d12=-668.0 z=15.726071176470588
- **CHANGE_POINT** `margin` value=3.579e+04 d1=0.0 d12=-3985.0 z=-10.217928054824561
- **ROBUST_OUTLIER** `margin` value=3.579e+04 d1=0.0 d12=-3985.0 z=-10.217928054824561
- **CHANGE_POINT** `imbalance` value=-5746 d1=0.0 d12=-1606.0 z=2.330673825210084
- **ROBUST_OUTLIER** `residual_proxy` value=1.824e+04 d1=0.0 d12=1031.0 z=3.883043794392523
- **PERSISTENT_DOWN** `wind_gen` value=1.352e+04 d1=0.0 d12=-494.0 z=-3.2075539866710012
- **ACCELERATION** `wind_gen` value=1.352e+04 d1=0.0 d12=-494.0 z=-3.2075539866710012
- **ROBUST_OUTLIER** `wind_gen` value=1.352e+04 d1=0.0 d12=-494.0 z=-3.2075539866710012
- **CHANGE_POINT** `ps_gen` value=-674 d1=0.0 d12=-20.0 z=0.8910690275229358
- **PERSISTENT_DOWN** `nuclear_gen` value=3331 d1=0.0 d12=-7.0 z=-1.686224375
- **ACCELERATION** `nuclear_gen` value=3331 d1=0.0 d12=-7.0 z=-1.686224375
- **PERSISTENT_DOWN** `thermal_base` value=5725 d1=0.0 d12=-120.0 z=-1.2177605850000002

## Nearest historical live analogues

- `2026-09-20T04:50:36.902238Z` distance=0.754 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:54:47.005275Z` distance=0.754 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:58:57.948602Z` distance=0.754 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:03:10.294370Z` distance=0.754 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:07:21.689505Z` distance=0.754 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 161.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

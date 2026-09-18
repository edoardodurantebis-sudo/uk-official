# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T09:09:00.361850Z`  
Memory snapshots: **1153**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1792 d1=-86.0 d12=-371.0 z=-15.639731078125
- **PERSISTENT_DOWN** `biomass_gen` value=1792 d1=-86.0 d12=-371.0 z=-15.639731078125
- **ROBUST_OUTLIER** `biomass_gen` value=1792 d1=-86.0 d12=-371.0 z=-15.639731078125
- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=4.0 z=-4.42465276
- **PERSISTENT_DOWN** `wind_gen` value=1.191e+04 d1=-119.0 d12=-512.0 z=-3.7055933833586625
- **ROBUST_OUTLIER** `wind_gen` value=1.191e+04 d1=-119.0 d12=-512.0 z=-3.7055933833586625
- **CHANGE_POINT** `ps_gen` value=163 d1=-61.0 d12=-218.0 z=-1.2622895948275863
- **ROBUST_OUTLIER** `imbalance` value=9602 d1=0.0 d12=-616.0 z=-3.24766814625
- **CHANGE_POINT** `thermal_base` value=6821 d1=-58.0 d12=-641.0 z=-0.64918867063129
- **PERSISTENT_UP** `interconnector_net` value=3658 d1=661.0 d12=501.0 z=2.64203631229848
- **ACCELERATION** `interconnector_net` value=3658 d1=661.0 d12=501.0 z=2.64203631229848
- **CHANGE_POINT** `ccgt_gen` value=3488 d1=-59.0 d12=-645.0 z=-0.6408264684664247
- **CHANGE_POINT** `ts_demand_forecast` value=1.764e+04 d1=0.0 d12=0.0 z=None
- **PERSISTENT_DOWN** `ps_gen` value=163 d1=-61.0 d12=-218.0 z=-1.2622895948275863
- **PERSISTENT_DOWN** `thermal_base` value=6821 d1=-58.0 d12=-641.0 z=-0.64918867063129

## Nearest historical live analogues

- `2026-09-18T07:23:09.699179Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:27:20.707745Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:31:32.031758Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:35:44.221296Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:39:57.955920Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

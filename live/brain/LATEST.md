# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T09:13:12.027753Z`  
Memory snapshots: **1154**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1744 d1=-48.0 d12=-429.0 z=-17.663200328125
- **PERSISTENT_DOWN** `biomass_gen` value=1744 d1=-48.0 d12=-429.0 z=-17.663200328125
- **ROBUST_OUTLIER** `biomass_gen` value=1744 d1=-48.0 d12=-429.0 z=-17.663200328125
- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=1.0 z=-4.42465276
- **CHANGE_POINT** `ps_gen` value=-66 d1=-229.0 d12=-610.0 z=-2.230679267241379
- **PERSISTENT_DOWN** `wind_gen` value=1.176e+04 d1=-153.0 d12=-549.0 z=-3.8342526810218978
- **ROBUST_OUTLIER** `wind_gen` value=1.176e+04 d1=-153.0 d12=-549.0 z=-3.8342526810218978
- **ROBUST_OUTLIER** `imbalance` value=9602 d1=0.0 d12=-23.0 z=-3.24766814625
- **CHANGE_POINT** `ccgt_gen` value=3473 d1=-15.0 d12=-521.0 z=-0.67448975
- **PERSISTENT_UP** `interconnector_net` value=3890 d1=232.0 d12=734.0 z=2.672341581703434
- **ACCELERATION** `interconnector_net` value=3890 d1=232.0 d12=734.0 z=2.672341581703434
- **CHANGE_POINT** `thermal_base` value=6807 d1=-14.0 d12=-517.0 z=-0.6720008579335793
- **PERSISTENT_DOWN** `ps_gen` value=-66 d1=-229.0 d12=-610.0 z=-2.230679267241379
- **CHANGE_POINT** `ts_demand_forecast` value=1.764e+04 d1=0.0 d12=0.0 z=None
- **PERSISTENT_DOWN** `ccgt_gen` value=3473 d1=-15.0 d12=-521.0 z=-0.67448975

## Nearest historical live analogues

- `2026-09-18T08:17:51.592822Z` distance=0.062 → {'next30m_imbalance_delta': -593.0, 'next30m_margin_delta': -112.0, 'next30m_residual_proxy_delta': 74.0}
- `2026-09-18T07:23:09.699179Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:27:20.707745Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:31:32.031758Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:35:44.221296Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

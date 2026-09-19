# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T23:40:45.024273Z`  
Memory snapshots: **1647**  
Current physical regime: **TIGHT**

Regime read: margin low, wind falling.

## Active patterns

- **ROBUST_OUTLIER** `ps_gen` value=-251 d1=0.0 d12=-118.0 z=-85.22376370588235
- **ROBUST_OUTLIER** `ind_demand` value=-1.189e+04 d1=0.0 d12=-14.0 z=-10.11734625
- **CHANGE_POINT** `wind_gen` value=1.6e+04 d1=-12.0 d12=761.0 z=3.0456999942489853
- **PERSISTENT_DOWN** `thermal_base` value=6465 d1=-61.0 d12=-744.0 z=-3.9268904272119345
- **ROBUST_OUTLIER** `thermal_base` value=6465 d1=-61.0 d12=-744.0 z=-3.9268904272119345
- **PERSISTENT_DOWN** `ccgt_gen` value=3127 d1=-63.0 d12=-743.0 z=-3.9103853604294483
- **ROBUST_OUTLIER** `ccgt_gen` value=3127 d1=-63.0 d12=-743.0 z=-3.9103853604294483
- **CHANGE_POINT** `margin` value=3.607e+04 d1=0.0 d12=11.0 z=-1.78065294
- **REVERSAL** `wind_gen` value=1.6e+04 d1=-12.0 d12=761.0 z=3.0456999942489853
- **ROBUST_OUTLIER** `wind_gen` value=1.6e+04 d1=-12.0 d12=761.0 z=3.0456999942489853
- **CHANGE_POINT** `biomass_gen` value=879 d1=-30.0 d12=-47.0 z=-0.40469385
- **REVERSAL** `interconnector_net` value=-8379 d1=2.0 d12=-733.0 z=-1.3378635729719832
- **REVERSAL** `nuclear_gen` value=3338 d1=2.0 d12=-1.0 z=0.67448975
- **PERSISTENT_DOWN** `biomass_gen` value=879 d1=-30.0 d12=-47.0 z=-0.40469385
- **ACCELERATION** `biomass_gen` value=879 d1=-30.0 d12=-47.0 z=-0.40469385

## Nearest historical live analogues

- `2026-09-19T19:24:22.442601Z` distance=0.106 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -119.0}
- `2026-09-19T19:28:35.593770Z` distance=0.106 → {'next30m_imbalance_delta': -36.0, 'next30m_margin_delta': 40.0, 'next30m_residual_proxy_delta': -119.0}
- `2026-09-19T18:21:25.144867Z` distance=0.110 → {'next30m_imbalance_delta': -611.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T18:25:36.560673Z` distance=0.110 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T18:29:47.180961Z` distance=0.110 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

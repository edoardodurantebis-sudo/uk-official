# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T09:56:02.414820Z`  
Memory snapshots: **518**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1204.0 z=-27.39086423780488
- **ROBUST_OUTLIER** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1204.0 z=-27.39086423780488
- **CHANGE_POINT** `margin` value=3.416e+04 d1=0.0 d12=-1586.0 z=-23.344445242105266
- **PERSISTENT_DOWN** `margin` value=3.416e+04 d1=0.0 d12=-1586.0 z=-23.344445242105266
- **ROBUST_OUTLIER** `margin` value=3.416e+04 d1=0.0 d12=-1586.0 z=-23.344445242105266
- **CHANGE_POINT** `imbalance` value=5367 d1=0.0 d12=-1338.0 z=-10.968337990654206
- **ROBUST_OUTLIER** `imbalance` value=5367 d1=0.0 d12=-1338.0 z=-10.968337990654206
- **CHANGE_POINT** `biomass_gen` value=3212 d1=11.0 d12=-30.0 z=-6.7448975
- **REVERSAL** `biomass_gen` value=3212 d1=11.0 d12=-30.0 z=-6.7448975
- **ACCELERATION** `biomass_gen` value=3212 d1=11.0 d12=-30.0 z=-6.7448975
- **ROBUST_OUTLIER** `biomass_gen` value=3212 d1=11.0 d12=-30.0 z=-6.7448975
- **CHANGE_POINT** `interconnector_net` value=1.031e+04 d1=1.0 d12=52.0 z=1.179061834943591
- **CHANGE_POINT** `thermal_base` value=9632 d1=-61.0 d12=-1261.0 z=-1.0228177899061033
- **CHANGE_POINT** `ccgt_gen` value=6305 d1=-62.0 d12=-1254.0 z=-1.0194577900763357
- **PERSISTENT_DOWN** `wind_gen` value=5591 d1=-26.0 d12=-752.0 z=-1.2697572128874388

## Nearest historical live analogues

- `2026-09-16T08:52:24.970739Z` distance=3.006 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=3.006 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=3.006 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:17:56.653795Z` distance=3.138 → {'next30m_imbalance_delta': 235.0, 'next30m_margin_delta': 235.0, 'next30m_residual_proxy_delta': -321.0}
- `2026-09-16T07:23:21.620957Z` distance=3.140 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

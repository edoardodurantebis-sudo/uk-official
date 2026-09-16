# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T10:00:23.940322Z`  
Memory snapshots: **519**  
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
- **PERSISTENT_DOWN** `biomass_gen` value=3212 d1=0.0 d12=-30.0 z=-6.7448975
- **ACCELERATION** `biomass_gen` value=3212 d1=0.0 d12=-30.0 z=-6.7448975
- **ROBUST_OUTLIER** `biomass_gen` value=3212 d1=0.0 d12=-30.0 z=-6.7448975
- **CHANGE_POINT** `thermal_base` value=9632 d1=0.0 d12=-1147.0 z=-1.0228177899061033
- **CHANGE_POINT** `ccgt_gen` value=6305 d1=0.0 d12=-1144.0 z=-1.0194577900763357
- **CHANGE_POINT** `interconnector_net` value=1.031e+04 d1=0.0 d12=55.0 z=0.9466238623525113
- **PERSISTENT_DOWN** `wind_gen` value=5591 d1=0.0 d12=-684.0 z=-1.2604045817699836
- **PERSISTENT_DOWN** `thermal_base` value=9632 d1=0.0 d12=-1147.0 z=-1.0228177899061033

## Nearest historical live analogues

- `2026-09-16T08:52:24.970739Z` distance=3.006 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=3.006 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=3.006 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:05:03.473837Z` distance=3.006 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:17:56.653795Z` distance=3.138 → {'next30m_imbalance_delta': 235.0, 'next30m_margin_delta': 235.0, 'next30m_residual_proxy_delta': -321.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

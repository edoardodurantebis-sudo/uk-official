# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T00:16:55.131775Z`  
Memory snapshots: **685**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=-657.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=657.0 z=10.40400439375
- **ROBUST_OUTLIER** `interconnector_net` value=-6590 d1=-49.0 d12=-834.0 z=-5.134139079442087
- **PERSISTENT_DOWN** `ccgt_gen` value=4533 d1=-41.0 d12=-1223.0 z=-3.5503107731164385
- **ROBUST_OUTLIER** `ccgt_gen` value=4533 d1=-41.0 d12=-1223.0 z=-3.5503107731164385
- **PERSISTENT_DOWN** `thermal_base` value=7843 d1=-43.0 d12=-1226.0 z=-3.5383824470387246
- **ROBUST_OUTLIER** `thermal_base` value=7843 d1=-43.0 d12=-1226.0 z=-3.5383824470387246
- **CHANGE_POINT** `imbalance` value=6451 d1=0.0 d12=-152.0 z=-0.607040775
- **CHANGE_POINT** `ind_generation` value=2.557e+04 d1=0.0 d12=-152.0 z=-0.16429878525641026
- **PERSISTENT_UP** `wind_gen` value=1.178e+04 d1=46.0 d12=783.0 z=1.2164758000243132
- **PERSISTENT_UP** `ps_gen` value=-244 d1=2.0 d12=5.0 z=-0.8143072029750479
- **PERSISTENT_DOWN** `nuclear_gen` value=3310 d1=-2.0 d12=-3.0 z=0.44965983333333326
- **ACCELERATION** `nuclear_gen` value=3310 d1=-2.0 d12=-3.0 z=0.44965983333333326
- **PERSISTENT_DOWN** `biomass_gen` value=3206 d1=-1.0 d12=-1.0 z=-0.25941913461538463
- **ACCELERATION** `biomass_gen` value=3206 d1=-1.0 d12=-1.0 z=-0.25941913461538463

## Nearest historical live analogues

- `2026-09-16T14:21:30.462993Z` distance=0.253 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.255 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:29:54.321922Z` distance=0.255 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:34:06.314775Z` distance=0.255 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:38:16.233128Z` distance=0.255 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

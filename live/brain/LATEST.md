# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T10:53:07.965768Z`  
Memory snapshots: **190**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **PERSISTENT_DOWN** `ts_demand_forecast` value=1.91e+04 d1=-1465.0 d12=-1465.0 z=-931.47034475
- **ACCELERATION** `ts_demand_forecast` value=1.91e+04 d1=-1465.0 d12=-1465.0 z=-931.47034475
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=-1465.0 d12=-1465.0 z=-931.47034475
- **CHANGE_POINT** `biomass_gen` value=1209 d1=-90.0 d12=-830.0 z=-35.34858781907895
- **PERSISTENT_DOWN** `biomass_gen` value=1209 d1=-90.0 d12=-830.0 z=-35.34858781907895
- **ROBUST_OUTLIER** `biomass_gen` value=1209 d1=-90.0 d12=-830.0 z=-35.34858781907895
- **PERSISTENT_DOWN** `residual_proxy` value=1005 d1=-1465.0 d12=-2323.0 z=-4.9646116292517
- **ACCELERATION** `residual_proxy` value=1005 d1=-1465.0 d12=-2323.0 z=-4.9646116292517
- **ROBUST_OUTLIER** `residual_proxy` value=1005 d1=-1465.0 d12=-2323.0 z=-4.9646116292517
- **CHANGE_POINT** `imbalance` value=-832 d1=0.0 d12=-467.0 z=-2.2420538912037036
- **CHANGE_POINT** `ind_demand` value=-1.227e+04 d1=0.0 d12=112.0 z=2.02346925
- **ROBUST_OUTLIER** `margin` value=3.449e+04 d1=0.0 d12=145.0 z=3.6232205801282054
- **CHANGE_POINT** `ind_generation` value=1.974e+04 d1=0.0 d12=-467.0 z=-1.5424806577868853
- **PERSISTENT_DOWN** `thermal_base` value=4970 d1=-92.0 d12=-197.0 z=-2.607433422992299
- **PERSISTENT_DOWN** `ccgt_gen` value=1642 d1=-90.0 d12=-204.0 z=-2.5947583825136613

## Nearest historical live analogues

- `2026-09-15T09:23:16.973095Z` distance=1.262 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:27:29.987536Z` distance=1.262 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:33:16.363033Z` distance=1.262 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:37:29.655273Z` distance=1.262 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:41:45.287890Z` distance=1.262 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

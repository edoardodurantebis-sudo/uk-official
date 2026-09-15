# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T11:01:34.132769Z`  
Memory snapshots: **192**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **PERSISTENT_DOWN** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=-1465.0 z=-931.47034475
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=-1465.0 z=-931.47034475
- **CHANGE_POINT** `biomass_gen` value=1268 d1=52.0 d12=-699.0 z=-31.766822128048783
- **REVERSAL** `biomass_gen` value=1268 d1=52.0 d12=-699.0 z=-31.766822128048783
- **ROBUST_OUTLIER** `biomass_gen` value=1268 d1=52.0 d12=-699.0 z=-31.766822128048783
- **CHANGE_POINT** `margin` value=3.521e+04 d1=0.0 d12=868.0 z=9.875221724358974
- **PERSISTENT_UP** `margin` value=3.521e+04 d1=0.0 d12=868.0 z=9.875221724358974
- **ACCELERATION** `margin` value=3.521e+04 d1=0.0 d12=868.0 z=9.875221724358974
- **ROBUST_OUTLIER** `margin` value=3.521e+04 d1=0.0 d12=868.0 z=9.875221724358974
- **PERSISTENT_DOWN** `residual_proxy` value=1005 d1=0.0 d12=-2323.0 z=-4.252679084119497
- **ROBUST_OUTLIER** `residual_proxy` value=1005 d1=0.0 d12=-2323.0 z=-4.252679084119497
- **CHANGE_POINT** `imbalance` value=-832 d1=0.0 d12=-467.0 z=-2.2420538912037036
- **CHANGE_POINT** `ind_demand` value=-1.227e+04 d1=0.0 d12=112.0 z=2.02346925
- **CHANGE_POINT** `ind_generation` value=1.974e+04 d1=0.0 d12=-467.0 z=-1.5424806577868853
- **PERSISTENT_DOWN** `ccgt_gen` value=1486 d1=-60.0 d12=-321.0 z=-1.9307200492270138

## Nearest historical live analogues

- `2026-09-15T09:23:16.973095Z` distance=2.829 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:27:29.987536Z` distance=2.829 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:33:16.363033Z` distance=2.829 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:37:29.655273Z` distance=2.829 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:41:45.287890Z` distance=2.829 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

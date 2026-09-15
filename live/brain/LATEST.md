# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T10:44:40.450787Z`  
Memory snapshots: **188**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **CHANGE_POINT** `biomass_gen` value=1344 d1=-70.0 d12=-695.0 z=-35.28246382394366
- **PERSISTENT_DOWN** `biomass_gen` value=1344 d1=-70.0 d12=-695.0 z=-35.28246382394366
- **ROBUST_OUTLIER** `biomass_gen` value=1344 d1=-70.0 d12=-695.0 z=-35.28246382394366
- **CHANGE_POINT** `ind_demand` value=-1.227e+04 d1=0.0 d12=112.0 z=2.593460588028169
- **CHANGE_POINT** `imbalance` value=-832 d1=0.0 d12=-467.0 z=-2.2420538912037036
- **ROBUST_OUTLIER** `margin` value=3.449e+04 d1=0.0 d12=145.0 z=3.6232205801282054
- **CHANGE_POINT** `ind_generation` value=1.974e+04 d1=0.0 d12=-467.0 z=-1.5424806577868853
- **PERSISTENT_DOWN** `ccgt_gen` value=1845 d1=-7.0 d12=-253.0 z=-2.3976724674657537
- **PERSISTENT_DOWN** `thermal_base` value=5170 d1=-7.0 d12=-254.0 z=-2.3867739562500003
- **REVERSAL** `wind_gen` value=1.153e+04 d1=14.0 d12=-24.0 z=-1.7168830000000002
- **ACCELERATION** `wind_gen` value=1.153e+04 d1=14.0 d12=-24.0 z=-1.7168830000000002
- **PERSISTENT_DOWN** `interconnector_net` value=1.108e+04 d1=-10.0 d12=-386.0 z=0.7798985163196196

## Nearest historical live analogues

- `2026-09-15T09:23:16.973095Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:27:29.987536Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:33:16.363033Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:37:29.655273Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:41:45.287890Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

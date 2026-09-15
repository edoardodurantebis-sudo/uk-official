# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T10:40:31.143417Z`  
Memory snapshots: **187**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high, wind rising.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **CHANGE_POINT** `biomass_gen` value=1414 d1=0.0 d12=-627.0 z=-34.43751952142858
- **PERSISTENT_DOWN** `biomass_gen` value=1414 d1=0.0 d12=-627.0 z=-34.43751952142858
- **ROBUST_OUTLIER** `biomass_gen` value=1414 d1=0.0 d12=-627.0 z=-34.43751952142858
- **CHANGE_POINT** `ind_demand` value=-1.227e+04 d1=0.0 d12=112.0 z=3.4688044285714286
- **CHANGE_POINT** `imbalance` value=-832 d1=0.0 d12=-467.0 z=-2.297083016509434
- **ROBUST_OUTLIER** `margin` value=3.449e+04 d1=0.0 d12=145.0 z=4.008669578014184
- **CHANGE_POINT** `ind_generation` value=1.974e+04 d1=0.0 d12=-467.0 z=-1.5309846706349206
- **ROBUST_OUTLIER** `ind_demand` value=-1.227e+04 d1=0.0 d12=112.0 z=3.4688044285714286
- **PERSISTENT_DOWN** `residual_proxy` value=2470 d1=0.0 d12=-858.0 z=-2.6546431444954126
- **PERSISTENT_DOWN** `ccgt_gen` value=1852 d1=0.0 d12=-427.0 z=-2.386892950913242
- **PERSISTENT_DOWN** `thermal_base` value=5177 d1=0.0 d12=-423.0 z=-2.3760434375
- **PERSISTENT_DOWN** `wind_gen` value=1.152e+04 d1=0.0 d12=-35.0 z=-2.2705527400510204
- **ACCELERATION** `wind_gen` value=1.152e+04 d1=0.0 d12=-35.0 z=-2.2705527400510204
- **PERSISTENT_UP** `wind_forecast` value=1.76e+04 d1=0.0 d12=858.0 z=1.8198497028301885

## Nearest historical live analogues

- `2026-09-15T09:23:16.973095Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:27:29.987536Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:33:16.363033Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:37:29.655273Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:41:45.287890Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

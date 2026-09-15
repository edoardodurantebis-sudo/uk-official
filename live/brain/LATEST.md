# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T10:36:19.373424Z`  
Memory snapshots: **186**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high, wind rising.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **CHANGE_POINT** `biomass_gen` value=1414 d1=-49.0 d12=-627.0 z=-35.46030670955882
- **PERSISTENT_DOWN** `biomass_gen` value=1414 d1=-49.0 d12=-627.0 z=-35.46030670955882
- **ROBUST_OUTLIER** `biomass_gen` value=1414 d1=-49.0 d12=-627.0 z=-35.46030670955882
- **ROBUST_OUTLIER** `margin` value=3.449e+04 d1=0.0 d12=-9.0 z=4.485892146825397
- **CHANGE_POINT** `imbalance` value=-832 d1=0.0 d12=-740.0 z=-2.354228646634615
- **CHANGE_POINT** `ind_generation` value=1.974e+04 d1=0.0 d12=-740.0 z=-1.4859059906015037
- **ROBUST_OUTLIER** `ind_demand` value=-1.227e+04 d1=0.0 d12=-16.0 z=3.4688044285714286
- **PERSISTENT_DOWN** `residual_proxy` value=2470 d1=0.0 d12=-858.0 z=-2.6546431444954126
- **ACCELERATION** `residual_proxy` value=2470 d1=0.0 d12=-858.0 z=-2.6546431444954126
- **PERSISTENT_DOWN** `ccgt_gen` value=1852 d1=-2.0 d12=-427.0 z=-2.3896208285714287
- **REVERSAL** `thermal_base` value=5177 d1=1.0 d12=-423.0 z=-2.3841712941847204
- **PERSISTENT_DOWN** `wind_gen` value=1.152e+04 d1=-42.0 d12=-35.0 z=-2.1492005808080807
- **ACCELERATION** `wind_gen` value=1.152e+04 d1=-42.0 d12=-35.0 z=-2.1492005808080807
- **PERSISTENT_UP** `wind_forecast` value=1.76e+04 d1=0.0 d12=858.0 z=1.8198497028301885

## Nearest historical live analogues

- `2026-09-15T09:23:16.973095Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:27:29.987536Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:33:16.363033Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:37:29.655273Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:41:45.287890Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

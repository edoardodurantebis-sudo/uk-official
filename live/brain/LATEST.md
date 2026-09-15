# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T10:19:29.495793Z`  
Memory snapshots: **182**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **CHANGE_POINT** `biomass_gen` value=1890 d1=-77.0 d12=-152.0 z=-36.16090965816326
- **PERSISTENT_DOWN** `biomass_gen` value=1890 d1=-77.0 d12=-152.0 z=-36.16090965816326
- **ACCELERATION** `biomass_gen` value=1890 d1=-77.0 d12=-152.0 z=-36.16090965816326
- **ROBUST_OUTLIER** `biomass_gen` value=1890 d1=-77.0 d12=-152.0 z=-36.16090965816326
- **CHANGE_POINT** `margin` value=3.449e+04 d1=145.0 d12=-9.0 z=4.485892146825397
- **CHANGE_POINT** `ccgt_gen` value=1837 d1=30.0 d12=-653.0 z=-2.5413810223214286
- **CHANGE_POINT** `thermal_base` value=5167 d1=27.0 d12=-640.0 z=-2.506043970779221
- **REVERSAL** `margin` value=3.449e+04 d1=145.0 d12=-9.0 z=4.485892146825397
- **ACCELERATION** `margin` value=3.449e+04 d1=145.0 d12=-9.0 z=4.485892146825397
- **ROBUST_OUTLIER** `margin` value=3.449e+04 d1=145.0 d12=-9.0 z=4.485892146825397
- **CHANGE_POINT** `imbalance` value=-832 d1=-467.0 d12=-740.0 z=-2.354228646634615
- **CHANGE_POINT** `ind_generation` value=1.974e+04 d1=-467.0 d12=-740.0 z=-1.4859059906015037
- **REVERSAL** `ind_demand` value=-1.227e+04 d1=112.0 d12=-16.0 z=3.4688044285714286
- **ACCELERATION** `ind_demand` value=-1.227e+04 d1=112.0 d12=-16.0 z=3.4688044285714286

## Nearest historical live analogues

- `2026-09-15T09:23:16.973095Z` distance=0.131 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:19:04.462321Z` distance=1.024 → {'next30m_imbalance_delta': 43.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T07:21:37.326101Z` distance=1.296 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:25:46.773269Z` distance=1.296 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:29:58.096076Z` distance=1.296 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

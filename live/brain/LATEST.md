# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T10:32:07.729613Z`  
Memory snapshots: **185**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high, wind rising.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **CHANGE_POINT** `biomass_gen` value=1463 d1=-93.0 d12=-580.0 z=-36.66484125390625
- **PERSISTENT_DOWN** `biomass_gen` value=1463 d1=-93.0 d12=-580.0 z=-36.66484125390625
- **ROBUST_OUTLIER** `biomass_gen` value=1463 d1=-93.0 d12=-580.0 z=-36.66484125390625
- **ROBUST_OUTLIER** `margin` value=3.449e+04 d1=0.0 d12=-9.0 z=4.485892146825397
- **CHANGE_POINT** `imbalance` value=-832 d1=0.0 d12=-740.0 z=-2.354228646634615
- **CHANGE_POINT** `ind_generation` value=1.974e+04 d1=0.0 d12=-740.0 z=-1.4859059906015037
- **ROBUST_OUTLIER** `ind_demand` value=-1.227e+04 d1=0.0 d12=-16.0 z=3.4688044285714286
- **PERSISTENT_UP** `ps_gen` value=-1204 d1=1.0 d12=2.0 z=-3.359682382492114
- **ROBUST_OUTLIER** `ps_gen` value=-1204 d1=1.0 d12=2.0 z=-3.359682382492114
- **PERSISTENT_DOWN** `residual_proxy` value=2470 d1=-858.0 d12=-858.0 z=-2.6546431444954126
- **ACCELERATION** `residual_proxy` value=2470 d1=-858.0 d12=-858.0 z=-2.6546431444954126
- **REVERSAL** `wind_gen` value=1.156e+04 d1=15.0 d12=-63.0 z=-2.1138899773550723
- **PERSISTENT_UP** `wind_forecast` value=1.76e+04 d1=858.0 d12=858.0 z=1.8198497028301885
- **ACCELERATION** `wind_forecast` value=1.76e+04 d1=858.0 d12=858.0 z=1.8198497028301885

## Nearest historical live analogues

- `2026-09-15T09:23:16.973095Z` distance=0.734 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:27:29.987536Z` distance=0.734 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:33:16.363033Z` distance=0.734 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:37:29.655273Z` distance=0.734 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:19:04.462321Z` distance=1.253 → {'next30m_imbalance_delta': 43.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

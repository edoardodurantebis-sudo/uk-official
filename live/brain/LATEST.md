# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T18:59:49.511883Z`  
Memory snapshots: **1921**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **ROBUST_OUTLIER** `thermal_base` value=1.207e+04 d1=0.0 d12=-261.0 z=5.127582429634641
- **ROBUST_OUTLIER** `ccgt_gen` value=8741 d1=0.0 d12=-259.0 z=5.104123916778976
- **CHANGE_POINT** `wind_gen` value=5556 d1=0.0 d12=-986.0 z=-1.4929122966690418
- **CHANGE_POINT** `biomass_gen` value=2344 d1=0.0 d12=86.0 z=1.2980006235465118
- **CHANGE_POINT** `interconnector_net` value=9874 d1=0.0 d12=-72.0 z=0.33737597965530647
- **PERSISTENT_DOWN** `margin` value=3.54e+04 d1=0.0 d12=-59.0 z=-2.2920713628318583
- **PERSISTENT_UP** `ind_generation` value=1.547e+04 d1=0.0 d12=24.0 z=1.493513017857143
- **ACCELERATION** `ind_generation` value=1.547e+04 d1=0.0 d12=24.0 z=1.493513017857143
- **PERSISTENT_DOWN** `wind_gen` value=5556 d1=0.0 d12=-986.0 z=-1.4929122966690418
- **PERSISTENT_UP** `biomass_gen` value=2344 d1=0.0 d12=86.0 z=1.2980006235465118
- **PERSISTENT_UP** `imbalance` value=-5141 d1=0.0 d12=24.0 z=1.1522533229166667
- **ACCELERATION** `imbalance` value=-5141 d1=0.0 d12=24.0 z=1.1522533229166667
- **PERSISTENT_DOWN** `nuclear_gen` value=3333 d1=0.0 d12=-2.0 z=-0.67448975
- **ACCELERATION** `nuclear_gen` value=3333 d1=0.0 d12=-2.0 z=-0.67448975
- **PERSISTENT_DOWN** `ps_gen` value=223 d1=0.0 d12=-307.0 z=0.624043148199446

## Nearest historical live analogues

- `2026-09-20T17:52:35.892709Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T17:56:46.494195Z` distance=0.026 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:00:58.540331Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:05:11.055248Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:49:59.741529Z` distance=0.027 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

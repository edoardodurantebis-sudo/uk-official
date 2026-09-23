# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T00:59:50.808074Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.244e+04 d1=0.0 d12=50.0 z=28.3285695
- **PERSISTENT_UP** `ind_demand` value=-1.244e+04 d1=0.0 d12=50.0 z=28.3285695
- **ROBUST_OUTLIER** `ind_demand` value=-1.244e+04 d1=0.0 d12=50.0 z=28.3285695
- **CHANGE_POINT** `interconnector_net` value=2279 d1=0.0 d12=-1102.0 z=-2.670204033148269
- **CHANGE_POINT** `imbalance` value=-7998 d1=0.0 d12=0.0 z=1.5076829705882353
- **CHANGE_POINT** `ind_generation` value=1.318e+04 d1=0.0 d12=0.0 z=1.5076829705882353
- **CHANGE_POINT** `thermal_base` value=1.342e+04 d1=0.0 d12=-335.0 z=-1.4292539298905609
- **CHANGE_POINT** `ccgt_gen` value=9696 d1=0.0 d12=-324.0 z=-1.4224096255798089
- **PERSISTENT_UP** `wind_gen` value=4392 d1=0.0 d12=528.0 z=2.1985824774774776
- **PERSISTENT_DOWN** `nuclear_gen` value=3726 d1=0.0 d12=-11.0 z=-1.5176019375
- **PERSISTENT_DOWN** `thermal_base` value=1.342e+04 d1=0.0 d12=-335.0 z=-1.4292539298905609
- **PERSISTENT_DOWN** `ccgt_gen` value=9696 d1=0.0 d12=-324.0 z=-1.4224096255798089
- **PERSISTENT_UP** `margin` value=3.724e+04 d1=0.0 d12=16.0 z=0.8874865131578948

## Nearest historical live analogues

- `2026-09-23T00:04:41.945935Z` distance=0.058 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:00:29.286244Z` distance=0.287 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:55:13.117327Z` distance=0.467 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:59:27.826421Z` distance=0.467 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:03:40.476515Z` distance=0.467 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T10:36:54.406869Z`  
Memory snapshots: **1802**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `margin` value=3.978e+04 d1=0.0 d12=889.0 z=27.6908701
- **ROBUST_OUTLIER** `margin` value=3.978e+04 d1=0.0 d12=889.0 z=27.6908701
- **CHANGE_POINT** `ind_generation` value=1.603e+04 d1=0.0 d12=47.0 z=24.0118351
- **ROBUST_OUTLIER** `ind_generation` value=1.603e+04 d1=0.0 d12=47.0 z=24.0118351
- **CHANGE_POINT** `ind_demand` value=-1.247e+04 d1=0.0 d12=-90.0 z=-13.40548378125
- **ROBUST_OUTLIER** `ind_demand` value=-1.247e+04 d1=0.0 d12=-90.0 z=-13.40548378125
- **CHANGE_POINT** `imbalance` value=-4140 d1=0.0 d12=47.0 z=7.1927368481781375
- **ROBUST_OUTLIER** `imbalance` value=-4140 d1=0.0 d12=47.0 z=7.1927368481781375
- **CHANGE_POINT** `wind_gen` value=1.396e+04 d1=-28.0 d12=-901.0 z=-2.840442397036474
- **PERSISTENT_DOWN** `wind_gen` value=1.396e+04 d1=-28.0 d12=-901.0 z=-2.840442397036474
- **CHANGE_POINT** `ps_gen` value=-926 d1=-16.0 d12=3.0 z=-0.6952889933920705
- **CHANGE_POINT** `biomass_gen` value=585 d1=-15.0 d12=-1.0 z=-0.6952078651877134
- **REVERSAL** `thermal_base` value=5845 d1=-1.0 d12=234.0 z=-2.2534322697869102
- **PERSISTENT_UP** `ccgt_gen` value=2512 d1=4.0 d12=238.0 z=-2.2317078023343373
- **PERSISTENT_UP** `residual_proxy` value=1.731e+04 d1=0.0 d12=93.0 z=2.1282036832298137

## Nearest historical live analogues

- `2026-09-20T09:20:07.153673Z` distance=0.336 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:24:18.809197Z` distance=0.336 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:28:32.169507Z` distance=0.336 → {'next30m_imbalance_delta': 33.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:32:44.320157Z` distance=0.336 → {'next30m_imbalance_delta': 33.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:36:54.599847Z` distance=0.336 → {'next30m_imbalance_delta': 33.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

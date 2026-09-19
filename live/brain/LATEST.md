# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T18:42:21.603067Z`  
Memory snapshots: **1576**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.62e+04 d1=0.0 d12=-614.0 z=-38.918058574999996
- **ROBUST_OUTLIER** `ind_generation` value=1.62e+04 d1=0.0 d12=-614.0 z=-38.918058574999996
- **CHANGE_POINT** `imbalance` value=-3750 d1=0.0 d12=-614.0 z=-10.223844631578947
- **ROBUST_OUTLIER** `imbalance` value=-3750 d1=0.0 d12=-614.0 z=-10.223844631578947
- **CHANGE_POINT** `margin` value=3.62e+04 d1=0.0 d12=-100.0 z=-2.712010869791667
- **CHANGE_POINT** `biomass_gen` value=970 d1=50.0 d12=288.0 z=2.3151404932432436
- **PERSISTENT_UP** `ccgt_gen` value=7040 d1=33.0 d12=126.0 z=4.145584167276051
- **ROBUST_OUTLIER** `ccgt_gen` value=7040 d1=33.0 d12=126.0 z=4.145584167276051
- **PERSISTENT_UP** `thermal_base` value=1.037e+04 d1=32.0 d12=126.0 z=4.060234892921147
- **ROBUST_OUTLIER** `thermal_base` value=1.037e+04 d1=32.0 d12=126.0 z=4.060234892921147
- **PERSISTENT_UP** `biomass_gen` value=970 d1=50.0 d12=288.0 z=2.3151404932432436
- **PERSISTENT_UP** `interconnector_net` value=-1195 d1=1.0 d12=1786.0 z=1.3399163421145686
- **PERSISTENT_DOWN** `wind_gen` value=1.41e+04 d1=-71.0 d12=-150.0 z=-1.0543747816091955
- **ACCELERATION** `wind_gen` value=1.41e+04 d1=-71.0 d12=-150.0 z=-1.0543747816091955
- **PERSISTENT_DOWN** `nuclear_gen` value=3329 d1=-1.0 d12=0.0 z=-0.67448975

## Nearest historical live analogues

- `2026-09-19T17:22:38.318939Z` distance=0.017 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:26:48.291042Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:31:01.384129Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:35:13.165368Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:39:26.231429Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T23:59:33.595851Z`  
Memory snapshots: **681**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=-657.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=657.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6490 d1=-39.0 d12=-950.0 z=-4.715315049848942
- **PERSISTENT_DOWN** `interconnector_net` value=-6490 d1=-39.0 d12=-950.0 z=-4.715315049848942
- **ROBUST_OUTLIER** `interconnector_net` value=-6490 d1=-39.0 d12=-950.0 z=-4.715315049848942
- **PERSISTENT_DOWN** `ccgt_gen` value=5013 d1=-238.0 d12=-858.0 z=-3.180727348458904
- **ROBUST_OUTLIER** `ccgt_gen` value=5013 d1=-238.0 d12=-858.0 z=-3.180727348458904
- **PERSISTENT_DOWN** `thermal_base` value=8330 d1=-233.0 d12=-851.0 z=-3.1642634171412296
- **ROBUST_OUTLIER** `thermal_base` value=8330 d1=-233.0 d12=-851.0 z=-3.1642634171412296
- **CHANGE_POINT** `imbalance` value=6451 d1=0.0 d12=-168.0 z=-0.607040775
- **CHANGE_POINT** `ind_generation` value=2.557e+04 d1=0.0 d12=-168.0 z=-0.16429878525641026
- **PERSISTENT_UP** `margin` value=3.451e+04 d1=0.0 d12=250.0 z=1.6287678407407407
- **PERSISTENT_UP** `nuclear_gen` value=3317 d1=5.0 d12=7.0 z=1.4988661111111112
- **ACCELERATION** `nuclear_gen` value=3317 d1=5.0 d12=7.0 z=1.4988661111111112
- **PERSISTENT_UP** `wind_gen` value=1.166e+04 d1=47.0 d12=1014.0 z=1.3035064229590585

## Nearest historical live analogues

- `2026-09-16T14:21:30.462993Z` distance=0.273 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.274 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:29:54.321922Z` distance=0.274 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:34:06.314775Z` distance=0.274 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:38:16.233128Z` distance=0.274 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

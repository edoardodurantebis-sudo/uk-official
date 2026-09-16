# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T23:51:11.579176Z`  
Memory snapshots: **679**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=-657.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=657.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6451 d1=-6.0 d12=-10843.0 z=-4.861931061122103
- **CHANGE_POINT** `ccgt_gen` value=5251 d1=-105.0 d12=-3158.0 z=-2.99747556706621
- **CHANGE_POINT** `thermal_base` value=8563 d1=-107.0 d12=-3152.0 z=-2.98527012357631
- **PERSISTENT_DOWN** `interconnector_net` value=-6451 d1=-6.0 d12=-10843.0 z=-4.861931061122103
- **ROBUST_OUTLIER** `interconnector_net` value=-6451 d1=-6.0 d12=-10843.0 z=-4.861931061122103
- **CHANGE_POINT** `ind_generation` value=2.572e+04 d1=0.0 d12=-42.0 z=1.1705660822580646
- **PERSISTENT_DOWN** `ccgt_gen` value=5251 d1=-105.0 d12=-3158.0 z=-2.99747556706621
- **PERSISTENT_DOWN** `thermal_base` value=8563 d1=-107.0 d12=-3152.0 z=-2.98527012357631
- **CHANGE_POINT** `imbalance` value=6603 d1=0.0 d12=-42.0 z=0.316973325136612
- **PERSISTENT_UP** `margin` value=3.451e+04 d1=23.0 d12=155.0 z=1.6287678407407407
- **PERSISTENT_UP** `wind_gen` value=1.161e+04 d1=78.0 d12=1483.0 z=1.4547160507066215
- **PERSISTENT_DOWN** `ps_gen` value=-250 d1=0.0 d12=-476.0 z=-0.9083796208907741
- **REVERSAL** `nuclear_gen` value=3312 d1=-2.0 d12=6.0 z=0.7494330555555556

## Nearest historical live analogues

- `2026-09-16T14:21:30.462993Z` distance=0.272 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.274 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:29:54.321922Z` distance=0.274 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:34:06.314775Z` distance=0.274 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:38:16.233128Z` distance=0.274 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T23:55:23.288978Z`  
Memory snapshots: **680**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=-657.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=657.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6451 d1=0.0 d12=-1165.0 z=-4.843665259371477
- **CHANGE_POINT** `ccgt_gen` value=5251 d1=0.0 d12=-609.0 z=-2.99747556706621
- **CHANGE_POINT** `thermal_base` value=8563 d1=0.0 d12=-614.0 z=-2.98527012357631
- **PERSISTENT_DOWN** `interconnector_net` value=-6451 d1=0.0 d12=-1165.0 z=-4.843665259371477
- **ROBUST_OUTLIER** `interconnector_net` value=-6451 d1=0.0 d12=-1165.0 z=-4.843665259371477
- **PERSISTENT_DOWN** `ccgt_gen` value=5251 d1=0.0 d12=-609.0 z=-2.99747556706621
- **PERSISTENT_DOWN** `thermal_base` value=8563 d1=0.0 d12=-614.0 z=-2.98527012357631
- **CHANGE_POINT** `imbalance` value=6451 d1=-152.0 d12=-168.0 z=-0.8168820305555556
- **CHANGE_POINT** `ind_generation` value=2.557e+04 d1=-152.0 d12=-168.0 z=-0.16221905379746834
- **PERSISTENT_UP** `margin` value=3.451e+04 d1=0.0 d12=250.0 z=1.6287678407407407
- **PERSISTENT_UP** `wind_gen` value=1.161e+04 d1=0.0 d12=1094.0 z=1.382137045020377
- **PERSISTENT_DOWN** `imbalance` value=6451 d1=-152.0 d12=-168.0 z=-0.8168820305555556
- **ACCELERATION** `imbalance` value=6451 d1=-152.0 d12=-168.0 z=-0.8168820305555556

## Nearest historical live analogues

- `2026-09-16T14:21:30.462993Z` distance=0.272 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.274 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:29:54.321922Z` distance=0.274 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:34:06.314775Z` distance=0.274 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:38:16.233128Z` distance=0.274 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

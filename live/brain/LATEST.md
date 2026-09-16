# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T06:03:52.494424Z`  
Memory snapshots: **463**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=8441 d1=125.0 d12=2137.0 z=10.680104415273556
- **CHANGE_POINT** `thermal_base` value=1.177e+04 d1=120.0 d12=2132.0 z=10.601307928625378
- **ROBUST_OUTLIER** `imbalance` value=7214 d1=0.0 d12=11.0 z=12.337974042307692
- **ROBUST_OUTLIER** `ind_generation` value=2.634e+04 d1=0.0 d12=11.0 z=12.337974042307692
- **PERSISTENT_UP** `ccgt_gen` value=8441 d1=125.0 d12=2137.0 z=10.680104415273556
- **ROBUST_OUTLIER** `ccgt_gen` value=8441 d1=125.0 d12=2137.0 z=10.680104415273556
- **PERSISTENT_UP** `thermal_base` value=1.177e+04 d1=120.0 d12=2132.0 z=10.601307928625378
- **ROBUST_OUTLIER** `thermal_base` value=1.177e+04 d1=120.0 d12=2132.0 z=10.601307928625378
- **CHANGE_POINT** `wind_gen` value=7899 d1=-30.0 d12=-1471.0 z=-3.2907605469444445
- **CHANGE_POINT** `interconnector_net` value=-1325 d1=550.0 d12=-87.0 z=-3.2022315756595323
- **PERSISTENT_DOWN** `wind_gen` value=7899 d1=-30.0 d12=-1471.0 z=-3.2907605469444445
- **ROBUST_OUTLIER** `wind_gen` value=7899 d1=-30.0 d12=-1471.0 z=-3.2907605469444445
- **REVERSAL** `interconnector_net` value=-1325 d1=550.0 d12=-87.0 z=-3.2022315756595323
- **ACCELERATION** `interconnector_net` value=-1325 d1=550.0 d12=-87.0 z=-3.2022315756595323
- **ROBUST_OUTLIER** `interconnector_net` value=-1325 d1=550.0 d12=-87.0 z=-3.2022315756595323

## Nearest historical live analogues

- `2026-09-16T03:32:58.473492Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:37:08.879637Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:41:19.622154Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:45:29.518871Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:49:41.884820Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

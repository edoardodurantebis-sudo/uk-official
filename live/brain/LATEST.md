# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T21:55:41.733384Z`  
Memory snapshots: **347**  
Current physical regime: **BALANCED**

## Active patterns

- **PERSISTENT_DOWN** `thermal_base` value=7638 d1=-343.0 d12=-3109.0 z=-9.06526404401806
- **ROBUST_OUTLIER** `thermal_base` value=7638 d1=-343.0 d12=-3109.0 z=-9.06526404401806
- **PERSISTENT_DOWN** `ccgt_gen` value=4315 d1=-336.0 d12=-3109.0 z=-9.003530777186098
- **ROBUST_OUTLIER** `ccgt_gen` value=4315 d1=-336.0 d12=-3109.0 z=-9.003530777186098
- **PERSISTENT_DOWN** `wind_gen` value=1.2e+04 d1=-77.0 d12=-323.0 z=4.32116636550308
- **ROBUST_OUTLIER** `wind_gen` value=1.2e+04 d1=-77.0 d12=-323.0 z=4.32116636550308
- **CHANGE_POINT** `ps_gen` value=-257 d1=2.0 d12=4.0 z=-0.6780396960526316
- **CHANGE_POINT** `interconnector_net` value=1332 d1=15.0 d12=1025.0 z=0.6622510246975807
- **ACCELERATION** `ps_gen` value=-257 d1=2.0 d12=4.0 z=-0.6780396960526316
- **PERSISTENT_UP** `interconnector_net` value=1332 d1=15.0 d12=1025.0 z=0.6622510246975807
- **PERSISTENT_DOWN** `nuclear_gen` value=3323 d1=-7.0 d12=0.0 z=0.337244875
- **ACCELERATION** `nuclear_gen` value=3323 d1=-7.0 d12=0.0 z=0.337244875
- **PERSISTENT_UP** `imbalance` value=5771 d1=0.0 d12=49.0 z=-0.020439083333333333
- **PERSISTENT_UP** `ind_generation` value=2.489e+04 d1=0.0 d12=49.0 z=-0.020439083333333333
- **PERSISTENT_DOWN** `biomass_gen` value=3255 d1=-7.0 d12=-6.0 z=-0.019837933823529413

## Nearest historical live analogues

- `2026-09-15T20:52:49.933053Z` distance=0.003 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:57:02.699458Z` distance=0.003 → {'next30m_imbalance_delta': 47.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T21:01:14.281286Z` distance=0.003 → {'next30m_imbalance_delta': 47.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:22:50.211969Z` distance=0.014 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:27:39.367678Z` distance=0.014 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

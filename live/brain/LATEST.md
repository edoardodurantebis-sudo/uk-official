# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T11:48:17.668676Z`  
Memory snapshots: **1819**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=0.0 z=41.6497420625
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=0.0 z=41.6497420625
- **CHANGE_POINT** `ind_generation` value=1.537e+04 d1=0.0 d12=14.0 z=2.455693293877551
- **CHANGE_POINT** `wind_gen` value=1.28e+04 d1=-26.0 d12=-955.0 z=-2.446528461102107
- **CHANGE_POINT** `margin` value=3.578e+04 d1=0.0 d12=-13.0 z=-2.3057213457760315
- **CHANGE_POINT** `residual_proxy` value=1.824e+04 d1=0.0 d12=0.0 z=1.6756600777108435
- **CHANGE_POINT** `imbalance` value=-5732 d1=0.0 d12=14.0 z=0.6897694530744336
- **PERSISTENT_DOWN** `wind_gen` value=1.28e+04 d1=-26.0 d12=-955.0 z=-2.446528461102107
- **PERSISTENT_DOWN** `nuclear_gen` value=3330 d1=-3.0 d12=-1.0 z=-1.48387745
- **ACCELERATION** `nuclear_gen` value=3330 d1=-3.0 d12=-1.0 z=-1.48387745
- **REVERSAL** `ps_gen` value=-667 d1=-4.0 d12=223.0 z=0.934384883027523
- **REVERSAL** `thermal_base` value=5728 d1=-4.0 d12=4.0 z=-0.7133929041198502
- **ACCELERATION** `thermal_base` value=5728 d1=-4.0 d12=4.0 z=-0.7133929041198502
- **REVERSAL** `ccgt_gen` value=2398 d1=-1.0 d12=5.0 z=-0.7037277212257099
- **ACCELERATION** `ccgt_gen` value=2398 d1=-1.0 d12=5.0 z=-0.7037277212257099

## Nearest historical live analogues

- `2026-09-20T10:53:43.403442Z` distance=0.711 → {'next30m_imbalance_delta': -1606.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:50:36.902238Z` distance=0.751 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:54:47.005275Z` distance=0.751 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:58:57.948602Z` distance=0.751 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:03:10.294370Z` distance=0.751 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

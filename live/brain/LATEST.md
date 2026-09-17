# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T20:17:50.035201Z`  
Memory snapshots: **970**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.116e+04 d1=0.0 d12=0.0 z=26.97959
- **CHANGE_POINT** `ind_generation` value=2.652e+04 d1=0.0 d12=24.0 z=-20.1975158996063
- **ROBUST_OUTLIER** `ind_generation` value=2.652e+04 d1=0.0 d12=24.0 z=-20.1975158996063
- **CHANGE_POINT** `imbalance` value=9708 d1=0.0 d12=24.0 z=-3.90423823325723
- **CHANGE_POINT** `interconnector_net` value=-1707 d1=-49.0 d12=-1235.0 z=-3.485865177895323
- **ROBUST_OUTLIER** `imbalance` value=9708 d1=0.0 d12=24.0 z=-3.90423823325723
- **PERSISTENT_DOWN** `interconnector_net` value=-1707 d1=-49.0 d12=-1235.0 z=-3.485865177895323
- **ROBUST_OUTLIER** `interconnector_net` value=-1707 d1=-49.0 d12=-1235.0 z=-3.485865177895323
- **CHANGE_POINT** `ps_gen` value=503 d1=1.0 d12=77.0 z=0.6755936612111293
- **CHANGE_POINT** `ccgt_gen` value=5109 d1=-194.0 d12=-1452.0 z=0.04419560129245567
- **CHANGE_POINT** `thermal_base` value=8429 d1=-191.0 d12=-1459.0 z=0.04250985819327731
- **REVERSAL** `wind_gen` value=1.586e+04 d1=-129.0 d12=397.0 z=1.2860220048377917
- **PERSISTENT_UP** `biomass_gen` value=3122 d1=18.0 d12=148.0 z=0.9471181528871392
- **ACCELERATION** `biomass_gen` value=3122 d1=18.0 d12=148.0 z=0.9471181528871392
- **PERSISTENT_UP** `ps_gen` value=503 d1=1.0 d12=77.0 z=0.6755936612111293

## Nearest historical live analogues

- `2026-09-17T19:23:15.447841Z` distance=0.128 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T18:57:56.745109Z` distance=0.131 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:10:36.600451Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

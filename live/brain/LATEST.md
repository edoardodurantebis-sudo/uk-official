# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T22:20:48.482562Z`  
Memory snapshots: **353**  
Current physical regime: **BALANCED**

## Active patterns

- **PERSISTENT_DOWN** `thermal_base` value=6532 d1=-194.0 d12=-2405.0 z=-10.749204593679458
- **ROBUST_OUTLIER** `thermal_base` value=6532 d1=-194.0 d12=-2405.0 z=-10.749204593679458
- **PERSISTENT_DOWN** `ccgt_gen` value=3207 d1=-192.0 d12=-2408.0 z=-10.679168990190583
- **ROBUST_OUTLIER** `ccgt_gen` value=3207 d1=-192.0 d12=-2408.0 z=-10.679168990190583
- **CHANGE_POINT** `interconnector_net` value=2768 d1=-25.0 d12=1510.0 z=1.6818626978789446
- **REVERSAL** `wind_gen` value=1.215e+04 d1=30.0 d12=-237.0 z=3.119991428319209
- **ROBUST_OUTLIER** `wind_gen` value=1.215e+04 d1=30.0 d12=-237.0 z=3.119991428319209
- **CHANGE_POINT** `margin` value=3.575e+04 d1=34.0 d12=34.0 z=1.0502768964285716
- **REVERSAL** `interconnector_net` value=2768 d1=-25.0 d12=1510.0 z=1.6818626978789446
- **PERSISTENT_UP** `margin` value=3.575e+04 d1=34.0 d12=34.0 z=1.0502768964285716
- **ACCELERATION** `margin` value=3.575e+04 d1=34.0 d12=34.0 z=1.0502768964285716
- **REVERSAL** `nuclear_gen` value=3325 d1=-2.0 d12=3.0 z=1.0117346249999999
- **ACCELERATION** `nuclear_gen` value=3325 d1=-2.0 d12=3.0 z=1.0117346249999999
- **PERSISTENT_DOWN** `ps_gen` value=-261 d1=-1.0 d12=-3.0 z=-0.6833413215223098
- **REVERSAL** `biomass_gen` value=3253 d1=-2.0 d12=2.0 z=-0.07782574038461537

## Nearest historical live analogues

- `2026-09-15T21:22:07.813465Z` distance=0.025 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T21:26:18.783967Z` distance=0.025 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:52:49.933053Z` distance=0.029 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:57:02.699458Z` distance=0.029 → {'next30m_imbalance_delta': 47.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T21:01:14.281286Z` distance=0.029 → {'next30m_imbalance_delta': 47.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

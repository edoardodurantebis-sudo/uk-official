# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T18:45:25.763787Z`  
Memory snapshots: **948**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.65e+04 d1=0.0 d12=10.0 z=-111.4594311875
- **ROBUST_OUTLIER** `ind_generation` value=2.65e+04 d1=0.0 d12=10.0 z=-111.4594311875
- **CHANGE_POINT** `imbalance` value=9682 d1=0.0 d12=10.0 z=-5.175411735576923
- **ROBUST_OUTLIER** `ind_demand` value=-1.125e+04 d1=0.0 d12=29.0 z=5.8455778333333335
- **ROBUST_OUTLIER** `imbalance` value=9682 d1=0.0 d12=10.0 z=-5.175411735576923
- **CHANGE_POINT** `thermal_base` value=1.042e+04 d1=0.0 d12=662.0 z=2.3806903022648083
- **CHANGE_POINT** `ccgt_gen` value=7092 d1=0.0 d12=657.0 z=2.3689396097560977
- **CHANGE_POINT** `interconnector_net` value=-443 d1=0.0 d12=-1153.0 z=-1.6438256536908882
- **PERSISTENT_UP** `nuclear_gen` value=3324 d1=0.0 d12=5.0 z=2.5293365625
- **ACCELERATION** `nuclear_gen` value=3324 d1=0.0 d12=5.0 z=2.5293365625
- **PERSISTENT_UP** `thermal_base` value=1.042e+04 d1=0.0 d12=662.0 z=2.3806903022648083
- **PERSISTENT_UP** `ccgt_gen` value=7092 d1=0.0 d12=657.0 z=2.3689396097560977
- **PERSISTENT_DOWN** `interconnector_net` value=-443 d1=0.0 d12=-1153.0 z=-1.6438256536908882
- **PERSISTENT_UP** `wind_gen` value=1.504e+04 d1=0.0 d12=356.0 z=1.114811036637931
- **PERSISTENT_UP** `biomass_gen` value=2927 d1=0.0 d12=16.0 z=0.4471430805348258

## Nearest historical live analogues

- `2026-09-17T16:51:11.529831Z` distance=0.040 → {'next30m_imbalance_delta': -25.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T17:21:14.586656Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:55:22.028914Z` distance=0.043 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:59:33.030689Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T17:04:23.689660Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

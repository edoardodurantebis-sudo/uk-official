# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T11:24:04.514292Z`  
Memory snapshots: **1185**  
Current physical regime: **BALANCED**

## Active patterns

- **ROBUST_OUTLIER** `biomass_gen` value=1085 d1=-1.0 d12=-80.0 z=-45.44374690625
- **CHANGE_POINT** `ind_generation` value=2.565e+04 d1=0.0 d12=-1107.0 z=-6.262601065860215
- **ROBUST_OUTLIER** `ind_generation` value=2.565e+04 d1=0.0 d12=-1107.0 z=-6.262601065860215
- **CHANGE_POINT** `ps_gen` value=-547 d1=167.0 d12=169.0 z=-2.0001305043252593
- **CHANGE_POINT** `imbalance` value=8982 d1=0.0 d12=1904.0 z=-1.5240755594149908
- **CHANGE_POINT** `thermal_base` value=5825 d1=-22.0 d12=-521.0 z=-1.473902942569993
- **CHANGE_POINT** `ccgt_gen` value=2490 d1=-22.0 d12=-528.0 z=-1.4702523705229225
- **CHANGE_POINT** `ind_demand` value=-1.074e+04 d1=0.0 d12=3052.0 z=1.1809529015017668
- **CHANGE_POINT** `margin` value=3.812e+04 d1=-2.0 d12=1771.0 z=1.0089242510416667
- **ACCELERATION** `ps_gen` value=-547 d1=167.0 d12=169.0 z=-2.0001305043252593
- **PERSISTENT_DOWN** `thermal_base` value=5825 d1=-22.0 d12=-521.0 z=-1.473902942569993
- **PERSISTENT_DOWN** `ccgt_gen` value=2490 d1=-22.0 d12=-528.0 z=-1.4702523705229225
- **REVERSAL** `margin` value=3.812e+04 d1=-2.0 d12=1771.0 z=1.0089242510416667
- **PERSISTENT_DOWN** `interconnector_net` value=5509 d1=0.0 d12=-56.0 z=0.7610432883976064
- **PERSISTENT_UP** `wind_gen` value=1.26e+04 d1=82.0 d12=374.0 z=0.1978943031784841

## Nearest historical live analogues

- `2026-09-18T05:50:47.091039Z` distance=0.518 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T05:54:59.248868Z` distance=0.518 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T05:59:09.222653Z` distance=0.518 → {'next30m_imbalance_delta': -67.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T06:03:20.906831Z` distance=0.518 → {'next30m_imbalance_delta': -67.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T06:07:33.046654Z` distance=0.518 → {'next30m_imbalance_delta': -67.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

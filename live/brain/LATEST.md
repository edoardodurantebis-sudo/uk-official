# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T15:24:09.005036Z`  
Memory snapshots: **1529**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=600 d1=14.0 d12=81.0 z=82.96223925
- **PERSISTENT_UP** `biomass_gen` value=600 d1=14.0 d12=81.0 z=82.96223925
- **ROBUST_OUTLIER** `biomass_gen` value=600 d1=14.0 d12=81.0 z=82.96223925
- **CHANGE_POINT** `ccgt_gen` value=3612 d1=-121.0 d12=389.0 z=2.370489338768116
- **CHANGE_POINT** `thermal_base` value=6943 d1=-130.0 d12=389.0 z=2.3571136459074733
- **CHANGE_POINT** `imbalance` value=-3174 d1=0.0 d12=56.0 z=0.67448975
- **REVERSAL** `ccgt_gen` value=3612 d1=-121.0 d12=389.0 z=2.370489338768116
- **REVERSAL** `thermal_base` value=6943 d1=-130.0 d12=389.0 z=2.3571136459074733
- **REVERSAL** `interconnector_net` value=-3300 d1=-40.0 d12=205.0 z=-1.6709413746223565
- **REVERSAL** `wind_gen` value=1.41e+04 d1=-35.0 d12=290.0 z=-1.559448552879581
- **PERSISTENT_UP** `margin` value=3.704e+04 d1=114.0 d12=114.0 z=1.1321792232142858
- **ACCELERATION** `margin` value=3.704e+04 d1=114.0 d12=114.0 z=1.1321792232142858
- **REVERSAL** `ps_gen` value=-516 d1=8.0 d12=-43.0 z=0.5123527908653845
- **PERSISTENT_DOWN** `nuclear_gen` value=3331 d1=-9.0 d12=0.0 z=0.0
- **ACCELERATION** `nuclear_gen` value=3331 d1=-9.0 d12=0.0 z=0.0

## Nearest historical live analogues

- `2026-09-19T14:21:11.929039Z` distance=0.037 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T14:25:23.497247Z` distance=0.037 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -57.0}
- `2026-09-19T14:29:36.625611Z` distance=0.037 → {'next30m_imbalance_delta': 56.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -57.0}
- `2026-09-19T13:51:46.286416Z` distance=0.057 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T13:55:56.183209Z` distance=0.057 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 64.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

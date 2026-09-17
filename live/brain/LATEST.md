# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T16:30:04.522443Z`  
Memory snapshots: **916**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=7811 d1=0.0 d12=1407.0 z=15.862772575
- **CHANGE_POINT** `ccgt_gen` value=4498 d1=0.0 d12=1404.0 z=15.453309605555555
- **PERSISTENT_UP** `thermal_base` value=7811 d1=0.0 d12=1407.0 z=15.862772575
- **ROBUST_OUTLIER** `thermal_base` value=7811 d1=0.0 d12=1407.0 z=15.862772575
- **PERSISTENT_UP** `ccgt_gen` value=4498 d1=0.0 d12=1404.0 z=15.453309605555555
- **ROBUST_OUTLIER** `ccgt_gen` value=4498 d1=0.0 d12=1404.0 z=15.453309605555555
- **CHANGE_POINT** `biomass_gen` value=3068 d1=0.0 d12=366.0 z=13.027644615740742
- **PERSISTENT_UP** `biomass_gen` value=3068 d1=0.0 d12=366.0 z=13.027644615740742
- **ROBUST_OUTLIER** `biomass_gen` value=3068 d1=0.0 d12=366.0 z=13.027644615740742
- **ROBUST_OUTLIER** `ps_gen` value=-255 d1=0.0 d12=69.0 z=12.634807992957747
- **CHANGE_POINT** `imbalance` value=1.162e+04 d1=0.0 d12=-34.0 z=-8.171702740384616
- **PERSISTENT_DOWN** `imbalance` value=1.162e+04 d1=0.0 d12=-34.0 z=-8.171702740384616
- **ACCELERATION** `imbalance` value=1.162e+04 d1=0.0 d12=-34.0 z=-8.171702740384616
- **ROBUST_OUTLIER** `imbalance` value=1.162e+04 d1=0.0 d12=-34.0 z=-8.171702740384616
- **ROBUST_OUTLIER** `residual_proxy` value=-2671 d1=0.0 d12=0.0 z=3.8890791968085106

## Nearest historical live analogues

- `2026-09-17T10:57:20.878127Z` distance=0.137 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:01:31.274983Z` distance=0.137 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:05:43.396655Z` distance=0.137 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:09:56.284661Z` distance=0.137 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:14:08.992825Z` distance=0.137 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

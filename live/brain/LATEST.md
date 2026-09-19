# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T10:42:29.837496Z`  
Memory snapshots: **1462**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low, wind falling.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.606e+04 d1=0.0 d12=-659.0 z=-20.534465722222222
- **ROBUST_OUTLIER** `ind_generation` value=2.606e+04 d1=0.0 d12=-659.0 z=-20.534465722222222
- **CHANGE_POINT** `imbalance` value=7134 d1=0.0 d12=-659.0 z=-4.879641895061728
- **ROBUST_OUTLIER** `imbalance` value=7134 d1=0.0 d12=-659.0 z=-4.879641895061728
- **CHANGE_POINT** `ind_demand` value=-1.322e+04 d1=0.0 d12=-8.0 z=-2.579337080777096
- **CHANGE_POINT** `margin` value=3.651e+04 d1=0.0 d12=59.0 z=-1.808514396067416
- **CHANGE_POINT** `thermal_base` value=6248 d1=-28.0 d12=-160.0 z=-1.4680071029411765
- **CHANGE_POINT** `biomass_gen` value=476 d1=-1.0 d12=0.0 z=-1.4636427575
- **CHANGE_POINT** `ccgt_gen` value=2917 d1=-24.0 d12=-159.0 z=-1.4261270204248366
- **CHANGE_POINT** `ps_gen` value=-695 d1=-1.0 d12=5.0 z=-0.893554797008547
- **PERSISTENT_UP** `residual_proxy` value=9284 d1=0.0 d12=331.0 z=-1.6819554525316456
- **PERSISTENT_DOWN** `thermal_base` value=6248 d1=-28.0 d12=-160.0 z=-1.4680071029411765
- **PERSISTENT_DOWN** `biomass_gen` value=476 d1=-1.0 d12=0.0 z=-1.4636427575
- **PERSISTENT_DOWN** `ccgt_gen` value=2917 d1=-24.0 d12=-159.0 z=-1.4261270204248366
- **PERSISTENT_DOWN** `wind_forecast` value=6656 d1=0.0 d12=-331.0 z=-1.266867704347826

## Nearest historical live analogues

- `2026-09-19T09:21:22.240716Z` distance=0.118 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T09:26:43.150108Z` distance=0.118 → {'next30m_imbalance_delta': 22.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T09:30:55.378368Z` distance=0.118 → {'next30m_imbalance_delta': 22.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T09:35:04.775644Z` distance=0.118 → {'next30m_imbalance_delta': 22.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T09:39:16.171123Z` distance=0.118 → {'next30m_imbalance_delta': 22.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

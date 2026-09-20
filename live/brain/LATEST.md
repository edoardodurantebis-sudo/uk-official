# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T12:34:29.670242Z`  
Memory snapshots: **1830**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low, wind falling.

## Active patterns

- **PERSISTENT_DOWN** `ind_demand` value=-1.182e+04 d1=0.0 d12=-2.0 z=41.481119625
- **ROBUST_OUTLIER** `ind_demand` value=-1.182e+04 d1=0.0 d12=-2.0 z=41.481119625
- **CHANGE_POINT** `ind_generation` value=1.538e+04 d1=0.0 d12=12.0 z=2.3431017234042555
- **CHANGE_POINT** `margin` value=3.578e+04 d1=0.0 d12=0.0 z=-2.134635153240741
- **CHANGE_POINT** `biomass_gen` value=582 d1=-1.0 d12=-3.0 z=-1.04239325
- **CHANGE_POINT** `ps_gen` value=-663 d1=7.0 d12=0.0 z=0.950417375
- **CHANGE_POINT** `imbalance` value=-5720 d1=0.0 d12=12.0 z=0.6872965174050633
- **PERSISTENT_UP** `ind_generation` value=1.538e+04 d1=0.0 d12=12.0 z=2.3431017234042555
- **CHANGE_POINT** `thermal_base` value=5749 d1=23.0 d12=17.0 z=-0.2977058206896551
- **CHANGE_POINT** `ccgt_gen` value=2414 d1=26.0 d12=15.0 z=-0.291015802247191
- **PERSISTENT_DOWN** `wind_gen` value=1.242e+04 d1=-108.0 d12=-412.0 z=-2.127920013793103
- **PERSISTENT_UP** `residual_proxy` value=1.832e+04 d1=73.0 d12=73.0 z=1.7943052626506022
- **ACCELERATION** `residual_proxy` value=1.832e+04 d1=73.0 d12=73.0 z=1.7943052626506022
- **PERSISTENT_DOWN** `wind_forecast` value=2287 d1=-73.0 d12=-73.0 z=-1.203927940860215
- **ACCELERATION** `wind_forecast` value=2287 d1=-73.0 d12=-73.0 z=-1.203927940860215

## Nearest historical live analogues

- `2026-09-20T11:23:04.537077Z` distance=0.015 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:27:16.047953Z` distance=0.015 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:31:27.990762Z` distance=0.015 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:35:41.173966Z` distance=0.015 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:39:54.159585Z` distance=0.015 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

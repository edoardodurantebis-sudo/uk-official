# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T15:10:08.327006Z`  
Memory snapshots: **897**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2664 d1=0.0 d12=393.0 z=16.162772898148148
- **PERSISTENT_UP** `biomass_gen` value=2664 d1=0.0 d12=393.0 z=16.162772898148148
- **ROBUST_OUTLIER** `biomass_gen` value=2664 d1=0.0 d12=393.0 z=16.162772898148148
- **PERSISTENT_UP** `thermal_base` value=6364 d1=0.0 d12=271.0 z=9.500085933333333
- **ROBUST_OUTLIER** `thermal_base` value=6364 d1=0.0 d12=271.0 z=9.500085933333333
- **PERSISTENT_UP** `ccgt_gen` value=3060 d1=0.0 d12=276.0 z=8.859822987288135
- **ROBUST_OUTLIER** `ccgt_gen` value=3060 d1=0.0 d12=276.0 z=8.859822987288135
- **CHANGE_POINT** `imbalance` value=1.168e+04 d1=0.0 d12=-260.0 z=-6.7448974999999995
- **ROBUST_OUTLIER** `ps_gen` value=-651 d1=0.0 d12=283.0 z=7.9790702340425534
- **ROBUST_OUTLIER** `imbalance` value=1.168e+04 d1=0.0 d12=-260.0 z=-6.7448974999999995
- **ROBUST_OUTLIER** `residual_proxy` value=-2671 d1=0.0 d12=271.0 z=3.8890791968085106
- **CHANGE_POINT** `ind_demand` value=-1.128e+04 d1=0.0 d12=-24.0 z=-1.1241495833333335
- **CHANGE_POINT** `margin` value=3.565e+04 d1=0.0 d12=-217.0 z=-0.6915654398734178
- **CHANGE_POINT** `interconnector_net` value=1065 d1=0.0 d12=465.0 z=0.41341114572454307
- **CHANGE_POINT** `ind_generation` value=2.849e+04 d1=0.0 d12=11.0 z=0.18548468125

## Nearest historical live analogues

- `2026-09-17T13:54:16.255911Z` distance=0.175 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T13:58:30.621005Z` distance=0.178 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:02:42.198136Z` distance=0.178 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:06:57.483529Z` distance=0.178 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:11:12.490811Z` distance=0.178 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

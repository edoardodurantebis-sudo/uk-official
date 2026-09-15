# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T17:37:38.944496Z`  
Memory snapshots: **286**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3213 d1=35.0 d12=711.0 z=62.263835046875
- **PERSISTENT_UP** `biomass_gen` value=3213 d1=35.0 d12=711.0 z=62.263835046875
- **ROBUST_OUTLIER** `biomass_gen` value=3213 d1=35.0 d12=711.0 z=62.263835046875
- **PERSISTENT_UP** `ccgt_gen` value=1.044e+04 d1=30.0 d12=273.0 z=22.088271474624058
- **ROBUST_OUTLIER** `ccgt_gen` value=1.044e+04 d1=30.0 d12=273.0 z=22.088271474624058
- **PERSISTENT_UP** `thermal_base` value=1.375e+04 d1=22.0 d12=271.0 z=21.97017736235955
- **ROBUST_OUTLIER** `thermal_base` value=1.375e+04 d1=22.0 d12=271.0 z=21.97017736235955
- **PERSISTENT_DOWN** `interconnector_net` value=-1749 d1=-24.0 d12=-2269.0 z=-3.267064451468281
- **ACCELERATION** `interconnector_net` value=-1749 d1=-24.0 d12=-2269.0 z=-3.267064451468281
- **ROBUST_OUTLIER** `interconnector_net` value=-1749 d1=-24.0 d12=-2269.0 z=-3.267064451468281
- **CHANGE_POINT** `imbalance` value=5772 d1=0.0 d12=-55.0 z=0.6969727416666667
- **CHANGE_POINT** `ind_generation` value=2.489e+04 d1=0.0 d12=-55.0 z=0.5430956428571428
- **PERSISTENT_DOWN** `nuclear_gen` value=3317 d1=-8.0 d12=-2.0 z=-2.4731290833333333
- **ACCELERATION** `nuclear_gen` value=3317 d1=-8.0 d12=-2.0 z=-2.4731290833333333
- **PERSISTENT_UP** `ps_gen` value=505 d1=3.0 d12=78.0 z=2.2485834017067003

## Nearest historical live analogues

- `2026-09-15T16:34:33.511782Z` distance=0.087 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T16:38:45.835004Z` distance=0.087 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T16:42:58.169534Z` distance=0.087 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T16:21:57.402275Z` distance=0.095 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 53.0}
- `2026-09-15T16:26:08.230608Z` distance=0.095 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 53.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

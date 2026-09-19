# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T04:35:21.377586Z`  
Memory snapshots: **1375**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `imbalance` value=9764 d1=0.0 d12=342.0 z=7.52730561
- **CHANGE_POINT** `ind_generation` value=2.696e+04 d1=0.0 d12=342.0 z=7.52730561
- **ROBUST_OUTLIER** `imbalance` value=9764 d1=0.0 d12=342.0 z=7.52730561
- **ROBUST_OUTLIER** `ind_generation` value=2.696e+04 d1=0.0 d12=342.0 z=7.52730561
- **CHANGE_POINT** `ind_demand` value=-1.087e+04 d1=0.0 d12=12.0 z=3.8221085833333333
- **ROBUST_OUTLIER** `ind_demand` value=-1.087e+04 d1=0.0 d12=12.0 z=3.8221085833333333
- **ROBUST_OUTLIER** `biomass_gen` value=693 d1=0.0 d12=0.0 z=-3.499171066666667
- **CHANGE_POINT** `interconnector_net` value=-1.091e+04 d1=0.0 d12=231.0 z=-0.5127482831270059
- **CHANGE_POINT** `ps_gen` value=-546 d1=0.0 d12=-2.0 z=-0.010967313008130081
- **PERSISTENT_UP** `interconnector_net` value=-1.091e+04 d1=0.0 d12=231.0 z=-0.5127482831270059
- **ACCELERATION** `interconnector_net` value=-1.091e+04 d1=0.0 d12=231.0 z=-0.5127482831270059
- **ACCELERATION** `ps_gen` value=-546 d1=0.0 d12=-2.0 z=-0.010967313008130081

## Nearest historical live analogues

- `2026-09-19T03:32:06.717243Z` distance=0.011 → {'next30m_imbalance_delta': 380.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:36:20.101769Z` distance=0.011 → {'next30m_imbalance_delta': 380.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:40:33.171803Z` distance=0.011 → {'next30m_imbalance_delta': 380.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:23:44.436802Z` distance=0.305 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 748.0}
- `2026-09-19T03:27:55.750125Z` distance=0.305 → {'next30m_imbalance_delta': 380.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 748.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

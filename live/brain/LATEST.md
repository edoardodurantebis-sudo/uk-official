# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T05:00:37.533796Z`  
Memory snapshots: **1381**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `imbalance` value=9720 d1=0.0 d12=-82.0 z=5.053484742307692
- **CHANGE_POINT** `ind_generation` value=2.691e+04 d1=0.0 d12=-87.0 z=4.9155995416666665
- **CHANGE_POINT** `ind_demand` value=-1.086e+04 d1=0.0 d12=14.0 z=4.72142825
- **CHANGE_POINT** `biomass_gen` value=693 d1=0.0 d12=0.0 z=-3.499171066666667
- **PERSISTENT_DOWN** `imbalance` value=9720 d1=0.0 d12=-82.0 z=5.053484742307692
- **ROBUST_OUTLIER** `imbalance` value=9720 d1=0.0 d12=-82.0 z=5.053484742307692
- **PERSISTENT_DOWN** `ind_generation` value=2.691e+04 d1=0.0 d12=-87.0 z=4.9155995416666665
- **ROBUST_OUTLIER** `ind_generation` value=2.691e+04 d1=0.0 d12=-87.0 z=4.9155995416666665
- **PERSISTENT_UP** `ind_demand` value=-1.086e+04 d1=0.0 d12=14.0 z=4.72142825
- **ROBUST_OUTLIER** `ind_demand` value=-1.086e+04 d1=0.0 d12=14.0 z=4.72142825
- **ACCELERATION** `biomass_gen` value=693 d1=0.0 d12=0.0 z=-3.499171066666667
- **ROBUST_OUTLIER** `biomass_gen` value=693 d1=0.0 d12=0.0 z=-3.499171066666667
- **CHANGE_POINT** `ccgt_gen` value=3083 d1=0.0 d12=26.0 z=-0.9506395389492754
- **CHANGE_POINT** `thermal_base` value=6423 d1=0.0 d12=25.0 z=-0.9136705124113474
- **CHANGE_POINT** `interconnector_net` value=-1.092e+04 d1=0.0 d12=144.0 z=-0.020268473288814693

## Nearest historical live analogues

- `2026-09-19T03:53:09.975185Z` distance=0.013 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:57:21.988080Z` distance=0.013 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T04:01:33.750127Z` distance=0.013 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T04:05:47.150254Z` distance=0.013 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:32:06.717243Z` distance=0.015 → {'next30m_imbalance_delta': 380.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

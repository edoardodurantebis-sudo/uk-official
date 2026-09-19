# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T04:31:06.739586Z`  
Memory snapshots: **1374**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `imbalance` value=9764 d1=0.0 d12=342.0 z=7.52730561
- **CHANGE_POINT** `ind_generation` value=2.696e+04 d1=0.0 d12=342.0 z=7.52730561
- **ROBUST_OUTLIER** `imbalance` value=9764 d1=0.0 d12=342.0 z=7.52730561
- **ROBUST_OUTLIER** `ind_generation` value=2.696e+04 d1=0.0 d12=342.0 z=7.52730561
- **CHANGE_POINT** `ind_demand` value=-1.087e+04 d1=0.0 d12=12.0 z=3.8221085833333333
- **PERSISTENT_UP** `ind_demand` value=-1.087e+04 d1=0.0 d12=12.0 z=3.8221085833333333
- **ROBUST_OUTLIER** `ind_demand` value=-1.087e+04 d1=0.0 d12=12.0 z=3.8221085833333333
- **CHANGE_POINT** `ccgt_gen` value=3058 d1=-1.0 d12=-3.0 z=-1.5701493947674419
- **ROBUST_OUTLIER** `biomass_gen` value=693 d1=0.0 d12=0.0 z=-3.499171066666667
- **CHANGE_POINT** `interconnector_net` value=-1.091e+04 d1=96.0 d12=231.0 z=-0.5945540941130906
- **ACCELERATION** `nuclear_gen` value=3345 d1=0.0 d12=-1.0 z=2.0234692499999998
- **CHANGE_POINT** `ps_gen` value=-546 d1=-1.0 d12=-2.0 z=-0.010922910931174088
- **ACCELERATION** `ccgt_gen` value=3058 d1=-1.0 d12=-3.0 z=-1.5701493947674419
- **ACCELERATION** `thermal_base` value=6403 d1=-1.0 d12=-4.0 z=-1.5439369102564104
- **PERSISTENT_UP** `margin` value=3.832e+04 d1=0.0 d12=7.0 z=1.0524365926724137

## Nearest historical live analogues

- `2026-09-19T03:32:06.717243Z` distance=0.011 → {'next30m_imbalance_delta': 380.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:36:20.101769Z` distance=0.011 → {'next30m_imbalance_delta': 380.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:23:44.436802Z` distance=0.305 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 748.0}
- `2026-09-19T03:27:55.750125Z` distance=0.305 → {'next30m_imbalance_delta': 380.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 748.0}
- `2026-09-19T02:54:16.089654Z` distance=0.305 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

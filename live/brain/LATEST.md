# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T23:22:50.106750Z`  
Memory snapshots: **1014**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.118e+04 d1=-7.0 d12=-22.0 z=-7.41938725
- **PERSISTENT_DOWN** `ind_demand` value=-1.118e+04 d1=-7.0 d12=-22.0 z=-7.41938725
- **ROBUST_OUTLIER** `ind_demand` value=-1.118e+04 d1=-7.0 d12=-22.0 z=-7.41938725
- **CHANGE_POINT** `ccgt_gen` value=3634 d1=1.0 d12=-439.0 z=-1.5106932792109256
- **CHANGE_POINT** `thermal_base` value=6952 d1=0.0 d12=-436.0 z=-1.5024805584024115
- **PERSISTENT_UP** `interconnector_net` value=-7190 d1=2.0 d12=1071.0 z=-3.334370668517125
- **ROBUST_OUTLIER** `interconnector_net` value=-7190 d1=2.0 d12=1071.0 z=-3.334370668517125
- **PERSISTENT_UP** `biomass_gen` value=1835 d1=50.0 d12=92.0 z=-3.0637343524945773
- **ROBUST_OUTLIER** `biomass_gen` value=1835 d1=50.0 d12=92.0 z=-3.0637343524945773
- **CHANGE_POINT** `margin` value=3.657e+04 d1=68.0 d12=135.0 z=0.7644217166666666
- **PERSISTENT_UP** `imbalance` value=9745 d1=31.0 d12=34.0 z=1.812691203125
- **ACCELERATION** `imbalance` value=9745 d1=31.0 d12=34.0 z=1.812691203125
- **PERSISTENT_UP** `ind_generation` value=2.656e+04 d1=31.0 d12=34.0 z=1.812691203125
- **ACCELERATION** `ind_generation` value=2.656e+04 d1=31.0 d12=34.0 z=1.812691203125
- **REVERSAL** `ccgt_gen` value=3634 d1=1.0 d12=-439.0 z=-1.5106932792109256

## Nearest historical live analogues

- `2026-09-17T19:52:34.655680Z` distance=0.039 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:56:45.301747Z` distance=0.039 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -68.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T20:00:59.852389Z` distance=0.039 → {'next30m_imbalance_delta': -22.0, 'next30m_margin_delta': -68.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T20:05:11.645283Z` distance=0.039 → {'next30m_imbalance_delta': -22.0, 'next30m_margin_delta': -68.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T20:09:24.491695Z` distance=0.039 → {'next30m_imbalance_delta': -22.0, 'next30m_margin_delta': -68.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

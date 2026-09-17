# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T23:43:44.916694Z`  
Memory snapshots: **1019**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.118e+04 d1=0.0 d12=-7.0 z=-7.41938725
- **ROBUST_OUTLIER** `ind_demand` value=-1.118e+04 d1=0.0 d12=-7.0 z=-7.41938725
- **CHANGE_POINT** `ps_gen` value=24 d1=72.0 d12=-24.0 z=-1.93915803125
- **CHANGE_POINT** `imbalance` value=9745 d1=0.0 d12=31.0 z=1.812691203125
- **CHANGE_POINT** `ind_generation` value=2.656e+04 d1=0.0 d12=31.0 z=1.812691203125
- **CHANGE_POINT** `thermal_base` value=7033 d1=-148.0 d12=-837.0 z=-1.075641758847032
- **CHANGE_POINT** `ccgt_gen` value=3713 d1=-149.0 d12=-831.0 z=-1.0713612060830018
- **CHANGE_POINT** `margin` value=3.657e+04 d1=0.0 d12=68.0 z=0.7644217166666666
- **PERSISTENT_UP** `biomass_gen` value=1961 d1=0.0 d12=81.0 z=-2.2762441280602634
- **REVERSAL** `ps_gen` value=24 d1=72.0 d12=-24.0 z=-1.93915803125
- **ACCELERATION** `ps_gen` value=24 d1=72.0 d12=-24.0 z=-1.93915803125
- **PERSISTENT_UP** `interconnector_net` value=-6156 d1=8.0 d12=2089.0 z=-1.304267616985438
- **PERSISTENT_DOWN** `wind_gen` value=1.458e+04 d1=-14.0 d12=-700.0 z=-1.2506931976320583
- **PERSISTENT_DOWN** `thermal_base` value=7033 d1=-148.0 d12=-837.0 z=-1.075641758847032
- **PERSISTENT_DOWN** `ccgt_gen` value=3713 d1=-149.0 d12=-831.0 z=-1.0713612060830018

## Nearest historical live analogues

- `2026-09-17T18:57:56.745109Z` distance=0.042 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=0.042 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=0.042 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:10:36.600451Z` distance=0.042 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:14:49.284800Z` distance=0.042 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

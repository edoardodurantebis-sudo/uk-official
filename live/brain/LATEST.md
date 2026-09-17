# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T23:35:24.193269Z`  
Memory snapshots: **1017**  
Current physical regime: **BALANCED**

Regime read: wind rising.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.118e+04 d1=0.0 d12=-22.0 z=-7.41938725
- **ROBUST_OUTLIER** `ind_demand` value=-1.118e+04 d1=0.0 d12=-22.0 z=-7.41938725
- **CHANGE_POINT** `ps_gen` value=52 d1=0.0 d12=1.0 z=-1.954938205882353
- **CHANGE_POINT** `imbalance` value=9745 d1=0.0 d12=34.0 z=1.812691203125
- **CHANGE_POINT** `ind_generation` value=2.656e+04 d1=0.0 d12=34.0 z=1.812691203125
- **CHANGE_POINT** `ccgt_gen` value=3846 d1=0.0 d12=-847.0 z=-1.209297934751773
- **CHANGE_POINT** `thermal_base` value=7164 d1=0.0 d12=-848.0 z=-1.2052279795342273
- **CHANGE_POINT** `margin` value=3.657e+04 d1=0.0 d12=135.0 z=0.7644217166666666
- **PERSISTENT_UP** `biomass_gen` value=1934 d1=0.0 d12=93.0 z=-2.4630095371819962
- **ACCELERATION** `biomass_gen` value=1934 d1=0.0 d12=93.0 z=-2.4630095371819962
- **ACCELERATION** `ps_gen` value=52 d1=0.0 d12=1.0 z=-1.954938205882353
- **PERSISTENT_UP** `interconnector_net` value=-6164 d1=0.0 d12=2082.0 z=-1.58131691827768
- **ACCELERATION** `interconnector_net` value=-6164 d1=0.0 d12=2082.0 z=-1.58131691827768
- **PERSISTENT_DOWN** `wind_gen` value=1.461e+04 d1=0.0 d12=-577.0 z=-1.1597783679417124
- **ACCELERATION** `nuclear_gen` value=3318 d1=0.0 d12=-1.0 z=-0.4496598333333333

## Nearest historical live analogues

- `2026-09-17T18:57:56.745109Z` distance=0.042 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=0.042 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=0.042 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:10:36.600451Z` distance=0.042 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:14:49.284800Z` distance=0.042 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

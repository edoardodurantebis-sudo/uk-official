# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T23:39:35.492580Z`  
Memory snapshots: **1018**  
Current physical regime: **BALANCED**

Regime read: wind rising.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.118e+04 d1=0.0 d12=-22.0 z=-7.41938725
- **ROBUST_OUTLIER** `ind_demand` value=-1.118e+04 d1=0.0 d12=-22.0 z=-7.41938725
- **CHANGE_POINT** `ps_gen` value=-48 d1=-100.0 d12=-96.0 z=-2.4177362053140095
- **CHANGE_POINT** `imbalance` value=9745 d1=0.0 d12=34.0 z=1.812691203125
- **CHANGE_POINT** `ind_generation` value=2.656e+04 d1=0.0 d12=34.0 z=1.812691203125
- **CHANGE_POINT** `thermal_base` value=7181 d1=17.0 d12=-898.0 z=-1.1048363249180329
- **CHANGE_POINT** `ccgt_gen` value=3862 d1=16.0 d12=-896.0 z=-1.09604584375
- **CHANGE_POINT** `margin` value=3.657e+04 d1=0.0 d12=135.0 z=0.7644217166666666
- **PERSISTENT_DOWN** `ps_gen` value=-48 d1=-100.0 d12=-96.0 z=-2.4177362053140095
- **ACCELERATION** `ps_gen` value=-48 d1=-100.0 d12=-96.0 z=-2.4177362053140095
- **PERSISTENT_UP** `biomass_gen` value=1961 d1=27.0 d12=84.0 z=-2.2986405901328273
- **PERSISTENT_UP** `interconnector_net` value=-6164 d1=0.0 d12=2082.0 z=-1.3615882047860361
- **PERSISTENT_DOWN** `wind_gen` value=1.459e+04 d1=-23.0 d12=-711.0 z=-1.2162929918032785
- **REVERSAL** `thermal_base` value=7181 d1=17.0 d12=-898.0 z=-1.1048363249180329
- **REVERSAL** `ccgt_gen` value=3862 d1=16.0 d12=-896.0 z=-1.09604584375

## Nearest historical live analogues

- `2026-09-17T18:57:56.745109Z` distance=0.042 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=0.042 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=0.042 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:10:36.600451Z` distance=0.042 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:14:49.284800Z` distance=0.042 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

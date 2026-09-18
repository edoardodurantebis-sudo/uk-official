# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T22:19:10.576953Z`  
Memory snapshots: **1286**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=2.618e+04 d1=0.0 d12=-41.0 z=16.891569391304348
- **PERSISTENT_DOWN** `thermal_base` value=7181 d1=-31.0 d12=-375.0 z=9.951549886871508
- **ROBUST_OUTLIER** `thermal_base` value=7181 d1=-31.0 d12=-375.0 z=9.951549886871508
- **PERSISTENT_DOWN** `ccgt_gen` value=3840 d1=-30.0 d12=-380.0 z=9.53714001344086
- **ROBUST_OUTLIER** `ccgt_gen` value=3840 d1=-30.0 d12=-380.0 z=9.53714001344086
- **CHANGE_POINT** `interconnector_net` value=-7634 d1=-118.0 d12=-6258.0 z=-7.222281292652027
- **PERSISTENT_DOWN** `interconnector_net` value=-7634 d1=-118.0 d12=-6258.0 z=-7.222281292652027
- **ROBUST_OUTLIER** `interconnector_net` value=-7634 d1=-118.0 d12=-6258.0 z=-7.222281292652027
- **CHANGE_POINT** `ind_demand` value=-1.089e+04 d1=0.0 d12=2.0 z=-3.950582821428571
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=0.0 d12=2.0 z=-3.950582821428571
- **CHANGE_POINT** `biomass_gen` value=925 d1=-25.0 d12=-699.0 z=-1.6133921484741784
- **CHANGE_POINT** `ps_gen` value=-637 d1=-167.0 d12=-1101.0 z=-0.4585014592696629
- **CHANGE_POINT** `imbalance` value=8990 d1=0.0 d12=-42.0 z=0.36988147580645164
- **PERSISTENT_DOWN** `biomass_gen` value=925 d1=-25.0 d12=-699.0 z=-1.6133921484741784
- **REVERSAL** `nuclear_gen` value=3341 d1=-1.0 d12=5.0 z=1.3489795

## Nearest historical live analogues

- `2026-09-18T19:32:42.521831Z` distance=0.039 → {'next30m_imbalance_delta': 17.0, 'next30m_margin_delta': 26.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:36:55.641647Z` distance=0.039 → {'next30m_imbalance_delta': 17.0, 'next30m_margin_delta': 26.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:54:36.333288Z` distance=0.289 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:58:51.197302Z` distance=0.289 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:03:04.185551Z` distance=0.289 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

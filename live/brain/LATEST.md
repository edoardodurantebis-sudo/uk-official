# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T22:14:57.472776Z`  
Memory snapshots: **1285**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=2.618e+04 d1=0.0 d12=-41.0 z=16.891569391304348
- **ROBUST_OUTLIER** `thermal_base` value=7212 d1=0.0 d12=-373.0 z=10.892206498511905
- **CHANGE_POINT** `interconnector_net` value=-7516 d1=0.0 d12=-6116.0 z=-8.295167972358122
- **ROBUST_OUTLIER** `ccgt_gen` value=3870 d1=0.0 d12=-377.0 z=10.285016018361581
- **PERSISTENT_DOWN** `interconnector_net` value=-7516 d1=0.0 d12=-6116.0 z=-8.295167972358122
- **ROBUST_OUTLIER** `interconnector_net` value=-7516 d1=0.0 d12=-6116.0 z=-8.295167972358122
- **CHANGE_POINT** `ind_demand` value=-1.089e+04 d1=0.0 d12=2.0 z=-3.950582821428571
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=0.0 d12=2.0 z=-3.950582821428571
- **CHANGE_POINT** `biomass_gen` value=950 d1=0.0 d12=-673.0 z=-1.534226684859155
- **CHANGE_POINT** `imbalance` value=8990 d1=0.0 d12=-42.0 z=0.36988147580645164
- **CHANGE_POINT** `ps_gen` value=-470 d1=0.0 d12=-1031.0 z=-0.03662959316479401
- **PERSISTENT_UP** `nuclear_gen` value=3342 d1=0.0 d12=4.0 z=1.686224375
- **ACCELERATION** `nuclear_gen` value=3342 d1=0.0 d12=4.0 z=1.686224375
- **PERSISTENT_DOWN** `wind_gen` value=1.645e+04 d1=0.0 d12=-257.0 z=-0.07456670603015075
- **ACCELERATION** `wind_gen` value=1.645e+04 d1=0.0 d12=-257.0 z=-0.07456670603015075

## Nearest historical live analogues

- `2026-09-18T19:32:42.521831Z` distance=0.039 → {'next30m_imbalance_delta': 17.0, 'next30m_margin_delta': 26.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:54:36.333288Z` distance=0.289 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:58:51.197302Z` distance=0.289 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:03:04.185551Z` distance=0.289 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:07:15.585093Z` distance=0.289 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -511.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

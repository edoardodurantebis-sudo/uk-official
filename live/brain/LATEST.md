# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T21:44:41.914660Z`  
Memory snapshots: **1278**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.624e+04 d1=0.0 d12=12.0 z=18.592456586956523
- **CHANGE_POINT** `ccgt_gen` value=3987 d1=-99.0 d12=-966.0 z=17.09088434322034
- **CHANGE_POINT** `thermal_base` value=7332 d1=-90.0 d12=-958.0 z=17.00961125840336
- **PERSISTENT_UP** `ind_generation` value=2.624e+04 d1=0.0 d12=12.0 z=18.592456586956523
- **ACCELERATION** `ind_generation` value=2.624e+04 d1=0.0 d12=12.0 z=18.592456586956523
- **ROBUST_OUTLIER** `ind_generation` value=2.624e+04 d1=0.0 d12=12.0 z=18.592456586956523
- **PERSISTENT_DOWN** `ccgt_gen` value=3987 d1=-99.0 d12=-966.0 z=17.09088434322034
- **ROBUST_OUTLIER** `ccgt_gen` value=3987 d1=-99.0 d12=-966.0 z=17.09088434322034
- **PERSISTENT_DOWN** `thermal_base` value=7332 d1=-90.0 d12=-958.0 z=17.00961125840336
- **ROBUST_OUTLIER** `thermal_base` value=7332 d1=-90.0 d12=-958.0 z=17.00961125840336
- **CHANGE_POINT** `interconnector_net` value=-6380 d1=-5022.0 d12=-5724.0 z=-10.041526414554905
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=0.0 d12=-6.0 z=-10.94172261111111
- **PERSISTENT_DOWN** `interconnector_net` value=-6380 d1=-5022.0 d12=-5724.0 z=-10.041526414554905
- **ACCELERATION** `interconnector_net` value=-6380 d1=-5022.0 d12=-5724.0 z=-10.041526414554905
- **ROBUST_OUTLIER** `interconnector_net` value=-6380 d1=-5022.0 d12=-5724.0 z=-10.041526414554905

## Nearest historical live analogues

- `2026-09-18T18:54:36.333288Z` distance=0.301 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:58:51.197302Z` distance=0.301 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:03:04.185551Z` distance=0.301 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:51:12.400587Z` distance=0.324 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:55:26.775797Z` distance=0.325 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

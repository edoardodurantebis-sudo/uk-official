# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T19:45:21.123872Z`  
Memory snapshots: **1275**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.089e+04 d1=0.0 d12=-6.0 z=-98.4755035
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=0.0 d12=-6.0 z=-98.4755035
- **CHANGE_POINT** `ccgt_gen` value=4220 d1=0.0 d12=-946.0 z=19.754547254237288
- **CHANGE_POINT** `thermal_base` value=7556 d1=0.0 d12=-948.0 z=19.548866787815125
- **CHANGE_POINT** `ind_generation` value=2.623e+04 d1=0.0 d12=-5.0 z=18.09392068478261
- **PERSISTENT_DOWN** `ccgt_gen` value=4220 d1=0.0 d12=-946.0 z=19.754547254237288
- **ROBUST_OUTLIER** `ccgt_gen` value=4220 d1=0.0 d12=-946.0 z=19.754547254237288
- **PERSISTENT_DOWN** `thermal_base` value=7556 d1=0.0 d12=-948.0 z=19.548866787815125
- **ROBUST_OUTLIER** `thermal_base` value=7556 d1=0.0 d12=-948.0 z=19.548866787815125
- **ROBUST_OUTLIER** `ind_generation` value=2.623e+04 d1=0.0 d12=-5.0 z=18.09392068478261
- **ROBUST_OUTLIER** `interconnector_net` value=-1376 d1=0.0 d12=-1074.0 z=-5.943423322305594
- **ROBUST_OUTLIER** `margin` value=3.75e+04 d1=0.0 d12=-21.0 z=-4.809754288690476
- **CHANGE_POINT** `biomass_gen` value=1624 d1=0.0 d12=94.0 z=0.7696960566600397
- **PERSISTENT_UP** `ps_gen` value=464 d1=0.0 d12=170.0 z=2.519536861723447
- **ACCELERATION** `ps_gen` value=464 d1=0.0 d12=170.0 z=2.519536861723447

## Nearest historical live analogues

- `2026-09-18T17:51:12.400587Z` distance=0.326 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:55:26.775797Z` distance=0.326 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:59:39.675441Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:03:52.862865Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:08:04.608022Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

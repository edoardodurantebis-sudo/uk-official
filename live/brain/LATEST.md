# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T19:32:42.521831Z`  
Memory snapshots: **1272**  
Current physical regime: **BALANCED**

Regime read: margin low, wind rising.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.089e+04 d1=0.0 d12=-155.0 z=-98.4755035
- **PERSISTENT_DOWN** `ind_demand` value=-1.089e+04 d1=0.0 d12=-155.0 z=-98.4755035
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=0.0 d12=-155.0 z=-98.4755035
- **PERSISTENT_DOWN** `ccgt_gen` value=4338 d1=-274.0 d12=-566.0 z=21.103526754237286
- **ACCELERATION** `ccgt_gen` value=4338 d1=-274.0 d12=-566.0 z=21.103526754237286
- **ROBUST_OUTLIER** `ccgt_gen` value=4338 d1=-274.0 d12=-566.0 z=21.103526754237286
- **PERSISTENT_DOWN** `thermal_base` value=7673 d1=-269.0 d12=-567.0 z=20.875174363445378
- **ACCELERATION** `thermal_base` value=7673 d1=-269.0 d12=-567.0 z=20.875174363445378
- **ROBUST_OUTLIER** `thermal_base` value=7673 d1=-269.0 d12=-567.0 z=20.875174363445378
- **ROBUST_OUTLIER** `ind_generation` value=2.623e+04 d1=0.0 d12=0.0 z=18.09392068478261
- **CHANGE_POINT** `margin` value=3.75e+04 d1=0.0 d12=-262.0 z=-5.050242003125
- **PERSISTENT_DOWN** `interconnector_net` value=-1416 d1=-505.0 d12=-1110.0 z=-6.322734850719424
- **ACCELERATION** `interconnector_net` value=-1416 d1=-505.0 d12=-1110.0 z=-6.322734850719424
- **ROBUST_OUTLIER** `interconnector_net` value=-1416 d1=-505.0 d12=-1110.0 z=-6.322734850719424
- **PERSISTENT_DOWN** `margin` value=3.75e+04 d1=0.0 d12=-262.0 z=-5.050242003125

## Nearest historical live analogues

- `2026-09-18T17:51:12.400587Z` distance=0.326 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:55:26.775797Z` distance=0.326 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:59:39.675441Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:03:52.862865Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:08:04.608022Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

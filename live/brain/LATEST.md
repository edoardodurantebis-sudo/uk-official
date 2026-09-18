# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T19:41:08.223702Z`  
Memory snapshots: **1274**  
Current physical regime: **BALANCED**

Regime read: margin low, wind rising.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.089e+04 d1=0.0 d12=-155.0 z=-98.4755035
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=0.0 d12=-155.0 z=-98.4755035
- **CHANGE_POINT** `ind_generation` value=2.623e+04 d1=0.0 d12=0.0 z=18.09392068478261
- **PERSISTENT_DOWN** `ccgt_gen` value=4220 d1=-27.0 d12=-811.0 z=19.754547254237288
- **ROBUST_OUTLIER** `ccgt_gen` value=4220 d1=-27.0 d12=-811.0 z=19.754547254237288
- **PERSISTENT_DOWN** `thermal_base` value=7556 d1=-29.0 d12=-807.0 z=19.548866787815125
- **ROBUST_OUTLIER** `thermal_base` value=7556 d1=-29.0 d12=-807.0 z=19.548866787815125
- **ROBUST_OUTLIER** `ind_generation` value=2.623e+04 d1=0.0 d12=0.0 z=18.09392068478261
- **REVERSAL** `interconnector_net` value=-1376 d1=24.0 d12=-1069.0 z=-6.01777146426105
- **ROBUST_OUTLIER** `interconnector_net` value=-1376 d1=24.0 d12=-1069.0 z=-6.01777146426105
- **ROBUST_OUTLIER** `margin` value=3.75e+04 d1=0.0 d12=-262.0 z=-5.050242003125
- **CHANGE_POINT** `biomass_gen` value=1624 d1=1.0 d12=94.0 z=0.9373321474226803
- **REVERSAL** `ps_gen` value=464 d1=-97.0 d12=170.0 z=2.5426219666666667
- **ACCELERATION** `ps_gen` value=464 d1=-97.0 d12=170.0 z=2.5426219666666667
- **PERSISTENT_UP** `biomass_gen` value=1624 d1=1.0 d12=94.0 z=0.9373321474226803

## Nearest historical live analogues

- `2026-09-18T17:51:12.400587Z` distance=0.326 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:55:26.775797Z` distance=0.326 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:59:39.675441Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:03:52.862865Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:08:04.608022Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

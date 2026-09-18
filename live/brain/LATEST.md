# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T19:36:55.641647Z`  
Memory snapshots: **1273**  
Current physical regime: **BALANCED**

Regime read: margin low, wind rising.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.089e+04 d1=0.0 d12=-155.0 z=-98.4755035
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=0.0 d12=-155.0 z=-98.4755035
- **CHANGE_POINT** `ind_generation` value=2.623e+04 d1=0.0 d12=0.0 z=18.09392068478261
- **PERSISTENT_DOWN** `ccgt_gen` value=4247 d1=-91.0 d12=-784.0 z=20.063212055084747
- **ROBUST_OUTLIER** `ccgt_gen` value=4247 d1=-91.0 d12=-784.0 z=20.063212055084747
- **PERSISTENT_DOWN** `thermal_base` value=7585 d1=-88.0 d12=-778.0 z=19.87760969117647
- **ROBUST_OUTLIER** `thermal_base` value=7585 d1=-88.0 d12=-778.0 z=19.87760969117647
- **ROBUST_OUTLIER** `ind_generation` value=2.623e+04 d1=0.0 d12=0.0 z=18.09392068478261
- **REVERSAL** `interconnector_net` value=-1400 d1=16.0 d12=-1093.0 z=-6.138093388070176
- **ACCELERATION** `interconnector_net` value=-1400 d1=16.0 d12=-1093.0 z=-6.138093388070176
- **ROBUST_OUTLIER** `interconnector_net` value=-1400 d1=16.0 d12=-1093.0 z=-6.138093388070176
- **ROBUST_OUTLIER** `margin` value=3.75e+04 d1=0.0 d12=-262.0 z=-5.050242003125
- **CHANGE_POINT** `biomass_gen` value=1623 d1=29.0 d12=93.0 z=1.3051376662499998
- **PERSISTENT_UP** `ps_gen` value=561 d1=115.0 d12=267.0 z=2.8424925178571425
- **PERSISTENT_UP** `biomass_gen` value=1623 d1=29.0 d12=93.0 z=1.3051376662499998

## Nearest historical live analogues

- `2026-09-18T17:51:12.400587Z` distance=0.326 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:55:26.775797Z` distance=0.326 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:59:39.675441Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:03:52.862865Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:08:04.608022Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

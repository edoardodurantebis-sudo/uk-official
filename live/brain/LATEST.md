# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T18:59:09.380511Z`  
Memory snapshots: **1580**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.621e+04 d1=0.0 d12=-603.0 z=-38.378466775
- **ROBUST_OUTLIER** `ind_generation` value=1.621e+04 d1=0.0 d12=-603.0 z=-38.378466775
- **CHANGE_POINT** `imbalance` value=-3742 d1=0.0 d12=-603.0 z=-10.081846789473685
- **ROBUST_OUTLIER** `imbalance` value=-3742 d1=0.0 d12=-603.0 z=-10.081846789473685
- **CHANGE_POINT** `biomass_gen` value=1007 d1=16.0 d12=254.0 z=2.388941669603524
- **CHANGE_POINT** `margin` value=3.62e+04 d1=0.0 d12=-100.0 z=-2.228225066964286
- **PERSISTENT_DOWN** `ccgt_gen` value=6773 d1=-210.0 d12=-246.0 z=3.45775521079258
- **ACCELERATION** `ccgt_gen` value=6773 d1=-210.0 d12=-246.0 z=3.45775521079258
- **ROBUST_OUTLIER** `ccgt_gen` value=6773 d1=-210.0 d12=-246.0 z=3.45775521079258
- **PERSISTENT_DOWN** `thermal_base` value=1.011e+04 d1=-209.0 d12=-237.0 z=3.366901959292763
- **ACCELERATION** `thermal_base` value=1.011e+04 d1=-209.0 d12=-237.0 z=3.366901959292763
- **ROBUST_OUTLIER** `thermal_base` value=1.011e+04 d1=-209.0 d12=-237.0 z=3.366901959292763
- **PERSISTENT_UP** `biomass_gen` value=1007 d1=16.0 d12=254.0 z=2.388941669603524
- **PERSISTENT_UP** `interconnector_net` value=-1134 d1=62.0 d12=1249.0 z=1.3981113559052334
- **PERSISTENT_UP** `nuclear_gen` value=3335 d1=1.0 d12=9.0 z=1.21408155

## Nearest historical live analogues

- `2026-09-19T17:22:38.318939Z` distance=0.017 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:26:48.291042Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:31:01.384129Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:35:13.165368Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:39:26.231429Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

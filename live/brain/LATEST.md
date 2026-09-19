# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T19:03:21.249483Z`  
Memory snapshots: **1581**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.621e+04 d1=0.0 d12=-603.0 z=-38.378466775
- **ROBUST_OUTLIER** `ind_generation` value=1.621e+04 d1=0.0 d12=-603.0 z=-38.378466775
- **CHANGE_POINT** `imbalance` value=-3742 d1=0.0 d12=-603.0 z=-10.081846789473685
- **ROBUST_OUTLIER** `imbalance` value=-3742 d1=0.0 d12=-603.0 z=-10.081846789473685
- **CHANGE_POINT** `biomass_gen` value=1013 d1=6.0 d12=254.0 z=2.4245975154185024
- **PERSISTENT_DOWN** `ccgt_gen` value=6545 d1=-228.0 d12=-310.0 z=3.1660413515886288
- **ROBUST_OUTLIER** `ccgt_gen` value=6545 d1=-228.0 d12=-310.0 z=3.1660413515886288
- **PERSISTENT_DOWN** `thermal_base` value=9881 d1=-227.0 d12=-304.0 z=3.114522982113487
- **ROBUST_OUTLIER** `thermal_base` value=9881 d1=-227.0 d12=-304.0 z=3.114522982113487
- **PERSISTENT_UP** `biomass_gen` value=1013 d1=6.0 d12=254.0 z=2.4245975154185024
- **PERSISTENT_UP** `interconnector_net` value=-726 d1=408.0 d12=1415.0 z=1.7873501366690239
- **PERSISTENT_UP** `nuclear_gen` value=3336 d1=1.0 d12=6.0 z=1.3489795
- **REVERSAL** `wind_gen` value=1.421e+04 d1=69.0 d12=-136.0 z=-0.6515825509433962
- **ACCELERATION** `wind_gen` value=1.421e+04 d1=69.0 d12=-136.0 z=-0.6515825509433962

## Nearest historical live analogues

- `2026-09-19T17:22:38.318939Z` distance=0.017 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:26:48.291042Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:31:01.384129Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:35:13.165368Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:39:26.231429Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

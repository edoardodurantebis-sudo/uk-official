# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T06:12:09.086152Z`  
Memory snapshots: **1398**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=-9598 d1=347.0 d12=1270.0 z=3.546815839679359
- **CHANGE_POINT** `imbalance` value=9697 d1=0.0 d12=-15.0 z=3.38011340625
- **CHANGE_POINT** `ind_generation` value=2.689e+04 d1=0.0 d12=-14.0 z=3.3042419213483147
- **ROBUST_OUTLIER** `ind_demand` value=-1.086e+04 d1=0.0 d12=0.0 z=4.72142825
- **PERSISTENT_UP** `interconnector_net` value=-9598 d1=347.0 d12=1270.0 z=3.546815839679359
- **ROBUST_OUTLIER** `interconnector_net` value=-9598 d1=347.0 d12=1270.0 z=3.546815839679359
- **ROBUST_OUTLIER** `imbalance` value=9697 d1=0.0 d12=-15.0 z=3.38011340625
- **ROBUST_OUTLIER** `ind_generation` value=2.689e+04 d1=0.0 d12=-14.0 z=3.3042419213483147
- **CHANGE_POINT** `thermal_base` value=6850 d1=-80.0 d12=84.0 z=0.2389553564572426
- **CHANGE_POINT** `ccgt_gen` value=3511 d1=-81.0 d12=85.0 z=0.22916114098073556
- **CHANGE_POINT** `margin` value=3.824e+04 d1=0.0 d12=-19.0 z=-0.20669847177419354
- **REVERSAL** `wind_gen` value=1.589e+04 d1=59.0 d12=-38.0 z=-0.5428036559523809
- **ACCELERATION** `wind_gen` value=1.589e+04 d1=59.0 d12=-38.0 z=-0.5428036559523809
- **PERSISTENT_UP** `biomass_gen` value=815 d1=58.0 d12=123.0 z=-0.2750346553398058
- **REVERSAL** `thermal_base` value=6850 d1=-80.0 d12=84.0 z=0.2389553564572426

## Nearest historical live analogues

- `2026-09-19T04:22:41.594365Z` distance=0.071 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T04:26:53.312473Z` distance=0.071 → {'next30m_imbalance_delta': -44.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T04:31:06.739586Z` distance=0.071 → {'next30m_imbalance_delta': -44.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T04:35:21.377586Z` distance=0.071 → {'next30m_imbalance_delta': -44.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T04:39:35.411935Z` distance=0.071 → {'next30m_imbalance_delta': -44.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

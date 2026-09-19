# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T15:36:46.393130Z`  
Memory snapshots: **1532**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=607 d1=1.0 d12=20.0 z=87.6836675
- **PERSISTENT_UP** `biomass_gen` value=607 d1=1.0 d12=20.0 z=87.6836675
- **ROBUST_OUTLIER** `biomass_gen` value=607 d1=1.0 d12=20.0 z=87.6836675
- **CHANGE_POINT** `ccgt_gen` value=3670 d1=-56.0 d12=317.0 z=2.6539705380434784
- **CHANGE_POINT** `thermal_base` value=7001 d1=-56.0 d12=318.0 z=2.6355506957295374
- **PERSISTENT_UP** `ps_gen` value=44 d1=234.0 d12=303.0 z=4.184455827669903
- **ROBUST_OUTLIER** `ps_gen` value=44 d1=234.0 d12=303.0 z=4.184455827669903
- **CHANGE_POINT** `imbalance` value=-3172 d1=0.0 d12=58.0 z=0.6985786696428571
- **REVERSAL** `ccgt_gen` value=3670 d1=-56.0 d12=317.0 z=2.6539705380434784
- **REVERSAL** `thermal_base` value=7001 d1=-56.0 d12=318.0 z=2.6355506957295374
- **ACCELERATION** `thermal_base` value=7001 d1=-56.0 d12=318.0 z=2.6355506957295374
- **PERSISTENT_UP** `wind_gen` value=1.423e+04 d1=46.0 d12=807.0 z=-1.2611149348659005
- **PERSISTENT_UP** `interconnector_net` value=-2964 d1=50.0 d12=586.0 z=-1.0845615913621263
- **ACCELERATION** `interconnector_net` value=-2964 d1=50.0 d12=586.0 z=-1.0845615913621263
- **PERSISTENT_UP** `imbalance` value=-3172 d1=0.0 d12=58.0 z=0.6985786696428571

## Nearest historical live analogues

- `2026-09-19T14:21:11.929039Z` distance=0.037 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T14:25:23.497247Z` distance=0.037 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -57.0}
- `2026-09-19T14:29:36.625611Z` distance=0.037 → {'next30m_imbalance_delta': 56.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -57.0}
- `2026-09-19T14:33:49.934792Z` distance=0.037 → {'next30m_imbalance_delta': 56.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -57.0}
- `2026-09-19T14:38:01.634013Z` distance=0.037 → {'next30m_imbalance_delta': 56.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -57.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

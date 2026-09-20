# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T16:18:48.495639Z`  
Memory snapshots: **1883**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1918 d1=103.0 d12=813.0 z=448.872928625
- **PERSISTENT_UP** `biomass_gen` value=1918 d1=103.0 d12=813.0 z=448.872928625
- **ROBUST_OUTLIER** `biomass_gen` value=1918 d1=103.0 d12=813.0 z=448.872928625
- **CHANGE_POINT** `ccgt_gen` value=4308 d1=270.0 d12=1492.0 z=69.5271326081081
- **PERSISTENT_UP** `ccgt_gen` value=4308 d1=270.0 d12=1492.0 z=69.5271326081081
- **ROBUST_OUTLIER** `ccgt_gen` value=4308 d1=270.0 d12=1492.0 z=69.5271326081081
- **CHANGE_POINT** `thermal_base` value=7645 d1=271.0 d12=1492.0 z=62.84270353658537
- **PERSISTENT_UP** `thermal_base` value=7645 d1=271.0 d12=1492.0 z=62.84270353658537
- **ROBUST_OUTLIER** `thermal_base` value=7645 d1=271.0 d12=1492.0 z=62.84270353658537
- **CHANGE_POINT** `imbalance` value=-5166 d1=0.0 d12=-6.0 z=14.371820057692307
- **ROBUST_OUTLIER** `imbalance` value=-5166 d1=0.0 d12=-6.0 z=14.371820057692307
- **CHANGE_POINT** `interconnector_net` value=1.012e+04 d1=-2.0 d12=5046.0 z=6.687160017818768
- **REVERSAL** `interconnector_net` value=1.012e+04 d1=-2.0 d12=5046.0 z=6.687160017818768
- **ROBUST_OUTLIER** `interconnector_net` value=1.012e+04 d1=-2.0 d12=5046.0 z=6.687160017818768
- **CHANGE_POINT** `margin` value=3.592e+04 d1=0.0 d12=0.0 z=4.016279875

## Nearest historical live analogues

- `2026-09-20T15:23:40.822404Z` distance=0.000 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:54:10.136499Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:58:25.329493Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:02:37.176302Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:06:50.185709Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

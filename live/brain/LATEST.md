# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T16:06:14.004105Z`  
Memory snapshots: **1880**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1712 d1=74.0 d12=782.0 z=379.400484375
- **PERSISTENT_UP** `biomass_gen` value=1712 d1=74.0 d12=782.0 z=379.400484375
- **ROBUST_OUTLIER** `biomass_gen` value=1712 d1=74.0 d12=782.0 z=379.400484375
- **CHANGE_POINT** `ccgt_gen` value=3869 d1=-141.0 d12=1163.0 z=56.58005445714286
- **REVERSAL** `ccgt_gen` value=3869 d1=-141.0 d12=1163.0 z=56.58005445714286
- **ROBUST_OUTLIER** `ccgt_gen` value=3869 d1=-141.0 d12=1163.0 z=56.58005445714286
- **CHANGE_POINT** `thermal_base` value=7203 d1=-143.0 d12=1162.0 z=50.77697194871795
- **REVERSAL** `thermal_base` value=7203 d1=-143.0 d12=1162.0 z=50.77697194871795
- **ROBUST_OUTLIER** `thermal_base` value=7203 d1=-143.0 d12=1162.0 z=50.77697194871795
- **PERSISTENT_DOWN** `imbalance` value=-5166 d1=0.0 d12=-8.0 z=14.371820057692307
- **ROBUST_OUTLIER** `imbalance` value=-5166 d1=0.0 d12=-8.0 z=14.371820057692307
- **CHANGE_POINT** `interconnector_net` value=9674 d1=1225.0 d12=4680.0 z=6.757984614552238
- **PERSISTENT_UP** `interconnector_net` value=9674 d1=1225.0 d12=4680.0 z=6.757984614552238
- **ROBUST_OUTLIER** `interconnector_net` value=9674 d1=1225.0 d12=4680.0 z=6.757984614552238
- **ROBUST_OUTLIER** `ps_gen` value=-13 d1=2.0 d12=773.0 z=4.220378721428571

## Nearest historical live analogues

- `2026-09-20T14:54:10.136499Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:58:25.329493Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:02:37.176302Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:06:50.185709Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:11:00.797261Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

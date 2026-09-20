# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T16:10:25.342120Z`  
Memory snapshots: **1881**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1712 d1=0.0 d12=724.0 z=379.400484375
- **PERSISTENT_UP** `biomass_gen` value=1712 d1=0.0 d12=724.0 z=379.400484375
- **ROBUST_OUTLIER** `biomass_gen` value=1712 d1=0.0 d12=724.0 z=379.400484375
- **CHANGE_POINT** `ccgt_gen` value=3869 d1=0.0 d12=1140.0 z=56.58005445714286
- **ROBUST_OUTLIER** `ccgt_gen` value=3869 d1=0.0 d12=1140.0 z=56.58005445714286
- **CHANGE_POINT** `thermal_base` value=7203 d1=0.0 d12=1140.0 z=50.77697194871795
- **ROBUST_OUTLIER** `thermal_base` value=7203 d1=0.0 d12=1140.0 z=50.77697194871795
- **CHANGE_POINT** `imbalance` value=-5166 d1=0.0 d12=-8.0 z=14.371820057692307
- **ROBUST_OUTLIER** `imbalance` value=-5166 d1=0.0 d12=-8.0 z=14.371820057692307
- **PERSISTENT_UP** `interconnector_net` value=9674 d1=0.0 d12=4601.0 z=6.750428165113679
- **ROBUST_OUTLIER** `interconnector_net` value=9674 d1=0.0 d12=4601.0 z=6.750428165113679
- **CHANGE_POINT** `margin` value=3.592e+04 d1=0.0 d12=14.0 z=4.016279875
- **PERSISTENT_UP** `ps_gen` value=-13 d1=0.0 d12=541.0 z=4.220378721428571
- **ROBUST_OUTLIER** `ps_gen` value=-13 d1=0.0 d12=541.0 z=4.220378721428571
- **ROBUST_OUTLIER** `margin` value=3.592e+04 d1=0.0 d12=14.0 z=4.016279875

## Nearest historical live analogues

- `2026-09-20T14:54:10.136499Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:58:25.329493Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:02:37.176302Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:06:50.185709Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:11:00.797261Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

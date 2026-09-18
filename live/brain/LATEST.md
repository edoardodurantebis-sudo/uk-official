# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T02:50:00.919485Z`  
Memory snapshots: **1063**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.821e+04 d1=0.0 d12=1507.0 z=16.35155865357143
- **ROBUST_OUTLIER** `margin` value=3.821e+04 d1=0.0 d12=1507.0 z=16.35155865357143
- **CHANGE_POINT** `imbalance` value=1.018e+04 d1=0.0 d12=15.0 z=5.700099651960784
- **CHANGE_POINT** `ind_generation` value=2.699e+04 d1=0.0 d12=15.0 z=5.700099651960784
- **ROBUST_OUTLIER** `imbalance` value=1.018e+04 d1=0.0 d12=15.0 z=5.700099651960784
- **ROBUST_OUTLIER** `ind_generation` value=2.699e+04 d1=0.0 d12=15.0 z=5.700099651960784
- **CHANGE_POINT** `biomass_gen` value=1750 d1=0.0 d12=-188.0 z=-1.1732720861344539
- **CHANGE_POINT** `wind_gen` value=1.401e+04 d1=0.0 d12=-521.0 z=-0.9221425739740821
- **CHANGE_POINT** `thermal_base` value=6750 d1=0.0 d12=-258.0 z=-0.7469132697939262
- **CHANGE_POINT** `ccgt_gen` value=3420 d1=0.0 d12=-255.0 z=-0.7360673704883227
- **CHANGE_POINT** `ind_demand` value=-1.12e+04 d1=0.0 d12=18.0 z=-0.6438311250000001
- **PERSISTENT_DOWN** `nuclear_gen` value=3330 d1=0.0 d12=-3.0 z=1.3489795
- **ACCELERATION** `nuclear_gen` value=3330 d1=0.0 d12=-3.0 z=1.3489795
- **PERSISTENT_DOWN** `biomass_gen` value=1750 d1=0.0 d12=-188.0 z=-1.1732720861344539
- **PERSISTENT_DOWN** `wind_gen` value=1.401e+04 d1=0.0 d12=-521.0 z=-0.9221425739740821

## Nearest historical live analogues

- `2026-09-18T01:50:42.136685Z` distance=0.686 → {'next30m_imbalance_delta': 34.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:54:53.197905Z` distance=0.687 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:24:23.203201Z` distance=0.687 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:29:09.319659Z` distance=0.687 → {'next30m_imbalance_delta': 34.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:33:19.678341Z` distance=0.687 → {'next30m_imbalance_delta': 34.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

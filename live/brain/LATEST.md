# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T15:48:50.027434Z`  
Memory snapshots: **1876**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1319 d1=57.0 d12=631.0 z=246.8632485
- **PERSISTENT_UP** `biomass_gen` value=1319 d1=57.0 d12=631.0 z=246.8632485
- **ROBUST_OUTLIER** `biomass_gen` value=1319 d1=57.0 d12=631.0 z=246.8632485
- **CHANGE_POINT** `ccgt_gen` value=3657 d1=220.0 d12=1029.0 z=54.7642161532258
- **PERSISTENT_UP** `ccgt_gen` value=3657 d1=220.0 d12=1029.0 z=54.7642161532258
- **ROBUST_OUTLIER** `ccgt_gen` value=3657 d1=220.0 d12=1029.0 z=54.7642161532258
- **CHANGE_POINT** `thermal_base` value=6997 d1=226.0 d12=1039.0 z=50.15029670588235
- **PERSISTENT_UP** `thermal_base` value=6997 d1=226.0 d12=1039.0 z=50.15029670588235
- **ROBUST_OUTLIER** `thermal_base` value=6997 d1=226.0 d12=1039.0 z=50.15029670588235
- **CHANGE_POINT** `imbalance` value=-5160 d1=0.0 d12=-2.0 z=14.527471538461539
- **ROBUST_OUTLIER** `imbalance` value=-5160 d1=0.0 d12=-2.0 z=14.527471538461539
- **CHANGE_POINT** `interconnector_net` value=7945 d1=0.0 d12=6215.0 z=6.4162509362606235
- **PERSISTENT_UP** `interconnector_net` value=7945 d1=0.0 d12=6215.0 z=6.4162509362606235
- **ROBUST_OUTLIER** `interconnector_net` value=7945 d1=0.0 d12=6215.0 z=6.4162509362606235
- **PERSISTENT_UP** `ps_gen` value=-10 d1=0.0 d12=344.0 z=4.335070043689321

## Nearest historical live analogues

- `2026-09-20T14:54:10.136499Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T10:57:55.935414Z` distance=0.059 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:02:06.579348Z` distance=0.059 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:06:18.746524Z` distance=0.059 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:10:29.817646Z` distance=0.059 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

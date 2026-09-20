# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T15:53:00.632411Z`  
Memory snapshots: **1877**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1412 d1=93.0 d12=673.0 z=278.227021875
- **PERSISTENT_UP** `biomass_gen` value=1412 d1=93.0 d12=673.0 z=278.227021875
- **ROBUST_OUTLIER** `biomass_gen` value=1412 d1=93.0 d12=673.0 z=278.227021875
- **CHANGE_POINT** `ccgt_gen` value=3834 d1=177.0 d12=1157.0 z=62.46645394354839
- **PERSISTENT_UP** `ccgt_gen` value=3834 d1=177.0 d12=1157.0 z=62.46645394354839
- **ROBUST_OUTLIER** `ccgt_gen` value=3834 d1=177.0 d12=1157.0 z=62.46645394354839
- **CHANGE_POINT** `thermal_base` value=7174 d1=177.0 d12=1167.0 z=57.172925279411764
- **PERSISTENT_UP** `thermal_base` value=7174 d1=177.0 d12=1167.0 z=57.172925279411764
- **ROBUST_OUTLIER** `thermal_base` value=7174 d1=177.0 d12=1167.0 z=57.172925279411764
- **CHANGE_POINT** `imbalance` value=-5160 d1=0.0 d12=-2.0 z=14.527471538461539
- **ROBUST_OUTLIER** `imbalance` value=-5160 d1=0.0 d12=-2.0 z=14.527471538461539
- **CHANGE_POINT** `interconnector_net` value=7946 d1=1.0 d12=5242.0 z=6.39867031598063
- **PERSISTENT_UP** `interconnector_net` value=7946 d1=1.0 d12=5242.0 z=6.39867031598063
- **ROBUST_OUTLIER** `interconnector_net` value=7946 d1=1.0 d12=5242.0 z=6.39867031598063
- **CHANGE_POINT** `ps_gen` value=-12 d1=-2.0 d12=241.0 z=4.297835653381642

## Nearest historical live analogues

- `2026-09-20T14:54:10.136499Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:58:25.329493Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T10:57:55.935414Z` distance=0.060 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:02:06.579348Z` distance=0.060 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:06:18.746524Z` distance=0.060 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

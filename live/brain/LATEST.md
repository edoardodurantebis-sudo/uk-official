# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T15:32:06.593730Z`  
Memory snapshots: **1872**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1160 d1=55.0 d12=573.0 z=193.241313375
- **PERSISTENT_UP** `biomass_gen` value=1160 d1=55.0 d12=573.0 z=193.241313375
- **ROBUST_OUTLIER** `biomass_gen` value=1160 d1=55.0 d12=573.0 z=193.241313375
- **CHANGE_POINT** `ccgt_gen` value=3035 d1=219.0 d12=565.0 z=27.697595217741938
- **PERSISTENT_UP** `ccgt_gen` value=3035 d1=219.0 d12=565.0 z=27.697595217741938
- **ROBUST_OUTLIER** `ccgt_gen` value=3035 d1=219.0 d12=565.0 z=27.697595217741938
- **CHANGE_POINT** `thermal_base` value=6367 d1=214.0 d12=568.0 z=25.154500088235295
- **ROBUST_OUTLIER** `imbalance` value=-5160 d1=0.0 d12=490.0 z=25.675576483333334
- **PERSISTENT_UP** `thermal_base` value=6367 d1=214.0 d12=568.0 z=25.154500088235295
- **ROBUST_OUTLIER** `thermal_base` value=6367 d1=214.0 d12=568.0 z=25.154500088235295
- **CHANGE_POINT** `interconnector_net` value=7945 d1=2872.0 d12=6282.0 z=7.7414824528808595
- **PERSISTENT_UP** `interconnector_net` value=7945 d1=2872.0 d12=6282.0 z=7.7414824528808595
- **ACCELERATION** `interconnector_net` value=7945 d1=2872.0 d12=6282.0 z=7.7414824528808595
- **ROBUST_OUTLIER** `interconnector_net` value=7945 d1=2872.0 d12=6282.0 z=7.7414824528808595
- **CHANGE_POINT** `margin` value=3.592e+04 d1=0.0 d12=535.0 z=4.016279875

## Nearest historical live analogues

- `2026-09-20T10:57:55.935414Z` distance=0.059 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:02:06.579348Z` distance=0.059 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:06:18.746524Z` distance=0.059 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:10:29.817646Z` distance=0.059 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:14:40.539694Z` distance=0.059 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

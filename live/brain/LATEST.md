# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T10:50:23.779495Z`  
Memory snapshots: **1177**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1082 d1=0.0 d12=-568.0 z=-45.570213734375
- **PERSISTENT_DOWN** `biomass_gen` value=1082 d1=0.0 d12=-568.0 z=-45.570213734375
- **ROBUST_OUTLIER** `biomass_gen` value=1082 d1=0.0 d12=-568.0 z=-45.570213734375
- **CHANGE_POINT** `imbalance` value=7078 d1=0.0 d12=-723.0 z=-4.065062984644913
- **CHANGE_POINT** `margin` value=3.635e+04 d1=0.0 d12=189.0 z=-3.968248029166667
- **CHANGE_POINT** `ind_demand` value=-1.38e+04 d1=0.0 d12=-607.0 z=-2.4560483652826854
- **CHANGE_POINT** `ind_generation` value=2.676e+04 d1=0.0 d12=-135.0 z=-2.42063072715736
- **ROBUST_OUTLIER** `imbalance` value=7078 d1=0.0 d12=-723.0 z=-4.065062984644913
- **ROBUST_OUTLIER** `margin` value=3.635e+04 d1=0.0 d12=189.0 z=-3.968248029166667
- **CHANGE_POINT** `thermal_base` value=6211 d1=0.0 d12=-153.0 z=-1.1653541536121674
- **CHANGE_POINT** `ccgt_gen` value=2876 d1=0.0 d12=-156.0 z=-1.1639560959346504
- **CHANGE_POINT** `interconnector_net` value=5704 d1=0.0 d12=878.0 z=0.8441030380442971
- **PERSISTENT_DOWN** `thermal_base` value=6211 d1=0.0 d12=-153.0 z=-1.1653541536121674
- **ACCELERATION** `thermal_base` value=6211 d1=0.0 d12=-153.0 z=-1.1653541536121674
- **PERSISTENT_DOWN** `ccgt_gen` value=2876 d1=0.0 d12=-156.0 z=-1.1639560959346504

## Nearest historical live analogues

- `2026-09-18T09:51:41.499535Z` distance=0.743 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:55:54.580890Z` distance=0.743 → {'next30m_imbalance_delta': -723.0, 'next30m_margin_delta': 189.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:21:34.020078Z` distance=0.746 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:25:46.604177Z` distance=0.746 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:30:05.383319Z` distance=0.746 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

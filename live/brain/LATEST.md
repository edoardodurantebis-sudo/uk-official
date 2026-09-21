# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T11:11:37.732087Z`  
Memory snapshots: **2151**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=0.0 d12=568.0 z=14.735006846153848
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=568.0 z=14.735006846153848
- **CHANGE_POINT** `nuclear_gen` value=3516 d1=-3.0 d12=22.0 z=2.9677549
- **CHANGE_POINT** `margin` value=3.65e+04 d1=0.0 d12=-3324.0 z=-1.6940672790697675
- **REVERSAL** `ccgt_gen` value=6722 d1=39.0 d12=-326.0 z=-3.5924950514184397
- **ROBUST_OUTLIER** `ccgt_gen` value=6722 d1=39.0 d12=-326.0 z=-3.5924950514184397
- **REVERSAL** `thermal_base` value=1.024e+04 d1=36.0 d12=-304.0 z=-3.3170734138627185
- **ROBUST_OUTLIER** `thermal_base` value=1.024e+04 d1=36.0 d12=-304.0 z=-3.3170734138627185
- **CHANGE_POINT** `residual_proxy` value=1.218e+04 d1=0.0 d12=1462.0 z=1.2135229663561076
- **CHANGE_POINT** `interconnector_net` value=1.124e+04 d1=-29.0 d12=427.0 z=0.9697290355871886
- **REVERSAL** `nuclear_gen` value=3516 d1=-3.0 d12=22.0 z=2.9677549
- **ACCELERATION** `nuclear_gen` value=3516 d1=-3.0 d12=22.0 z=2.9677549
- **CHANGE_POINT** `imbalance` value=-3871 d1=0.0 d12=-4440.0 z=-0.5238932564276049
- **CHANGE_POINT** `ind_generation` value=1.774e+04 d1=0.0 d12=-3991.0 z=-0.11899781625375375
- **CHANGE_POINT** `biomass_gen` value=3015 d1=-1.0 d12=65.0 z=0.0

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.508 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.508 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.508 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.508 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.508 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

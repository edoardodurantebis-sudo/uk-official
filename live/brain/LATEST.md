# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T11:20:04.554808Z`  
Memory snapshots: **2153**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=0.0 d12=585.0 z=14.735006846153848
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=585.0 z=14.735006846153848
- **CHANGE_POINT** `nuclear_gen` value=3516 d1=0.0 d12=23.0 z=2.83285695
- **CHANGE_POINT** `margin` value=3.65e+04 d1=0.0 d12=-4517.0 z=-1.6940672790697675
- **ROBUST_OUTLIER** `ccgt_gen` value=6722 d1=0.0 d12=-254.0 z=-3.5924950514184397
- **ROBUST_OUTLIER** `thermal_base` value=1.024e+04 d1=0.0 d12=-231.0 z=-3.3170734138627185
- **CHANGE_POINT** `residual_proxy` value=1.218e+04 d1=0.0 d12=1462.0 z=1.2135229663561076
- **CHANGE_POINT** `interconnector_net` value=1.124e+04 d1=0.0 d12=401.0 z=0.9769037448359659
- **CHANGE_POINT** `imbalance` value=-3871 d1=0.0 d12=-7439.0 z=-0.5238932564276049
- **CHANGE_POINT** `ind_generation` value=1.774e+04 d1=0.0 d12=-6990.0 z=-0.12127397953328233
- **CHANGE_POINT** `biomass_gen` value=3015 d1=0.0 d12=48.0 z=0.0
- **REVERSAL** `ts_demand_forecast` value=2.15e+04 d1=-104.0 d12=345.0 z=1.7110217922794118

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.507 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.507 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.507 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.507 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.507 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

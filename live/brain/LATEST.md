# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T11:12:04.755936Z`  
Memory snapshots: **1469**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.675e+04 d1=0.0 d12=-9313.0 z=-151.64028446111112
- **ROBUST_OUTLIER** `ind_generation` value=1.675e+04 d1=0.0 d12=-9313.0 z=-151.64028446111112
- **CHANGE_POINT** `imbalance` value=-3378 d1=0.0 d12=-10512.0 z=-11.691155666666669
- **ROBUST_OUTLIER** `imbalance` value=-3378 d1=0.0 d12=-10512.0 z=-11.691155666666669
- **ROBUST_OUTLIER** `residual_proxy` value=1.298e+04 d1=0.0 d12=4022.0 z=8.057219948369566
- **ROBUST_OUTLIER** `demand_forecast` value=1.963e+04 d1=0.0 d12=3691.0 z=6.81345219590164
- **CHANGE_POINT** `margin` value=3.555e+04 d1=0.0 d12=-959.0 z=-2.1281940228670253
- **CHANGE_POINT** `ps_gen` value=-809 d1=-57.0 d12=-116.0 z=-1.5254282953586498
- **CHANGE_POINT** `biomass_gen` value=474 d1=2.0 d12=-3.0 z=-1.0550946803571428
- **CHANGE_POINT** `ind_demand` value=-1.178e+04 d1=0.0 d12=1442.0 z=0.1766238536906854
- **PERSISTENT_DOWN** `thermal_base` value=6104 d1=-5.0 d12=-189.0 z=-2.1028209852941178
- **PERSISTENT_DOWN** `ccgt_gen` value=2773 d1=-7.0 d12=-193.0 z=-2.060940902777778
- **PERSISTENT_DOWN** `ps_gen` value=-809 d1=-57.0 d12=-116.0 z=-1.5254282953586498
- **REVERSAL** `biomass_gen` value=474 d1=2.0 d12=-3.0 z=-1.0550946803571428
- **ACCELERATION** `biomass_gen` value=474 d1=2.0 d12=-3.0 z=-1.0550946803571428

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.571 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.571 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.571 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.571 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.571 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

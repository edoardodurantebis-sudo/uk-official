# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T11:37:21.494450Z`  
Memory snapshots: **1475**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.678e+04 d1=0.0 d12=-9288.0 z=-151.26556793333333
- **ROBUST_OUTLIER** `ind_generation` value=1.678e+04 d1=0.0 d12=-9288.0 z=-151.26556793333333
- **CHANGE_POINT** `imbalance` value=-3354 d1=0.0 d12=-10488.0 z=-10.624078292948719
- **ROBUST_OUTLIER** `imbalance` value=-3354 d1=0.0 d12=-10488.0 z=-10.624078292948719
- **CHANGE_POINT** `ps_gen` value=-935 d1=-2.0 d12=-241.0 z=-2.2145746791666667
- **ROBUST_OUTLIER** `residual_proxy` value=1.298e+04 d1=0.0 d12=3691.0 z=3.6455618127049183
- **ROBUST_OUTLIER** `demand_forecast` value=1.963e+04 d1=0.0 d12=3691.0 z=3.40672609795082
- **PERSISTENT_DOWN** `ps_gen` value=-935 d1=-2.0 d12=-241.0 z=-2.2145746791666667
- **CHANGE_POINT** `ind_demand` value=-1.178e+04 d1=0.0 d12=1442.0 z=0.17693481117957746
- **PERSISTENT_DOWN** `nuclear_gen` value=3330 d1=-4.0 d12=-3.0 z=-0.8993196666666666
- **ACCELERATION** `nuclear_gen` value=3330 d1=-4.0 d12=-3.0 z=-0.8993196666666666
- **REVERSAL** `wind_gen` value=1.566e+04 d1=31.0 d12=-202.0 z=-0.8847718485294118
- **ACCELERATION** `wind_gen` value=1.566e+04 d1=31.0 d12=-202.0 z=-0.8847718485294118
- **PERSISTENT_UP** `biomass_gen` value=478 d1=1.0 d12=4.0 z=-0.6922820455635492
- **REVERSAL** `interconnector_net` value=-1551 d1=-7.0 d12=202.0 z=0.1563225080186239

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.325 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.325 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.325 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.325 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.325 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

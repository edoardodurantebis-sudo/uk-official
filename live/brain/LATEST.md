# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T11:41:32.574175Z`  
Memory snapshots: **1476**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.678e+04 d1=0.0 d12=-9288.0 z=-151.26556793333333
- **ROBUST_OUTLIER** `ind_generation` value=1.678e+04 d1=0.0 d12=-9288.0 z=-151.26556793333333
- **CHANGE_POINT** `imbalance` value=-3354 d1=0.0 d12=-10488.0 z=-10.624078292948719
- **ROBUST_OUTLIER** `imbalance` value=-3354 d1=0.0 d12=-10488.0 z=-10.624078292948719
- **CHANGE_POINT** `ps_gen` value=-937 d1=-2.0 d12=-242.0 z=-2.225816175
- **ROBUST_OUTLIER** `demand_forecast` value=1.963e+04 d1=0.0 d12=0.0 z=3.40672609795082
- **ROBUST_OUTLIER** `residual_proxy` value=1.298e+04 d1=0.0 d12=0.0 z=3.331524652808989
- **CHANGE_POINT** `margin` value=3.666e+04 d1=0.0 d12=149.0 z=-0.5379366104294478
- **PERSISTENT_DOWN** `ps_gen` value=-937 d1=-2.0 d12=-242.0 z=-2.225816175
- **CHANGE_POINT** `ind_demand` value=-1.178e+04 d1=0.0 d12=1442.0 z=0.17693481117957746
- **REVERSAL** `thermal_base` value=6119 d1=3.0 d12=-88.0 z=-2.036694539215686
- **REVERSAL** `ccgt_gen` value=2790 d1=4.0 d12=-81.0 z=-1.9859975972222221
- **PERSISTENT_DOWN** `nuclear_gen` value=3329 d1=-1.0 d12=-7.0 z=-1.1241495833333335
- **ACCELERATION** `nuclear_gen` value=3329 d1=-1.0 d12=-7.0 z=-1.1241495833333335
- **PERSISTENT_DOWN** `wind_gen` value=1.564e+04 d1=-19.0 d12=-243.0 z=-0.9679118446327682

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.325 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.325 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.325 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.325 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.325 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

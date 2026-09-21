# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T11:03:12.814990Z`  
Memory snapshots: **2149**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=0.0 d12=568.0 z=14.735006846153848
- **PERSISTENT_UP** `ind_demand` value=-1.224e+04 d1=0.0 d12=568.0 z=14.735006846153848
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=568.0 z=14.735006846153848
- **REVERSAL** `ccgt_gen` value=6651 d1=33.0 d12=-545.0 z=-3.728349724468085
- **ROBUST_OUTLIER** `ccgt_gen` value=6651 d1=33.0 d12=-545.0 z=-3.728349724468085
- **CHANGE_POINT** `margin` value=3.65e+04 d1=0.0 d12=-3324.0 z=-1.6940672790697675
- **REVERSAL** `thermal_base` value=1.016e+04 d1=39.0 d12=-533.0 z=-3.458689027590848
- **ROBUST_OUTLIER** `thermal_base` value=1.016e+04 d1=39.0 d12=-533.0 z=-3.458689027590848
- **CHANGE_POINT** `residual_proxy` value=1.218e+04 d1=0.0 d12=1462.0 z=1.2135229663561076
- **CHANGE_POINT** `interconnector_net` value=1.128e+04 d1=150.0 d12=526.0 z=1.04840900856974
- **CHANGE_POINT** `imbalance` value=-3871 d1=0.0 d12=-4440.0 z=-0.5238932564276049
- **PERSISTENT_UP** `ts_demand_forecast` value=2.161e+04 d1=0.0 d12=449.0 z=2.2268080716911767
- **CHANGE_POINT** `ind_generation` value=1.774e+04 d1=0.0 d12=-3991.0 z=-0.11899781625375375
- **PERSISTENT_UP** `nuclear_gen` value=3509 d1=6.0 d12=12.0 z=2.02346925
- **ACCELERATION** `nuclear_gen` value=3509 d1=6.0 d12=12.0 z=2.02346925

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.508 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.508 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.508 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.508 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.508 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

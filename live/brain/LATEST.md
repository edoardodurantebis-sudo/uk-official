# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T10:58:55.909932Z`  
Memory snapshots: **2148**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=0.0 d12=568.0 z=14.735006846153848
- **PERSISTENT_UP** `ind_demand` value=-1.224e+04 d1=0.0 d12=568.0 z=14.735006846153848
- **ACCELERATION** `ind_demand` value=-1.224e+04 d1=0.0 d12=568.0 z=14.735006846153848
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=568.0 z=14.735006846153848
- **REVERSAL** `ccgt_gen` value=6618 d1=15.0 d12=-677.0 z=-3.791493445744681
- **ACCELERATION** `ccgt_gen` value=6618 d1=15.0 d12=-677.0 z=-3.791493445744681
- **ROBUST_OUTLIER** `ccgt_gen` value=6618 d1=15.0 d12=-677.0 z=-3.791493445744681
- **REVERSAL** `thermal_base` value=1.012e+04 d1=13.0 d12=-665.0 z=-3.5294968344549122
- **ACCELERATION** `thermal_base` value=1.012e+04 d1=13.0 d12=-665.0 z=-3.5294968344549122
- **ROBUST_OUTLIER** `thermal_base` value=1.012e+04 d1=13.0 d12=-665.0 z=-3.5294968344549122
- **CHANGE_POINT** `residual_proxy` value=1.218e+04 d1=0.0 d12=1462.0 z=1.2135229663561076
- **CHANGE_POINT** `interconnector_net` value=1.114e+04 d1=27.0 d12=401.0 z=0.8090691688311688
- **CHANGE_POINT** `imbalance` value=-3871 d1=0.0 d12=-4440.0 z=-0.5238932564276049
- **PERSISTENT_UP** `ts_demand_forecast` value=2.161e+04 d1=0.0 d12=449.0 z=2.2268080716911767
- **ACCELERATION** `ts_demand_forecast` value=2.161e+04 d1=0.0 d12=449.0 z=2.2268080716911767

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.507 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.507 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.507 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.507 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.507 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

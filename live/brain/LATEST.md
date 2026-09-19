# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T08:05:42.408180Z`  
Memory snapshots: **1425**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.208e+04 d1=0.0 d12=-726.0 z=-67.2803525625
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-726.0 z=-67.2803525625
- **CHANGE_POINT** `margin` value=3.703e+04 d1=0.0 d12=-1004.0 z=-26.4948004921875
- **ROBUST_OUTLIER** `margin` value=3.703e+04 d1=0.0 d12=-1004.0 z=-26.4948004921875
- **PERSISTENT_DOWN** `ps_gen` value=-685 d1=0.0 d12=-493.0 z=-24.1130085625
- **ACCELERATION** `ps_gen` value=-685 d1=0.0 d12=-493.0 z=-24.1130085625
- **ROBUST_OUTLIER** `ps_gen` value=-685 d1=0.0 d12=-493.0 z=-24.1130085625
- **CHANGE_POINT** `interconnector_net` value=-3224 d1=0.0 d12=2707.0 z=20.778069012024048
- **PERSISTENT_UP** `interconnector_net` value=-3224 d1=0.0 d12=2707.0 z=20.778069012024048
- **ROBUST_OUTLIER** `interconnector_net` value=-3224 d1=0.0 d12=2707.0 z=20.778069012024048
- **ROBUST_OUTLIER** `residual_proxy` value=1.219e+04 d1=0.0 d12=2510.0 z=10.71499539556962
- **CHANGE_POINT** `imbalance` value=8458 d1=0.0 d12=-1020.0 z=-2.902867278481013
- **CHANGE_POINT** `ind_generation` value=2.687e+04 d1=0.0 d12=-38.0 z=-0.1686224375
- **CHANGE_POINT** `ts_demand_forecast` value=1.956e+04 d1=0.0 d12=2131.0 z=None
- **PERSISTENT_DOWN** `biomass_gen` value=806 d1=0.0 d12=-172.0 z=-0.0366877269874477

## Nearest historical live analogues

- `2026-09-19T06:54:14.045129Z` distance=0.849 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T06:58:26.669758Z` distance=0.849 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:02:41.681401Z` distance=0.849 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:06:54.491036Z` distance=0.849 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:11:05.764149Z` distance=0.849 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

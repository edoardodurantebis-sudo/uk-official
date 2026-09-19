# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T08:14:05.838743Z`  
Memory snapshots: **1427**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ts_demand_forecast` value=1.956e+04 d1=0.0 d12=1148.0 z=398.960687125
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.956e+04 d1=0.0 d12=1148.0 z=398.960687125
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=0.0 z=-57.668873625
- **CHANGE_POINT** `margin` value=3.703e+04 d1=0.0 d12=0.0 z=-26.4948004921875
- **ROBUST_OUTLIER** `margin` value=3.703e+04 d1=0.0 d12=0.0 z=-26.4948004921875
- **PERSISTENT_UP** `interconnector_net` value=-1739 d1=431.0 d12=4230.0 z=24.792567123246492
- **ROBUST_OUTLIER** `interconnector_net` value=-1739 d1=431.0 d12=4230.0 z=24.792567123246492
- **ROBUST_OUTLIER** `residual_proxy` value=1.219e+04 d1=0.0 d12=2510.0 z=10.71499539556962
- **REVERSAL** `ps_gen` value=-592 d1=97.0 d12=-174.0 z=-8.431121875
- **ACCELERATION** `ps_gen` value=-592 d1=97.0 d12=-174.0 z=-8.431121875
- **ROBUST_OUTLIER** `ps_gen` value=-592 d1=97.0 d12=-174.0 z=-8.431121875
- **CHANGE_POINT** `imbalance` value=8458 d1=0.0 d12=0.0 z=-2.902867278481013
- **CHANGE_POINT** `ind_generation` value=2.687e+04 d1=0.0 d12=0.0 z=-0.24526900000000001
- **PERSISTENT_DOWN** `wind_gen` value=1.543e+04 d1=-109.0 d12=-272.0 z=-1.839335549703264
- **PERSISTENT_DOWN** `nuclear_gen` value=3331 d1=-2.0 d12=-10.0 z=-1.5738094166666665

## Nearest historical live analogues

- `2026-09-19T07:19:33.283836Z` distance=0.782 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T06:54:14.045129Z` distance=0.849 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T06:58:26.669758Z` distance=0.849 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:02:41.681401Z` distance=0.849 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:06:54.491036Z` distance=0.849 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

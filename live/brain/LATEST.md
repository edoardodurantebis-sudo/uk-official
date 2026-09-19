# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T07:53:08.075404Z`  
Memory snapshots: **1422**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.208e+04 d1=0.0 d12=-726.0 z=-67.2803525625
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-726.0 z=-67.2803525625
- **CHANGE_POINT** `margin` value=3.703e+04 d1=0.0 d12=-1004.0 z=-26.4948004921875
- **ROBUST_OUTLIER** `margin` value=3.703e+04 d1=0.0 d12=-1004.0 z=-26.4948004921875
- **CHANGE_POINT** `interconnector_net` value=-3866 d1=11.0 d12=3845.0 z=19.04250821242485
- **REVERSAL** `ps_gen` value=-422 d1=1.0 d12=-48.0 z=20.2346925
- **ROBUST_OUTLIER** `ps_gen` value=-422 d1=1.0 d12=-48.0 z=20.2346925
- **PERSISTENT_UP** `interconnector_net` value=-3866 d1=11.0 d12=3845.0 z=19.04250821242485
- **ROBUST_OUTLIER** `interconnector_net` value=-3866 d1=11.0 d12=3845.0 z=19.04250821242485
- **PERSISTENT_UP** `residual_proxy` value=1.219e+04 d1=0.0 d12=2510.0 z=10.71499539556962
- **ACCELERATION** `residual_proxy` value=1.219e+04 d1=0.0 d12=2510.0 z=10.71499539556962
- **ROBUST_OUTLIER** `residual_proxy` value=1.219e+04 d1=0.0 d12=2510.0 z=10.71499539556962
- **CHANGE_POINT** `imbalance` value=8458 d1=0.0 d12=-1020.0 z=-2.902867278481013
- **CHANGE_POINT** `ind_generation` value=2.687e+04 d1=0.0 d12=-38.0 z=-0.1686224375
- **REVERSAL** `wind_gen` value=1.572e+04 d1=8.0 d12=-89.0 z=-0.9580219947780678

## Nearest historical live analogues

- `2026-09-19T06:54:14.045129Z` distance=0.849 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T06:58:26.669758Z` distance=0.849 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:19:46.344592Z` distance=1.065 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:23:56.984916Z` distance=1.066 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:28:08.328313Z` distance=1.066 → {'next30m_imbalance_delta': -29.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

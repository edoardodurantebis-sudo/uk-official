# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T07:48:55.634175Z`  
Memory snapshots: **1421**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.208e+04 d1=0.0 d12=-726.0 z=-67.2803525625
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-726.0 z=-67.2803525625
- **CHANGE_POINT** `margin` value=3.703e+04 d1=0.0 d12=-1004.0 z=-26.4948004921875
- **ROBUST_OUTLIER** `margin` value=3.703e+04 d1=0.0 d12=-1004.0 z=-26.4948004921875
- **CHANGE_POINT** `interconnector_net` value=-3877 d1=26.0 d12=4477.0 z=19.012771189378757
- **PERSISTENT_DOWN** `ps_gen` value=-423 d1=-2.0 d12=-101.0 z=20.0660700625
- **ROBUST_OUTLIER** `ps_gen` value=-423 d1=-2.0 d12=-101.0 z=20.0660700625
- **PERSISTENT_UP** `interconnector_net` value=-3877 d1=26.0 d12=4477.0 z=19.012771189378757
- **ROBUST_OUTLIER** `interconnector_net` value=-3877 d1=26.0 d12=4477.0 z=19.012771189378757
- **PERSISTENT_UP** `residual_proxy` value=1.219e+04 d1=2510.0 d12=2510.0 z=10.71499539556962
- **ACCELERATION** `residual_proxy` value=1.219e+04 d1=2510.0 d12=2510.0 z=10.71499539556962
- **ROBUST_OUTLIER** `residual_proxy` value=1.219e+04 d1=2510.0 d12=2510.0 z=10.71499539556962
- **CHANGE_POINT** `imbalance` value=8458 d1=0.0 d12=-1020.0 z=-2.902867278481013
- **CHANGE_POINT** `ind_generation` value=2.687e+04 d1=0.0 d12=-38.0 z=-0.1686224375
- **REVERSAL** `wind_gen` value=1.571e+04 d1=19.0 d12=-142.0 z=-1.028731051061008

## Nearest historical live analogues

- `2026-09-19T06:54:14.045129Z` distance=0.849 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:19:46.344592Z` distance=1.062 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:23:56.984916Z` distance=1.063 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:28:08.328313Z` distance=1.063 → {'next30m_imbalance_delta': -29.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:32:19.562106Z` distance=1.063 → {'next30m_imbalance_delta': -29.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

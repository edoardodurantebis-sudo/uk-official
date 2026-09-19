# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T07:57:20.386172Z`  
Memory snapshots: **1423**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.208e+04 d1=0.0 d12=-726.0 z=-67.2803525625
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-726.0 z=-67.2803525625
- **CHANGE_POINT** `margin` value=3.703e+04 d1=0.0 d12=-1004.0 z=-26.4948004921875
- **ROBUST_OUTLIER** `margin` value=3.703e+04 d1=0.0 d12=-1004.0 z=-26.4948004921875
- **CHANGE_POINT** `interconnector_net` value=-3843 d1=23.0 d12=2634.0 z=19.104685624248496
- **REVERSAL** `ps_gen` value=-421 d1=1.0 d12=-123.0 z=20.4033149375
- **ROBUST_OUTLIER** `ps_gen` value=-421 d1=1.0 d12=-123.0 z=20.4033149375
- **PERSISTENT_UP** `interconnector_net` value=-3843 d1=23.0 d12=2634.0 z=19.104685624248496
- **ROBUST_OUTLIER** `interconnector_net` value=-3843 d1=23.0 d12=2634.0 z=19.104685624248496
- **PERSISTENT_UP** `residual_proxy` value=1.219e+04 d1=0.0 d12=2510.0 z=10.71499539556962
- **ROBUST_OUTLIER** `residual_proxy` value=1.219e+04 d1=0.0 d12=2510.0 z=10.71499539556962
- **CHANGE_POINT** `imbalance` value=8458 d1=0.0 d12=-1020.0 z=-2.902867278481013
- **CHANGE_POINT** `ind_generation` value=2.687e+04 d1=0.0 d12=-38.0 z=-0.1686224375
- **REVERSAL** `nuclear_gen` value=3335 d1=-6.0 d12=1.0 z=-0.6744897499999999
- **ACCELERATION** `nuclear_gen` value=3335 d1=-6.0 d12=1.0 z=-0.6744897499999999

## Nearest historical live analogues

- `2026-09-19T06:54:14.045129Z` distance=0.849 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T06:58:26.669758Z` distance=0.849 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:02:41.681401Z` distance=0.849 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:19:46.344592Z` distance=1.062 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:23:56.984916Z` distance=1.063 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

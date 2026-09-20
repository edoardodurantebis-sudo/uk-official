# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T11:44:05.611277Z`  
Memory snapshots: **1818**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=41.6497420625
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=41.6497420625
- **CHANGE_POINT** `ind_generation` value=1.537e+04 d1=0.0 d12=-654.0 z=4.878400409999999
- **CHANGE_POINT** `margin` value=3.578e+04 d1=0.0 d12=-13.0 z=-3.503319895522388
- **ROBUST_OUTLIER** `ind_generation` value=1.537e+04 d1=0.0 d12=-654.0 z=4.878400409999999
- **CHANGE_POINT** `wind_gen` value=1.283e+04 d1=-48.0 d12=-950.0 z=-2.535151129310345
- **CHANGE_POINT** `residual_proxy` value=1.824e+04 d1=0.0 d12=0.0 z=1.6756600777108435
- **ROBUST_OUTLIER** `margin` value=3.578e+04 d1=0.0 d12=-13.0 z=-3.503319895522388
- **CHANGE_POINT** `imbalance` value=-5732 d1=0.0 d12=-1592.0 z=1.4778741380890053
- **CHANGE_POINT** `nuclear_gen` value=3333 d1=1.0 d12=-7.0 z=-1.0117346249999999
- **CHANGE_POINT** `ps_gen` value=-663 d1=2.0 d12=260.0 z=0.9591368004587156
- **CHANGE_POINT** `biomass_gen` value=585 d1=-1.0 d12=-2.0 z=-0.6975711482889734
- **PERSISTENT_DOWN** `wind_gen` value=1.283e+04 d1=-48.0 d12=-950.0 z=-2.535151129310345
- **REVERSAL** `nuclear_gen` value=3333 d1=1.0 d12=-7.0 z=-1.0117346249999999
- **PERSISTENT_UP** `ps_gen` value=-663 d1=2.0 d12=260.0 z=0.9591368004587156

## Nearest historical live analogues

- `2026-09-20T04:50:36.902238Z` distance=0.749 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:54:47.005275Z` distance=0.749 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:58:57.948602Z` distance=0.749 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:03:10.294370Z` distance=0.749 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:07:21.689505Z` distance=0.749 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 161.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

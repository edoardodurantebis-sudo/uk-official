# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T11:35:41.173966Z`  
Memory snapshots: **1816**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=41.6497420625
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=41.6497420625
- **CHANGE_POINT** `ind_generation` value=1.537e+04 d1=0.0 d12=-654.0 z=13.830191696261682
- **ROBUST_OUTLIER** `ind_generation` value=1.537e+04 d1=0.0 d12=-654.0 z=13.830191696261682
- **CHANGE_POINT** `margin` value=3.578e+04 d1=0.0 d12=-3998.0 z=-7.289516552795031
- **ROBUST_OUTLIER** `margin` value=3.578e+04 d1=0.0 d12=-3998.0 z=-7.289516552795031
- **CHANGE_POINT** `wind_gen` value=1.288e+04 d1=-235.0 d12=-1051.0 z=-2.613351952412281
- **CHANGE_POINT** `imbalance` value=-5732 d1=0.0 d12=-1592.0 z=2.1894651697819314
- **CHANGE_POINT** `nuclear_gen` value=3332 d1=1.0 d12=-3.0 z=-1.3489795
- **CHANGE_POINT** `ps_gen` value=-665 d1=-1.0 d12=262.0 z=0.9467608417431193
- **PERSISTENT_DOWN** `wind_gen` value=1.288e+04 d1=-235.0 d12=-1051.0 z=-2.613351952412281
- **REVERSAL** `nuclear_gen` value=3332 d1=1.0 d12=-3.0 z=-1.3489795
- **ACCELERATION** `nuclear_gen` value=3332 d1=1.0 d12=-3.0 z=-1.3489795
- **REVERSAL** `ps_gen` value=-665 d1=-1.0 d12=262.0 z=0.9467608417431193
- **REVERSAL** `thermal_base` value=5730 d1=1.0 d12=-115.0 z=-0.8563574544939576

## Nearest historical live analogues

- `2026-09-20T04:50:36.902238Z` distance=0.749 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:54:47.005275Z` distance=0.749 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:58:57.948602Z` distance=0.749 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:03:10.294370Z` distance=0.749 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:07:21.689505Z` distance=0.749 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 161.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

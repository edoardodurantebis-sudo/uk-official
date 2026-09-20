# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T11:27:16.047953Z`  
Memory snapshots: **1814**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=41.6497420625
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=41.6497420625
- **CHANGE_POINT** `ind_generation` value=1.537e+04 d1=14.0 d12=-654.0 z=13.830191696261682
- **REVERSAL** `ind_generation` value=1.537e+04 d1=14.0 d12=-654.0 z=13.830191696261682
- **ROBUST_OUTLIER** `ind_generation` value=1.537e+04 d1=14.0 d12=-654.0 z=13.830191696261682
- **CHANGE_POINT** `margin` value=3.578e+04 d1=0.0 d12=-3998.0 z=-7.289516552795031
- **PERSISTENT_DOWN** `margin` value=3.578e+04 d1=0.0 d12=-3998.0 z=-7.289516552795031
- **ROBUST_OUTLIER** `margin` value=3.578e+04 d1=0.0 d12=-3998.0 z=-7.289516552795031
- **CHANGE_POINT** `wind_gen` value=1.325e+04 d1=-40.0 d12=-709.0 z=-3.4794010888746802
- **CHANGE_POINT** `nuclear_gen` value=3328 d1=-3.0 d12=-5.0 z=-2.697959
- **CHANGE_POINT** `imbalance` value=-5732 d1=14.0 d12=-1592.0 z=2.1894651697819314
- **PERSISTENT_DOWN** `wind_gen` value=1.325e+04 d1=-40.0 d12=-709.0 z=-3.4794010888746802
- **ROBUST_OUTLIER** `wind_gen` value=1.325e+04 d1=-40.0 d12=-709.0 z=-3.4794010888746802
- **CHANGE_POINT** `ps_gen` value=-664 d1=-2.0 d12=262.0 z=0.9529488211009174
- **PERSISTENT_DOWN** `nuclear_gen` value=3328 d1=-3.0 d12=-5.0 z=-2.697959

## Nearest historical live analogues

- `2026-09-20T04:50:36.902238Z` distance=0.758 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:54:47.005275Z` distance=0.758 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:58:57.948602Z` distance=0.758 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:03:10.294370Z` distance=0.758 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:07:21.689505Z` distance=0.758 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 161.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

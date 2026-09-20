# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T11:31:27.990762Z`  
Memory snapshots: **1815**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=41.6497420625
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=41.6497420625
- **CHANGE_POINT** `ind_generation` value=1.537e+04 d1=0.0 d12=-654.0 z=13.830191696261682
- **ROBUST_OUTLIER** `ind_generation` value=1.537e+04 d1=0.0 d12=-654.0 z=13.830191696261682
- **CHANGE_POINT** `margin` value=3.578e+04 d1=0.0 d12=-3998.0 z=-7.289516552795031
- **PERSISTENT_DOWN** `margin` value=3.578e+04 d1=0.0 d12=-3998.0 z=-7.289516552795031
- **ROBUST_OUTLIER** `margin` value=3.578e+04 d1=0.0 d12=-3998.0 z=-7.289516552795031
- **CHANGE_POINT** `wind_gen` value=1.311e+04 d1=-138.0 d12=-816.0 z=-2.947690964398734
- **CHANGE_POINT** `imbalance` value=-5732 d1=0.0 d12=-1592.0 z=2.1894651697819314
- **CHANGE_POINT** `nuclear_gen` value=3331 d1=3.0 d12=-4.0 z=-1.686224375
- **CHANGE_POINT** `ps_gen` value=-664 d1=0.0 d12=263.0 z=0.9529488211009174
- **PERSISTENT_DOWN** `wind_gen` value=1.311e+04 d1=-138.0 d12=-816.0 z=-2.947690964398734
- **REVERSAL** `nuclear_gen` value=3331 d1=3.0 d12=-4.0 z=-1.686224375
- **ACCELERATION** `nuclear_gen` value=3331 d1=3.0 d12=-4.0 z=-1.686224375
- **REVERSAL** `thermal_base` value=5729 d1=8.0 d12=-116.0 z=-1.0368189545454545

## Nearest historical live analogues

- `2026-09-20T04:50:36.902238Z` distance=0.750 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:54:47.005275Z` distance=0.750 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:58:57.948602Z` distance=0.750 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:03:10.294370Z` distance=0.750 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:07:21.689505Z` distance=0.750 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 161.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

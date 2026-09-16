# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T09:43:25.079561Z`  
Memory snapshots: **515**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1204.0 z=-53.47740160714286
- **ROBUST_OUTLIER** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1204.0 z=-53.47740160714286
- **CHANGE_POINT** `margin` value=3.451e+04 d1=0.0 d12=-1237.0 z=-33.17820654545454
- **ROBUST_OUTLIER** `margin` value=3.451e+04 d1=0.0 d12=-1237.0 z=-33.17820654545454
- **CHANGE_POINT** `imbalance` value=5364 d1=0.0 d12=-1341.0 z=-10.9872489182243
- **ROBUST_OUTLIER** `imbalance` value=5364 d1=0.0 d12=-1341.0 z=-10.9872489182243
- **CHANGE_POINT** `biomass_gen` value=3219 d1=41.0 d12=-15.0 z=-4.384183375
- **REVERSAL** `biomass_gen` value=3219 d1=41.0 d12=-15.0 z=-4.384183375
- **ACCELERATION** `biomass_gen` value=3219 d1=41.0 d12=-15.0 z=-4.384183375
- **ROBUST_OUTLIER** `biomass_gen` value=3219 d1=41.0 d12=-15.0 z=-4.384183375
- **CHANGE_POINT** `residual_proxy` value=-813 d1=0.0 d12=0.0 z=-1.838736388535032
- **CHANGE_POINT** `ind_generation` value=2.6e+04 d1=0.0 d12=-161.0 z=-1.6541058154761903
- **CHANGE_POINT** `thermal_base` value=9658 d1=-1.0 d12=-1378.0 z=-1.0022347693661973
- **CHANGE_POINT** `ccgt_gen` value=6334 d1=-3.0 d12=-1374.0 z=-0.9964863247210803
- **REVERSAL** `nuclear_gen` value=3324 d1=2.0 d12=-4.0 z=-1.686224375

## Nearest historical live analogues

- `2026-09-16T08:17:56.653795Z` distance=3.086 → {'next30m_imbalance_delta': 235.0, 'next30m_margin_delta': 235.0, 'next30m_residual_proxy_delta': -321.0}
- `2026-09-16T07:23:21.620957Z` distance=3.089 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:27:32.881343Z` distance=3.089 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:31:44.991160Z` distance=3.089 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:35:56.436252Z` distance=3.089 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

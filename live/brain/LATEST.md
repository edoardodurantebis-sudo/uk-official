# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T09:39:12.760497Z`  
Memory snapshots: **514**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.451e+04 d1=0.0 d12=-2052.0 z=-78.16298525961538
- **ROBUST_OUTLIER** `margin` value=3.451e+04 d1=0.0 d12=-2052.0 z=-78.16298525961538
- **CHANGE_POINT** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1219.0 z=-53.47740160714286
- **ROBUST_OUTLIER** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1219.0 z=-53.47740160714286
- **CHANGE_POINT** `biomass_gen` value=3178 d1=30.0 d12=-58.0 z=-18.21122325
- **REVERSAL** `biomass_gen` value=3178 d1=30.0 d12=-58.0 z=-18.21122325
- **ACCELERATION** `biomass_gen` value=3178 d1=30.0 d12=-58.0 z=-18.21122325
- **ROBUST_OUTLIER** `biomass_gen` value=3178 d1=30.0 d12=-58.0 z=-18.21122325
- **CHANGE_POINT** `imbalance` value=5364 d1=0.0 d12=-1743.0 z=-10.9872489182243
- **ROBUST_OUTLIER** `imbalance` value=5364 d1=0.0 d12=-1743.0 z=-10.9872489182243
- **CHANGE_POINT** `ind_generation` value=2.6e+04 d1=0.0 d12=-558.0 z=-1.6541058154761903
- **CHANGE_POINT** `thermal_base` value=9659 d1=-96.0 d12=-1391.0 z=-1.0014431147300469
- **CHANGE_POINT** `ccgt_gen` value=6337 d1=-94.0 d12=-1385.0 z=-0.994109966236054
- **PERSISTENT_DOWN** `nuclear_gen` value=3322 d1=-2.0 d12=-6.0 z=-2.360714125
- **PERSISTENT_DOWN** `wind_gen` value=5652 d1=-24.0 d12=-834.0 z=-1.429728272887324

## Nearest historical live analogues

- `2026-09-16T08:17:56.653795Z` distance=3.086 → {'next30m_imbalance_delta': 235.0, 'next30m_margin_delta': 235.0, 'next30m_residual_proxy_delta': -321.0}
- `2026-09-16T07:23:21.620957Z` distance=3.089 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:27:32.881343Z` distance=3.089 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:31:44.991160Z` distance=3.089 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:35:56.436252Z` distance=3.089 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

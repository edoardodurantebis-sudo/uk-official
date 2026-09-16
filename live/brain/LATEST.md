# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T09:47:37.425581Z`  
Memory snapshots: **516**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1204.0 z=-36.22662689516129
- **ROBUST_OUTLIER** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1204.0 z=-36.22662689516129
- **CHANGE_POINT** `margin` value=3.451e+04 d1=0.0 d12=-1237.0 z=-20.86658289736842
- **ROBUST_OUTLIER** `margin` value=3.451e+04 d1=0.0 d12=-1237.0 z=-20.86658289736842
- **CHANGE_POINT** `imbalance` value=5364 d1=0.0 d12=-1341.0 z=-10.9872489182243
- **ROBUST_OUTLIER** `imbalance` value=5364 d1=0.0 d12=-1341.0 z=-10.9872489182243
- **CHANGE_POINT** `biomass_gen` value=3224 d1=5.0 d12=-18.0 z=-2.697959
- **CHANGE_POINT** `ind_generation` value=2.6e+04 d1=0.0 d12=-161.0 z=-1.6541058154761903
- **CHANGE_POINT** `interconnector_net` value=1.031e+04 d1=1.0 d12=66.0 z=1.3762889311818063
- **CHANGE_POINT** `thermal_base` value=9669 d1=11.0 d12=-1343.0 z=-0.9935265683685446
- **CHANGE_POINT** `ccgt_gen` value=6345 d1=11.0 d12=-1333.0 z=-0.9877730102759835
- **REVERSAL** `biomass_gen` value=3224 d1=5.0 d12=-18.0 z=-2.697959
- **ACCELERATION** `biomass_gen` value=3224 d1=5.0 d12=-18.0 z=-2.697959
- **PERSISTENT_UP** `interconnector_net` value=1.031e+04 d1=1.0 d12=66.0 z=1.3762889311818063
- **REVERSAL** `wind_gen` value=5657 d1=39.0 d12=-736.0 z=-1.2903039210853355

## Nearest historical live analogues

- `2026-09-16T08:52:24.970739Z` distance=2.968 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:17:56.653795Z` distance=3.086 → {'next30m_imbalance_delta': 235.0, 'next30m_margin_delta': 235.0, 'next30m_residual_proxy_delta': -321.0}
- `2026-09-16T07:23:21.620957Z` distance=3.089 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:27:32.881343Z` distance=3.089 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:31:44.991160Z` distance=3.089 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

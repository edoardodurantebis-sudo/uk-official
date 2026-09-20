# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T16:14:37.449707Z`  
Memory snapshots: **1882**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1815 d1=103.0 d12=761.0 z=414.1367065
- **PERSISTENT_UP** `biomass_gen` value=1815 d1=103.0 d12=761.0 z=414.1367065
- **ROBUST_OUTLIER** `biomass_gen` value=1815 d1=103.0 d12=761.0 z=414.1367065
- **CHANGE_POINT** `ccgt_gen` value=4038 d1=169.0 d12=1277.0 z=63.09369832857143
- **PERSISTENT_UP** `ccgt_gen` value=4038 d1=169.0 d12=1277.0 z=63.09369832857143
- **ROBUST_OUTLIER** `ccgt_gen` value=4038 d1=169.0 d12=1277.0 z=63.09369832857143
- **CHANGE_POINT** `thermal_base` value=7374 d1=171.0 d12=1277.0 z=56.691728217948715
- **PERSISTENT_UP** `thermal_base` value=7374 d1=171.0 d12=1277.0 z=56.691728217948715
- **ROBUST_OUTLIER** `thermal_base` value=7374 d1=171.0 d12=1277.0 z=56.691728217948715
- **CHANGE_POINT** `imbalance` value=-5166 d1=0.0 d12=-6.0 z=14.371820057692307
- **ROBUST_OUTLIER** `imbalance` value=-5166 d1=0.0 d12=-6.0 z=14.371820057692307
- **PERSISTENT_UP** `interconnector_net` value=1.012e+04 d1=447.0 d12=5048.0 z=6.967383694527178
- **ROBUST_OUTLIER** `interconnector_net` value=1.012e+04 d1=447.0 d12=5048.0 z=6.967383694527178
- **CHANGE_POINT** `margin` value=3.592e+04 d1=0.0 d12=0.0 z=4.016279875
- **PERSISTENT_UP** `ps_gen` value=-13 d1=0.0 d12=493.0 z=4.1971802926540285

## Nearest historical live analogues

- `2026-09-20T14:54:10.136499Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:58:25.329493Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:02:37.176302Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:06:50.185709Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:11:00.797261Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

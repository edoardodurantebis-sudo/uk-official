# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T05:38:46.661269Z`  
Memory snapshots: **457**  
Current physical regime: **LOOSE**

Regime read: margin high, wind rising.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=7625 d1=276.0 d12=3525.0 z=27.58192503255814
- **CHANGE_POINT** `thermal_base` value=1.096e+04 d1=279.0 d12=3531.0 z=26.70614820945946
- **PERSISTENT_UP** `ccgt_gen` value=7625 d1=276.0 d12=3525.0 z=27.58192503255814
- **ROBUST_OUTLIER** `ccgt_gen` value=7625 d1=276.0 d12=3525.0 z=27.58192503255814
- **PERSISTENT_UP** `thermal_base` value=1.096e+04 d1=279.0 d12=3531.0 z=26.70614820945946
- **ROBUST_OUTLIER** `thermal_base` value=1.096e+04 d1=279.0 d12=3531.0 z=26.70614820945946
- **CHANGE_POINT** `imbalance` value=7173 d1=0.0 d12=26.0 z=16.73308613829787
- **CHANGE_POINT** `ind_generation` value=2.629e+04 d1=0.0 d12=26.0 z=16.73308613829787
- **ROBUST_OUTLIER** `imbalance` value=7173 d1=0.0 d12=26.0 z=16.73308613829787
- **ROBUST_OUTLIER** `ind_generation` value=2.629e+04 d1=0.0 d12=26.0 z=16.73308613829787
- **PERSISTENT_DOWN** `interconnector_net` value=-1757 d1=-70.0 d12=-809.0 z=-7.333778935576923
- **ROBUST_OUTLIER** `interconnector_net` value=-1757 d1=-70.0 d12=-809.0 z=-7.333778935576923
- **CHANGE_POINT** `margin` value=3.755e+04 d1=0.0 d12=5.0 z=2.3591081970238097
- **CHANGE_POINT** `wind_gen` value=8594 d1=-69.0 d12=-616.0 z=-2.348776253318584
- **CHANGE_POINT** `ind_demand` value=-1.222e+04 d1=0.0 d12=-21.0 z=-1.1522533229166667

## Nearest historical live analogues

- `2026-09-16T03:32:58.473492Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:37:08.879637Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:41:19.622154Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:45:29.518871Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:49:41.884820Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

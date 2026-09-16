# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T05:34:36.913190Z`  
Memory snapshots: **456**  
Current physical regime: **LOOSE**

Regime read: margin high, wind rising.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=7349 d1=325.0 d12=3427.0 z=29.098405968586388
- **CHANGE_POINT** `thermal_base` value=1.068e+04 d1=331.0 d12=3427.0 z=27.904895033919598
- **PERSISTENT_UP** `ccgt_gen` value=7349 d1=325.0 d12=3427.0 z=29.098405968586388
- **ROBUST_OUTLIER** `ccgt_gen` value=7349 d1=325.0 d12=3427.0 z=29.098405968586388
- **PERSISTENT_UP** `thermal_base` value=1.068e+04 d1=331.0 d12=3427.0 z=27.904895033919598
- **ROBUST_OUTLIER** `thermal_base` value=1.068e+04 d1=331.0 d12=3427.0 z=27.904895033919598
- **CHANGE_POINT** `imbalance` value=7173 d1=0.0 d12=26.0 z=16.73308613829787
- **CHANGE_POINT** `ind_generation` value=2.629e+04 d1=0.0 d12=26.0 z=16.73308613829787
- **ROBUST_OUTLIER** `imbalance` value=7173 d1=0.0 d12=26.0 z=16.73308613829787
- **ROBUST_OUTLIER** `ind_generation` value=2.629e+04 d1=0.0 d12=26.0 z=16.73308613829787
- **PERSISTENT_DOWN** `interconnector_net` value=-1687 d1=-332.0 d12=-814.0 z=-7.439322907635468
- **ACCELERATION** `interconnector_net` value=-1687 d1=-332.0 d12=-814.0 z=-7.439322907635468
- **ROBUST_OUTLIER** `interconnector_net` value=-1687 d1=-332.0 d12=-814.0 z=-7.439322907635468
- **CHANGE_POINT** `wind_gen` value=8663 d1=-153.0 d12=-605.0 z=-2.2959903611111114
- **CHANGE_POINT** `ind_demand` value=-1.222e+04 d1=0.0 d12=-21.0 z=-1.1522533229166667

## Nearest historical live analogues

- `2026-09-16T03:32:58.473492Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:37:08.879637Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:41:19.622154Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:45:29.518871Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:49:41.884820Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

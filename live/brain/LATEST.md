# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-14T23:57:18.949614Z`  
Memory snapshots: **34**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=4547.0 z=10.631353956034483
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=4547.0 z=10.631353956034483
- **CHANGE_POINT** `biomass_gen` value=2729 d1=36.0 d12=152.0 z=7.41938725
- **PERSISTENT_UP** `biomass_gen` value=2729 d1=36.0 d12=152.0 z=7.41938725
- **ROBUST_OUTLIER** `biomass_gen` value=2729 d1=36.0 d12=152.0 z=7.41938725
- **CHANGE_POINT** `imbalance` value=210 d1=0.0 d12=273.0 z=4.741266183823529
- **CHANGE_POINT** `ind_generation` value=2.07e+04 d1=0.0 d12=274.0 z=4.605801435714286
- **CHANGE_POINT** `margin` value=3.272e+04 d1=0.0 d12=248.0 z=3.406744838983051
- **PERSISTENT_UP** `imbalance` value=210 d1=0.0 d12=273.0 z=4.741266183823529
- **ROBUST_OUTLIER** `imbalance` value=210 d1=0.0 d12=273.0 z=4.741266183823529
- **PERSISTENT_UP** `ind_generation` value=2.07e+04 d1=0.0 d12=274.0 z=4.605801435714286
- **ROBUST_OUTLIER** `ind_generation` value=2.07e+04 d1=0.0 d12=274.0 z=4.605801435714286
- **CHANGE_POINT** `interconnector_net` value=-985 d1=-30.0 d12=2891.0 z=2.5390915795454547
- **PERSISTENT_UP** `margin` value=3.272e+04 d1=0.0 d12=248.0 z=3.406744838983051
- **ACCELERATION** `margin` value=3.272e+04 d1=0.0 d12=248.0 z=3.406744838983051

## Nearest historical live analogues

- `2026-09-14T22:50:17.291209Z` distance=11.448 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -10.0}
- `2026-09-14T22:54:28.088906Z` distance=11.457 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': -8.0}
- `2026-09-14T22:58:38.297578Z` distance=11.540 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 116.0}
- `2026-09-14T22:46:06.193811Z` distance=11.618 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': -10.0}
- `2026-09-14T22:41:53.412159Z` distance=11.704 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 5.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-14T23:53:08.620374Z`  
Memory snapshots: **33**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=4573.0 z=10.670474522491348
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=4573.0 z=10.670474522491348
- **CHANGE_POINT** `biomass_gen` value=2693 d1=0.0 d12=133.0 z=6.68358025
- **CHANGE_POINT** `imbalance` value=210 d1=23.0 d12=273.0 z=4.741266183823529
- **PERSISTENT_UP** `biomass_gen` value=2693 d1=0.0 d12=133.0 z=6.68358025
- **ROBUST_OUTLIER** `biomass_gen` value=2693 d1=0.0 d12=133.0 z=6.68358025
- **CHANGE_POINT** `ind_generation` value=2.07e+04 d1=23.0 d12=274.0 z=4.605801435714286
- **PERSISTENT_UP** `imbalance` value=210 d1=23.0 d12=273.0 z=4.741266183823529
- **ROBUST_OUTLIER** `imbalance` value=210 d1=23.0 d12=273.0 z=4.741266183823529
- **CHANGE_POINT** `interconnector_net` value=-955 d1=0.0 d12=3642.0 z=2.610905233735572
- **PERSISTENT_UP** `ind_generation` value=2.07e+04 d1=23.0 d12=274.0 z=4.605801435714286
- **ROBUST_OUTLIER** `ind_generation` value=2.07e+04 d1=23.0 d12=274.0 z=4.605801435714286
- **PERSISTENT_UP** `margin` value=3.272e+04 d1=239.0 d12=248.0 z=3.406744838983051
- **ACCELERATION** `margin` value=3.272e+04 d1=239.0 d12=248.0 z=3.406744838983051
- **ROBUST_OUTLIER** `margin` value=3.272e+04 d1=239.0 d12=248.0 z=3.406744838983051

## Nearest historical live analogues

- `2026-09-14T22:50:17.291209Z` distance=11.485 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -10.0}
- `2026-09-14T22:54:28.088906Z` distance=11.494 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': -8.0}
- `2026-09-14T22:46:06.193811Z` distance=11.654 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': -10.0}
- `2026-09-14T22:41:53.412159Z` distance=11.740 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 5.0}
- `2026-09-14T22:37:42.328398Z` distance=12.027 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 147.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

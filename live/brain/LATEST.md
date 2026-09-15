# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T00:01:29.159410Z`  
Memory snapshots: **35**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=4566.0 z=10.16965816130363
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=4566.0 z=10.16965816130363
- **CHANGE_POINT** `biomass_gen` value=2742 d1=13.0 d12=70.0 z=7.515742928571428
- **PERSISTENT_UP** `biomass_gen` value=2742 d1=13.0 d12=70.0 z=7.515742928571428
- **ROBUST_OUTLIER** `biomass_gen` value=2742 d1=13.0 d12=70.0 z=7.515742928571428
- **CHANGE_POINT** `imbalance` value=210 d1=0.0 d12=273.0 z=4.741266183823529
- **CHANGE_POINT** `ind_generation` value=2.07e+04 d1=0.0 d12=274.0 z=4.605801435714286
- **CHANGE_POINT** `margin` value=3.272e+04 d1=0.0 d12=248.0 z=3.406744838983051
- **PERSISTENT_UP** `imbalance` value=210 d1=0.0 d12=273.0 z=4.741266183823529
- **ROBUST_OUTLIER** `imbalance` value=210 d1=0.0 d12=273.0 z=4.741266183823529
- **PERSISTENT_UP** `ind_generation` value=2.07e+04 d1=0.0 d12=274.0 z=4.605801435714286
- **ROBUST_OUTLIER** `ind_generation` value=2.07e+04 d1=0.0 d12=274.0 z=4.605801435714286
- **CHANGE_POINT** `interconnector_net` value=-805 d1=180.0 d12=2240.0 z=2.562591956284153
- **PERSISTENT_UP** `margin` value=3.272e+04 d1=0.0 d12=248.0 z=3.406744838983051
- **ROBUST_OUTLIER** `margin` value=3.272e+04 d1=0.0 d12=248.0 z=3.406744838983051

## Nearest historical live analogues

- `2026-09-14T22:50:17.291209Z` distance=10.990 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -10.0}
- `2026-09-14T22:54:28.088906Z` distance=10.999 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': -8.0}
- `2026-09-14T23:02:51.731221Z` distance=11.020 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 158.0}
- `2026-09-14T22:58:38.297578Z` distance=11.078 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 116.0}
- `2026-09-14T22:46:06.193811Z` distance=11.167 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': -10.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

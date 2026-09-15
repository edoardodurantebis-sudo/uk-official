# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T00:05:39.935821Z`  
Memory snapshots: **36**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=4544.0 z=9.745949995253165
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=4544.0 z=9.745949995253165
- **CHANGE_POINT** `biomass_gen` value=2742 d1=0.0 d12=59.0 z=7.0146934
- **PERSISTENT_UP** `biomass_gen` value=2742 d1=0.0 d12=59.0 z=7.0146934
- **ROBUST_OUTLIER** `biomass_gen` value=2742 d1=0.0 d12=59.0 z=7.0146934
- **CHANGE_POINT** `imbalance` value=210 d1=0.0 d12=273.0 z=4.741266183823529
- **CHANGE_POINT** `ind_generation` value=2.07e+04 d1=0.0 d12=274.0 z=4.605801435714286
- **CHANGE_POINT** `margin` value=3.272e+04 d1=0.0 d12=248.0 z=3.406744838983051
- **ROBUST_OUTLIER** `imbalance` value=210 d1=0.0 d12=273.0 z=4.741266183823529
- **ROBUST_OUTLIER** `ind_generation` value=2.07e+04 d1=0.0 d12=274.0 z=4.605801435714286
- **CHANGE_POINT** `interconnector_net` value=-805 d1=0.0 d12=1822.0 z=2.4681806736842105
- **ROBUST_OUTLIER** `margin` value=3.272e+04 d1=0.0 d12=248.0 z=3.406744838983051
- **CHANGE_POINT** `wind_gen` value=1.202e+04 d1=0.0 d12=-373.0 z=-0.9941173554104479
- **PERSISTENT_UP** `interconnector_net` value=-805 d1=0.0 d12=1822.0 z=2.4681806736842105
- **PERSISTENT_DOWN** `wind_gen` value=1.202e+04 d1=0.0 d12=-373.0 z=-0.9941173554104479

## Nearest historical live analogues

- `2026-09-14T22:50:17.291209Z` distance=10.572 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -10.0}
- `2026-09-14T22:54:28.088906Z` distance=10.581 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': -8.0}
- `2026-09-14T23:02:51.731221Z` distance=10.600 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 158.0}
- `2026-09-14T23:07:03.439519Z` distance=10.641 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 4566.0}
- `2026-09-14T22:58:38.297578Z` distance=10.656 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 116.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

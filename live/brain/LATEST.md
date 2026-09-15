# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T17:29:14.777763Z`  
Memory snapshots: **284**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3098 d1=92.0 d12=822.0 z=52.725827314285716
- **PERSISTENT_UP** `biomass_gen` value=3098 d1=92.0 d12=822.0 z=52.725827314285716
- **ROBUST_OUTLIER** `biomass_gen` value=3098 d1=92.0 d12=822.0 z=52.725827314285716
- **PERSISTENT_UP** `ccgt_gen` value=1.04e+04 d1=9.0 d12=583.0 z=21.999522823308272
- **ROBUST_OUTLIER** `ccgt_gen` value=1.04e+04 d1=9.0 d12=583.0 z=21.999522823308272
- **PERSISTENT_UP** `thermal_base` value=1.372e+04 d1=14.0 d12=585.0 z=21.899444354868915
- **ROBUST_OUTLIER** `thermal_base` value=1.372e+04 d1=14.0 d12=585.0 z=21.899444354868915
- **PERSISTENT_DOWN** `interconnector_net` value=-769 d1=-20.0 d12=-1392.0 z=-4.121152268952803
- **ROBUST_OUTLIER** `interconnector_net` value=-769 d1=-20.0 d12=-1392.0 z=-4.121152268952803
- **REVERSAL** `ps_gen` value=500 d1=-1.0 d12=128.0 z=2.944671891287284
- **CHANGE_POINT** `imbalance` value=5772 d1=0.0 d12=-55.0 z=0.6969727416666667
- **CHANGE_POINT** `ind_generation` value=2.489e+04 d1=0.0 d12=-55.0 z=0.5395918000000001
- **PERSISTENT_DOWN** `margin` value=3.482e+04 d1=0.0 d12=-94.0 z=-1.1917150505181346
- **PERSISTENT_UP** `nuclear_gen` value=3324 d1=5.0 d12=2.0 z=-0.8993196666666666
- **ACCELERATION** `nuclear_gen` value=3324 d1=5.0 d12=2.0 z=-0.8993196666666666

## Nearest historical live analogues

- `2026-09-15T16:34:33.511782Z` distance=0.087 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T16:21:57.402275Z` distance=0.096 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 53.0}
- `2026-09-15T16:26:08.230608Z` distance=0.096 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 53.0}
- `2026-09-15T16:30:22.410859Z` distance=0.096 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 53.0}
- `2026-09-15T15:52:27.365496Z` distance=0.142 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

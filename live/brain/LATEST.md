# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T04:12:31.535347Z`  
Memory snapshots: **741**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.15e+04 d1=0.0 d12=11.0 z=34.8036711
- **CHANGE_POINT** `ind_generation` value=2.639e+04 d1=0.0 d12=746.0 z=25.5294370375
- **ROBUST_OUTLIER** `ind_generation` value=2.639e+04 d1=0.0 d12=746.0 z=25.5294370375
- **CHANGE_POINT** `interconnector_net` value=-1.07e+04 d1=-213.0 d12=-2421.0 z=-20.48422900091575
- **PERSISTENT_DOWN** `interconnector_net` value=-1.07e+04 d1=-213.0 d12=-2421.0 z=-20.48422900091575
- **ROBUST_OUTLIER** `interconnector_net` value=-1.07e+04 d1=-213.0 d12=-2421.0 z=-20.48422900091575
- **CHANGE_POINT** `imbalance` value=7273 d1=0.0 d12=746.0 z=16.231269467741935
- **ROBUST_OUTLIER** `imbalance` value=7273 d1=0.0 d12=746.0 z=16.231269467741935
- **CHANGE_POINT** `margin` value=3.584e+04 d1=0.0 d12=-9.0 z=9.095392083333333
- **ROBUST_OUTLIER** `margin` value=3.584e+04 d1=0.0 d12=-9.0 z=9.095392083333333
- **CHANGE_POINT** `biomass_gen` value=3150 d1=109.0 d12=1119.0 z=-2.3063197903225805
- **CHANGE_POINT** `wind_gen` value=1.377e+04 d1=95.0 d12=378.0 z=0.8891001249999999
- **CHANGE_POINT** `nuclear_gen` value=3310 d1=-4.0 d12=-1.0 z=-0.67448975
- **CHANGE_POINT** `ps_gen` value=-328 d1=-41.0 d12=36.0 z=-0.3523107972508591
- **PERSISTENT_UP** `biomass_gen` value=3150 d1=109.0 d12=1119.0 z=-2.3063197903225805

## Nearest historical live analogues

- `2026-09-17T02:52:02.690108Z` distance=0.591 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:56:14.879410Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T03:00:26.007200Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T03:04:39.344891Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T03:08:48.749095Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 1126.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

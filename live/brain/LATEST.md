# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T10:33:39.002246Z`  
Memory snapshots: **1173**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low, wind falling.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1165 d1=-170.0 d12=-497.0 z=-42.07129815625
- **PERSISTENT_DOWN** `biomass_gen` value=1165 d1=-170.0 d12=-497.0 z=-42.07129815625
- **ROBUST_OUTLIER** `biomass_gen` value=1165 d1=-170.0 d12=-497.0 z=-42.07129815625
- **ROBUST_OUTLIER** `imbalance` value=7078 d1=0.0 d12=-1022.0 z=-11.75972879125
- **ROBUST_OUTLIER** `ind_demand` value=-1.38e+04 d1=0.0 d12=-611.0 z=-6.691721959543568
- **CHANGE_POINT** `ind_generation` value=2.676e+04 d1=0.0 d12=-434.0 z=-4.01995891
- **ROBUST_OUTLIER** `margin` value=3.635e+04 d1=0.0 d12=144.0 z=-5.713534866402117
- **ROBUST_OUTLIER** `ind_generation` value=2.676e+04 d1=0.0 d12=-434.0 z=-4.01995891
- **ROBUST_OUTLIER** `ps_gen` value=-716 d1=0.0 d12=-296.0 z=-3.210071587962963
- **PERSISTENT_UP** `residual_proxy` value=8839 d1=84.0 d12=84.0 z=2.791638131944444
- **ACCELERATION** `residual_proxy` value=8839 d1=84.0 d12=84.0 z=2.791638131944444
- **PERSISTENT_DOWN** `nuclear_gen` value=3328 d1=-2.0 d12=-7.0 z=-1.8885713
- **PERSISTENT_DOWN** `wind_forecast` value=7615 d1=-84.0 d12=-84.0 z=-1.4801302847222222
- **ACCELERATION** `wind_forecast` value=7615 d1=-84.0 d12=-84.0 z=-1.4801302847222222
- **PERSISTENT_DOWN** `thermal_base` value=6346 d1=-11.0 d12=-69.0 z=-1.1095550365653246

## Nearest historical live analogues

- `2026-09-18T09:21:34.020078Z` distance=0.743 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:25:46.604177Z` distance=0.743 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:30:05.383319Z` distance=0.743 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:34:18.274964Z` distance=0.743 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:39:05.140398Z` distance=0.743 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

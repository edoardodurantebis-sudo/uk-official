# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T10:42:00.268257Z`  
Memory snapshots: **1175**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low, wind falling.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1088 d1=-40.0 d12=-562.0 z=-45.317280078125
- **PERSISTENT_DOWN** `biomass_gen` value=1088 d1=-40.0 d12=-562.0 z=-45.317280078125
- **ROBUST_OUTLIER** `biomass_gen` value=1088 d1=-40.0 d12=-562.0 z=-45.317280078125
- **CHANGE_POINT** `imbalance` value=7078 d1=0.0 d12=-723.0 z=-11.75972879125
- **ROBUST_OUTLIER** `imbalance` value=7078 d1=0.0 d12=-723.0 z=-11.75972879125
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.968e+04 d1=0.0 d12=588.0 z=8.710640149774775
- **CHANGE_POINT** `ind_demand` value=-1.38e+04 d1=0.0 d12=-607.0 z=-6.691721959543568
- **CHANGE_POINT** `margin` value=3.635e+04 d1=0.0 d12=189.0 z=-5.713534866402117
- **ROBUST_OUTLIER** `ind_demand` value=-1.38e+04 d1=0.0 d12=-607.0 z=-6.691721959543568
- **CHANGE_POINT** `ind_generation` value=2.676e+04 d1=0.0 d12=-135.0 z=-4.01995891
- **ROBUST_OUTLIER** `margin` value=3.635e+04 d1=0.0 d12=189.0 z=-5.713534866402117
- **ROBUST_OUTLIER** `ind_generation` value=2.676e+04 d1=0.0 d12=-135.0 z=-4.01995891
- **PERSISTENT_DOWN** `ps_gen` value=-723 d1=-2.0 d12=-269.0 z=-3.116503978794643
- **ROBUST_OUTLIER** `ps_gen` value=-723 d1=-2.0 d12=-269.0 z=-3.116503978794643
- **PERSISTENT_UP** `residual_proxy` value=8839 d1=0.0 d12=84.0 z=2.791638131944444

## Nearest historical live analogues

- `2026-09-18T09:21:34.020078Z` distance=0.743 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:25:46.604177Z` distance=0.743 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:30:05.383319Z` distance=0.743 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:34:18.274964Z` distance=0.743 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:39:05.140398Z` distance=0.743 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

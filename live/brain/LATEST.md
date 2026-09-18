# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T10:46:10.518844Z`  
Memory snapshots: **1176**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1082 d1=-6.0 d12=-568.0 z=-45.570213734375
- **PERSISTENT_DOWN** `biomass_gen` value=1082 d1=-6.0 d12=-568.0 z=-45.570213734375
- **ROBUST_OUTLIER** `biomass_gen` value=1082 d1=-6.0 d12=-568.0 z=-45.570213734375
- **CHANGE_POINT** `imbalance` value=7078 d1=0.0 d12=-723.0 z=-6.621990478888889
- **CHANGE_POINT** `margin` value=3.635e+04 d1=0.0 d12=189.0 z=-5.692542343837535
- **ROBUST_OUTLIER** `imbalance` value=7078 d1=0.0 d12=-723.0 z=-6.621990478888889
- **CHANGE_POINT** `ind_demand` value=-1.38e+04 d1=0.0 d12=-607.0 z=-3.7441750211970075
- **ROBUST_OUTLIER** `margin` value=3.635e+04 d1=0.0 d12=189.0 z=-5.692542343837535
- **CHANGE_POINT** `ind_generation` value=2.676e+04 d1=0.0 d12=-135.0 z=-3.0414879409937887
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.968e+04 d1=0.0 d12=588.0 z=4.355320074887388
- **ROBUST_OUTLIER** `ind_demand` value=-1.38e+04 d1=0.0 d12=-607.0 z=-3.7441750211970075
- **ROBUST_OUTLIER** `ind_generation` value=2.676e+04 d1=0.0 d12=-135.0 z=-3.0414879409937887
- **REVERSAL** `ps_gen` value=-719 d1=4.0 d12=-229.0 z=-2.690131265957447
- **PERSISTENT_DOWN** `thermal_base` value=6211 d1=-91.0 d12=-153.0 z=-1.1870183671572425
- **ACCELERATION** `thermal_base` value=6211 d1=-91.0 d12=-153.0 z=-1.1870183671572425

## Nearest historical live analogues

- `2026-09-18T09:51:41.499535Z` distance=0.740 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:21:34.020078Z` distance=0.743 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:25:46.604177Z` distance=0.743 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:30:05.383319Z` distance=0.743 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:34:18.274964Z` distance=0.743 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

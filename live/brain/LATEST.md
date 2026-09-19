# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T10:00:22.010182Z`  
Memory snapshots: **1452**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.893e+04 d1=0.0 d12=1130.0 z=293.065796375
- **CHANGE_POINT** `ind_demand` value=-1.321e+04 d1=0.0 d12=-1128.0 z=-87.42136593055555
- **ROBUST_OUTLIER** `ind_demand` value=-1.321e+04 d1=0.0 d12=-1128.0 z=-87.42136593055555
- **CHANGE_POINT** `margin` value=3.645e+04 d1=0.0 d12=-1141.0 z=-14.67426480487805
- **PERSISTENT_DOWN** `margin` value=3.645e+04 d1=0.0 d12=-1141.0 z=-14.67426480487805
- **ROBUST_OUTLIER** `margin` value=3.645e+04 d1=0.0 d12=-1141.0 z=-14.67426480487805
- **CHANGE_POINT** `imbalance` value=7793 d1=0.0 d12=-1139.0 z=-3.973829471153846
- **ROBUST_OUTLIER** `ind_generation` value=2.672e+04 d1=0.0 d12=-10.0 z=-4.071919601851852
- **CHANGE_POINT** `ps_gen` value=-699 d1=0.0 d12=-19.0 z=-1.9859975972222221
- **ROBUST_OUTLIER** `imbalance` value=7793 d1=0.0 d12=-1139.0 z=-3.973829471153846
- **ROBUST_OUTLIER** `biomass_gen` value=476 d1=0.0 d12=0.0 z=-3.4518004852941178
- **ROBUST_OUTLIER** `residual_proxy` value=8953 d1=0.0 d12=0.0 z=-3.094968789556962
- **CHANGE_POINT** `wind_gen` value=1.573e+04 d1=0.0 d12=659.0 z=-0.2734417905405405
- **ACCELERATION** `nuclear_gen` value=3329 d1=0.0 d12=2.0 z=-1.7986393333333333
- **PERSISTENT_DOWN** `thermal_base` value=6381 d1=0.0 d12=-127.0 z=-0.8816859477124184

## Nearest historical live analogues

- `2026-09-18T09:21:34.020078Z` distance=0.927 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:25:46.604177Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:30:05.383319Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:34:18.274964Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:39:05.140398Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

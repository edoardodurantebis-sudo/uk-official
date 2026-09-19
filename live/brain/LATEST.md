# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T10:08:44.121340Z`  
Memory snapshots: **1454**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.893e+04 d1=0.0 d12=1130.0 z=293.065796375
- **CHANGE_POINT** `ind_demand` value=-1.321e+04 d1=0.0 d12=-1128.0 z=-87.42136593055555
- **ROBUST_OUTLIER** `ind_demand` value=-1.321e+04 d1=0.0 d12=-1128.0 z=-87.42136593055555
- **CHANGE_POINT** `margin` value=3.645e+04 d1=0.0 d12=-1141.0 z=-14.67426480487805
- **ROBUST_OUTLIER** `margin` value=3.645e+04 d1=0.0 d12=-1141.0 z=-14.67426480487805
- **CHANGE_POINT** `imbalance` value=7793 d1=0.0 d12=-1139.0 z=-3.973829471153846
- **ROBUST_OUTLIER** `ind_generation` value=2.672e+04 d1=0.0 d12=-10.0 z=-4.071919601851852
- **ROBUST_OUTLIER** `imbalance` value=7793 d1=0.0 d12=-1139.0 z=-3.973829471153846
- **CHANGE_POINT** `ps_gen` value=-690 d1=9.0 d12=-267.0 z=-1.7294608974358974
- **PERSISTENT_UP** `biomass_gen` value=478 d1=0.0 d12=2.0 z=-3.37244875
- **ACCELERATION** `biomass_gen` value=478 d1=0.0 d12=2.0 z=-3.37244875
- **ROBUST_OUTLIER** `biomass_gen` value=478 d1=0.0 d12=2.0 z=-3.37244875
- **CHANGE_POINT** `thermal_base` value=6328 d1=-6.0 d12=-189.0 z=-1.1153327238562092
- **ROBUST_OUTLIER** `residual_proxy` value=8953 d1=0.0 d12=0.0 z=-3.094968789556962
- **CHANGE_POINT** `ccgt_gen` value=2999 d1=-7.0 d12=-190.0 z=-1.0646357818627452

## Nearest historical live analogues

- `2026-09-18T09:21:34.020078Z` distance=0.927 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:25:46.604177Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:30:05.383319Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:34:18.274964Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:39:05.140398Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

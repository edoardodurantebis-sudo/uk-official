# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T09:51:56.482534Z`  
Memory snapshots: **1450**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.893e+04 d1=0.0 d12=1130.0 z=293.065796375
- **CHANGE_POINT** `ind_demand` value=-1.321e+04 d1=2.0 d12=-1128.0 z=-87.42136593055555
- **REVERSAL** `ind_demand` value=-1.321e+04 d1=2.0 d12=-1128.0 z=-87.42136593055555
- **ROBUST_OUTLIER** `ind_demand` value=-1.321e+04 d1=2.0 d12=-1128.0 z=-87.42136593055555
- **CHANGE_POINT** `margin` value=3.645e+04 d1=-27.0 d12=-1141.0 z=-14.67426480487805
- **PERSISTENT_DOWN** `margin` value=3.645e+04 d1=-27.0 d12=-1141.0 z=-14.67426480487805
- **ROBUST_OUTLIER** `margin` value=3.645e+04 d1=-27.0 d12=-1141.0 z=-14.67426480487805
- **CHANGE_POINT** `imbalance` value=7793 d1=22.0 d12=-1139.0 z=-3.973829471153846
- **CHANGE_POINT** `ps_gen` value=-700 d1=1.0 d12=-3.0 z=-2.63215512195122
- **REVERSAL** `ind_generation` value=2.672e+04 d1=22.0 d12=-10.0 z=-4.071919601851852
- **ACCELERATION** `ind_generation` value=2.672e+04 d1=22.0 d12=-10.0 z=-4.071919601851852
- **ROBUST_OUTLIER** `ind_generation` value=2.672e+04 d1=22.0 d12=-10.0 z=-4.071919601851852
- **REVERSAL** `imbalance` value=7793 d1=22.0 d12=-1139.0 z=-3.973829471153846
- **ROBUST_OUTLIER** `imbalance` value=7793 d1=22.0 d12=-1139.0 z=-3.973829471153846
- **PERSISTENT_DOWN** `interconnector_net` value=-1019 d1=0.0 d12=-1093.0 z=3.754995175373134

## Nearest historical live analogues

- `2026-09-18T09:21:34.020078Z` distance=0.927 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:25:46.604177Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:30:05.383319Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:34:18.274964Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:39:05.140398Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

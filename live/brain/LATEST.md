# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T09:30:55.378368Z`  
Memory snapshots: **1445**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **PERSISTENT_UP** `ts_demand_forecast` value=1.893e+04 d1=0.0 d12=1130.0 z=293.065796375
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.893e+04 d1=0.0 d12=1130.0 z=293.065796375
- **PERSISTENT_DOWN** `ind_demand` value=-1.322e+04 d1=0.0 d12=-1135.0 z=-98.433347890625
- **ROBUST_OUTLIER** `ind_demand` value=-1.322e+04 d1=0.0 d12=-1135.0 z=-98.433347890625
- **PERSISTENT_DOWN** `margin` value=3.648e+04 d1=0.0 d12=-1137.0 z=-19.637603213114755
- **ROBUST_OUTLIER** `margin` value=3.648e+04 d1=0.0 d12=-1137.0 z=-19.637603213114755
- **CHANGE_POINT** `ps_gen` value=-423 d1=-1.0 d12=-1.0 z=14.409553749999999
- **PERSISTENT_DOWN** `ps_gen` value=-423 d1=-1.0 d12=-1.0 z=14.409553749999999
- **ACCELERATION** `ps_gen` value=-423 d1=-1.0 d12=-1.0 z=14.409553749999999
- **ROBUST_OUTLIER** `ps_gen` value=-423 d1=-1.0 d12=-1.0 z=14.409553749999999
- **PERSISTENT_DOWN** `interconnector_net` value=-976 d1=-536.0 d12=-1003.0 z=7.408278007058824
- **ACCELERATION** `interconnector_net` value=-976 d1=-536.0 d12=-1003.0 z=7.408278007058824
- **ROBUST_OUTLIER** `interconnector_net` value=-976 d1=-536.0 d12=-1003.0 z=7.408278007058824
- **PERSISTENT_DOWN** `imbalance` value=7771 d1=0.0 d12=-1227.0 z=-4.661352239878543
- **ROBUST_OUTLIER** `imbalance` value=7771 d1=0.0 d12=-1227.0 z=-4.661352239878543

## Nearest historical live analogues

- `2026-09-18T09:21:34.020078Z` distance=0.927 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:25:46.604177Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:30:05.383319Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:34:18.274964Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:39:05.140398Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

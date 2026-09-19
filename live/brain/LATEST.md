# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T09:35:04.775644Z`  
Memory snapshots: **1446**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.893e+04 d1=0.0 d12=1130.0 z=293.065796375
- **CHANGE_POINT** `ind_demand` value=-1.322e+04 d1=0.0 d12=-1135.0 z=-98.433347890625
- **ROBUST_OUTLIER** `ind_demand` value=-1.322e+04 d1=0.0 d12=-1135.0 z=-98.433347890625
- **ROBUST_OUTLIER** `margin` value=3.648e+04 d1=0.0 d12=-1137.0 z=-19.637603213114755
- **CHANGE_POINT** `ps_gen` value=-423 d1=0.0 d12=0.0 z=12.1408155
- **ACCELERATION** `ps_gen` value=-423 d1=0.0 d12=0.0 z=12.1408155
- **ROBUST_OUTLIER** `ps_gen` value=-423 d1=0.0 d12=0.0 z=12.1408155
- **CHANGE_POINT** `residual_proxy` value=8953 d1=0.0 d12=0.0 z=-3.094968789556962
- **ROBUST_OUTLIER** `imbalance` value=7771 d1=0.0 d12=-1227.0 z=-4.661352239878543
- **ROBUST_OUTLIER** `ind_generation` value=2.67e+04 d1=0.0 d12=-91.0 z=-4.621503842592593
- **PERSISTENT_DOWN** `interconnector_net` value=-976 d1=0.0 d12=-1003.0 z=4.269988546869378
- **ACCELERATION** `interconnector_net` value=-976 d1=0.0 d12=-1003.0 z=4.269988546869378
- **ROBUST_OUTLIER** `interconnector_net` value=-976 d1=0.0 d12=-1003.0 z=4.269988546869378
- **PERSISTENT_UP** `wind_gen` value=1.521e+04 d1=0.0 d12=119.0 z=-3.684712523148148
- **ACCELERATION** `wind_gen` value=1.521e+04 d1=0.0 d12=119.0 z=-3.684712523148148

## Nearest historical live analogues

- `2026-09-18T09:21:34.020078Z` distance=0.927 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:25:46.604177Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:30:05.383319Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:34:18.274964Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:39:05.140398Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

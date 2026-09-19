# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T09:21:22.240716Z`  
Memory snapshots: **1443**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **PERSISTENT_UP** `ts_demand_forecast` value=1.893e+04 d1=1130.0 d12=1130.0 z=293.065796375
- **ACCELERATION** `ts_demand_forecast` value=1.893e+04 d1=1130.0 d12=1130.0 z=293.065796375
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.893e+04 d1=1130.0 d12=1130.0 z=293.065796375
- **PERSISTENT_DOWN** `ind_demand` value=-1.322e+04 d1=-1130.0 d12=-1135.0 z=-98.433347890625
- **ACCELERATION** `ind_demand` value=-1.322e+04 d1=-1130.0 d12=-1135.0 z=-98.433347890625
- **ROBUST_OUTLIER** `ind_demand` value=-1.322e+04 d1=-1130.0 d12=-1135.0 z=-98.433347890625
- **REVERSAL** `interconnector_net` value=-458 d1=25.0 d12=-498.0 z=19.702700584507042
- **ROBUST_OUTLIER** `interconnector_net` value=-458 d1=25.0 d12=-498.0 z=19.702700584507042
- **PERSISTENT_DOWN** `margin` value=3.648e+04 d1=-1114.0 d12=-1137.0 z=-19.637603213114755
- **ACCELERATION** `margin` value=3.648e+04 d1=-1114.0 d12=-1137.0 z=-19.637603213114755
- **ROBUST_OUTLIER** `margin` value=3.648e+04 d1=-1114.0 d12=-1137.0 z=-19.637603213114755
- **CHANGE_POINT** `ps_gen` value=-422 d1=1.0 d12=1.0 z=16.05285605
- **PERSISTENT_UP** `ps_gen` value=-422 d1=1.0 d12=1.0 z=16.05285605
- **ACCELERATION** `ps_gen` value=-422 d1=1.0 d12=1.0 z=16.05285605
- **ROBUST_OUTLIER** `ps_gen` value=-422 d1=1.0 d12=1.0 z=16.05285605

## Nearest historical live analogues

- `2026-09-18T09:21:34.020078Z` distance=0.927 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:25:46.604177Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:30:05.383319Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:34:18.274964Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:39:05.140398Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T08:18:19.086544Z`  
Memory snapshots: **1428**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ts_demand_forecast` value=1.78e+04 d1=-1758.0 d12=-610.0 z=102.522442
- **PERSISTENT_DOWN** `ts_demand_forecast` value=1.78e+04 d1=-1758.0 d12=-610.0 z=102.522442
- **ACCELERATION** `ts_demand_forecast` value=1.78e+04 d1=-1758.0 d12=-610.0 z=102.522442
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.78e+04 d1=-1758.0 d12=-610.0 z=102.522442
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=0.0 z=-50.460264421875
- **CHANGE_POINT** `interconnector_net` value=-1740 d1=-1.0 d12=4230.0 z=24.78986375751503
- **ROBUST_OUTLIER** `margin` value=3.703e+04 d1=0.0 d12=0.0 z=-26.4948004921875
- **REVERSAL** `interconnector_net` value=-1740 d1=-1.0 d12=4230.0 z=24.78986375751503
- **ROBUST_OUTLIER** `interconnector_net` value=-1740 d1=-1.0 d12=4230.0 z=24.78986375751503
- **CHANGE_POINT** `ps_gen` value=-424 d1=168.0 d12=-4.0 z=19.897447625
- **REVERSAL** `ps_gen` value=-424 d1=168.0 d12=-4.0 z=19.897447625
- **ACCELERATION** `ps_gen` value=-424 d1=168.0 d12=-4.0 z=19.897447625
- **ROBUST_OUTLIER** `ps_gen` value=-424 d1=168.0 d12=-4.0 z=19.897447625
- **CHANGE_POINT** `imbalance` value=8458 d1=0.0 d12=0.0 z=-2.902867278481013
- **PERSISTENT_DOWN** `residual_proxy` value=9068 d1=-3120.0 d12=-610.0 z=-2.6040427056962026

## Nearest historical live analogues

- `2026-09-19T07:23:46.754706Z` distance=0.107 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:19:33.283836Z` distance=0.656 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T06:54:14.045129Z` distance=0.735 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T06:58:26.669758Z` distance=0.735 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:02:41.681401Z` distance=0.735 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

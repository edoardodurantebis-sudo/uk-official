# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T10:38:13.905363Z`  
Memory snapshots: **1461**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low, wind falling.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.606e+04 d1=0.0 d12=-637.0 z=-20.534465722222222
- **ROBUST_OUTLIER** `ind_generation` value=2.606e+04 d1=0.0 d12=-637.0 z=-20.534465722222222
- **CHANGE_POINT** `imbalance` value=7134 d1=0.0 d12=-637.0 z=-4.879641895061728
- **CHANGE_POINT** `margin` value=3.651e+04 d1=0.0 d12=32.0 z=-3.5722105226480836
- **ROBUST_OUTLIER** `imbalance` value=7134 d1=0.0 d12=-637.0 z=-4.879641895061728
- **CHANGE_POINT** `ind_demand` value=-1.322e+04 d1=0.0 d12=-6.0 z=-2.579337080777096
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.893e+04 d1=0.0 d12=0.0 z=4.241665666317991
- **ROBUST_OUTLIER** `margin` value=3.651e+04 d1=0.0 d12=32.0 z=-3.5722105226480836
- **CHANGE_POINT** `biomass_gen` value=477 d1=-1.0 d12=0.0 z=-1.5416908571428571
- **CHANGE_POINT** `thermal_base` value=6276 d1=1.0 d12=-157.0 z=-1.3445710702614377
- **CHANGE_POINT** `ccgt_gen` value=2941 d1=2.0 d12=-158.0 z=-1.3203247066993464
- **CHANGE_POINT** `wind_gen` value=1.59e+04 d1=35.0 d12=309.0 z=0.9350880625000001
- **PERSISTENT_UP** `residual_proxy` value=9284 d1=0.0 d12=331.0 z=-1.6819554525316456
- **ACCELERATION** `residual_proxy` value=9284 d1=0.0 d12=331.0 z=-1.6819554525316456
- **ACCELERATION** `biomass_gen` value=477 d1=-1.0 d12=0.0 z=-1.5416908571428571

## Nearest historical live analogues

- `2026-09-19T09:21:22.240716Z` distance=0.118 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T09:26:43.150108Z` distance=0.118 → {'next30m_imbalance_delta': 22.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T09:30:55.378368Z` distance=0.118 → {'next30m_imbalance_delta': 22.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T09:35:04.775644Z` distance=0.118 → {'next30m_imbalance_delta': 22.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T09:39:16.171123Z` distance=0.118 → {'next30m_imbalance_delta': 22.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

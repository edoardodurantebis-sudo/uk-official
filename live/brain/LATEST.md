# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T09:06:29.286591Z`  
Memory snapshots: **165**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2041 d1=-3.0 d12=-860.0 z=-74.96471792857143
- **PERSISTENT_DOWN** `biomass_gen` value=2041 d1=-3.0 d12=-860.0 z=-74.96471792857143
- **ROBUST_OUTLIER** `biomass_gen` value=2041 d1=-3.0 d12=-860.0 z=-74.96471792857143
- **CHANGE_POINT** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=1346.0 z=56.657139
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=1346.0 z=56.657139
- **CHANGE_POINT** `wind_gen` value=1.199e+04 d1=-40.0 d12=-764.0 z=-3.052498483974359
- **CHANGE_POINT** `ps_gen` value=-862 d1=-87.0 d12=-316.0 z=-2.6733425857664233
- **CHANGE_POINT** `ccgt_gen` value=2528 d1=-53.0 d12=-477.0 z=-1.7392266988873437
- **CHANGE_POINT** `thermal_base` value=5840 d1=-56.0 d12=-478.0 z=-1.732948287722908
- **PERSISTENT_DOWN** `wind_gen` value=1.199e+04 d1=-40.0 d12=-764.0 z=-3.052498483974359
- **ROBUST_OUTLIER** `wind_gen` value=1.199e+04 d1=-40.0 d12=-764.0 z=-3.052498483974359
- **PERSISTENT_DOWN** `ps_gen` value=-862 d1=-87.0 d12=-316.0 z=-2.6733425857664233
- **ACCELERATION** `ps_gen` value=-862 d1=-87.0 d12=-316.0 z=-2.6733425857664233
- **PERSISTENT_UP** `interconnector_net` value=1.036e+04 d1=316.0 d12=2064.0 z=2.5176768630206228
- **CHANGE_POINT** `demand_forecast` value=2.007e+04 d1=0.0 d12=1346.0 z=None

## Nearest historical live analogues

- `2026-09-15T03:51:58.464857Z` distance=0.313 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:56:09.070441Z` distance=0.313 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:00:20.228720Z` distance=0.313 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:04:32.418140Z` distance=0.313 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:08:45.476934Z` distance=0.313 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

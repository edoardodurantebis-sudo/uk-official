# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T08:58:08.555915Z`  
Memory snapshots: **163**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2043 d1=1.0 d12=-1118.0 z=-78.57805587499999
- **REVERSAL** `biomass_gen` value=2043 d1=1.0 d12=-1118.0 z=-78.57805587499999
- **ROBUST_OUTLIER** `biomass_gen` value=2043 d1=1.0 d12=-1118.0 z=-78.57805587499999
- **CHANGE_POINT** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=1346.0 z=56.657139
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=1346.0 z=56.657139
- **CHANGE_POINT** `wind_gen` value=1.205e+04 d1=-14.0 d12=-645.0 z=-2.9249507427884613
- **CHANGE_POINT** `ccgt_gen` value=2749 d1=-104.0 d12=-252.0 z=-1.5441418759936407
- **CHANGE_POINT** `thermal_base` value=6063 d1=-107.0 d12=-257.0 z=-1.5288434333333332
- **CHANGE_POINT** `ps_gen` value=-540 d1=-2.0 d12=-252.0 z=-1.08654167
- **PERSISTENT_DOWN** `wind_gen` value=1.205e+04 d1=-14.0 d12=-645.0 z=-2.9249507427884613
- **PERSISTENT_UP** `interconnector_net` value=9811 d1=49.0 d12=1878.0 z=2.420099438975847
- **PERSISTENT_UP** `ind_generation` value=2.043e+04 d1=0.0 d12=404.0 z=2.0488260075187967
- **ACCELERATION** `ind_generation` value=2.043e+04 d1=0.0 d12=404.0 z=2.0488260075187967
- **CHANGE_POINT** `demand_forecast` value=2.007e+04 d1=0.0 d12=1346.0 z=None
- **CHANGE_POINT** `residual_proxy` value=3328 d1=0.0 d12=1664.0 z=0.0

## Nearest historical live analogues

- `2026-09-15T03:51:58.464857Z` distance=0.314 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:56:09.070441Z` distance=0.314 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:00:20.228720Z` distance=0.314 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:04:32.418140Z` distance=0.314 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:08:45.476934Z` distance=0.314 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

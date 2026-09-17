# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T01:40:48.692118Z`  
Memory snapshots: **705**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2539 d1=-149.0 d12=-665.0 z=-224.942331625
- **PERSISTENT_DOWN** `biomass_gen` value=2539 d1=-149.0 d12=-665.0 z=-224.942331625
- **ROBUST_OUTLIER** `biomass_gen` value=2539 d1=-149.0 d12=-665.0 z=-224.942331625
- **ROBUST_OUTLIER** `ind_demand` value=-1.165e+04 d1=0.0 d12=116.0 z=16.32265195
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `ccgt_gen` value=4061 d1=12.0 d12=-383.0 z=-3.7245316667571973
- **CHANGE_POINT** `thermal_base` value=7373 d1=6.0 d12=-389.0 z=-3.6913315051212936
- **REVERSAL** `ccgt_gen` value=4061 d1=12.0 d12=-383.0 z=-3.7245316667571973
- **ROBUST_OUTLIER** `ccgt_gen` value=4061 d1=12.0 d12=-383.0 z=-3.7245316667571973
- **REVERSAL** `thermal_base` value=7373 d1=6.0 d12=-389.0 z=-3.6913315051212936
- **ROBUST_OUTLIER** `thermal_base` value=7373 d1=6.0 d12=-389.0 z=-3.6913315051212936
- **ROBUST_OUTLIER** `interconnector_net` value=-6663 d1=0.0 d12=-71.0 z=-3.347634260488382
- **CHANGE_POINT** `ps_gen` value=-308 d1=1.0 d12=-64.0 z=-0.7400272155870445
- **PERSISTENT_UP** `wind_gen` value=1.301e+04 d1=51.0 d12=686.0 z=1.1425344094303798

## Nearest historical live analogues

- `2026-09-17T00:03:44.260171Z` distance=0.254 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:07:55.537385Z` distance=0.254 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:12:06.744150Z` distance=0.254 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:16:55.131775Z` distance=0.254 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:21:07.276189Z` distance=0.254 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

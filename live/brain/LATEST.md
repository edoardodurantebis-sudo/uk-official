# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T07:34:09.642854Z`  
Memory snapshots: **143**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3237 d1=-4.0 d12=32.0 z=2.697959
- **CHANGE_POINT** `interconnector_net` value=6381 d1=3322.0 d12=7018.0 z=2.6280326337381514
- **CHANGE_POINT** `wind_gen` value=1.246e+04 d1=-28.0 d12=-1212.0 z=-2.0321165544871795
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=0.0 d12=155.0 z=3.1074706339285716
- **CHANGE_POINT** `thermal_base` value=6612 d1=-157.0 d12=-632.0 z=-1.1073452854381445
- **CHANGE_POINT** `ccgt_gen` value=3295 d1=-153.0 d12=-619.0 z=-1.0695233887468032
- **CHANGE_POINT** `margin` value=3.413e+04 d1=0.0 d12=231.0 z=0.9323828897058823
- **REVERSAL** `biomass_gen` value=3237 d1=-4.0 d12=32.0 z=2.697959
- **PERSISTENT_UP** `interconnector_net` value=6381 d1=3322.0 d12=7018.0 z=2.6280326337381514
- **ACCELERATION** `interconnector_net` value=6381 d1=3322.0 d12=7018.0 z=2.6280326337381514
- **CHANGE_POINT** `ind_generation` value=2.003e+04 d1=0.0 d12=136.0 z=-0.24274695372750643
- **CHANGE_POINT** `imbalance` value=-454 d1=0.0 d12=136.0 z=-0.24163421456185566
- **PERSISTENT_DOWN** `nuclear_gen` value=3317 d1=-4.0 d12=-13.0 z=-2.1583672
- **PERSISTENT_DOWN** `wind_gen` value=1.246e+04 d1=-28.0 d12=-1212.0 z=-2.0321165544871795
- **PERSISTENT_DOWN** `thermal_base` value=6612 d1=-157.0 d12=-632.0 z=-1.1073452854381445

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=1.003 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=1.003 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=1.003 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=1.003 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=1.003 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

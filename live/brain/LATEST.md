# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T09:58:31.364029Z`  
Memory snapshots: **177**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **REVERSAL** `biomass_gen` value=2040 d1=1.0 d12=-1.0 z=-52.385370583333334
- **ACCELERATION** `biomass_gen` value=2040 d1=1.0 d12=-1.0 z=-52.385370583333334
- **ROBUST_OUTLIER** `biomass_gen` value=2040 d1=1.0 d12=-1.0 z=-52.385370583333334
- **CHANGE_POINT** `margin` value=3.434e+04 d1=0.0 d12=266.0 z=2.9334951031746033
- **CHANGE_POINT** `ccgt_gen` value=1942 d1=-156.0 d12=-586.0 z=-2.431394188622755
- **CHANGE_POINT** `thermal_base` value=5266 d1=-158.0 d12=-574.0 z=-2.411180697743468
- **REVERSAL** `wind_gen` value=1.173e+04 d1=175.0 d12=-260.0 z=-3.1857255988700564
- **ACCELERATION** `wind_gen` value=1.173e+04 d1=175.0 d12=-260.0 z=-3.1857255988700564
- **ROBUST_OUTLIER** `wind_gen` value=1.173e+04 d1=175.0 d12=-260.0 z=-3.1857255988700564
- **CHANGE_POINT** `imbalance` value=-365 d1=0.0 d12=-230.0 z=0.5944655423728814
- **ACCELERATION** `ps_gen` value=-1101 d1=-169.0 d12=-239.0 z=-2.5523495502481386
- **PERSISTENT_DOWN** `ccgt_gen` value=1942 d1=-156.0 d12=-586.0 z=-2.431394188622755
- **PERSISTENT_DOWN** `thermal_base` value=5266 d1=-158.0 d12=-574.0 z=-2.411180697743468

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=0.863 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=0.863 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=0.863 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=0.863 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=0.863 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

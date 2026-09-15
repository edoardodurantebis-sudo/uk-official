# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T09:50:06.277373Z`  
Memory snapshots: **175**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **ACCELERATION** `biomass_gen` value=2041 d1=0.0 d12=-2.0 z=-54.16850440517241
- **ROBUST_OUTLIER** `biomass_gen` value=2041 d1=0.0 d12=-2.0 z=-54.16850440517241
- **CHANGE_POINT** `wind_gen` value=1.155e+04 d1=0.0 d12=-497.0 z=-3.9866007587859427
- **CHANGE_POINT** `margin` value=3.434e+04 d1=-154.0 d12=266.0 z=2.9334951031746033
- **PERSISTENT_DOWN** `wind_gen` value=1.155e+04 d1=0.0 d12=-497.0 z=-3.9866007587859427
- **ROBUST_OUTLIER** `wind_gen` value=1.155e+04 d1=0.0 d12=-497.0 z=-3.9866007587859427
- **CHANGE_POINT** `ccgt_gen` value=2279 d1=0.0 d12=-470.0 z=-1.961389347636816
- **CHANGE_POINT** `thermal_base` value=5600 d1=0.0 d12=-463.0 z=-1.9463135959409594
- **REVERSAL** `margin` value=3.434e+04 d1=-154.0 d12=266.0 z=2.9334951031746033
- **ACCELERATION** `margin` value=3.434e+04 d1=-154.0 d12=266.0 z=2.9334951031746033
- **CHANGE_POINT** `imbalance` value=-365 d1=-273.0 d12=-230.0 z=0.5944655423728814
- **CHANGE_POINT** `nuclear_gen` value=3321 d1=0.0 d12=7.0 z=-0.2697959
- **PERSISTENT_DOWN** `ccgt_gen` value=2279 d1=0.0 d12=-470.0 z=-1.961389347636816

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=0.828 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=0.828 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=0.828 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=0.828 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=0.828 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T10:11:03.790761Z`  
Memory snapshots: **180**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **CHANGE_POINT** `biomass_gen` value=1967 d1=-46.0 d12=-73.0 z=-38.8066893372093
- **PERSISTENT_DOWN** `biomass_gen` value=1967 d1=-46.0 d12=-73.0 z=-38.8066893372093
- **ROBUST_OUTLIER** `biomass_gen` value=1967 d1=-46.0 d12=-73.0 z=-38.8066893372093
- **CHANGE_POINT** `margin` value=3.434e+04 d1=0.0 d12=-154.0 z=2.9334951031746033
- **CHANGE_POINT** `ccgt_gen` value=1807 d1=-23.0 d12=-703.0 z=-2.579585651648999
- **CHANGE_POINT** `thermal_base` value=5140 d1=-14.0 d12=-687.0 z=-2.5236702233487835
- **CHANGE_POINT** `nuclear_gen` value=3333 d1=9.0 d12=16.0 z=2.02346925
- **REVERSAL** `ps_gen` value=-1229 d1=3.0 d12=-69.0 z=-2.9808095403225807
- **PERSISTENT_DOWN** `ccgt_gen` value=1807 d1=-23.0 d12=-703.0 z=-2.579585651648999
- **PERSISTENT_DOWN** `thermal_base` value=5140 d1=-14.0 d12=-687.0 z=-2.5236702233487835
- **ACCELERATION** `wind_gen` value=1.175e+04 d1=-66.0 d12=-294.0 z=-2.3033107420212766
- **PERSISTENT_UP** `nuclear_gen` value=3333 d1=9.0 d12=16.0 z=2.02346925
- **ACCELERATION** `nuclear_gen` value=3333 d1=9.0 d12=16.0 z=2.02346925
- **REVERSAL** `interconnector_net` value=1.144e+04 d1=-83.0 d12=853.0 z=1.1947157956360839

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

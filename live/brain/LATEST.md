# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T10:06:53.196731Z`  
Memory snapshots: **179**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **CHANGE_POINT** `biomass_gen` value=2013 d1=-26.0 d12=-26.0 z=-39.20266034756098
- **PERSISTENT_DOWN** `biomass_gen` value=2013 d1=-26.0 d12=-26.0 z=-39.20266034756098
- **ACCELERATION** `biomass_gen` value=2013 d1=-26.0 d12=-26.0 z=-39.20266034756098
- **ROBUST_OUTLIER** `biomass_gen` value=2013 d1=-26.0 d12=-26.0 z=-39.20266034756098
- **CHANGE_POINT** `margin` value=3.434e+04 d1=0.0 d12=266.0 z=2.9334951031746033
- **CHANGE_POINT** `ccgt_gen` value=1830 d1=-16.0 d12=-670.0 z=-2.559724351590106
- **CHANGE_POINT** `thermal_base` value=5154 d1=-13.0 d12=-660.0 z=-2.496076173451835
- **PERSISTENT_DOWN** `ps_gen` value=-1232 d1=-10.0 d12=-246.0 z=-2.9908515713399506
- **ACCELERATION** `ps_gen` value=-1232 d1=-10.0 d12=-246.0 z=-2.9908515713399506
- **PERSISTENT_DOWN** `ccgt_gen` value=1830 d1=-16.0 d12=-670.0 z=-2.559724351590106
- **PERSISTENT_DOWN** `thermal_base` value=5154 d1=-13.0 d12=-660.0 z=-2.496076173451835
- **REVERSAL** `wind_gen` value=1.181e+04 d1=37.0 d12=-187.0 z=-2.447187169871795
- **CHANGE_POINT** `nuclear_gen` value=3324 d1=3.0 d12=10.0 z=0.25293365624999997
- **REVERSAL** `interconnector_net` value=1.152e+04 d1=-116.0 d12=984.0 z=1.213533589346381

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

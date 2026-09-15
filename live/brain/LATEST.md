# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T10:02:43.028914Z`  
Memory snapshots: **178**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **CHANGE_POINT** `biomass_gen` value=2039 d1=-1.0 d12=0.0 z=-43.691947138888885
- **PERSISTENT_DOWN** `biomass_gen` value=2039 d1=-1.0 d12=0.0 z=-43.691947138888885
- **ACCELERATION** `biomass_gen` value=2039 d1=-1.0 d12=0.0 z=-43.691947138888885
- **ROBUST_OUTLIER** `biomass_gen` value=2039 d1=-1.0 d12=0.0 z=-43.691947138888885
- **CHANGE_POINT** `margin` value=3.434e+04 d1=0.0 d12=266.0 z=2.9334951031746033
- **CHANGE_POINT** `ccgt_gen` value=1846 d1=-96.0 d12=-654.0 z=-2.5625804159738714
- **CHANGE_POINT** `thermal_base` value=5167 d1=-99.0 d12=-647.0 z=-2.521662962660444
- **PERSISTENT_DOWN** `ps_gen` value=-1222 d1=-121.0 d12=-236.0 z=-2.957378134615385
- **REVERSAL** `wind_gen` value=1.178e+04 d1=48.0 d12=-224.0 z=-2.8157547519404917
- **ACCELERATION** `wind_gen` value=1.178e+04 d1=48.0 d12=-224.0 z=-2.8157547519404917
- **PERSISTENT_DOWN** `ccgt_gen` value=1846 d1=-96.0 d12=-654.0 z=-2.5625804159738714
- **PERSISTENT_DOWN** `thermal_base` value=5167 d1=-99.0 d12=-647.0 z=-2.521662962660444
- **CHANGE_POINT** `nuclear_gen` value=3321 d1=-3.0 d12=7.0 z=-0.29977322222222225

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=0.906 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

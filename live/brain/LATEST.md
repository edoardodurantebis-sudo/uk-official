# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T09:54:19.998323Z`  
Memory snapshots: **176**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **PERSISTENT_DOWN** `biomass_gen` value=2039 d1=-2.0 d12=-5.0 z=-52.43033656666667
- **ACCELERATION** `biomass_gen` value=2039 d1=-2.0 d12=-5.0 z=-52.43033656666667
- **ROBUST_OUTLIER** `biomass_gen` value=2039 d1=-2.0 d12=-5.0 z=-52.43033656666667
- **CHANGE_POINT** `wind_gen` value=1.155e+04 d1=3.0 d12=-475.0 z=-3.780827217754173
- **CHANGE_POINT** `margin` value=3.434e+04 d1=0.0 d12=266.0 z=2.9334951031746033
- **CHANGE_POINT** `thermal_base` value=5424 d1=-176.0 d12=-472.0 z=-2.2273847558139535
- **CHANGE_POINT** `ccgt_gen` value=2098 d1=-181.0 d12=-483.0 z=-2.209281353458738
- **REVERSAL** `wind_gen` value=1.155e+04 d1=3.0 d12=-475.0 z=-3.780827217754173
- **ROBUST_OUTLIER** `wind_gen` value=1.155e+04 d1=3.0 d12=-475.0 z=-3.780827217754173
- **ACCELERATION** `margin` value=3.434e+04 d1=0.0 d12=266.0 z=2.9334951031746033
- **CHANGE_POINT** `imbalance` value=-365 d1=0.0 d12=-230.0 z=0.5944655423728814
- **CHANGE_POINT** `nuclear_gen` value=3326 d1=5.0 d12=11.0 z=0.40469384999999997
- **PERSISTENT_DOWN** `thermal_base` value=5424 d1=-176.0 d12=-472.0 z=-2.2273847558139535

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=0.828 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=0.828 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=0.828 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=0.828 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=0.828 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

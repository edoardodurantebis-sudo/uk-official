# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T12:32:04.458827Z`  
Memory snapshots: **1488**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.676e+04 d1=0.0 d12=-18.0 z=-43.97408664215686
- **ACCELERATION** `ind_generation` value=1.676e+04 d1=0.0 d12=-18.0 z=-43.97408664215686
- **ROBUST_OUTLIER** `ind_generation` value=1.676e+04 d1=0.0 d12=-18.0 z=-43.97408664215686
- **CHANGE_POINT** `imbalance` value=-3250 d1=0.0 d12=104.0 z=-7.742084306862745
- **PERSISTENT_UP** `imbalance` value=-3250 d1=0.0 d12=104.0 z=-7.742084306862745
- **ROBUST_OUTLIER** `imbalance` value=-3250 d1=0.0 d12=104.0 z=-7.742084306862745
- **CHANGE_POINT** `wind_gen` value=1.535e+04 d1=48.0 d12=-292.0 z=-2.6249472229381445
- **ROBUST_OUTLIER** `demand_forecast` value=1.951e+04 d1=0.0 d12=-122.0 z=3.2718281479508198
- **CHANGE_POINT** `nuclear_gen` value=3329 d1=1.0 d12=0.0 z=-1.21408155
- **REVERSAL** `residual_proxy` value=1.285e+04 d1=1.0 d12=-121.0 z=2.954730270344828
- **CHANGE_POINT** `ccgt_gen` value=2974 d1=33.0 d12=184.0 z=-0.7626922557692308
- **CHANGE_POINT** `thermal_base` value=6303 d1=34.0 d12=184.0 z=-0.7626140389447237
- **REVERSAL** `wind_gen` value=1.535e+04 d1=48.0 d12=-292.0 z=-2.6249472229381445
- **CHANGE_POINT** `margin` value=3.676e+04 d1=0.0 d12=98.0 z=-0.32056138295053005
- **PERSISTENT_DOWN** `wind_forecast` value=6655 d1=-1.0 d12=-1.0 z=-1.2727328326086955

## Nearest historical live analogues

- `2026-09-19T11:24:42.200097Z` distance=0.035 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.035 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.035 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.035 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T07:48:55.634175Z` distance=0.304 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

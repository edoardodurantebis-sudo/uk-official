# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T12:40:30.410850Z`  
Memory snapshots: **1490**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.676e+04 d1=0.0 d12=-18.0 z=-43.97408664215686
- **ROBUST_OUTLIER** `ind_generation` value=1.676e+04 d1=0.0 d12=-18.0 z=-43.97408664215686
- **CHANGE_POINT** `imbalance` value=-3250 d1=0.0 d12=104.0 z=-7.742084306862745
- **ROBUST_OUTLIER** `imbalance` value=-3250 d1=0.0 d12=104.0 z=-7.742084306862745
- **CHANGE_POINT** `nuclear_gen` value=3323 d1=0.0 d12=-7.0 z=-2.83285695
- **CHANGE_POINT** `wind_gen` value=1.53e+04 d1=0.0 d12=-336.0 z=-2.710806423809524
- **ROBUST_OUTLIER** `demand_forecast` value=1.951e+04 d1=0.0 d12=0.0 z=3.2718281479508198
- **PERSISTENT_UP** `residual_proxy` value=1.285e+04 d1=0.0 d12=1.0 z=2.954730270344828
- **PERSISTENT_DOWN** `nuclear_gen` value=3323 d1=0.0 d12=-7.0 z=-2.83285695
- **ACCELERATION** `nuclear_gen` value=3323 d1=0.0 d12=-7.0 z=-2.83285695
- **PERSISTENT_DOWN** `wind_gen` value=1.53e+04 d1=0.0 d12=-336.0 z=-2.710806423809524
- **CHANGE_POINT** `thermal_base` value=6322 d1=0.0 d12=206.0 z=-0.6561249300742574
- **CHANGE_POINT** `ccgt_gen` value=2999 d1=0.0 d12=213.0 z=-0.6404246111111112
- **CHANGE_POINT** `margin` value=3.676e+04 d1=0.0 d12=98.0 z=-0.32574101032315983
- **PERSISTENT_DOWN** `wind_forecast` value=6655 d1=0.0 d12=-1.0 z=-1.2727328326086955

## Nearest historical live analogues

- `2026-09-19T11:24:42.200097Z` distance=0.035 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.035 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.035 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.035 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:41:32.574175Z` distance=0.035 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

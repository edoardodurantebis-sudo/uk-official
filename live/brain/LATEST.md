# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T12:44:42.746708Z`  
Memory snapshots: **1491**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.676e+04 d1=0.0 d12=-18.0 z=-40.02775480654762
- **ROBUST_OUTLIER** `ind_generation` value=1.676e+04 d1=0.0 d12=-18.0 z=-40.02775480654762
- **CHANGE_POINT** `imbalance` value=-3250 d1=0.0 d12=104.0 z=-7.738434847327282
- **ROBUST_OUTLIER** `imbalance` value=-3250 d1=0.0 d12=104.0 z=-7.738434847327282
- **CHANGE_POINT** `wind_gen` value=1.529e+04 d1=-8.0 d12=-456.0 z=-2.6854103534883724
- **CHANGE_POINT** `nuclear_gen` value=3326 d1=3.0 d12=-8.0 z=-2.02346925
- **ROBUST_OUTLIER** `demand_forecast` value=1.951e+04 d1=0.0 d12=0.0 z=3.2718281479508198
- **PERSISTENT_DOWN** `wind_gen` value=1.529e+04 d1=-8.0 d12=-456.0 z=-2.6854103534883724
- **CHANGE_POINT** `thermal_base` value=6341 d1=19.0 d12=219.0 z=-0.6010642835443037
- **CHANGE_POINT** `ccgt_gen` value=3015 d1=16.0 d12=227.0 z=-0.5923627597150259
- **CHANGE_POINT** `margin` value=3.676e+04 d1=0.0 d12=-24.0 z=-0.23222737573443009
- **REVERSAL** `nuclear_gen` value=3326 d1=3.0 d12=-8.0 z=-2.02346925
- **ACCELERATION** `nuclear_gen` value=3326 d1=3.0 d12=-8.0 z=-2.02346925
- **PERSISTENT_UP** `thermal_base` value=6341 d1=19.0 d12=219.0 z=-0.6010642835443037
- **PERSISTENT_UP** `ccgt_gen` value=3015 d1=16.0 d12=227.0 z=-0.5923627597150259

## Nearest historical live analogues

- `2026-09-19T11:50:05.858742Z` distance=0.031 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.035 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.035 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.035 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.035 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

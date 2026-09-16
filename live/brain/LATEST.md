# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T03:12:02.701601Z`  
Memory snapshots: **422**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=1.0 z=26.994413950549454
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=1.0 z=26.994413950549454
- **CHANGE_POINT** `ccgt_gen` value=2532 d1=-68.0 d12=-504.0 z=-7.242982238461538
- **CHANGE_POINT** `thermal_base` value=5863 d1=-67.0 d12=-503.0 z=-6.398537898648649
- **PERSISTENT_DOWN** `ccgt_gen` value=2532 d1=-68.0 d12=-504.0 z=-7.242982238461538
- **ROBUST_OUTLIER** `ccgt_gen` value=2532 d1=-68.0 d12=-504.0 z=-7.242982238461538
- **PERSISTENT_DOWN** `thermal_base` value=5863 d1=-67.0 d12=-503.0 z=-6.398537898648649
- **ROBUST_OUTLIER** `thermal_base` value=5863 d1=-67.0 d12=-503.0 z=-6.398537898648649
- **CHANGE_POINT** `imbalance` value=6027 d1=0.0 d12=20.0 z=2.378463855263158
- **CHANGE_POINT** `ind_generation` value=2.515e+04 d1=0.0 d12=20.0 z=2.325826724137931
- **CHANGE_POINT** `interconnector_net` value=2403 d1=-225.0 d12=-1494.0 z=-2.274764027267819
- **CHANGE_POINT** `wind_gen` value=9788 d1=-61.0 d12=-361.0 z=-1.1147147564732143
- **PERSISTENT_DOWN** `interconnector_net` value=2403 d1=-225.0 d12=-1494.0 z=-2.274764027267819
- **PERSISTENT_DOWN** `wind_gen` value=9788 d1=-61.0 d12=-361.0 z=-1.1147147564732143
- **ACCELERATION** `nuclear_gen` value=3331 d1=1.0 d12=1.0 z=0.94428565

## Nearest historical live analogues

- `2026-09-16T01:51:47.907050Z` distance=0.980 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:56:00.416093Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:00:10.670180Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:04:21.558749Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:08:33.939552Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

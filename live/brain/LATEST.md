# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T02:51:04.821431Z`  
Memory snapshots: **417**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=1.0 d12=1462.0 z=36.12487749264706
- **PERSISTENT_UP** `margin` value=3.754e+04 d1=1.0 d12=1462.0 z=36.12487749264706
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=1.0 d12=1462.0 z=36.12487749264706
- **CHANGE_POINT** `ccgt_gen` value=2686 d1=-7.0 d12=-459.0 z=-4.816548599358975
- **CHANGE_POINT** `thermal_base` value=6014 d1=-9.0 d12=-457.0 z=-4.72142825
- **PERSISTENT_DOWN** `ccgt_gen` value=2686 d1=-7.0 d12=-459.0 z=-4.816548599358975
- **ROBUST_OUTLIER** `ccgt_gen` value=2686 d1=-7.0 d12=-459.0 z=-4.816548599358975
- **PERSISTENT_DOWN** `thermal_base` value=6014 d1=-9.0 d12=-457.0 z=-4.72142825
- **ROBUST_OUTLIER** `thermal_base` value=6014 d1=-9.0 d12=-457.0 z=-4.72142825
- **CHANGE_POINT** `imbalance` value=6027 d1=20.0 d12=58.0 z=2.378463855263158
- **CHANGE_POINT** `ind_generation` value=2.515e+04 d1=20.0 d12=58.0 z=2.325826724137931
- **CHANGE_POINT** `interconnector_net` value=3444 d1=24.0 d12=-1127.0 z=-0.7582546757559395
- **PERSISTENT_UP** `imbalance` value=6027 d1=20.0 d12=58.0 z=2.378463855263158
- **PERSISTENT_UP** `ind_generation` value=2.515e+04 d1=20.0 d12=58.0 z=2.325826724137931
- **PERSISTENT_DOWN** `wind_gen` value=9897 d1=-115.0 d12=-327.0 z=-0.9665030330090341

## Nearest historical live analogues

- `2026-09-16T01:51:47.907050Z` distance=0.980 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:56:00.416093Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:22:27.619756Z` distance=1.013 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:26:39.733829Z` distance=1.013 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 43.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:30:51.171877Z` distance=1.013 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 43.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

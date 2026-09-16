# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T02:55:13.457050Z`  
Memory snapshots: **418**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=1462.0 z=36.12487749264706
- **PERSISTENT_UP** `margin` value=3.754e+04 d1=0.0 d12=1462.0 z=36.12487749264706
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=1462.0 z=36.12487749264706
- **CHANGE_POINT** `ccgt_gen` value=2686 d1=0.0 d12=-435.0 z=-4.84327155967742
- **CHANGE_POINT** `thermal_base` value=6014 d1=0.0 d12=-435.0 z=-4.772981606687898
- **PERSISTENT_DOWN** `ccgt_gen` value=2686 d1=0.0 d12=-435.0 z=-4.84327155967742
- **ROBUST_OUTLIER** `ccgt_gen` value=2686 d1=0.0 d12=-435.0 z=-4.84327155967742
- **PERSISTENT_DOWN** `thermal_base` value=6014 d1=0.0 d12=-435.0 z=-4.772981606687898
- **ROBUST_OUTLIER** `thermal_base` value=6014 d1=0.0 d12=-435.0 z=-4.772981606687898
- **CHANGE_POINT** `imbalance` value=6027 d1=0.0 d12=58.0 z=2.378463855263158
- **CHANGE_POINT** `ind_generation` value=2.515e+04 d1=0.0 d12=58.0 z=2.325826724137931
- **CHANGE_POINT** `interconnector_net` value=3444 d1=0.0 d12=-840.0 z=-0.7582546757559395
- **PERSISTENT_UP** `imbalance` value=6027 d1=0.0 d12=58.0 z=2.378463855263158
- **PERSISTENT_UP** `ind_generation` value=2.515e+04 d1=0.0 d12=58.0 z=2.325826724137931
- **PERSISTENT_DOWN** `wind_gen` value=9897 d1=0.0 d12=-293.0 z=-0.9562446881205673

## Nearest historical live analogues

- `2026-09-16T01:51:47.907050Z` distance=0.980 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:56:00.416093Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:00:10.670180Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:22:27.619756Z` distance=1.013 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:26:39.733829Z` distance=1.013 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 43.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

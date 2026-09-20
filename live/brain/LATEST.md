# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T11:18:52.907637Z`  
Memory snapshots: **1812**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=37.09693625
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=37.09693625
- **CHANGE_POINT** `ind_generation` value=1.536e+04 d1=0.0 d12=-668.0 z=13.74194070093458
- **ROBUST_OUTLIER** `ind_generation` value=1.536e+04 d1=0.0 d12=-668.0 z=13.74194070093458
- **CHANGE_POINT** `margin` value=3.579e+04 d1=0.0 d12=-3985.0 z=-7.235054647515527
- **ROBUST_OUTLIER** `margin` value=3.579e+04 d1=0.0 d12=-3985.0 z=-7.235054647515527
- **CHANGE_POINT** `imbalance` value=-5746 d1=0.0 d12=-1606.0 z=2.1600481713395636
- **ROBUST_OUTLIER** `residual_proxy` value=1.824e+04 d1=0.0 d12=1031.0 z=3.883043794392523
- **PERSISTENT_DOWN** `wind_gen` value=1.338e+04 d1=-137.0 d12=-653.0 z=-3.4542050833333335
- **ROBUST_OUTLIER** `wind_gen` value=1.338e+04 d1=-137.0 d12=-653.0 z=-3.4542050833333335
- **CHANGE_POINT** `ps_gen` value=-665 d1=9.0 d12=37.0 z=0.9467608417431193
- **PERSISTENT_DOWN** `nuclear_gen` value=3331 d1=0.0 d12=-6.0 z=-1.686224375
- **PERSISTENT_DOWN** `thermal_base` value=5723 d1=-2.0 d12=-126.0 z=-1.2031438783783783
- **PERSISTENT_DOWN** `ccgt_gen` value=2392 d1=-2.0 d12=-120.0 z=-1.1929092260089686
- **PERSISTENT_UP** `ps_gen` value=-665 d1=9.0 d12=37.0 z=0.9467608417431193

## Nearest historical live analogues

- `2026-09-20T04:50:36.902238Z` distance=0.754 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:54:47.005275Z` distance=0.754 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:58:57.948602Z` distance=0.754 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:03:10.294370Z` distance=0.754 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:07:21.689505Z` distance=0.754 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 161.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

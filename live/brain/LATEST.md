# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T08:22:11.835472Z`  
Memory snapshots: **496**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.656e+04 d1=235.0 d12=235.0 z=-40.72231865625
- **PERSISTENT_UP** `margin` value=3.656e+04 d1=235.0 d12=235.0 z=-40.72231865625
- **ACCELERATION** `margin` value=3.656e+04 d1=235.0 d12=235.0 z=-40.72231865625
- **ROBUST_OUTLIER** `margin` value=3.656e+04 d1=235.0 d12=235.0 z=-40.72231865625
- **PERSISTENT_DOWN** `ind_demand` value=-1.267e+04 d1=-2.0 d12=-2.0 z=-23.814676557692305
- **ACCELERATION** `ind_demand` value=-1.267e+04 d1=-2.0 d12=-2.0 z=-23.814676557692305
- **ROBUST_OUTLIER** `ind_demand` value=-1.267e+04 d1=-2.0 d12=-2.0 z=-23.814676557692305
- **CHANGE_POINT** `biomass_gen` value=3243 d1=1.0 d12=11.0 z=3.709693625
- **PERSISTENT_UP** `biomass_gen` value=3243 d1=1.0 d12=11.0 z=3.709693625
- **ROBUST_OUTLIER** `biomass_gen` value=3243 d1=1.0 d12=11.0 z=3.709693625
- **CHANGE_POINT** `wind_gen` value=6912 d1=-83.0 d12=-987.0 z=-1.611300657344485
- **CHANGE_POINT** `ps_gen` value=230 d1=0.0 d12=8.0 z=1.3489795
- **CHANGE_POINT** `ind_generation` value=2.656e+04 d1=123.0 d12=123.0 z=1.2546452692307692
- **PERSISTENT_UP** `interconnector_net` value=1.01e+04 d1=0.0 d12=313.0 z=2.482937651474531
- **PERSISTENT_DOWN** `wind_gen` value=6912 d1=-83.0 d12=-987.0 z=-1.611300657344485

## Nearest historical live analogues

- `2026-09-16T07:23:21.620957Z` distance=0.135 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:27:32.881343Z` distance=0.135 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:19:10.764986Z` distance=0.528 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:54:08.413156Z` distance=0.655 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:58:18.248300Z` distance=0.655 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

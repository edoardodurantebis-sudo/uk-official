# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T21:48:54.630983Z`  
Memory snapshots: **1279**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.624e+04 d1=0.0 d12=12.0 z=18.592456586956523
- **CHANGE_POINT** `ccgt_gen` value=3956 d1=-31.0 d12=-853.0 z=16.736491423728815
- **CHANGE_POINT** `thermal_base` value=7299 d1=-33.0 d12=-849.0 z=16.63552450630252
- **PERSISTENT_UP** `ind_generation` value=2.624e+04 d1=0.0 d12=12.0 z=18.592456586956523
- **ROBUST_OUTLIER** `ind_generation` value=2.624e+04 d1=0.0 d12=12.0 z=18.592456586956523
- **PERSISTENT_DOWN** `ccgt_gen` value=3956 d1=-31.0 d12=-853.0 z=16.736491423728815
- **ROBUST_OUTLIER** `ccgt_gen` value=3956 d1=-31.0 d12=-853.0 z=16.736491423728815
- **PERSISTENT_DOWN** `thermal_base` value=7299 d1=-33.0 d12=-849.0 z=16.63552450630252
- **ROBUST_OUTLIER** `thermal_base` value=7299 d1=-33.0 d12=-849.0 z=16.63552450630252
- **CHANGE_POINT** `interconnector_net` value=-6403 d1=-23.0 d12=-5596.0 z=-10.040799099383918
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=0.0 d12=-6.0 z=-10.94172261111111
- **PERSISTENT_DOWN** `interconnector_net` value=-6403 d1=-23.0 d12=-5596.0 z=-10.040799099383918
- **ACCELERATION** `interconnector_net` value=-6403 d1=-23.0 d12=-5596.0 z=-10.040799099383918
- **ROBUST_OUTLIER** `interconnector_net` value=-6403 d1=-23.0 d12=-5596.0 z=-10.040799099383918
- **PERSISTENT_UP** `margin` value=3.753e+04 d1=0.0 d12=5.0 z=-4.39184803125

## Nearest historical live analogues

- `2026-09-18T18:54:36.333288Z` distance=0.293 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:58:51.197302Z` distance=0.293 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:03:04.185551Z` distance=0.293 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:07:15.585093Z` distance=0.293 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -511.0}
- `2026-09-18T17:51:12.400587Z` distance=0.317 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

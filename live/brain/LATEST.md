# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T20:36:00.984640Z`  
Memory snapshots: **328**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `wind_gen` value=1.193e+04 d1=67.0 d12=1494.0 z=5.905532477777778
- **PERSISTENT_UP** `wind_gen` value=1.193e+04 d1=67.0 d12=1494.0 z=5.905532477777778
- **ROBUST_OUTLIER** `wind_gen` value=1.193e+04 d1=67.0 d12=1494.0 z=5.905532477777778
- **CHANGE_POINT** `margin` value=3.57e+04 d1=0.0 d12=52.0 z=1.4484617640117994
- **CHANGE_POINT** `thermal_base` value=1.273e+04 d1=-242.0 d12=-1095.0 z=-1.3093931941309256
- **CHANGE_POINT** `ccgt_gen` value=9410 d1=-243.0 d12=-1098.0 z=-1.298317153307175
- **CHANGE_POINT** `ind_demand` value=-1.191e+04 d1=0.0 d12=-3.0 z=0.67448975
- **CHANGE_POINT** `imbalance` value=5788 d1=0.0 d12=32.0 z=0.30833817142857145
- **CHANGE_POINT** `ind_generation` value=2.491e+04 d1=0.0 d12=32.0 z=0.30833817142857145
- **PERSISTENT_DOWN** `thermal_base` value=1.273e+04 d1=-242.0 d12=-1095.0 z=-1.3093931941309256
- **PERSISTENT_DOWN** `ccgt_gen` value=9410 d1=-243.0 d12=-1098.0 z=-1.298317153307175
- **PERSISTENT_DOWN** `ps_gen` value=-262 d1=-4.0 d12=-423.0 z=-0.6869145611842105
- **PERSISTENT_UP** `biomass_gen` value=3277 d1=3.0 d12=14.0 z=0.6379040751043116
- **REVERSAL** `interconnector_net` value=77 d1=25.0 d12=-600.0 z=-0.15094940117438513
- **ACCELERATION** `interconnector_net` value=77 d1=25.0 d12=-600.0 z=-0.15094940117438513

## Nearest historical live analogues

- `2026-09-15T19:31:50.302711Z` distance=0.034 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:36:02.892054Z` distance=0.034 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:40:15.609389Z` distance=0.034 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:50:55.506503Z` distance=0.086 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.086 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

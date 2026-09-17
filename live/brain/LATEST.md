# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T20:09:24.491695Z`  
Memory snapshots: **968**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.652e+04 d1=0.0 d12=7.0 z=-27.467518755319148
- **ROBUST_OUTLIER** `ind_generation` value=2.652e+04 d1=0.0 d12=7.0 z=-27.467518755319148
- **ROBUST_OUTLIER** `ind_demand` value=-1.116e+04 d1=0.0 d12=0.0 z=26.97959
- **CHANGE_POINT** `interconnector_net` value=-1332 d1=-595.0 d12=-898.0 z=-2.9225385492761693
- **ROBUST_OUTLIER** `imbalance` value=9708 d1=0.0 d12=7.0 z=-4.08535880221519
- **CHANGE_POINT** `wind_gen` value=1.601e+04 d1=118.0 d12=699.0 z=1.3923633926608026
- **PERSISTENT_DOWN** `interconnector_net` value=-1332 d1=-595.0 d12=-898.0 z=-2.9225385492761693
- **ACCELERATION** `interconnector_net` value=-1332 d1=-595.0 d12=-898.0 z=-2.9225385492761693
- **CHANGE_POINT** `ps_gen` value=504 d1=1.0 d12=226.0 z=0.7148125067934782
- **CHANGE_POINT** `ccgt_gen` value=5447 d1=-75.0 d12=-1180.0 z=0.21616271044303798
- **CHANGE_POINT** `thermal_base` value=8765 d1=-76.0 d12=-1187.0 z=0.21357555870995423
- **PERSISTENT_UP** `wind_gen` value=1.601e+04 d1=118.0 d12=699.0 z=1.3923633926608026
- **PERSISTENT_UP** `ps_gen` value=504 d1=1.0 d12=226.0 z=0.7148125067934782
- **PERSISTENT_UP** `biomass_gen` value=3006 d1=149.0 d12=20.0 z=0.5532523518987342
- **ACCELERATION** `biomass_gen` value=3006 d1=149.0 d12=20.0 z=0.5532523518987342

## Nearest historical live analogues

- `2026-09-17T18:57:56.745109Z` distance=0.131 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:10:36.600451Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:14:49.284800Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

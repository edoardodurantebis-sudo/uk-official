# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T08:31:21.232151Z`  
Memory snapshots: **498**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low, wind rising.

## Active patterns

- **PERSISTENT_UP** `margin` value=3.656e+04 d1=0.0 d12=235.0 z=-40.72231865625
- **ROBUST_OUTLIER** `margin` value=3.656e+04 d1=0.0 d12=235.0 z=-40.72231865625
- **PERSISTENT_DOWN** `ind_demand` value=-1.267e+04 d1=0.0 d12=-2.0 z=-23.814676557692305
- **ROBUST_OUTLIER** `ind_demand` value=-1.267e+04 d1=0.0 d12=-2.0 z=-23.814676557692305
- **CHANGE_POINT** `wind_gen` value=6719 d1=-118.0 d12=-1125.0 z=-1.6881161106578275
- **CHANGE_POINT** `biomass_gen` value=3236 d1=3.0 d12=7.0 z=1.3489795
- **CHANGE_POINT** `ps_gen` value=230 d1=0.0 d12=4.0 z=1.3489795
- **CHANGE_POINT** `ind_generation` value=2.656e+04 d1=0.0 d12=123.0 z=1.2546452692307692
- **PERSISTENT_DOWN** `residual_proxy` value=-813 d1=-321.0 d12=-428.0 z=-2.513226138535032
- **ACCELERATION** `residual_proxy` value=-813 d1=-321.0 d12=-428.0 z=-2.513226138535032
- **PERSISTENT_UP** `interconnector_net` value=1.024e+04 d1=143.0 d12=457.0 z=2.457218043076923
- **PERSISTENT_UP** `wind_forecast` value=1.933e+04 d1=321.0 d12=321.0 z=2.0535420414012737
- **ACCELERATION** `wind_forecast` value=1.933e+04 d1=321.0 d12=321.0 z=2.0535420414012737
- **PERSISTENT_DOWN** `wind_gen` value=6719 d1=-118.0 d12=-1125.0 z=-1.6881161106578275
- **ACCELERATION** `biomass_gen` value=3236 d1=3.0 d12=7.0 z=1.3489795

## Nearest historical live analogues

- `2026-09-16T07:23:21.620957Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:27:32.881343Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:31:44.991160Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:35:56.436252Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:19:10.764986Z` distance=0.727 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

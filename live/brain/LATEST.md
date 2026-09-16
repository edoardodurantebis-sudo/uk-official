# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T08:39:47.959049Z`  
Memory snapshots: **500**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low, wind rising.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.656e+04 d1=0.0 d12=235.0 z=-40.72231865625
- **ROBUST_OUTLIER** `ind_demand` value=-1.267e+04 d1=0.0 d12=-2.0 z=-23.814676557692305
- **CHANGE_POINT** `wind_gen` value=6695 d1=-24.0 d12=-946.0 z=-1.645473253853804
- **CHANGE_POINT** `biomass_gen` value=3236 d1=0.0 d12=7.0 z=1.3489795
- **CHANGE_POINT** `ps_gen` value=230 d1=0.0 d12=2.0 z=1.3489795
- **PERSISTENT_DOWN** `residual_proxy` value=-813 d1=0.0 d12=-1677.0 z=-2.513226138535032
- **PERSISTENT_UP** `interconnector_net` value=1.024e+04 d1=0.0 d12=454.0 z=2.3282678250728863
- **PERSISTENT_UP** `wind_forecast` value=1.933e+04 d1=0.0 d12=321.0 z=2.0535420414012737
- **PERSISTENT_DOWN** `wind_gen` value=6695 d1=-24.0 d12=-946.0 z=-1.645473253853804
- **PERSISTENT_UP** `biomass_gen` value=3236 d1=0.0 d12=7.0 z=1.3489795
- **PERSISTENT_DOWN** `ccgt_gen` value=7985 d1=-94.0 d12=-287.0 z=0.5008428060190703
- **PERSISTENT_DOWN** `thermal_base` value=1.132e+04 d1=-94.0 d12=-286.0 z=0.5005212376042908

## Nearest historical live analogues

- `2026-09-16T07:23:21.620957Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:27:32.881343Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:31:44.991160Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:35:56.436252Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:40:08.214272Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T08:35:35.956217Z`  
Memory snapshots: **499**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low, wind rising.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.656e+04 d1=0.0 d12=235.0 z=-40.72231865625
- **ROBUST_OUTLIER** `ind_demand` value=-1.267e+04 d1=0.0 d12=-2.0 z=-23.814676557692305
- **CHANGE_POINT** `wind_gen` value=6719 d1=0.0 d12=-1076.0 z=-1.6466876511773547
- **CHANGE_POINT** `biomass_gen` value=3236 d1=0.0 d12=9.0 z=1.3489795
- **CHANGE_POINT** `ps_gen` value=230 d1=0.0 d12=2.0 z=1.3489795
- **CHANGE_POINT** `ind_generation` value=2.656e+04 d1=0.0 d12=123.0 z=1.2546452692307692
- **PERSISTENT_DOWN** `residual_proxy` value=-813 d1=0.0 d12=-428.0 z=-2.513226138535032
- **ACCELERATION** `residual_proxy` value=-813 d1=0.0 d12=-428.0 z=-2.513226138535032
- **PERSISTENT_UP** `interconnector_net` value=1.024e+04 d1=0.0 d12=454.0 z=2.4296153128949216
- **PERSISTENT_UP** `wind_forecast` value=1.933e+04 d1=0.0 d12=321.0 z=2.0535420414012737
- **ACCELERATION** `wind_forecast` value=1.933e+04 d1=0.0 d12=321.0 z=2.0535420414012737
- **PERSISTENT_DOWN** `wind_gen` value=6719 d1=0.0 d12=-1076.0 z=-1.6466876511773547
- **PERSISTENT_DOWN** `ccgt_gen` value=8079 d1=0.0 d12=-170.0 z=0.5483156691623264
- **PERSISTENT_DOWN** `thermal_base` value=1.141e+04 d1=0.0 d12=-168.0 z=0.5481692955186631
- **ACCELERATION** `nuclear_gen` value=3330 d1=0.0 d12=2.0 z=0.337244875

## Nearest historical live analogues

- `2026-09-16T07:23:21.620957Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:27:32.881343Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:31:44.991160Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:35:56.436252Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:40:08.214272Z` distance=0.517 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

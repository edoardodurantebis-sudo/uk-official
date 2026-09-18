# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T22:40:12.982445Z`  
Memory snapshots: **1291**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.618e+04 d1=0.0 d12=-64.0 z=10.11734625
- **ROBUST_OUTLIER** `ind_generation` value=2.618e+04 d1=0.0 d12=-64.0 z=10.11734625
- **CHANGE_POINT** `interconnector_net` value=-8614 d1=0.0 d12=-2211.0 z=-6.240918392602647
- **PERSISTENT_DOWN** `interconnector_net` value=-8614 d1=0.0 d12=-2211.0 z=-6.240918392602647
- **ROBUST_OUTLIER** `interconnector_net` value=-8614 d1=0.0 d12=-2211.0 z=-6.240918392602647
- **CHANGE_POINT** `ind_demand` value=-1.089e+04 d1=0.0 d12=2.0 z=-3.7403522500000004
- **PERSISTENT_DOWN** `thermal_base` value=7027 d1=0.0 d12=-272.0 z=4.277684993421053
- **ROBUST_OUTLIER** `thermal_base` value=7027 d1=0.0 d12=-272.0 z=4.277684993421053
- **PERSISTENT_DOWN** `ccgt_gen` value=3689 d1=0.0 d12=-267.0 z=4.050696103064067
- **ROBUST_OUTLIER** `ccgt_gen` value=3689 d1=0.0 d12=-267.0 z=4.050696103064067
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=0.0 d12=2.0 z=-3.7403522500000004
- **CHANGE_POINT** `biomass_gen` value=952 d1=0.0 d12=49.0 z=-1.527893447769953
- **CHANGE_POINT** `wind_gen` value=1.594e+04 d1=0.0 d12=-914.0 z=-1.0186929099037139
- **CHANGE_POINT** `ps_gen` value=-708 d1=0.0 d12=-814.0 z=-0.6438890808128545
- **CHANGE_POINT** `imbalance` value=8984 d1=0.0 d12=-65.0 z=0.3263660080645161

## Nearest historical live analogues

- `2026-09-18T19:53:59.381022Z` distance=0.023 → {'next30m_imbalance_delta': -59.0, 'next30m_margin_delta': 78.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T21:44:41.914660Z` distance=0.023 → {'next30m_imbalance_delta': -59.0, 'next30m_margin_delta': 78.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:32:42.521831Z` distance=0.033 → {'next30m_imbalance_delta': 17.0, 'next30m_margin_delta': 26.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:36:55.641647Z` distance=0.033 → {'next30m_imbalance_delta': 17.0, 'next30m_margin_delta': 26.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:41:08.223702Z` distance=0.033 → {'next30m_imbalance_delta': -42.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T03:38:54.767220Z`  
Memory snapshots: **733**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2119 d1=86.0 d12=84.0 z=-133.0584325
- **PERSISTENT_UP** `biomass_gen` value=2119 d1=86.0 d12=84.0 z=-133.0584325
- **ACCELERATION** `biomass_gen` value=2119 d1=86.0 d12=84.0 z=-133.0584325
- **ROBUST_OUTLIER** `biomass_gen` value=2119 d1=86.0 d12=84.0 z=-133.0584325
- **ROBUST_OUTLIER** `ind_demand` value=-1.152e+04 d1=0.0 d12=11.0 z=33.31979365
- **CHANGE_POINT** `margin` value=3.585e+04 d1=0.0 d12=1.0 z=11.051880240963856
- **CHANGE_POINT** `interconnector_net` value=-9820 d1=3.0 d12=-3348.0 z=-10.245820488095237
- **ROBUST_OUTLIER** `margin` value=3.585e+04 d1=0.0 d12=1.0 z=11.051880240963856
- **REVERSAL** `interconnector_net` value=-9820 d1=3.0 d12=-3348.0 z=-10.245820488095237
- **ACCELERATION** `interconnector_net` value=-9820 d1=3.0 d12=-3348.0 z=-10.245820488095237
- **ROBUST_OUTLIER** `interconnector_net` value=-9820 d1=3.0 d12=-3348.0 z=-10.245820488095237
- **CHANGE_POINT** `ind_generation` value=2.565e+04 d1=0.0 d12=15.0 z=0.3709693625
- **CHANGE_POINT** `imbalance` value=6527 d1=0.0 d12=15.0 z=0.07708454285714286
- **PERSISTENT_UP** `wind_gen` value=1.362e+04 d1=127.0 d12=223.0 z=0.7917367040139064
- **REVERSAL** `thermal_base` value=6951 d1=-107.0 d12=50.0 z=-0.7572873757884522

## Nearest historical live analogues

- `2026-09-17T02:22:41.615797Z` distance=0.591 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:26:53.112988Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:31:05.012181Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:35:17.375315Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:39:29.397540Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

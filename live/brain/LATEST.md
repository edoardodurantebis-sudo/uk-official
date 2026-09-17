# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T03:43:09.899670Z`  
Memory snapshots: **734**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2308 d1=189.0 d12=274.0 z=-86.28651016071429
- **PERSISTENT_UP** `biomass_gen` value=2308 d1=189.0 d12=274.0 z=-86.28651016071429
- **ACCELERATION** `biomass_gen` value=2308 d1=189.0 d12=274.0 z=-86.28651016071429
- **ROBUST_OUTLIER** `biomass_gen` value=2308 d1=189.0 d12=274.0 z=-86.28651016071429
- **ROBUST_OUTLIER** `ind_demand` value=-1.152e+04 d1=0.0 d12=0.0 z=33.31979365
- **CHANGE_POINT** `interconnector_net` value=-9820 d1=0.0 d12=-3347.0 z=-10.333429922768879
- **CHANGE_POINT** `margin` value=3.585e+04 d1=0.0 d12=-10.0 z=10.020990571428571
- **PERSISTENT_DOWN** `interconnector_net` value=-9820 d1=0.0 d12=-3347.0 z=-10.333429922768879
- **ROBUST_OUTLIER** `interconnector_net` value=-9820 d1=0.0 d12=-3347.0 z=-10.333429922768879
- **ROBUST_OUTLIER** `margin` value=3.585e+04 d1=0.0 d12=-10.0 z=10.020990571428571
- **CHANGE_POINT** `ind_generation` value=2.565e+04 d1=0.0 d12=14.0 z=0.3709693625
- **CHANGE_POINT** `imbalance` value=6527 d1=0.0 d12=14.0 z=0.07708454285714286
- **REVERSAL** `ccgt_gen` value=3518 d1=-120.0 d12=3.0 z=-0.8385548243243243
- **ACCELERATION** `ccgt_gen` value=3518 d1=-120.0 d12=3.0 z=-0.8385548243243243
- **PERSISTENT_UP** `wind_gen` value=1.373e+04 d1=115.0 d12=296.0 z=0.8352881064

## Nearest historical live analogues

- `2026-09-17T02:22:41.615797Z` distance=0.591 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:26:53.112988Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:31:05.012181Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:35:17.375315Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:39:29.397540Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

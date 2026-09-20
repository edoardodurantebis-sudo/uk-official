# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T07:35:11.628590Z`  
Memory snapshots: **1759**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=888 d1=0.0 d12=1.0 z=-7.7505004
- **CHANGE_POINT** `margin` value=3.803e+04 d1=0.0 d12=553.0 z=6.784573367647059
- **PERSISTENT_UP** `biomass_gen` value=888 d1=0.0 d12=1.0 z=-7.7505004
- **ACCELERATION** `biomass_gen` value=888 d1=0.0 d12=1.0 z=-7.7505004
- **ROBUST_OUTLIER** `biomass_gen` value=888 d1=0.0 d12=1.0 z=-7.7505004
- **ROBUST_OUTLIER** `margin` value=3.803e+04 d1=0.0 d12=553.0 z=6.784573367647059
- **CHANGE_POINT** `interconnector_net` value=-6754 d1=0.0 d12=2608.0 z=2.772185144736842
- **PERSISTENT_UP** `interconnector_net` value=-6754 d1=0.0 d12=2608.0 z=2.772185144736842
- **ACCELERATION** `interconnector_net` value=-6754 d1=0.0 d12=2608.0 z=2.772185144736842
- **CHANGE_POINT** `imbalance` value=-6364 d1=0.0 d12=490.0 z=0.3362135451070336
- **CHANGE_POINT** `ind_generation` value=1.359e+04 d1=0.0 d12=490.0 z=0.3362135451070336
- **PERSISTENT_UP** `nuclear_gen` value=3339 d1=0.0 d12=12.0 z=2.0234692499999998
- **PERSISTENT_DOWN** `ps_gen` value=-841 d1=0.0 d12=-36.0 z=-1.3346286542553192
- **ACCELERATION** `ps_gen` value=-841 d1=0.0 d12=-36.0 z=-1.3346286542553192
- **PERSISTENT_DOWN** `wind_gen` value=1.566e+04 d1=0.0 d12=-182.0 z=0.8090033753561253

## Nearest historical live analogues

- `2026-09-20T03:50:56.701349Z` distance=0.180 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:55:08.305963Z` distance=0.180 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -31.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:59:21.752625Z` distance=0.180 → {'next30m_imbalance_delta': -236.0, 'next30m_margin_delta': -31.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:03:34.178375Z` distance=0.180 → {'next30m_imbalance_delta': -236.0, 'next30m_margin_delta': -31.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:07:46.833176Z` distance=0.180 → {'next30m_imbalance_delta': -236.0, 'next30m_margin_delta': -31.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

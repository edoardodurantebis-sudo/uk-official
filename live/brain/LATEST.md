# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T09:32:44.320157Z`  
Memory snapshots: **1787**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.598e+04 d1=0.0 d12=2861.0 z=23.615572371875
- **ROBUST_OUTLIER** `ind_generation` value=1.598e+04 d1=0.0 d12=2861.0 z=23.615572371875
- **ROBUST_OUTLIER** `margin` value=3.889e+04 d1=0.0 d12=1436.0 z=20.9858288125
- **CHANGE_POINT** `imbalance` value=-4187 d1=0.0 d12=2861.0 z=7.064392644736842
- **CHANGE_POINT** `ind_demand` value=-1.238e+04 d1=0.0 d12=-67.0 z=-6.7448975
- **ROBUST_OUTLIER** `imbalance` value=-4187 d1=0.0 d12=2861.0 z=7.064392644736842
- **ROBUST_OUTLIER** `ind_demand` value=-1.238e+04 d1=0.0 d12=-67.0 z=-6.7448975
- **PERSISTENT_DOWN** `ccgt_gen` value=2287 d1=-116.0 d12=-406.0 z=-4.658453777027027
- **ROBUST_OUTLIER** `ccgt_gen` value=2287 d1=-116.0 d12=-406.0 z=-4.658453777027027
- **PERSISTENT_DOWN** `thermal_base` value=5621 d1=-122.0 d12=-407.0 z=-4.563776428915663
- **ROBUST_OUTLIER** `thermal_base` value=5621 d1=-122.0 d12=-407.0 z=-4.563776428915663
- **CHANGE_POINT** `biomass_gen` value=587 d1=0.0 d12=2.0 z=-0.6832922263458401
- **PERSISTENT_DOWN** `interconnector_net` value=-4457 d1=-594.0 d12=-1213.0 z=2.179064273939064
- **ACCELERATION** `interconnector_net` value=-4457 d1=-594.0 d12=-1213.0 z=2.179064273939064
- **PERSISTENT_DOWN** `wind_gen` value=1.489e+04 d1=-35.0 d12=-168.0 z=-1.0787176312607945

## Nearest historical live analogues

- `2026-09-20T07:22:31.595881Z` distance=0.323 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:26:42.911856Z` distance=0.323 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:30:56.792344Z` distance=0.323 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:35:11.628590Z` distance=0.323 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:39:23.525158Z` distance=0.323 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T19:31:50.302711Z`  
Memory snapshots: **313**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high, wind falling.

## Active patterns

- **PERSISTENT_DOWN** `biomass_gen` value=3272 d1=-7.0 d12=-24.0 z=31.149163
- **ACCELERATION** `biomass_gen` value=3272 d1=-7.0 d12=-24.0 z=31.149163
- **ROBUST_OUTLIER** `biomass_gen` value=3272 d1=-7.0 d12=-24.0 z=31.149163
- **PERSISTENT_UP** `residual_proxy` value=942 d1=116.0 d12=116.0 z=6.7052216323529406
- **ACCELERATION** `residual_proxy` value=942 d1=116.0 d12=116.0 z=6.7052216323529406
- **ROBUST_OUTLIER** `residual_proxy` value=942 d1=116.0 d12=116.0 z=6.7052216323529406
- **PERSISTENT_DOWN** `ind_demand` value=-1.191e+04 d1=0.0 d12=-2.0 z=4.0469384999999996
- **ROBUST_OUTLIER** `ind_demand` value=-1.191e+04 d1=0.0 d12=-2.0 z=4.0469384999999996
- **CHANGE_POINT** `margin` value=3.564e+04 d1=0.0 d12=-11.0 z=1.982413352173913
- **CHANGE_POINT** `ps_gen` value=424 d1=1.0 d12=-380.0 z=0.5501632729028698
- **CHANGE_POINT** `interconnector_net` value=680 d1=1180.0 d12=2241.0 z=-0.458357363260274
- **CHANGE_POINT** `imbalance` value=5756 d1=0.0 d12=19.0 z=-0.23460513043478262
- **CHANGE_POINT** `ind_generation` value=2.488e+04 d1=0.0 d12=19.0 z=-0.23460513043478262
- **PERSISTENT_UP** `wind_gen` value=1.044e+04 d1=53.0 d12=587.0 z=0.7745514162087912
- **PERSISTENT_DOWN** `thermal_base` value=1.383e+04 d1=-20.0 d12=-270.0 z=0.6439960282017735

## Nearest historical live analogues

- `2026-09-15T18:24:34.306197Z` distance=0.084 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:28:44.303435Z` distance=0.084 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:32:54.292117Z` distance=0.084 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:37:05.511843Z` distance=0.084 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:20:25.201646Z` distance=0.087 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T09:47:28.614992Z`  
Memory snapshots: **1162**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1652 d1=-10.0 d12=-321.0 z=-21.541516390625
- **PERSISTENT_DOWN** `biomass_gen` value=1652 d1=-10.0 d12=-321.0 z=-21.541516390625
- **ROBUST_OUTLIER** `biomass_gen` value=1652 d1=-10.0 d12=-321.0 z=-21.541516390625
- **CHANGE_POINT** `ind_demand` value=-1.318e+04 d1=0.0 d12=-1450.0 z=-15.732676578313253
- **ROBUST_OUTLIER** `ind_demand` value=-1.318e+04 d1=0.0 d12=-1450.0 z=-15.732676578313253
- **CHANGE_POINT** `imbalance` value=8100 d1=0.0 d12=-1502.0 z=-8.313086168749999
- **ROBUST_OUTLIER** `imbalance` value=8100 d1=0.0 d12=-1502.0 z=-8.313086168749999
- **CHANGE_POINT** `margin` value=3.621e+04 d1=0.0 d12=-1472.0 z=-5.975025361111111
- **ROBUST_OUTLIER** `margin` value=3.621e+04 d1=0.0 d12=-1472.0 z=-5.975025361111111
- **CHANGE_POINT** `ps_gen` value=-423 d1=-3.0 d12=-650.0 z=-3.63592130859375
- **CHANGE_POINT** `residual_proxy` value=8755 d1=0.0 d12=0.0 z=2.0047334236111114
- **CHANGE_POINT** `wind_gen` value=1.185e+04 d1=35.0 d12=-346.0 z=-1.961851915579119
- **CHANGE_POINT** `ind_generation` value=2.719e+04 d1=0.0 d12=-53.0 z=-1.678130498
- **ROBUST_OUTLIER** `ps_gen` value=-423 d1=-3.0 d12=-650.0 z=-3.63592130859375
- **CHANGE_POINT** `interconnector_net` value=4869 d1=-1.0 d12=1997.0 z=1.1087813348834603

## Nearest historical live analogues

- `2026-09-18T08:34:36.525091Z` distance=1.865 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:38:47.543853Z` distance=1.865 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:43:00.251145Z` distance=1.865 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:47:16.640835Z` distance=1.865 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:22:03.400207Z` distance=1.865 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 74.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

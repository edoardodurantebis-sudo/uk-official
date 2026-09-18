# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T11:15:41.362227Z`  
Memory snapshots: **1183**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1083 d1=0.0 d12=-338.0 z=-45.528058125
- **ROBUST_OUTLIER** `biomass_gen` value=1083 d1=0.0 d12=-338.0 z=-45.528058125
- **CHANGE_POINT** `ind_generation` value=2.565e+04 d1=0.0 d12=-1107.0 z=-7.172276891141141
- **ROBUST_OUTLIER** `ind_generation` value=2.565e+04 d1=0.0 d12=-1107.0 z=-7.172276891141141
- **CHANGE_POINT** `thermal_base` value=5872 d1=-80.0 d12=-497.0 z=-1.437676851517341
- **CHANGE_POINT** `ccgt_gen` value=2538 d1=-82.0 d12=-500.0 z=-1.4362148072615606
- **CHANGE_POINT** `ind_demand` value=-1.074e+04 d1=0.0 d12=3052.0 z=1.1809529015017668
- **CHANGE_POINT** `margin` value=3.813e+04 d1=0.0 d12=1773.0 z=1.0145449989583333
- **REVERSAL** `ps_gen` value=-546 d1=-121.0 d12=175.0 z=-2.0047334236111114
- **ACCELERATION** `ps_gen` value=-546 d1=-121.0 d12=175.0 z=-2.0047334236111114
- **PERSISTENT_DOWN** `thermal_base` value=5872 d1=-80.0 d12=-497.0 z=-1.437676851517341
- **PERSISTENT_DOWN** `ccgt_gen` value=2538 d1=-82.0 d12=-500.0 z=-1.4362148072615606
- **REVERSAL** `interconnector_net` value=5518 d1=-381.0 d12=331.0 z=0.7623898549443353
- **ACCELERATION** `interconnector_net` value=5518 d1=-381.0 d12=331.0 z=0.7623898549443353
- **PERSISTENT_UP** `wind_gen` value=1.219e+04 d1=46.0 d12=197.0 z=-0.253987546484375

## Nearest historical live analogues

- `2026-09-18T05:50:47.091039Z` distance=0.520 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T05:54:59.248868Z` distance=0.520 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T05:59:09.222653Z` distance=0.520 → {'next30m_imbalance_delta': -67.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T06:03:20.906831Z` distance=0.520 → {'next30m_imbalance_delta': -67.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T06:07:33.046654Z` distance=0.520 → {'next30m_imbalance_delta': -67.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

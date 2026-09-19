# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T15:11:32.339324Z`  
Memory snapshots: **1526**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=587 d1=0.0 d12=112.0 z=74.1938725
- **ROBUST_OUTLIER** `biomass_gen` value=587 d1=0.0 d12=112.0 z=74.1938725
- **CHANGE_POINT** `thermal_base` value=7122 d1=-43.0 d12=603.0 z=3.2164279893238437
- **CHANGE_POINT** `ccgt_gen` value=3781 d1=-50.0 d12=591.0 z=3.196494902173913
- **REVERSAL** `thermal_base` value=7122 d1=-43.0 d12=603.0 z=3.2164279893238437
- **ROBUST_OUTLIER** `thermal_base` value=7122 d1=-43.0 d12=603.0 z=3.2164279893238437
- **REVERSAL** `ccgt_gen` value=3781 d1=-50.0 d12=591.0 z=3.196494902173913
- **ROBUST_OUTLIER** `ccgt_gen` value=3781 d1=-50.0 d12=591.0 z=3.196494902173913
- **CHANGE_POINT** `imbalance` value=-3174 d1=0.0 d12=65.0 z=0.30460827419354836
- **PERSISTENT_UP** `nuclear_gen` value=3341 d1=7.0 d12=12.0 z=2.248299166666667
- **ACCELERATION** `nuclear_gen` value=3341 d1=7.0 d12=12.0 z=2.248299166666667
- **REVERSAL** `interconnector_net` value=-3275 d1=129.0 d12=-3.0 z=-1.885749167154812
- **ACCELERATION** `interconnector_net` value=-3275 d1=129.0 d12=-3.0 z=-1.885749167154812
- **REVERSAL** `wind_gen` value=1.418e+04 d1=294.0 d12=-76.0 z=-1.6274025944767443
- **PERSISTENT_DOWN** `ps_gen` value=-633 d1=-86.0 d12=-379.0 z=-0.3125684207317073

## Nearest historical live analogues

- `2026-09-19T13:51:46.286416Z` distance=0.022 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T13:55:56.183209Z` distance=0.022 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 64.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T14:00:11.889935Z` distance=0.022 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 64.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T14:04:22.992173Z` distance=0.022 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 64.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T14:08:33.763772Z` distance=0.022 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 64.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

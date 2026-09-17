# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T15:48:07.638841Z`  
Memory snapshots: **906**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-259 d1=16.0 d12=385.0 z=19.230133297872342
- **PERSISTENT_UP** `ps_gen` value=-259 d1=16.0 d12=385.0 z=19.230133297872342
- **ROBUST_OUTLIER** `ps_gen` value=-259 d1=16.0 d12=385.0 z=19.230133297872342
- **PERSISTENT_UP** `biomass_gen` value=2836 d1=85.0 d12=195.0 z=11.865217537634408
- **ROBUST_OUTLIER** `biomass_gen` value=2836 d1=85.0 d12=195.0 z=11.865217537634408
- **PERSISTENT_UP** `thermal_base` value=6574 d1=86.0 d12=419.0 z=11.216968933333334
- **ROBUST_OUTLIER** `thermal_base` value=6574 d1=86.0 d12=419.0 z=11.216968933333334
- **PERSISTENT_UP** `ccgt_gen` value=3265 d1=88.0 d12=414.0 z=10.422200374293785
- **ROBUST_OUTLIER** `ccgt_gen` value=3265 d1=88.0 d12=414.0 z=10.422200374293785
- **CHANGE_POINT** `imbalance` value=1.166e+04 d1=0.0 d12=-21.0 z=-7.289677682692308
- **ROBUST_OUTLIER** `imbalance` value=1.166e+04 d1=0.0 d12=-21.0 z=-7.289677682692308
- **ROBUST_OUTLIER** `residual_proxy` value=-2671 d1=0.0 d12=0.0 z=3.8890791968085106
- **CHANGE_POINT** `interconnector_net` value=1530 d1=-14.0 d12=867.0 z=0.9435788493637725
- **CHANGE_POINT** `ind_generation` value=2.847e+04 d1=0.0 d12=-21.0 z=-0.41218818055555556
- **CHANGE_POINT** `margin` value=3.564e+04 d1=0.0 d12=-14.0 z=-0.3633829465973535

## Nearest historical live analogues

- `2026-09-17T14:53:15.567552Z` distance=0.008 → {'next30m_imbalance_delta': -261.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T13:54:16.255911Z` distance=0.183 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T13:58:30.621005Z` distance=0.185 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:02:42.198136Z` distance=0.185 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:06:57.483529Z` distance=0.185 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

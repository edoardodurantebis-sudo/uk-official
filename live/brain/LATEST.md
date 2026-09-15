# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T00:43:24.244822Z`  
Memory snapshots: **45**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=0.0 z=7.5162158398773
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=0.0 z=7.5162158398773
- **CHANGE_POINT** `biomass_gen` value=3034 d1=41.0 d12=341.0 z=4.8288690951327435
- **PERSISTENT_UP** `biomass_gen` value=3034 d1=41.0 d12=341.0 z=4.8288690951327435
- **ROBUST_OUTLIER** `biomass_gen` value=3034 d1=41.0 d12=341.0 z=4.8288690951327435
- **CHANGE_POINT** `imbalance` value=264 d1=0.0 d12=54.0 z=2.727284641304348
- **CHANGE_POINT** `ind_generation` value=2.075e+04 d1=0.0 d12=53.0 z=2.727284641304348
- **CHANGE_POINT** `wind_gen` value=1.185e+04 d1=-47.0 d12=-202.0 z=-1.0803862563150073
- **CHANGE_POINT** `margin` value=3.27e+04 d1=0.0 d12=-23.0 z=0.7987378618421054
- **CHANGE_POINT** `ps_gen` value=-70 d1=-58.0 d12=-54.0 z=None
- **ACCELERATION** `wind_gen` value=1.185e+04 d1=-47.0 d12=-202.0 z=-1.0803862563150073
- **PERSISTENT_UP** `interconnector_net` value=311 d1=47.0 d12=1266.0 z=1.0672594222334684
- **PERSISTENT_DOWN** `thermal_base` value=7088 d1=-37.0 d12=-806.0 z=-0.9623653114280016
- **PERSISTENT_DOWN** `ccgt_gen` value=3774 d1=-38.0 d12=-803.0 z=-0.9593041096421471
- **REVERSAL** `nuclear_gen` value=3314 d1=1.0 d12=-3.0 z=0.0

## Nearest historical live analogues

- `2026-09-14T23:32:10.678260Z` distance=0.717 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:36:23.316269Z` distance=0.717 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:40:34.642541Z` distance=0.717 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:48:58.458997Z` distance=0.717 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:28:00.797408Z` distance=6.260 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 4389.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T12:05:01.670377Z`  
Memory snapshots: **1823**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=0.0 z=41.6497420625
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=0.0 z=41.6497420625
- **CHANGE_POINT** `ind_generation` value=1.537e+04 d1=0.0 d12=14.0 z=2.455693293877551
- **CHANGE_POINT** `wind_gen` value=1.259e+04 d1=0.0 d12=-928.0 z=-2.4078181640044574
- **CHANGE_POINT** `imbalance` value=-5732 d1=0.0 d12=14.0 z=0.6897694530744336
- **PERSISTENT_DOWN** `wind_gen` value=1.259e+04 d1=0.0 d12=-928.0 z=-2.4078181640044574
- **ACCELERATION** `ps_gen` value=-667 d1=0.0 d12=7.0 z=0.934384883027523
- **ACCELERATION** `biomass_gen` value=587 d1=0.0 d12=-2.0 z=-0.5951380147058823
- **PERSISTENT_UP** `nuclear_gen` value=3337 d1=0.0 d12=6.0 z=0.5395918
- **ACCELERATION** `ccgt_gen` value=2396 d1=0.0 d12=2.0 z=-0.504327381563927
- **PERSISTENT_UP** `thermal_base` value=5733 d1=0.0 d12=8.0 z=-0.503567915625
- **ACCELERATION** `thermal_base` value=5733 d1=0.0 d12=8.0 z=-0.503567915625
- **PERSISTENT_UP** `interconnector_net` value=-4473 d1=0.0 d12=622.0 z=0.4025218844067203

## Nearest historical live analogues

- `2026-09-20T10:57:55.935414Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:02:06.579348Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:06:18.746524Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:10:29.817646Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T10:53:43.403442Z` distance=0.723 → {'next30m_imbalance_delta': -1606.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

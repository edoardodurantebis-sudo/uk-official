# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T17:33:27.127854Z`  
Memory snapshots: **285**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3178 d1=80.0 d12=770.0 z=62.771062217741935
- **PERSISTENT_UP** `biomass_gen` value=3178 d1=80.0 d12=770.0 z=62.771062217741935
- **ROBUST_OUTLIER** `biomass_gen` value=3178 d1=80.0 d12=770.0 z=62.771062217741935
- **PERSISTENT_UP** `ccgt_gen` value=1.04e+04 d1=5.0 d12=378.0 z=22.012201202067672
- **ROBUST_OUTLIER** `ccgt_gen` value=1.04e+04 d1=5.0 d12=378.0 z=22.012201202067672
- **PERSISTENT_UP** `thermal_base` value=1.373e+04 d1=6.0 d12=384.0 z=21.91460142790262
- **ROBUST_OUTLIER** `thermal_base` value=1.373e+04 d1=6.0 d12=384.0 z=21.91460142790262
- **PERSISTENT_DOWN** `interconnector_net` value=-1725 d1=-956.0 d12=-2295.0 z=-3.456124855991055
- **ACCELERATION** `interconnector_net` value=-1725 d1=-956.0 d12=-2295.0 z=-3.456124855991055
- **ROBUST_OUTLIER** `interconnector_net` value=-1725 d1=-956.0 d12=-2295.0 z=-3.456124855991055
- **PERSISTENT_UP** `ps_gen` value=502 d1=2.0 d12=78.0 z=2.918243366251944
- **CHANGE_POINT** `imbalance` value=5772 d1=0.0 d12=-55.0 z=0.6969727416666667
- **CHANGE_POINT** `ind_generation` value=2.489e+04 d1=0.0 d12=-55.0 z=0.5430956428571428
- **PERSISTENT_UP** `wind_gen` value=1.063e+04 d1=21.0 d12=417.0 z=0.7067619868421052
- **PERSISTENT_DOWN** `imbalance` value=5772 d1=0.0 d12=-55.0 z=0.6969727416666667

## Nearest historical live analogues

- `2026-09-15T16:34:33.511782Z` distance=0.087 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T16:38:45.835004Z` distance=0.087 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T16:21:57.402275Z` distance=0.095 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 53.0}
- `2026-09-15T16:26:08.230608Z` distance=0.095 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 53.0}
- `2026-09-15T16:30:22.410859Z` distance=0.095 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 53.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

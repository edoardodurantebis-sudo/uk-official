# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T23:49:36.074086Z`  
Memory snapshots: **374**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.208e+04 d1=0.0 d12=0.0 z=-37.546596083333334
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=0.0 z=-37.546596083333334
- **CHANGE_POINT** `thermal_base` value=6559 d1=2.0 d12=23.0 z=-6.465231018292683
- **CHANGE_POINT** `ccgt_gen` value=3227 d1=-1.0 d12=16.0 z=-6.440862591886268
- **PERSISTENT_UP** `thermal_base` value=6559 d1=2.0 d12=23.0 z=-6.465231018292683
- **ROBUST_OUTLIER** `thermal_base` value=6559 d1=2.0 d12=23.0 z=-6.465231018292683
- **REVERSAL** `ccgt_gen` value=3227 d1=-1.0 d12=16.0 z=-6.440862591886268
- **ROBUST_OUTLIER** `ccgt_gen` value=3227 d1=-1.0 d12=16.0 z=-6.440862591886268
- **CHANGE_POINT** `biomass_gen` value=3219 d1=-4.0 d12=-42.0 z=-2.7689579210526314
- **CHANGE_POINT** `interconnector_net` value=3987 d1=2.0 d12=-96.0 z=2.1471257041666667
- **PERSISTENT_DOWN** `biomass_gen` value=3219 d1=-4.0 d12=-42.0 z=-2.7689579210526314
- **REVERSAL** `interconnector_net` value=3987 d1=2.0 d12=-96.0 z=2.1471257041666667
- **CHANGE_POINT** `wind_gen` value=1.066e+04 d1=30.0 d12=-1306.0 z=-0.09320061378519974
- **PERSISTENT_UP** `nuclear_gen` value=3332 d1=3.0 d12=7.0 z=2.02346925
- **ACCELERATION** `nuclear_gen` value=3332 d1=3.0 d12=7.0 z=2.02346925

## Nearest historical live analogues

- `2026-09-15T18:20:25.201646Z` distance=0.723 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:50:55.506503Z` distance=0.723 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.723 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:59:22.215947Z` distance=0.723 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:03:35.364442Z` distance=0.723 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

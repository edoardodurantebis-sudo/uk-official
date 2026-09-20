# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T12:00:48.103185Z`  
Memory snapshots: **1822**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=0.0 z=41.6497420625
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=0.0 z=41.6497420625
- **CHANGE_POINT** `wind_gen` value=1.259e+04 d1=-73.0 d12=-928.0 z=-2.467670390364188
- **CHANGE_POINT** `ind_generation` value=1.537e+04 d1=0.0 d12=14.0 z=2.455693293877551
- **CHANGE_POINT** `margin` value=3.578e+04 d1=0.0 d12=-13.0 z=-2.3057213457760315
- **CHANGE_POINT** `imbalance` value=-5732 d1=0.0 d12=14.0 z=0.6897694530744336
- **PERSISTENT_DOWN** `wind_gen` value=1.259e+04 d1=-73.0 d12=-928.0 z=-2.467670390364188
- **REVERSAL** `ps_gen` value=-667 d1=-3.0 d12=7.0 z=0.934384883027523
- **ACCELERATION** `ps_gen` value=-667 d1=-3.0 d12=7.0 z=0.934384883027523
- **ACCELERATION** `biomass_gen` value=587 d1=-2.0 d12=-2.0 z=-0.5995464444444444
- **PERSISTENT_UP** `interconnector_net` value=-4473 d1=111.0 d12=622.0 z=0.5744652179358718
- **REVERSAL** `thermal_base` value=5733 d1=-5.0 d12=8.0 z=-0.5450673625461254
- **ACCELERATION** `thermal_base` value=5733 d1=-5.0 d12=8.0 z=-0.5450673625461254
- **PERSISTENT_UP** `nuclear_gen` value=3337 d1=2.0 d12=6.0 z=0.5395918
- **ACCELERATION** `nuclear_gen` value=3337 d1=2.0 d12=6.0 z=0.5395918

## Nearest historical live analogues

- `2026-09-20T10:57:55.935414Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:02:06.579348Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:06:18.746524Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T10:53:43.403442Z` distance=0.723 → {'next30m_imbalance_delta': -1606.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:50:36.902238Z` distance=0.757 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

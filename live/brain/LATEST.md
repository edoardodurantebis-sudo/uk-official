# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T11:56:36.378175Z`  
Memory snapshots: **1821**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=0.0 z=41.6497420625
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=0.0 z=41.6497420625
- **CHANGE_POINT** `ind_generation` value=1.537e+04 d1=0.0 d12=14.0 z=2.455693293877551
- **CHANGE_POINT** `wind_gen` value=1.266e+04 d1=-105.0 d12=-1040.0 z=-2.4022922602739722
- **CHANGE_POINT** `margin` value=3.578e+04 d1=0.0 d12=-13.0 z=-2.3057213457760315
- **CHANGE_POINT** `residual_proxy` value=1.824e+04 d1=0.0 d12=0.0 z=1.6756600777108435
- **CHANGE_POINT** `imbalance` value=-5732 d1=0.0 d12=14.0 z=0.6897694530744336
- **PERSISTENT_DOWN** `wind_gen` value=1.266e+04 d1=-105.0 d12=-1040.0 z=-2.4022922602739722
- **PERSISTENT_UP** `ccgt_gen` value=2403 d1=6.0 d12=11.0 z=-0.663057720338983
- **ACCELERATION** `ccgt_gen` value=2403 d1=6.0 d12=11.0 z=-0.663057720338983
- **PERSISTENT_UP** `thermal_base` value=5738 d1=11.0 d12=8.0 z=-0.6599122491687448
- **ACCELERATION** `thermal_base` value=5738 d1=11.0 d12=8.0 z=-0.6599122491687448
- **PERSISTENT_UP** `biomass_gen` value=589 d1=3.0 d12=4.0 z=-0.6287616313559322
- **ACCELERATION** `biomass_gen` value=589 d1=3.0 d12=4.0 z=-0.6287616313559322
- **PERSISTENT_UP** `interconnector_net` value=-4584 d1=42.0 d12=556.0 z=0.5262798568717539

## Nearest historical live analogues

- `2026-09-20T10:57:55.935414Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:02:06.579348Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T10:53:43.403442Z` distance=0.717 → {'next30m_imbalance_delta': -1606.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:50:36.902238Z` distance=0.755 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:54:47.005275Z` distance=0.755 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

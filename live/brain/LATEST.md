# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T11:52:26.539051Z`  
Memory snapshots: **1820**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=0.0 z=41.6497420625
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=0.0 z=41.6497420625
- **CHANGE_POINT** `ind_generation` value=1.537e+04 d1=0.0 d12=14.0 z=2.455693293877551
- **CHANGE_POINT** `wind_gen` value=1.276e+04 d1=-37.0 d12=-1032.0 z=-2.342717298723898
- **CHANGE_POINT** `margin` value=3.578e+04 d1=0.0 d12=-13.0 z=-2.3057213457760315
- **CHANGE_POINT** `residual_proxy` value=1.824e+04 d1=0.0 d12=0.0 z=1.6756600777108435
- **CHANGE_POINT** `imbalance` value=-5732 d1=0.0 d12=14.0 z=0.6897694530744336
- **PERSISTENT_DOWN** `wind_gen` value=1.276e+04 d1=-37.0 d12=-1032.0 z=-2.342717298723898
- **PERSISTENT_DOWN** `nuclear_gen` value=3330 d1=0.0 d12=-7.0 z=-1.686224375
- **ACCELERATION** `nuclear_gen` value=3330 d1=0.0 d12=-7.0 z=-1.686224375
- **PERSISTENT_DOWN** `thermal_base` value=5727 d1=-1.0 d12=-3.0 z=-0.6774874822222222
- **ACCELERATION** `thermal_base` value=5727 d1=-1.0 d12=-3.0 z=-0.6774874822222222
- **REVERSAL** `ccgt_gen` value=2397 d1=-1.0 d12=4.0 z=-0.6734800348053892
- **ACCELERATION** `biomass_gen` value=586 d1=0.0 d12=-1.0 z=-0.6588039418604651
- **PERSISTENT_UP** `interconnector_net` value=-4626 d1=0.0 d12=885.0 z=0.43313730511675824

## Nearest historical live analogues

- `2026-09-20T10:57:55.935414Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T10:53:43.403442Z` distance=0.711 → {'next30m_imbalance_delta': -1606.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:50:36.902238Z` distance=0.753 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:54:47.005275Z` distance=0.753 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:58:57.948602Z` distance=0.753 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

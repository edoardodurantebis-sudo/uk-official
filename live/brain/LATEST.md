# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T12:23:39.094440Z`  
Memory snapshots: **1486**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.675e+04 d1=0.0 d12=-28.0 z=-44.018170939542486
- **ROBUST_OUTLIER** `ind_generation` value=1.675e+04 d1=0.0 d12=-28.0 z=-44.018170939542486
- **CHANGE_POINT** `imbalance` value=-3260 d1=0.0 d12=94.0 z=-7.7486969514705875
- **ROBUST_OUTLIER** `imbalance` value=-3260 d1=0.0 d12=94.0 z=-7.7486969514705875
- **ROBUST_OUTLIER** `demand_forecast` value=1.951e+04 d1=0.0 d12=-122.0 z=3.2718281479508198
- **PERSISTENT_DOWN** `wind_gen` value=1.533e+04 d1=-208.0 d12=-300.0 z=-3.0038751161202186
- **ROBUST_OUTLIER** `wind_gen` value=1.533e+04 d1=-208.0 d12=-300.0 z=-3.0038751161202186
- **PERSISTENT_DOWN** `nuclear_gen` value=3323 d1=-3.0 d12=-11.0 z=-2.83285695
- **CHANGE_POINT** `margin` value=3.676e+04 d1=-24.0 d12=98.0 z=-0.32056138295053005
- **REVERSAL** `thermal_base` value=6250 d1=-1.0 d12=129.0 z=-0.9855238834196891
- **PERSISTENT_UP** `ccgt_gen` value=2927 d1=2.0 d12=140.0 z=-0.9365971658031088
- **ACCELERATION** `biomass_gen` value=477 d1=0.0 d12=0.0 z=-0.39345235416666663
- **REVERSAL** `ps_gen` value=-617 d1=-3.0 d12=316.0 z=-0.3559807013888889
- **ACCELERATION** `ps_gen` value=-617 d1=-3.0 d12=316.0 z=-0.3559807013888889
- **REVERSAL** `margin` value=3.676e+04 d1=-24.0 d12=98.0 z=-0.32056138295053005

## Nearest historical live analogues

- `2026-09-19T11:24:42.200097Z` distance=0.037 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.037 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T07:48:55.634175Z` distance=0.309 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.309 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.309 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T12:19:26.895649Z`  
Memory snapshots: **1485**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.675e+04 d1=0.0 d12=-28.0 z=-44.018170939542486
- **ROBUST_OUTLIER** `ind_generation` value=1.675e+04 d1=0.0 d12=-28.0 z=-44.018170939542486
- **CHANGE_POINT** `imbalance` value=-3260 d1=0.0 d12=94.0 z=-7.7486969514705875
- **ROBUST_OUTLIER** `imbalance` value=-3260 d1=0.0 d12=94.0 z=-7.7486969514705875
- **ROBUST_OUTLIER** `demand_forecast` value=1.951e+04 d1=0.0 d12=-122.0 z=3.2718281479508198
- **PERSISTENT_DOWN** `nuclear_gen` value=3326 d1=-3.0 d12=-8.0 z=-2.697959
- **ACCELERATION** `nuclear_gen` value=3326 d1=-3.0 d12=-8.0 z=-2.697959
- **CHANGE_POINT** `ps_gen` value=-614 d1=-217.0 d12=321.0 z=-0.3442708098958333
- **CHANGE_POINT** `margin` value=3.678e+04 d1=0.0 d12=122.0 z=-0.2919611108657244
- **PERSISTENT_DOWN** `wind_gen` value=1.554e+04 d1=-108.0 d12=-140.0 z=-1.5956500371428572
- **ACCELERATION** `wind_gen` value=1.554e+04 d1=-108.0 d12=-140.0 z=-1.5956500371428572
- **PERSISTENT_UP** `thermal_base` value=6251 d1=40.0 d12=135.0 z=-0.9820291178756477
- **PERSISTENT_UP** `ccgt_gen` value=2925 d1=43.0 d12=143.0 z=-0.9435866968911917
- **PERSISTENT_UP** `biomass_gen` value=477 d1=2.0 d12=0.0 z=-0.6399005320512821
- **ACCELERATION** `biomass_gen` value=477 d1=2.0 d12=0.0 z=-0.6399005320512821

## Nearest historical live analogues

- `2026-09-19T11:24:42.200097Z` distance=0.044 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T07:48:55.634175Z` distance=0.307 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.307 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.307 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.307 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

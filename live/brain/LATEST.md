# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T12:11:04.601097Z`  
Memory snapshots: **1483**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.675e+04 d1=0.0 d12=-3.0 z=-72.06994732978724
- **ROBUST_OUTLIER** `ind_generation` value=1.675e+04 d1=0.0 d12=-3.0 z=-72.06994732978724
- **CHANGE_POINT** `imbalance` value=-3260 d1=0.0 d12=118.0 z=-7.7486969514705875
- **ROBUST_OUTLIER** `imbalance` value=-3260 d1=0.0 d12=118.0 z=-7.7486969514705875
- **ROBUST_OUTLIER** `demand_forecast` value=1.951e+04 d1=0.0 d12=-122.0 z=3.2718281479508198
- **CHANGE_POINT** `ps_gen` value=-397 d1=271.0 d12=425.0 z=0.6960926245551601
- **CHANGE_POINT** `margin` value=3.678e+04 d1=0.0 d12=1230.0 z=-0.28965817484662576
- **PERSISTENT_DOWN** `nuclear_gen` value=3329 d1=-3.0 d12=-5.0 z=-1.686224375
- **PERSISTENT_UP** `ccgt_gen` value=2882 d1=56.0 d12=107.0 z=-1.173976754054054
- **PERSISTENT_UP** `thermal_base` value=6211 d1=53.0 d12=102.0 z=-1.1501825210526317
- **PERSISTENT_DOWN** `wind_gen` value=1.564e+04 d1=-141.0 d12=-123.0 z=-0.8360441811377246
- **ACCELERATION** `wind_gen` value=1.564e+04 d1=-141.0 d12=-123.0 z=-0.8360441811377246
- **PERSISTENT_UP** `ps_gen` value=-397 d1=271.0 d12=425.0 z=0.6960926245551601
- **ACCELERATION** `biomass_gen` value=475 d1=0.0 d12=1.0 z=-0.684011958235294
- **REVERSAL** `interconnector_net` value=-1604 d1=4.0 d12=-53.0 z=0.06463462597241867

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.307 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.307 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.307 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.307 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.307 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

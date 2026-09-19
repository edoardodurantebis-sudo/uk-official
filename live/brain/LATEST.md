# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T12:48:57.062606Z`  
Memory snapshots: **1492**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.676e+04 d1=0.0 d12=10.0 z=-36.728362616120215
- **ROBUST_OUTLIER** `ind_generation` value=1.676e+04 d1=0.0 d12=10.0 z=-36.728362616120215
- **CHANGE_POINT** `imbalance` value=-3250 d1=0.0 d12=10.0 z=-6.181236771161826
- **ROBUST_OUTLIER** `imbalance` value=-3250 d1=0.0 d12=10.0 z=-6.181236771161826
- **CHANGE_POINT** `wind_gen` value=1.53e+04 d1=7.0 d12=-498.0 z=-2.4672125065789476
- **ROBUST_OUTLIER** `demand_forecast` value=1.951e+04 d1=0.0 d12=0.0 z=3.2718281479508198
- **CHANGE_POINT** `thermal_base` value=6363 d1=22.0 d12=242.0 z=-0.5251752251908397
- **CHANGE_POINT** `ccgt_gen` value=3038 d1=23.0 d12=251.0 z=-0.5102357694300518
- **REVERSAL** `wind_gen` value=1.53e+04 d1=7.0 d12=-498.0 z=-2.4672125065789476
- **ACCELERATION** `nuclear_gen` value=3325 d1=-1.0 d12=-9.0 z=-2.29326515
- **CHANGE_POINT** `interconnector_net` value=-1814 d1=-23.0 d12=-324.0 z=-0.23649473242677826
- **CHANGE_POINT** `margin` value=3.676e+04 d1=0.0 d12=-24.0 z=-0.0534249306930693
- **PERSISTENT_UP** `thermal_base` value=6363 d1=22.0 d12=242.0 z=-0.5251752251908397
- **PERSISTENT_UP** `ccgt_gen` value=3038 d1=23.0 d12=251.0 z=-0.5102357694300518
- **PERSISTENT_DOWN** `biomass_gen` value=475 d1=-1.0 d12=-1.0 z=-0.5058673124999999

## Nearest historical live analogues

- `2026-09-19T11:54:18.195696Z` distance=0.008 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:50:05.858742Z` distance=0.031 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.035 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.035 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.035 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T13:01:30.497725Z`  
Memory snapshots: **1495**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.679e+04 d1=0.0 d12=40.0 z=-36.61779052595629
- **PERSISTENT_UP** `ind_generation` value=1.679e+04 d1=0.0 d12=40.0 z=-36.61779052595629
- **ACCELERATION** `ind_generation` value=1.679e+04 d1=0.0 d12=40.0 z=-36.61779052595629
- **ROBUST_OUTLIER** `ind_generation` value=1.679e+04 d1=0.0 d12=40.0 z=-36.61779052595629
- **CHANGE_POINT** `imbalance` value=-3220 d1=0.0 d12=40.0 z=-6.164444495228216
- **PERSISTENT_UP** `imbalance` value=-3220 d1=0.0 d12=40.0 z=-6.164444495228216
- **ACCELERATION** `imbalance` value=-3220 d1=0.0 d12=40.0 z=-6.164444495228216
- **ROBUST_OUTLIER** `imbalance` value=-3220 d1=0.0 d12=40.0 z=-6.164444495228216
- **CHANGE_POINT** `wind_gen` value=1.508e+04 d1=-71.0 d12=-562.0 z=-3.5185881958333334
- **PERSISTENT_DOWN** `wind_gen` value=1.508e+04 d1=-71.0 d12=-562.0 z=-3.5185881958333334
- **ROBUST_OUTLIER** `wind_gen` value=1.508e+04 d1=-71.0 d12=-562.0 z=-3.5185881958333334
- **ROBUST_OUTLIER** `demand_forecast` value=1.951e+04 d1=0.0 d12=0.0 z=3.2718281479508198
- **CHANGE_POINT** `interconnector_net` value=-2160 d1=-307.0 d12=-556.0 z=-0.6399300702391119
- **CHANGE_POINT** `ccgt_gen` value=3113 d1=30.0 d12=231.0 z=-0.24510146653005466
- **CHANGE_POINT** `thermal_base` value=6441 d1=27.0 d12=230.0 z=-0.24050170710455765

## Nearest historical live analogues

- `2026-09-19T11:54:18.195696Z` distance=0.085 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:58:27.853052Z` distance=0.085 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T12:02:38.156173Z` distance=0.085 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T12:06:51.129462Z` distance=0.085 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 1.0}
- `2026-09-19T11:50:05.858742Z` distance=0.090 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

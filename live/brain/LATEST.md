# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T13:20:25.382168Z`  
Memory snapshots: **871**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=2.848e+04 d1=0.0 d12=-3.0 z=21.364325739837398
- **ROBUST_OUTLIER** `wind_forecast` value=1.898e+04 d1=0.0 d12=-47.0 z=-18.21122325
- **CHANGE_POINT** `thermal_base` value=5538 d1=276.0 d12=422.0 z=2.7470128000000003
- **CHANGE_POINT** `ccgt_gen` value=2232 d1=279.0 d12=424.0 z=2.5493426144067795
- **ROBUST_OUTLIER** `imbalance` value=1.194e+04 d1=0.0 d12=-3.0 z=4.151269343283582
- **ROBUST_OUTLIER** `demand_forecast` value=1.604e+04 d1=0.0 d12=0.0 z=-4.089440593835617
- **ROBUST_OUTLIER** `residual_proxy` value=-2942 d1=0.0 d12=47.0 z=-3.6916438992957747
- **PERSISTENT_DOWN** `wind_gen` value=1.339e+04 d1=-104.0 d12=-760.0 z=-3.2957826098339718
- **ROBUST_OUTLIER** `wind_gen` value=1.339e+04 d1=-104.0 d12=-760.0 z=-3.2957826098339718
- **CHANGE_POINT** `biomass_gen` value=1971 d1=44.0 d12=-40.0 z=-1.1080903035714287
- **PERSISTENT_UP** `thermal_base` value=5538 d1=276.0 d12=422.0 z=2.7470128000000003
- **ACCELERATION** `thermal_base` value=5538 d1=276.0 d12=422.0 z=2.7470128000000003
- **CHANGE_POINT** `ps_gen` value=-690 d1=-5.0 d12=263.0 z=0.6693605503802281
- **PERSISTENT_UP** `ccgt_gen` value=2232 d1=279.0 d12=424.0 z=2.5493426144067795
- **ACCELERATION** `ccgt_gen` value=2232 d1=279.0 d12=424.0 z=2.5493426144067795

## Nearest historical live analogues

- `2026-09-17T12:25:34.603993Z` distance=0.032 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 47.0}
- `2026-09-17T12:21:21.942046Z` distance=0.033 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 47.0}
- `2026-09-17T11:51:58.101795Z` distance=0.171 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T11:56:11.138716Z` distance=0.171 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T12:00:23.510142Z` distance=0.171 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

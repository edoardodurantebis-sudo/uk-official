# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T12:17:55.983116Z`  
Memory snapshots: **210**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `imbalance` value=5650 d1=0.0 d12=-1.0 z=21.3874568
- **ROBUST_OUTLIER** `ind_generation` value=2.475e+04 d1=0.0 d12=-2.0 z=15.06200987825059
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=0.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=0.0 z=-6.6449730925925925
- **ROBUST_OUTLIER** `margin` value=3.518e+04 d1=0.0 d12=-334.0 z=3.359662214454976
- **CHANGE_POINT** `wind_gen` value=1.097e+04 d1=67.0 d12=-255.0 z=-1.2932775664349958
- **CHANGE_POINT** `ccgt_gen` value=1458 d1=0.0 d12=-8.0 z=-0.9886170327620968
- **CHANGE_POINT** `thermal_base` value=4787 d1=6.0 d12=-5.0 z=-0.9732502248498498
- **CHANGE_POINT** `ps_gen` value=-1091 d1=-166.0 d12=117.0 z=-0.8711827467532467
- **CHANGE_POINT** `biomass_gen` value=1709 d1=32.0 d12=430.0 z=-0.30782654835651074
- **REVERSAL** `wind_gen` value=1.097e+04 d1=67.0 d12=-255.0 z=-1.2932775664349958
- **ACCELERATION** `wind_gen` value=1.097e+04 d1=67.0 d12=-255.0 z=-1.2932775664349958
- **ACCELERATION** `nuclear_gen` value=3329 d1=6.0 d12=3.0 z=1.1803570625
- **PERSISTENT_DOWN** `ccgt_gen` value=1458 d1=0.0 d12=-8.0 z=-0.9886170327620968
- **ACCELERATION** `ccgt_gen` value=1458 d1=0.0 d12=-8.0 z=-0.9886170327620968

## Nearest historical live analogues

- `2026-09-15T11:05:46.278538Z` distance=0.050 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:09:57.090238Z` distance=0.050 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:14:08.250499Z` distance=0.050 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:18:18.946730Z` distance=0.050 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:22:30.581865Z` distance=0.599 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

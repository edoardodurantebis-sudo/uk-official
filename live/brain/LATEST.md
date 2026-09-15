# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T12:51:33.314202Z`  
Memory snapshots: **218**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=5650 d1=0.0 d12=0.0 z=12.906223931034482
- **ROBUST_OUTLIER** `imbalance` value=5650 d1=0.0 d12=0.0 z=12.906223931034482
- **CHANGE_POINT** `ind_generation` value=2.475e+04 d1=0.0 d12=1.0 z=9.337530773273274
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=0.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `ind_generation` value=2.475e+04 d1=0.0 d12=1.0 z=9.337530773273274
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=0.0 z=-6.6449730925925925
- **ROBUST_OUTLIER** `residual_proxy` value=756 d1=0.0 d12=-249.0 z=-3.155063532560707
- **CHANGE_POINT** `interconnector_net` value=1.129e+04 d1=1.0 d12=-2.0 z=0.5426156643835616
- **CHANGE_POINT** `biomass_gen` value=1725 d1=1.0 d12=142.0 z=-0.31390097349042706
- **CHANGE_POINT** `ps_gen` value=-1082 d1=4.0 d12=36.0 z=-0.3034541311394892
- **PERSISTENT_DOWN** `margin` value=3.517e+04 d1=-4.0 d12=-10.0 z=1.872329406354515
- **ACCELERATION** `margin` value=3.517e+04 d1=-4.0 d12=-10.0 z=1.872329406354515
- **PERSISTENT_DOWN** `wind_gen` value=1.042e+04 d1=-147.0 d12=-136.0 z=-1.549683832001522
- **ACCELERATION** `wind_gen` value=1.042e+04 d1=-147.0 d12=-136.0 z=-1.549683832001522
- **REVERSAL** `ccgt_gen` value=1464 d1=5.0 d12=-10.0 z=-0.7809084023020775

## Nearest historical live analogues

- `2026-09-15T11:52:29.344058Z` distance=0.357 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:56:43.921407Z` distance=0.357 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:05:46.278538Z` distance=0.360 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:09:57.090238Z` distance=0.360 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:14:08.250499Z` distance=0.360 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

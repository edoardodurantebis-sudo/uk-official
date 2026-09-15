# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T12:38:58.535756Z`  
Memory snapshots: **215**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high, wind rising.

## Active patterns

- **CHANGE_POINT** `imbalance` value=5650 d1=0.0 d12=-1.0 z=16.534479654618472
- **ROBUST_OUTLIER** `imbalance` value=5650 d1=0.0 d12=-1.0 z=16.534479654618472
- **CHANGE_POINT** `ind_generation` value=2.475e+04 d1=0.0 d12=-1.0 z=10.722061198275863
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=0.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `ind_generation` value=2.475e+04 d1=0.0 d12=-1.0 z=10.722061198275863
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=0.0 z=-6.6449730925925925
- **ROBUST_OUTLIER** `margin` value=3.518e+04 d1=0.0 d12=-340.0 z=3.3404824111374407
- **PERSISTENT_DOWN** `residual_proxy` value=756 d1=0.0 d12=-249.0 z=-3.155063532560707
- **ROBUST_OUTLIER** `residual_proxy` value=756 d1=0.0 d12=-249.0 z=-3.155063532560707
- **CHANGE_POINT** `ccgt_gen` value=1477 d1=7.0 d12=20.0 z=-0.7786361179112857
- **CHANGE_POINT** `thermal_base` value=4808 d1=6.0 d12=19.0 z=-0.7711171591934575
- **CHANGE_POINT** `ps_gen` value=-1074 d1=5.0 d12=151.0 z=-0.35098839655172415
- **CHANGE_POINT** `biomass_gen` value=1725 d1=3.0 d12=290.0 z=-0.2901129589552239
- **PERSISTENT_UP** `wind_forecast` value=1.785e+04 d1=0.0 d12=249.0 z=1.673498153301887
- **PERSISTENT_DOWN** `wind_gen` value=1.054e+04 d1=-253.0 d12=-770.0 z=-1.6066621146938775

## Nearest historical live analogues

- `2026-09-15T11:05:46.278538Z` distance=0.360 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:09:57.090238Z` distance=0.360 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:14:08.250499Z` distance=0.360 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:18:18.946730Z` distance=0.360 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:22:30.581865Z` distance=0.601 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T12:34:47.588906Z`  
Memory snapshots: **214**  
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
- **ACCELERATION** `residual_proxy` value=756 d1=0.0 d12=-249.0 z=-3.155063532560707
- **ROBUST_OUTLIER** `residual_proxy` value=756 d1=0.0 d12=-249.0 z=-3.155063532560707
- **CHANGE_POINT** `ccgt_gen` value=1470 d1=0.0 d12=13.0 z=-0.7945421086468276
- **CHANGE_POINT** `thermal_base` value=4802 d1=0.0 d12=13.0 z=-0.7848123825437112
- **CHANGE_POINT** `ps_gen` value=-1079 d1=0.0 d12=143.0 z=-0.40589650631500745
- **PERSISTENT_UP** `ind_demand` value=-1.19e+04 d1=0.0 d12=3.0 z=2.289715203947368
- **CHANGE_POINT** `biomass_gen` value=1722 d1=0.0 d12=342.0 z=-0.2878481556258322

## Nearest historical live analogues

- `2026-09-15T11:05:46.278538Z` distance=0.362 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:09:57.090238Z` distance=0.362 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:14:08.250499Z` distance=0.362 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:18:18.946730Z` distance=0.362 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:22:30.581865Z` distance=0.706 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

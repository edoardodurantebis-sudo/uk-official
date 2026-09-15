# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T12:43:09.309119Z`  
Memory snapshots: **216**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=5650 d1=0.0 d12=-1.0 z=16.534479654618472
- **ROBUST_OUTLIER** `imbalance` value=5650 d1=0.0 d12=-1.0 z=16.534479654618472
- **CHANGE_POINT** `ind_generation` value=2.475e+04 d1=0.0 d12=-1.0 z=10.722061198275863
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=0.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `ind_generation` value=2.475e+04 d1=0.0 d12=-1.0 z=10.722061198275863
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=0.0 z=-6.6449730925925925
- **ROBUST_OUTLIER** `residual_proxy` value=756 d1=0.0 d12=-249.0 z=-3.155063532560707
- **CHANGE_POINT** `ccgt_gen` value=1471 d1=-6.0 d12=13.0 z=-0.7793935460415496
- **CHANGE_POINT** `thermal_base` value=4801 d1=-7.0 d12=12.0 z=-0.7714975820642979
- **CHANGE_POINT** `ps_gen` value=-1075 d1=-1.0 d12=149.0 z=-0.33382685261824324
- **CHANGE_POINT** `biomass_gen` value=1722 d1=-3.0 d12=238.0 z=-0.295869389993146
- **REVERSAL** `wind_gen` value=1.061e+04 d1=72.0 d12=-717.0 z=-1.5060151087308002
- **ACCELERATION** `wind_gen` value=1.061e+04 d1=72.0 d12=-717.0 z=-1.5060151087308002
- **PERSISTENT_DOWN** `nuclear_gen` value=3330 d1=-1.0 d12=-1.0 z=1.0791836
- **REVERSAL** `ccgt_gen` value=1471 d1=-6.0 d12=13.0 z=-0.7793935460415496

## Nearest historical live analogues

- `2026-09-15T11:05:46.278538Z` distance=0.359 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:09:57.090238Z` distance=0.359 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:14:08.250499Z` distance=0.359 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:18:18.946730Z` distance=0.359 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:22:30.581865Z` distance=0.537 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

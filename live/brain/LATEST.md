# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T12:22:10.076168Z`  
Memory snapshots: **211**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=5650 d1=0.0 d12=-1.0 z=16.534479654618472
- **ROBUST_OUTLIER** `imbalance` value=5650 d1=0.0 d12=-1.0 z=16.534479654618472
- **CHANGE_POINT** `ind_generation` value=2.475e+04 d1=0.0 d12=-2.0 z=12.793634896586346
- **ROBUST_OUTLIER** `ind_generation` value=2.475e+04 d1=0.0 d12=-2.0 z=12.793634896586346
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=0.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=0.0 z=-6.6449730925925925
- **PERSISTENT_DOWN** `margin` value=3.518e+04 d1=-6.0 d12=-340.0 z=3.3404824111374407
- **ROBUST_OUTLIER** `margin` value=3.518e+04 d1=-6.0 d12=-340.0 z=3.3404824111374407
- **CHANGE_POINT** `wind_gen` value=1.095e+04 d1=-20.0 d12=-249.0 z=-1.265099173339012
- **CHANGE_POINT** `ccgt_gen` value=1458 d1=0.0 d12=-18.0 z=-0.9435830565104166
- **CHANGE_POINT** `thermal_base` value=4792 d1=5.0 d12=-6.0 z=-0.9408759071879936
- **CHANGE_POINT** `ps_gen` value=-1092 d1=-1.0 d12=113.0 z=-0.8505113244803696
- **CHANGE_POINT** `biomass_gen` value=1723 d1=14.0 d12=439.0 z=-0.2832062913669065
- **PERSISTENT_UP** `nuclear_gen` value=3334 d1=5.0 d12=12.0 z=2.0234692499999998
- **PERSISTENT_DOWN** `ccgt_gen` value=1458 d1=0.0 d12=-18.0 z=-0.9435830565104166

## Nearest historical live analogues

- `2026-09-15T11:05:46.278538Z` distance=0.061 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:09:57.090238Z` distance=0.061 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:14:08.250499Z` distance=0.061 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:18:18.946730Z` distance=0.061 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:22:30.581865Z` distance=0.609 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

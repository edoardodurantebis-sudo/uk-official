# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T10:40:33.108079Z`  
Memory snapshots: **833**  
Current physical regime: **TIGHT**

Regime read: margin low, wind falling.

## Active patterns

- **PERSISTENT_DOWN** `wind_forecast` value=1.903e+04 d1=0.0 d12=-223.0 z=-15.041121425
- **ROBUST_OUTLIER** `wind_forecast` value=1.903e+04 d1=0.0 d12=-223.0 z=-15.041121425
- **CHANGE_POINT** `margin` value=3.444e+04 d1=0.0 d12=24.0 z=-10.860496633233533
- **ROBUST_OUTLIER** `margin` value=3.444e+04 d1=0.0 d12=24.0 z=-10.860496633233533
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.986e+04 d1=0.0 d12=0.0 z=8.692120082608696
- **CHANGE_POINT** `imbalance` value=6691 d1=0.0 d12=28.0 z=-4.118692728723404
- **ROBUST_OUTLIER** `imbalance` value=6691 d1=0.0 d12=28.0 z=-4.118692728723404
- **CHANGE_POINT** `thermal_base` value=5126 d1=5.0 d12=3.0 z=-1.3832755889830508
- **CHANGE_POINT** `ccgt_gen` value=1810 d1=-1.0 d12=0.0 z=-1.383251385673959
- **REVERSAL** `wind_gen` value=1.582e+04 d1=-93.0 d12=162.0 z=3.359795984126984
- **ACCELERATION** `wind_gen` value=1.582e+04 d1=-93.0 d12=162.0 z=3.359795984126984
- **ROBUST_OUTLIER** `wind_gen` value=1.582e+04 d1=-93.0 d12=162.0 z=3.359795984126984
- **CHANGE_POINT** `ind_demand` value=-1.304e+04 d1=0.0 d12=-30.0 z=-0.9476216116692426
- **PERSISTENT_DOWN** `biomass_gen` value=1992 d1=-19.0 d12=-35.0 z=-1.4959950994055484
- **ACCELERATION** `biomass_gen` value=1992 d1=-19.0 d12=-35.0 z=-1.4959950994055484

## Nearest historical live analogues

- `2026-09-17T09:19:56.543683Z` distance=0.166 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:24:08.362874Z` distance=0.166 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:28:21.130076Z` distance=0.166 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:32:33.001998Z` distance=0.166 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:36:45.320295Z` distance=0.166 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

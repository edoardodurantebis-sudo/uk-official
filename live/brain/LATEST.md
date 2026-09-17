# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T10:31:30.033860Z`  
Memory snapshots: **831**  
Current physical regime: **TIGHT**

Regime read: margin low, wind falling.

## Active patterns

- **PERSISTENT_DOWN** `wind_forecast` value=1.903e+04 d1=-223.0 d12=-223.0 z=-15.041121425
- **ACCELERATION** `wind_forecast` value=1.903e+04 d1=-223.0 d12=-223.0 z=-15.041121425
- **ROBUST_OUTLIER** `wind_forecast` value=1.903e+04 d1=-223.0 d12=-223.0 z=-15.041121425
- **ROBUST_OUTLIER** `margin` value=3.444e+04 d1=0.0 d12=-33.0 z=-12.34133947972973
- **PERSISTENT_UP** `wind_gen` value=1.592e+04 d1=108.0 d12=220.0 z=4.408656011946903
- **ROBUST_OUTLIER** `wind_gen` value=1.592e+04 d1=108.0 d12=220.0 z=4.408656011946903
- **PERSISTENT_UP** `imbalance` value=6691 d1=0.0 d12=54.0 z=-4.222892347826087
- **ROBUST_OUTLIER** `imbalance` value=6691 d1=0.0 d12=54.0 z=-4.222892347826087
- **PERSISTENT_DOWN** `ccgt_gen` value=1811 d1=0.0 d12=-5.0 z=-1.7637315304824561
- **ACCELERATION** `ccgt_gen` value=1811 d1=0.0 d12=-5.0 z=-1.7637315304824561
- **PERSISTENT_DOWN** `thermal_base` value=5121 d1=-3.0 d12=-7.0 z=-1.7544973339877836
- **ACCELERATION** `thermal_base` value=5121 d1=-3.0 d12=-7.0 z=-1.7544973339877836
- **REVERSAL** `biomass_gen` value=2011 d1=-7.0 d12=21.0 z=-1.4699039571713148
- **ACCELERATION** `biomass_gen` value=2011 d1=-7.0 d12=21.0 z=-1.4699039571713148
- **PERSISTENT_DOWN** `ind_demand` value=-1.304e+04 d1=0.0 d12=-53.0 z=-0.9857092970257235

## Nearest historical live analogues

- `2026-09-17T09:19:56.543683Z` distance=0.167 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:24:08.362874Z` distance=0.167 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:28:21.130076Z` distance=0.167 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:32:33.001998Z` distance=0.167 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:36:45.320295Z` distance=0.167 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

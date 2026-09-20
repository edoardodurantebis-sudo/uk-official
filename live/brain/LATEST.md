# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T08:50:43.883869Z`  
Memory snapshots: **1777**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=586 d1=1.0 d12=-300.0 z=-6.231000547619048
- **CHANGE_POINT** `interconnector_net` value=-3244 d1=1.0 d12=3568.0 z=5.037696171052632
- **CHANGE_POINT** `thermal_base` value=5957 d1=-72.0 d12=-1276.0 z=-4.777809746130031
- **CHANGE_POINT** `ccgt_gen` value=2623 d1=-70.0 d12=-1274.0 z=-4.740106427692308
- **REVERSAL** `biomass_gen` value=586 d1=1.0 d12=-300.0 z=-6.231000547619048
- **ROBUST_OUTLIER** `biomass_gen` value=586 d1=1.0 d12=-300.0 z=-6.231000547619048
- **PERSISTENT_UP** `interconnector_net` value=-3244 d1=1.0 d12=3568.0 z=5.037696171052632
- **ROBUST_OUTLIER** `interconnector_net` value=-3244 d1=1.0 d12=3568.0 z=5.037696171052632
- **PERSISTENT_DOWN** `thermal_base` value=5957 d1=-72.0 d12=-1276.0 z=-4.777809746130031
- **ROBUST_OUTLIER** `thermal_base` value=5957 d1=-72.0 d12=-1276.0 z=-4.777809746130031
- **PERSISTENT_DOWN** `ccgt_gen` value=2623 d1=-70.0 d12=-1274.0 z=-4.740106427692308
- **ROBUST_OUTLIER** `ccgt_gen` value=2623 d1=-70.0 d12=-1274.0 z=-4.740106427692308
- **CHANGE_POINT** `wind_gen` value=1.5e+04 d1=-80.0 d12=-357.0 z=-1.2051650543710022
- **PERSISTENT_DOWN** `ps_gen` value=-935 d1=-1.0 d12=-4.0 z=-1.6539349720744683
- **PERSISTENT_DOWN** `wind_gen` value=1.5e+04 d1=-80.0 d12=-357.0 z=-1.2051650543710022

## Nearest historical live analogues

- `2026-09-20T06:23:42.476737Z` distance=0.064 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:27:53.569946Z` distance=0.064 → {'next30m_imbalance_delta': 52.0, 'next30m_margin_delta': 205.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:32:06.254579Z` distance=0.064 → {'next30m_imbalance_delta': 52.0, 'next30m_margin_delta': 205.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:36:16.278783Z` distance=0.064 → {'next30m_imbalance_delta': 52.0, 'next30m_margin_delta': 205.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:40:27.666634Z` distance=0.064 → {'next30m_imbalance_delta': 52.0, 'next30m_margin_delta': 205.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

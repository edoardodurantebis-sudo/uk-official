# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T09:45:56.215503Z`  
Memory snapshots: **174**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **PERSISTENT_DOWN** `biomass_gen` value=2041 d1=-2.0 d12=-1.0 z=-56.1512716875
- **ACCELERATION** `biomass_gen` value=2041 d1=-2.0 d12=-1.0 z=-56.1512716875
- **ROBUST_OUTLIER** `biomass_gen` value=2041 d1=-2.0 d12=-1.0 z=-56.1512716875
- **CHANGE_POINT** `margin` value=3.45e+04 d1=0.0 d12=420.0 z=4.582247825396826
- **CHANGE_POINT** `ind_demand` value=-1.225e+04 d1=0.0 d12=145.0 z=4.150706153846154
- **CHANGE_POINT** `wind_gen` value=1.155e+04 d1=-70.0 d12=-511.0 z=-3.999378325320513
- **ROBUST_OUTLIER** `margin` value=3.45e+04 d1=0.0 d12=420.0 z=4.582247825396826
- **CHANGE_POINT** `imbalance` value=-92 d1=0.0 d12=43.0 z=2.154937591101695
- **ROBUST_OUTLIER** `ind_demand` value=-1.225e+04 d1=0.0 d12=145.0 z=4.150706153846154
- **CHANGE_POINT** `ccgt_gen` value=2279 d1=-146.0 d12=-574.0 z=-2.005562442477876
- **PERSISTENT_DOWN** `wind_gen` value=1.155e+04 d1=-70.0 d12=-511.0 z=-3.999378325320513
- **ROBUST_OUTLIER** `wind_gen` value=1.155e+04 d1=-70.0 d12=-511.0 z=-3.999378325320513
- **CHANGE_POINT** `thermal_base` value=5600 d1=-147.0 d12=-570.0 z=-1.9788957378428926

## Nearest historical live analogues

- `2026-09-15T07:21:37.326101Z` distance=1.212 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:25:46.773269Z` distance=1.212 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:29:58.096076Z` distance=1.212 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:34:09.642854Z` distance=1.212 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:38:22.525585Z` distance=1.212 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

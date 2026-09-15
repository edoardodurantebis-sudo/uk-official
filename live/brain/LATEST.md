# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T09:41:45.287890Z`  
Memory snapshots: **173**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **REVERSAL** `biomass_gen` value=2043 d1=2.0 d12=-53.0 z=-54.16850440517241
- **ROBUST_OUTLIER** `biomass_gen` value=2043 d1=2.0 d12=-53.0 z=-54.16850440517241
- **CHANGE_POINT** `margin` value=3.45e+04 d1=0.0 d12=420.0 z=5.605468213592234
- **CHANGE_POINT** `wind_gen` value=1.162e+04 d1=-27.0 d12=-610.0 z=-3.8480504967948717
- **ROBUST_OUTLIER** `margin` value=3.45e+04 d1=0.0 d12=420.0 z=5.605468213592234
- **CHANGE_POINT** `imbalance` value=-92 d1=0.0 d12=383.0 z=2.154937591101695
- **ROBUST_OUTLIER** `ind_demand` value=-1.225e+04 d1=0.0 d12=54.0 z=4.150706153846154
- **PERSISTENT_DOWN** `wind_gen` value=1.162e+04 d1=-27.0 d12=-610.0 z=-3.8480504967948717
- **ROBUST_OUTLIER** `wind_gen` value=1.162e+04 d1=-27.0 d12=-610.0 z=-3.8480504967948717
- **CHANGE_POINT** `ccgt_gen` value=2425 d1=-61.0 d12=-546.0 z=-1.7951535981912146
- **CHANGE_POINT** `thermal_base` value=5747 d1=-69.0 d12=-540.0 z=-1.7601703361850443
- **PERSISTENT_DOWN** `ps_gen` value=-1206 d1=-42.0 d12=-664.0 z=-2.903820635856079
- **CHANGE_POINT** `nuclear_gen` value=3322 d1=-8.0 d12=6.0 z=-0.13489795

## Nearest historical live analogues

- `2026-09-15T07:21:37.326101Z` distance=1.299 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:25:46.773269Z` distance=1.299 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:29:58.096076Z` distance=1.299 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:34:09.642854Z` distance=1.299 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:38:22.525585Z` distance=1.299 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T09:37:29.655273Z`  
Memory snapshots: **172**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=-50.0 z=56.657139
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=-50.0 z=56.657139
- **PERSISTENT_DOWN** `biomass_gen` value=2041 d1=-1.0 d12=-154.0 z=-56.22353844642857
- **ROBUST_OUTLIER** `biomass_gen` value=2041 d1=-1.0 d12=-154.0 z=-56.22353844642857
- **CHANGE_POINT** `margin` value=3.45e+04 d1=0.0 d12=453.0 z=7.217040325000001
- **ROBUST_OUTLIER** `margin` value=3.45e+04 d1=0.0 d12=453.0 z=7.217040325000001
- **CHANGE_POINT** `wind_gen` value=1.165e+04 d1=-102.0 d12=-743.0 z=-3.7896811915064106
- **CHANGE_POINT** `imbalance` value=-92 d1=0.0 d12=383.0 z=2.154937591101695
- **ROBUST_OUTLIER** `ind_demand` value=-1.225e+04 d1=0.0 d12=54.0 z=4.150706153846154
- **PERSISTENT_DOWN** `wind_gen` value=1.165e+04 d1=-102.0 d12=-743.0 z=-3.7896811915064106
- **ROBUST_OUTLIER** `wind_gen` value=1.165e+04 d1=-102.0 d12=-743.0 z=-3.7896811915064106
- **CHANGE_POINT** `ccgt_gen` value=2486 d1=-6.0 d12=-521.0 z=-1.6976118642857143
- **CHANGE_POINT** `thermal_base` value=5816 d1=2.0 d12=-504.0 z=-1.6590202429577465
- **PERSISTENT_DOWN** `ps_gen` value=-1164 d1=-3.0 d12=-623.0 z=-2.626138332175926
- **PERSISTENT_UP** `interconnector_net` value=1.144e+04 d1=28.0 d12=1736.0 z=1.8498355701967995

## Nearest historical live analogues

- `2026-09-15T07:21:37.326101Z` distance=1.401 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:25:46.773269Z` distance=1.401 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:29:58.096076Z` distance=1.401 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:34:09.642854Z` distance=1.401 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T07:38:22.525585Z` distance=1.401 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

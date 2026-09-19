# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T17:01:39.109374Z`  
Memory snapshots: **1552**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **PERSISTENT_DOWN** `biomass_gen` value=605 d1=0.0 d12=-87.0 z=43.167344
- **ROBUST_OUTLIER** `biomass_gen` value=605 d1=0.0 d12=-87.0 z=43.167344
- **PERSISTENT_UP** `ps_gen` value=983 d1=0.0 d12=545.0 z=7.4725728216845875
- **ROBUST_OUTLIER** `ps_gen` value=983 d1=0.0 d12=545.0 z=7.4725728216845875
- **CHANGE_POINT** `thermal_base` value=8563 d1=576.0 d12=1161.0 z=4.470126423790322
- **CHANGE_POINT** `ccgt_gen` value=5227 d1=575.0 d12=1156.0 z=4.385253993650793
- **PERSISTENT_UP** `thermal_base` value=8563 d1=576.0 d12=1161.0 z=4.470126423790322
- **ACCELERATION** `thermal_base` value=8563 d1=576.0 d12=1161.0 z=4.470126423790322
- **ROBUST_OUTLIER** `thermal_base` value=8563 d1=576.0 d12=1161.0 z=4.470126423790322
- **CHANGE_POINT** `margin` value=3.626e+04 d1=0.0 d12=-789.0 z=-2.440341387152778
- **PERSISTENT_UP** `ccgt_gen` value=5227 d1=575.0 d12=1156.0 z=4.385253993650793
- **ACCELERATION** `ccgt_gen` value=5227 d1=575.0 d12=1156.0 z=4.385253993650793
- **ROBUST_OUTLIER** `ccgt_gen` value=5227 d1=575.0 d12=1156.0 z=4.385253993650793
- **CHANGE_POINT** `ind_generation` value=1.68e+04 d1=0.0 d12=23.0 z=2.0234692499999998
- **CHANGE_POINT** `interconnector_net` value=30 d1=-495.0 d12=1411.0 z=1.5368970422885573

## Nearest historical live analogues

- `2026-09-19T11:50:05.858742Z` distance=0.167 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.171 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.171 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.171 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.171 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

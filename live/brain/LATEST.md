# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T17:10:02.143135Z`  
Memory snapshots: **1554**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=605 d1=0.0 d12=-101.0 z=43.167344
- **ROBUST_OUTLIER** `biomass_gen` value=605 d1=0.0 d12=-101.0 z=43.167344
- **CHANGE_POINT** `ps_gen` value=916 d1=0.0 d12=477.0 z=6.49361700490196
- **CHANGE_POINT** `thermal_base` value=9174 d1=0.0 d12=1643.0 z=5.539559335648148
- **CHANGE_POINT** `ccgt_gen` value=5840 d1=0.0 d12=1644.0 z=5.529150543209877
- **ROBUST_OUTLIER** `ps_gen` value=916 d1=0.0 d12=477.0 z=6.49361700490196
- **PERSISTENT_UP** `thermal_base` value=9174 d1=0.0 d12=1643.0 z=5.539559335648148
- **ACCELERATION** `thermal_base` value=9174 d1=0.0 d12=1643.0 z=5.539559335648148
- **ROBUST_OUTLIER** `thermal_base` value=9174 d1=0.0 d12=1643.0 z=5.539559335648148
- **PERSISTENT_UP** `ccgt_gen` value=5840 d1=0.0 d12=1644.0 z=5.529150543209877
- **ACCELERATION** `ccgt_gen` value=5840 d1=0.0 d12=1644.0 z=5.529150543209877
- **ROBUST_OUTLIER** `ccgt_gen` value=5840 d1=0.0 d12=1644.0 z=5.529150543209877
- **CHANGE_POINT** `margin` value=3.626e+04 d1=0.0 d12=-789.0 z=-2.440341387152778
- **CHANGE_POINT** `ind_generation` value=1.68e+04 d1=0.0 d12=23.0 z=2.0234692499999998
- **ROBUST_OUTLIER** `residual_proxy` value=1.259e+04 d1=0.0 d12=-206.0 z=-3.1556484732142858

## Nearest historical live analogues

- `2026-09-19T11:50:05.858742Z` distance=0.167 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.171 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.171 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.171 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.171 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

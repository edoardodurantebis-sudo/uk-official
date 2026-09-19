# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T17:05:49.699644Z`  
Memory snapshots: **1553**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **PERSISTENT_DOWN** `biomass_gen` value=605 d1=0.0 d12=-102.0 z=43.167344
- **ROBUST_OUTLIER** `biomass_gen` value=605 d1=0.0 d12=-102.0 z=43.167344
- **CHANGE_POINT** `ccgt_gen` value=5840 d1=613.0 d12=1677.0 z=5.573194466174184
- **CHANGE_POINT** `thermal_base` value=9174 d1=611.0 d12=1679.0 z=5.551248715224111
- **REVERSAL** `ps_gen` value=916 d1=-67.0 d12=477.0 z=6.844564370274914
- **ROBUST_OUTLIER** `ps_gen` value=916 d1=-67.0 d12=477.0 z=6.844564370274914
- **PERSISTENT_UP** `ccgt_gen` value=5840 d1=613.0 d12=1677.0 z=5.573194466174184
- **ROBUST_OUTLIER** `ccgt_gen` value=5840 d1=613.0 d12=1677.0 z=5.573194466174184
- **PERSISTENT_UP** `thermal_base` value=9174 d1=611.0 d12=1679.0 z=5.551248715224111
- **ROBUST_OUTLIER** `thermal_base` value=9174 d1=611.0 d12=1679.0 z=5.551248715224111
- **CHANGE_POINT** `margin` value=3.626e+04 d1=0.0 d12=-789.0 z=-2.440341387152778
- **CHANGE_POINT** `ind_generation` value=1.68e+04 d1=0.0 d12=23.0 z=2.0234692499999998
- **ROBUST_OUTLIER** `residual_proxy` value=1.259e+04 d1=0.0 d12=-206.0 z=-3.1556484732142858
- **CHANGE_POINT** `imbalance` value=-3150 d1=0.0 d12=23.0 z=0.9635567857142858
- **CHANGE_POINT** `interconnector_net` value=-871 d1=-901.0 d12=42.0 z=0.7757257038295244

## Nearest historical live analogues

- `2026-09-19T11:50:05.858742Z` distance=0.167 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.171 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.171 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.171 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.171 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

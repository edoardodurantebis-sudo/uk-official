# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T16:52:42.433757Z`  
Memory snapshots: **1550**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **PERSISTENT_DOWN** `biomass_gen` value=606 d1=0.0 d12=-22.0 z=43.504588875
- **ROBUST_OUTLIER** `biomass_gen` value=606 d1=0.0 d12=-22.0 z=43.504588875
- **PERSISTENT_UP** `ps_gen` value=982 d1=1.0 d12=599.0 z=7.588622860000001
- **ROBUST_OUTLIER** `ps_gen` value=982 d1=1.0 d12=599.0 z=7.588622860000001
- **CHANGE_POINT** `thermal_base` value=7881 d1=34.0 d12=597.0 z=3.1226377314814813
- **CHANGE_POINT** `ccgt_gen` value=4545 d1=36.0 d12=592.0 z=3.101973833473154
- **CHANGE_POINT** `margin` value=3.626e+04 d1=-665.0 d12=-789.0 z=-2.440341387152778
- **CHANGE_POINT** `interconnector_net` value=495 d1=-25.0 d12=2878.0 z=1.9965244275128864
- **CHANGE_POINT** `ind_generation` value=1.68e+04 d1=0.0 d12=22.0 z=1.93915803125
- **ROBUST_OUTLIER** `residual_proxy` value=1.259e+04 d1=0.0 d12=-206.0 z=-3.1556484732142858
- **PERSISTENT_UP** `thermal_base` value=7881 d1=34.0 d12=597.0 z=3.1226377314814813
- **ROBUST_OUTLIER** `thermal_base` value=7881 d1=34.0 d12=597.0 z=3.1226377314814813
- **PERSISTENT_UP** `ccgt_gen` value=4545 d1=36.0 d12=592.0 z=3.101973833473154
- **ROBUST_OUTLIER** `ccgt_gen` value=4545 d1=36.0 d12=592.0 z=3.101973833473154
- **CHANGE_POINT** `imbalance` value=-3151 d1=0.0 d12=22.0 z=0.9515123258928571

## Nearest historical live analogues

- `2026-09-19T11:50:05.858742Z` distance=0.167 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.172 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.172 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.172 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.172 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

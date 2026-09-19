# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T17:14:13.893695Z`  
Memory snapshots: **1555**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=605 d1=0.0 d12=-62.0 z=34.5338752
- **ROBUST_OUTLIER** `biomass_gen` value=605 d1=0.0 d12=-62.0 z=34.5338752
- **CHANGE_POINT** `thermal_base` value=9534 d1=360.0 d12=2043.0 z=5.961778361273792
- **CHANGE_POINT** `ccgt_gen` value=6204 d1=364.0 d12=2051.0 z=5.937672886661807
- **REVERSAL** `ps_gen` value=831 d1=-85.0 d12=327.0 z=6.07040775
- **ROBUST_OUTLIER** `ps_gen` value=831 d1=-85.0 d12=327.0 z=6.07040775
- **PERSISTENT_UP** `thermal_base` value=9534 d1=360.0 d12=2043.0 z=5.961778361273792
- **ROBUST_OUTLIER** `thermal_base` value=9534 d1=360.0 d12=2043.0 z=5.961778361273792
- **PERSISTENT_UP** `ccgt_gen` value=6204 d1=364.0 d12=2051.0 z=5.937672886661807
- **ROBUST_OUTLIER** `ccgt_gen` value=6204 d1=364.0 d12=2051.0 z=5.937672886661807
- **CHANGE_POINT** `margin` value=3.626e+04 d1=0.0 d12=-665.0 z=-2.440341387152778
- **CHANGE_POINT** `ind_generation` value=1.68e+04 d1=0.0 d12=23.0 z=2.0234692499999998
- **ROBUST_OUTLIER** `residual_proxy` value=1.259e+04 d1=0.0 d12=-206.0 z=-3.1556484732142858
- **CHANGE_POINT** `imbalance` value=-3150 d1=0.0 d12=23.0 z=0.9635567857142858
- **PERSISTENT_DOWN** `interconnector_net` value=-1294 d1=-423.0 d12=-305.0 z=0.4045345844155844

## Nearest historical live analogues

- `2026-09-19T11:50:05.858742Z` distance=0.169 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.173 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.173 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.173 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.173 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

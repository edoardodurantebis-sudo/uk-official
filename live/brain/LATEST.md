# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T17:18:26.903543Z`  
Memory snapshots: **1556**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=605 d1=0.0 d12=-13.0 z=28.778229333333332
- **ROBUST_OUTLIER** `biomass_gen` value=605 d1=0.0 d12=-13.0 z=28.778229333333332
- **CHANGE_POINT** `ccgt_gen` value=6381 d1=177.0 d12=2168.0 z=5.969514546398892
- **CHANGE_POINT** `thermal_base` value=9717 d1=183.0 d12=2171.0 z=5.91148687739726
- **PERSISTENT_UP** `ccgt_gen` value=6381 d1=177.0 d12=2168.0 z=5.969514546398892
- **ROBUST_OUTLIER** `ccgt_gen` value=6381 d1=177.0 d12=2168.0 z=5.969514546398892
- **PERSISTENT_UP** `thermal_base` value=9717 d1=183.0 d12=2171.0 z=5.91148687739726
- **ROBUST_OUTLIER** `thermal_base` value=9717 d1=183.0 d12=2171.0 z=5.91148687739726
- **REVERSAL** `ps_gen` value=795 d1=-36.0 d12=238.0 z=5.026822220138889
- **ROBUST_OUTLIER** `ps_gen` value=795 d1=-36.0 d12=238.0 z=5.026822220138889
- **CHANGE_POINT** `margin` value=3.626e+04 d1=0.0 d12=-665.0 z=-2.440341387152778
- **CHANGE_POINT** `ind_generation` value=1.68e+04 d1=0.0 d12=1.0 z=2.0234692499999998
- **ROBUST_OUTLIER** `residual_proxy` value=1.259e+04 d1=0.0 d12=-206.0 z=-3.1556484732142858
- **CHANGE_POINT** `imbalance` value=-3150 d1=0.0 d12=1.0 z=0.9635567857142858
- **PERSISTENT_UP** `nuclear_gen` value=3336 d1=6.0 d12=3.0 z=1.686224375

## Nearest historical live analogues

- `2026-09-19T11:50:05.858742Z` distance=0.172 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.176 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.176 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.176 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.176 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

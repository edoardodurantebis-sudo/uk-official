# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T23:36:27.405223Z`  
Memory snapshots: **371**  
Current physical regime: **BALANCED**

Regime read: wind rising.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.208e+04 d1=0.0 d12=-166.0 z=-37.546596083333334
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-166.0 z=-37.546596083333334
- **CHANGE_POINT** `thermal_base` value=6558 d1=2.0 d12=64.0 z=-8.510064397309417
- **CHANGE_POINT** `ccgt_gen` value=3228 d1=-1.0 d12=62.0 z=-8.442213484222224
- **PERSISTENT_UP** `thermal_base` value=6558 d1=2.0 d12=64.0 z=-8.510064397309417
- **ROBUST_OUTLIER** `thermal_base` value=6558 d1=2.0 d12=64.0 z=-8.510064397309417
- **REVERSAL** `ccgt_gen` value=3228 d1=-1.0 d12=62.0 z=-8.442213484222224
- **ROBUST_OUTLIER** `ccgt_gen` value=3228 d1=-1.0 d12=62.0 z=-8.442213484222224
- **CHANGE_POINT** `biomass_gen` value=3235 d1=-11.0 d12=-19.0 z=-1.6329751842105265
- **REVERSAL** `interconnector_net` value=3962 d1=24.0 d12=-190.0 z=2.1958997822944895
- **ACCELERATION** `interconnector_net` value=3962 d1=24.0 d12=-190.0 z=2.1958997822944895
- **CHANGE_POINT** `wind_gen` value=1.061e+04 d1=211.0 d12=-1309.0 z=-0.13913835707269154
- **CHANGE_POINT** `ps_gen` value=190 d1=165.0 d12=345.0 z=0.11757160779816514
- **PERSISTENT_UP** `nuclear_gen` value=3330 d1=3.0 d12=2.0 z=1.7986393333333333
- **ACCELERATION** `nuclear_gen` value=3330 d1=3.0 d12=2.0 z=1.7986393333333333

## Nearest historical live analogues

- `2026-09-15T17:50:55.506503Z` distance=0.725 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.725 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:59:22.215947Z` distance=0.725 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:03:35.364442Z` distance=0.725 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:07:47.333244Z` distance=0.725 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

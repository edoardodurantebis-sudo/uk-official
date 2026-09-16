# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T07:27:32.881343Z`  
Memory snapshots: **483**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.632e+04 d1=0.0 d12=-1122.0 z=-50.628886859375
- **PERSISTENT_DOWN** `margin` value=3.632e+04 d1=0.0 d12=-1122.0 z=-50.628886859375
- **ROBUST_OUTLIER** `margin` value=3.632e+04 d1=0.0 d12=-1122.0 z=-50.628886859375
- **PERSISTENT_DOWN** `ind_demand` value=-1.266e+04 d1=0.0 d12=-444.0 z=-18.290574985294118
- **ACCELERATION** `ind_demand` value=-1.266e+04 d1=0.0 d12=-444.0 z=-18.290574985294118
- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-444.0 z=-18.290574985294118
- **PERSISTENT_DOWN** `thermal_base` value=1.145e+04 d1=-133.0 d12=-395.0 z=4.548605253558719
- **ROBUST_OUTLIER** `thermal_base` value=1.145e+04 d1=-133.0 d12=-395.0 z=4.548605253558719
- **PERSISTENT_DOWN** `ccgt_gen` value=8124 d1=-127.0 d12=-394.0 z=4.536649652767921
- **ROBUST_OUTLIER** `ccgt_gen` value=8124 d1=-127.0 d12=-394.0 z=4.536649652767921
- **CHANGE_POINT** `ind_generation` value=2.644e+04 d1=0.0 d12=126.0 z=0.6790937755972697
- **REVERSAL** `wind_gen` value=8003 d1=-59.0 d12=404.0 z=-1.7692977455138663
- **PERSISTENT_UP** `interconnector_net` value=6948 d1=0.0 d12=3361.0 z=1.6526312572342794
- **PERSISTENT_DOWN** `biomass_gen` value=3229 d1=-3.0 d12=-3.0 z=-1.0117346249999999
- **ACCELERATION** `biomass_gen` value=3229 d1=-3.0 d12=-3.0 z=-1.0117346249999999

## Nearest historical live analogues

- `2026-09-16T06:20:37.850603Z` distance=1.383 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:24:49.356241Z` distance=1.383 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:29:00.658838Z` distance=1.383 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:33:09.371452Z` distance=1.383 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:51:19.396641Z` distance=1.402 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

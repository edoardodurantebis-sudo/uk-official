# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T07:31:44.991160Z`  
Memory snapshots: **484**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.632e+04 d1=0.0 d12=-1122.0 z=-50.628886859375
- **ROBUST_OUTLIER** `margin` value=3.632e+04 d1=0.0 d12=-1122.0 z=-50.628886859375
- **PERSISTENT_DOWN** `ind_demand` value=-1.266e+04 d1=0.0 d12=-444.0 z=-18.290574985294118
- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-444.0 z=-18.290574985294118
- **PERSISTENT_DOWN** `thermal_base` value=1.142e+04 d1=-33.0 d12=-512.0 z=3.2838350043431053
- **ROBUST_OUTLIER** `thermal_base` value=1.142e+04 d1=-33.0 d12=-512.0 z=3.2838350043431053
- **PERSISTENT_DOWN** `ccgt_gen` value=8089 d1=-35.0 d12=-511.0 z=3.282370314332247
- **ROBUST_OUTLIER** `ccgt_gen` value=8089 d1=-35.0 d12=-511.0 z=3.282370314332247
- **CHANGE_POINT** `ind_generation` value=2.644e+04 d1=0.0 d12=126.0 z=0.6790937755972697
- **PERSISTENT_UP** `interconnector_net` value=9784 d1=2836.0 d12=6199.0 z=2.672485659688013
- **ACCELERATION** `interconnector_net` value=9784 d1=2836.0 d12=6199.0 z=2.672485659688013
- **CHANGE_POINT** `imbalance` value=6872 d1=0.0 d12=-318.0 z=-0.342999906996587
- **REVERSAL** `wind_gen` value=7899 d1=-104.0 d12=354.0 z=-1.8650870414979754
- **PERSISTENT_UP** `ind_generation` value=2.644e+04 d1=0.0 d12=126.0 z=0.6790937755972697
- **PERSISTENT_DOWN** `imbalance` value=6872 d1=0.0 d12=-318.0 z=-0.342999906996587

## Nearest historical live analogues

- `2026-09-16T06:20:37.850603Z` distance=1.383 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:24:49.356241Z` distance=1.383 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:29:00.658838Z` distance=1.383 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:33:09.371452Z` distance=1.383 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:37:20.897017Z` distance=1.383 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T08:13:46.767575Z`  
Memory snapshots: **494**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.632e+04 d1=0.0 d12=0.0 z=-50.628886859375
- **ROBUST_OUTLIER** `margin` value=3.632e+04 d1=0.0 d12=0.0 z=-50.628886859375
- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=0.0 z=-22.857708194444445
- **ROBUST_OUTLIER** `residual_proxy` value=864 d1=0.0 d12=1249.0 z=4.691355458598727
- **CHANGE_POINT** `wind_gen` value=7037 d1=-80.0 d12=-1025.0 z=-1.7584216332948643
- **CHANGE_POINT** `ps_gen` value=230 d1=0.0 d12=8.0 z=1.3489795
- **PERSISTENT_UP** `biomass_gen` value=3240 d1=1.0 d12=8.0 z=2.697959
- **ACCELERATION** `biomass_gen` value=3240 d1=1.0 d12=8.0 z=2.697959
- **CHANGE_POINT** `ind_generation` value=2.644e+04 d1=0.0 d12=0.0 z=0.6832493571428571
- **PERSISTENT_UP** `interconnector_net` value=1.01e+04 d1=27.0 d12=3149.0 z=2.482937651474531
- **PERSISTENT_DOWN** `wind_gen` value=7037 d1=-80.0 d12=-1025.0 z=-1.7584216332948643
- **PERSISTENT_UP** `thermal_base` value=1.195e+04 d1=116.0 d12=363.0 z=1.737052911911033
- **PERSISTENT_UP** `ccgt_gen` value=8620 d1=121.0 d12=369.0 z=1.7322347041338009
- **PERSISTENT_DOWN** `nuclear_gen` value=3328 d1=-5.0 d12=-6.0 z=-0.337244875

## Nearest historical live analogues

- `2026-09-16T07:19:10.764986Z` distance=1.002 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:54:08.413156Z` distance=1.130 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:58:18.248300Z` distance=1.130 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T07:02:28.186045Z` distance=1.130 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T07:06:38.418412Z` distance=1.130 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

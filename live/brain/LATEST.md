# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T07:19:10.764986Z`  
Memory snapshots: **481**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.632e+04 d1=-1077.0 d12=-1122.0 z=-50.628886859375
- **PERSISTENT_DOWN** `margin` value=3.632e+04 d1=-1077.0 d12=-1122.0 z=-50.628886859375
- **ACCELERATION** `margin` value=3.632e+04 d1=-1077.0 d12=-1122.0 z=-50.628886859375
- **ROBUST_OUTLIER** `margin` value=3.632e+04 d1=-1077.0 d12=-1122.0 z=-50.628886859375
- **ROBUST_OUTLIER** `ind_demand` value=-1.247e+04 d1=0.0 d12=-249.0 z=-10.553780794117648
- **REVERSAL** `thermal_base` value=1.168e+04 d1=30.0 d12=-93.0 z=6.006843270942409
- **ROBUST_OUTLIER** `thermal_base` value=1.168e+04 d1=30.0 d12=-93.0 z=6.006843270942409
- **REVERSAL** `ccgt_gen` value=8343 d1=22.0 d12=-101.0 z=5.96218519687771
- **ROBUST_OUTLIER** `ccgt_gen` value=8343 d1=22.0 d12=-101.0 z=5.96218519687771
- **CHANGE_POINT** `interconnector_net` value=6948 d1=41.0 d12=6044.0 z=1.687853577294686
- **PERSISTENT_UP** `nuclear_gen` value=3337 d1=8.0 d12=8.0 z=2.697959
- **ACCELERATION** `nuclear_gen` value=3337 d1=8.0 d12=8.0 z=2.697959
- **CHANGE_POINT** `imbalance` value=7314 d1=0.0 d12=124.0 z=0.67448975
- **CHANGE_POINT** `ind_generation` value=2.644e+04 d1=0.0 d12=124.0 z=0.67448975
- **PERSISTENT_UP** `wind_gen` value=8121 d1=18.0 d12=414.0 z=-1.7094630974789915

## Nearest historical live analogues

- `2026-09-16T06:20:37.850603Z` distance=0.926 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:24:49.356241Z` distance=0.926 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:51:19.396641Z` distance=0.955 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:55:30.704372Z` distance=0.955 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -79.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:59:40.455597Z` distance=0.955 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -79.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

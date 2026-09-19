# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T19:20:09.701755Z`  
Memory snapshots: **1585**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.621e+04 d1=0.0 d12=8.0 z=-38.378466775
- **ROBUST_OUTLIER** `ind_generation` value=1.621e+04 d1=0.0 d12=8.0 z=-38.378466775
- **CHANGE_POINT** `imbalance` value=-3742 d1=0.0 d12=8.0 z=-10.081846789473685
- **ROBUST_OUTLIER** `imbalance` value=-3742 d1=0.0 d12=8.0 z=-10.081846789473685
- **CHANGE_POINT** `ccgt_gen` value=6032 d1=0.0 d12=-855.0 z=2.2313564449886965
- **CHANGE_POINT** `thermal_base` value=9360 d1=0.0 d12=-859.0 z=2.2202376883458648
- **CHANGE_POINT** `wind_gen` value=1.388e+04 d1=0.0 d12=-347.0 z=-1.3614444029774126
- **PERSISTENT_UP** `interconnector_net` value=698 d1=0.0 d12=2803.0 z=3.1458698028642154
- **ROBUST_OUTLIER** `interconnector_net` value=698 d1=0.0 d12=2803.0 z=3.1458698028642154
- **PERSISTENT_DOWN** `ccgt_gen` value=6032 d1=0.0 d12=-855.0 z=2.2313564449886965
- **PERSISTENT_DOWN** `thermal_base` value=9360 d1=0.0 d12=-859.0 z=2.2202376883458648
- **PERSISTENT_DOWN** `wind_gen` value=1.388e+04 d1=0.0 d12=-347.0 z=-1.3614444029774126
- **ACCELERATION** `nuclear_gen` value=3328 d1=0.0 d12=-4.0 z=-0.8093876999999999
- **PERSISTENT_UP** `ps_gen` value=825 d1=0.0 d12=1.0 z=0.5681144168110918

## Nearest historical live analogues

- `2026-09-19T18:21:25.144867Z` distance=0.000 → {'next30m_imbalance_delta': -611.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T18:25:36.560673Z` distance=0.000 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:22:38.318939Z` distance=0.017 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:26:48.291042Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:31:01.384129Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

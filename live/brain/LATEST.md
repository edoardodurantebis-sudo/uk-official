# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T19:15:57.660081Z`  
Memory snapshots: **1584**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.621e+04 d1=0.0 d12=8.0 z=-38.378466775
- **ROBUST_OUTLIER** `ind_generation` value=1.621e+04 d1=0.0 d12=8.0 z=-38.378466775
- **CHANGE_POINT** `imbalance` value=-3742 d1=0.0 d12=8.0 z=-10.081846789473685
- **ROBUST_OUTLIER** `imbalance` value=-3742 d1=0.0 d12=8.0 z=-10.081846789473685
- **PERSISTENT_UP** `interconnector_net` value=698 d1=68.0 d12=2804.0 z=3.1458698028642154
- **ROBUST_OUTLIER** `interconnector_net` value=698 d1=68.0 d12=2804.0 z=3.1458698028642154
- **CHANGE_POINT** `ps_gen` value=825 d1=0.0 d12=1.0 z=0.6750742298526863
- **PERSISTENT_DOWN** `ccgt_gen` value=6032 d1=-180.0 d12=-721.0 z=2.3054622598531687
- **PERSISTENT_DOWN** `thermal_base` value=9360 d1=-182.0 d12=-721.0 z=2.3030721162026295
- **PERSISTENT_DOWN** `wind_gen` value=1.388e+04 d1=-52.0 d12=-439.0 z=-1.3738073435582823
- **PERSISTENT_DOWN** `nuclear_gen` value=3328 d1=-2.0 d12=0.0 z=-1.0117346249999999
- **ACCELERATION** `nuclear_gen` value=3328 d1=-2.0 d12=0.0 z=-1.0117346249999999
- **PERSISTENT_UP** `ps_gen` value=825 d1=0.0 d12=1.0 z=0.6750742298526863
- **ACCELERATION** `ps_gen` value=825 d1=0.0 d12=1.0 z=0.6750742298526863

## Nearest historical live analogues

- `2026-09-19T18:21:25.144867Z` distance=0.000 → {'next30m_imbalance_delta': -611.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:22:38.318939Z` distance=0.017 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:26:48.291042Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:31:01.384129Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:35:13.165368Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

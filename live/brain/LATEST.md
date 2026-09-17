# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T13:54:16.255911Z`  
Memory snapshots: **879**  
Current physical regime: **BALANCED**

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=2.848e+04 d1=0.0 d12=4.0 z=12.280803938679245
- **CHANGE_POINT** `thermal_base` value=5884 d1=99.0 d12=653.0 z=5.575781933333333
- **CHANGE_POINT** `ccgt_gen` value=2579 d1=103.0 d12=655.0 z=5.193952142655367
- **CHANGE_POINT** `wind_gen` value=1.23e+04 d1=-120.0 d12=-1579.0 z=-5.173672335249042
- **PERSISTENT_UP** `thermal_base` value=5884 d1=99.0 d12=653.0 z=5.575781933333333
- **ROBUST_OUTLIER** `thermal_base` value=5884 d1=99.0 d12=653.0 z=5.575781933333333
- **PERSISTENT_UP** `ccgt_gen` value=2579 d1=103.0 d12=655.0 z=5.193952142655367
- **ROBUST_OUTLIER** `ccgt_gen` value=2579 d1=103.0 d12=655.0 z=5.193952142655367
- **PERSISTENT_DOWN** `wind_gen` value=1.23e+04 d1=-120.0 d12=-1579.0 z=-5.173672335249042
- **ROBUST_OUTLIER** `wind_gen` value=1.23e+04 d1=-120.0 d12=-1579.0 z=-5.173672335249042
- **CHANGE_POINT** `ps_gen` value=-442 d1=244.0 d12=246.0 z=1.9713850994208495
- **ROBUST_OUTLIER** `imbalance` value=1.194e+04 d1=0.0 d12=3.0 z=3.352700176238739
- **CHANGE_POINT** `interconnector_net` value=691 d1=19.0 d12=1067.0 z=0.5037855540123457
- **CHANGE_POINT** `margin` value=3.587e+04 d1=-578.0 d12=-572.0 z=-0.2636259313929314
- **PERSISTENT_UP** `ps_gen` value=-442 d1=244.0 d12=246.0 z=1.9713850994208495

## Nearest historical live analogues

- `2026-09-17T12:55:08.915438Z` distance=0.340 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T12:59:20.777172Z` distance=0.340 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T12:33:59.762276Z` distance=0.346 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': -11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T12:38:10.122034Z` distance=0.346 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': -11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T12:42:21.058328Z` distance=0.346 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': -11.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

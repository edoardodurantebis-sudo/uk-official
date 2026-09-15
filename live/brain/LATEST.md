# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T16:42:58.169534Z`  
Memory snapshots: **273**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2408 d1=132.0 d12=663.0 z=19.646307824468085
- **PERSISTENT_UP** `ccgt_gen` value=1.003e+04 d1=210.0 d12=3600.0 z=21.581072810211946
- **ROBUST_OUTLIER** `ccgt_gen` value=1.003e+04 d1=210.0 d12=3600.0 z=21.581072810211946
- **PERSISTENT_UP** `thermal_base` value=1.335e+04 d1=207.0 d12=3598.0 z=21.385065075525812
- **ROBUST_OUTLIER** `thermal_base` value=1.335e+04 d1=207.0 d12=3598.0 z=21.385065075525812
- **PERSISTENT_UP** `biomass_gen` value=2408 d1=132.0 d12=663.0 z=19.646307824468085
- **ROBUST_OUTLIER** `biomass_gen` value=2408 d1=132.0 d12=663.0 z=19.646307824468085
- **CHANGE_POINT** `interconnector_net` value=570 d1=-53.0 d12=-4362.0 z=-12.188221808051601
- **PERSISTENT_DOWN** `interconnector_net` value=570 d1=-53.0 d12=-4362.0 z=-12.188221808051601
- **ROBUST_OUTLIER** `interconnector_net` value=570 d1=-53.0 d12=-4362.0 z=-12.188221808051601
- **CHANGE_POINT** `ps_gen` value=424 d1=52.0 d12=560.0 z=3.689619525297619
- **PERSISTENT_UP** `ps_gen` value=424 d1=52.0 d12=560.0 z=3.689619525297619
- **ROBUST_OUTLIER** `ps_gen` value=424 d1=52.0 d12=560.0 z=3.689619525297619
- **CHANGE_POINT** `imbalance` value=5827 d1=0.0 d12=10.0 z=1.2429882535714287
- **CHANGE_POINT** `ind_generation` value=2.495e+04 d1=0.0 d12=10.0 z=1.1267044687499999

## Nearest historical live analogues

- `2026-09-15T13:25:09.783150Z` distance=0.239 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:29:22.306019Z` distance=0.239 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:33:32.333732Z` distance=0.239 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:37:45.498739Z` distance=0.239 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:41:57.247780Z` distance=0.239 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

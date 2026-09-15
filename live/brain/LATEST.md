# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T16:34:33.511782Z`  
Memory snapshots: **271**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **PERSISTENT_UP** `ccgt_gen` value=9601 d1=149.0 d12=3958.0 z=20.473817960500963
- **ROBUST_OUTLIER** `ccgt_gen` value=9601 d1=149.0 d12=3958.0 z=20.473817960500963
- **PERSISTENT_UP** `thermal_base` value=1.292e+04 d1=147.0 d12=3958.0 z=20.29401664627151
- **ROBUST_OUTLIER** `thermal_base` value=1.292e+04 d1=147.0 d12=3958.0 z=20.29401664627151
- **CHANGE_POINT** `biomass_gen` value=2106 d1=104.0 d12=369.0 z=10.978396994680852
- **PERSISTENT_DOWN** `interconnector_net` value=677 d1=-2014.0 d12=-4213.0 z=-12.051396753511852
- **ACCELERATION** `interconnector_net` value=677 d1=-2014.0 d12=-4213.0 z=-12.051396753511852
- **ROBUST_OUTLIER** `interconnector_net` value=677 d1=-2014.0 d12=-4213.0 z=-12.051396753511852
- **PERSISTENT_UP** `biomass_gen` value=2106 d1=104.0 d12=369.0 z=10.978396994680852
- **ROBUST_OUTLIER** `biomass_gen` value=2106 d1=104.0 d12=369.0 z=10.978396994680852
- **CHANGE_POINT** `ps_gen` value=125 d1=1.0 d12=260.0 z=2.91379572
- **CHANGE_POINT** `imbalance` value=5827 d1=0.0 d12=10.0 z=1.2429882535714287
- **CHANGE_POINT** `ind_generation` value=2.495e+04 d1=0.0 d12=10.0 z=1.1267044687499999
- **PERSISTENT_UP** `ps_gen` value=125 d1=1.0 d12=260.0 z=2.91379572
- **CHANGE_POINT** `margin` value=3.491e+04 d1=0.0 d12=266.0 z=-0.8632070893782384

## Nearest historical live analogues

- `2026-09-15T13:25:09.783150Z` distance=0.239 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:29:22.306019Z` distance=0.239 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:33:32.333732Z` distance=0.239 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:37:45.498739Z` distance=0.239 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:41:57.247780Z` distance=0.239 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

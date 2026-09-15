# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T16:38:45.835004Z`  
Memory snapshots: **272**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **PERSISTENT_UP** `ccgt_gen` value=9817 d1=216.0 d12=3774.0 z=21.035242954720616
- **ROBUST_OUTLIER** `ccgt_gen` value=9817 d1=216.0 d12=3774.0 z=21.035242954720616
- **PERSISTENT_UP** `thermal_base` value=1.314e+04 d1=216.0 d12=3774.0 z=20.851147759082217
- **ROBUST_OUTLIER** `thermal_base` value=1.314e+04 d1=216.0 d12=3774.0 z=20.851147759082217
- **CHANGE_POINT** `biomass_gen` value=2276 d1=170.0 d12=534.0 z=15.85768454787234
- **PERSISTENT_UP** `biomass_gen` value=2276 d1=170.0 d12=534.0 z=15.85768454787234
- **ROBUST_OUTLIER** `biomass_gen` value=2276 d1=170.0 d12=534.0 z=15.85768454787234
- **PERSISTENT_DOWN** `interconnector_net` value=623 d1=-54.0 d12=-4265.0 z=-12.91020512983947
- **ACCELERATION** `interconnector_net` value=623 d1=-54.0 d12=-4265.0 z=-12.91020512983947
- **ROBUST_OUTLIER** `interconnector_net` value=623 d1=-54.0 d12=-4265.0 z=-12.91020512983947
- **CHANGE_POINT** `ps_gen` value=372 d1=247.0 d12=508.0 z=3.5645842763944224
- **PERSISTENT_UP** `ps_gen` value=372 d1=247.0 d12=508.0 z=3.5645842763944224
- **ACCELERATION** `ps_gen` value=372 d1=247.0 d12=508.0 z=3.5645842763944224
- **ROBUST_OUTLIER** `ps_gen` value=372 d1=247.0 d12=508.0 z=3.5645842763944224
- **CHANGE_POINT** `imbalance` value=5827 d1=0.0 d12=10.0 z=1.2429882535714287

## Nearest historical live analogues

- `2026-09-15T13:25:09.783150Z` distance=0.239 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:29:22.306019Z` distance=0.239 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:33:32.333732Z` distance=0.239 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:37:45.498739Z` distance=0.239 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:41:57.247780Z` distance=0.239 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T06:06:03.123914Z`  
Memory snapshots: **122**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.99e+04 d1=0.0 d12=-115.0 z=-14.306282592105264
- **CHANGE_POINT** `imbalance` value=-587 d1=0.0 d12=-114.0 z=-14.1029675
- **ROBUST_OUTLIER** `ind_generation` value=1.99e+04 d1=0.0 d12=-115.0 z=-14.306282592105264
- **ROBUST_OUTLIER** `imbalance` value=-587 d1=0.0 d12=-114.0 z=-14.1029675
- **CHANGE_POINT** `ccgt_gen` value=4131 d1=91.0 d12=297.0 z=1.4698323849878936
- **CHANGE_POINT** `ps_gen` value=29 d1=-88.0 d12=844.0 z=0.8619926920849421
- **CHANGE_POINT** `margin` value=3.393e+04 d1=0.0 d12=-138.0 z=-0.37154096398305086
- **CHANGE_POINT** `interconnector_net` value=-2521 d1=1053.0 d12=2731.0 z=0.259688660989011
- **PERSISTENT_UP** `ccgt_gen` value=4131 d1=91.0 d12=297.0 z=1.4698323849878936
- **PERSISTENT_UP** `thermal_base` value=7457 d1=96.0 d12=290.0 z=1.4594983024096386
- **REVERSAL** `ps_gen` value=29 d1=-88.0 d12=844.0 z=0.8619926920849421
- **ACCELERATION** `ps_gen` value=29 d1=-88.0 d12=844.0 z=0.8619926920849421
- **PERSISTENT_DOWN** `wind_gen` value=1.341e+04 d1=-4.0 d12=-178.0 z=0.7857708398775216
- **ACCELERATION** `wind_gen` value=1.341e+04 d1=-4.0 d12=-178.0 z=0.7857708398775216
- **PERSISTENT_UP** `interconnector_net` value=-2521 d1=1053.0 d12=2731.0 z=0.259688660989011

## Nearest historical live analogues

- `2026-09-15T04:50:38.818178Z` distance=0.198 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:54:51.558349Z` distance=0.198 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -73.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:59:03.674440Z` distance=0.198 → {'next30m_imbalance_delta': -51.0, 'next30m_margin_delta': -73.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T05:03:14.856536Z` distance=0.198 → {'next30m_imbalance_delta': -51.0, 'next30m_margin_delta': -73.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T05:07:24.996057Z` distance=0.198 → {'next30m_imbalance_delta': -51.0, 'next30m_margin_delta': -73.0, 'next30m_residual_proxy_delta': -671.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

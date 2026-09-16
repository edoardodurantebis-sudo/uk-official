# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T14:25:41.401432Z`  
Memory snapshots: **582**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **ROBUST_OUTLIER** `ps_gen` value=233 d1=0.0 d12=236.0 z=79.5897905
- **CHANGE_POINT** `interconnector_net` value=1.245e+04 d1=1.0 d12=416.0 z=3.124405535672854
- **CHANGE_POINT** `biomass_gen` value=3238 d1=1.0 d12=8.0 z=2.1198249285714286
- **CHANGE_POINT** `margin` value=3.466e+04 d1=0.0 d12=-764.0 z=-1.595188948619632
- **PERSISTENT_UP** `interconnector_net` value=1.245e+04 d1=1.0 d12=416.0 z=3.124405535672854
- **ROBUST_OUTLIER** `interconnector_net` value=1.245e+04 d1=1.0 d12=416.0 z=3.124405535672854
- **CHANGE_POINT** `thermal_base` value=9567 d1=-1.0 d12=-849.0 z=-0.8447817165841583
- **CHANGE_POINT** `ccgt_gen` value=6279 d1=-1.0 d12=-848.0 z=-0.8205300326784282
- **CHANGE_POINT** `imbalance` value=6670 d1=37.0 d12=190.0 z=0.6375458669796558
- **CHANGE_POINT** `wind_gen` value=5324 d1=32.0 d12=1076.0 z=0.36913724748490945
- **PERSISTENT_UP** `biomass_gen` value=3238 d1=1.0 d12=8.0 z=2.1198249285714286
- **CHANGE_POINT** `ind_generation` value=2.545e+04 d1=37.0 d12=190.0 z=0.042155609375
- **PERSISTENT_DOWN** `margin` value=3.466e+04 d1=0.0 d12=-764.0 z=-1.595188948619632
- **ACCELERATION** `margin` value=3.466e+04 d1=0.0 d12=-764.0 z=-1.595188948619632
- **ACCELERATION** `nuclear_gen` value=3288 d1=0.0 d12=-1.0 z=-1.4453351785714286

## Nearest historical live analogues

- `2026-09-16T13:22:42.271610Z` distance=0.444 → {'next30m_imbalance_delta': 304.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T13:26:53.207268Z` distance=0.444 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -319.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T13:31:04.124177Z` distance=0.444 → {'next30m_imbalance_delta': 153.0, 'next30m_margin_delta': -319.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T11:24:42.519084Z` distance=0.475 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T11:28:54.017041Z` distance=0.475 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 36.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

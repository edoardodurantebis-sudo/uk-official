# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T04:19:00.574253Z`  
Memory snapshots: **438**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=7021 d1=0.0 d12=996.0 z=10.750957833333333
- **CHANGE_POINT** `ind_generation` value=2.614e+04 d1=0.0 d12=996.0 z=10.750957833333333
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=0.0 z=12.687507192105263
- **ROBUST_OUTLIER** `imbalance` value=7021 d1=0.0 d12=996.0 z=10.750957833333333
- **ROBUST_OUTLIER** `ind_generation` value=2.614e+04 d1=0.0 d12=996.0 z=10.750957833333333
- **CHANGE_POINT** `interconnector_net` value=385 d1=139.0 d12=-2077.0 z=-5.214548725971922
- **CHANGE_POINT** `ccgt_gen` value=3690 d1=-26.0 d12=1195.0 z=4.9462581666666665
- **CHANGE_POINT** `thermal_base` value=7019 d1=-28.0 d12=1197.0 z=4.804442373076923
- **REVERSAL** `interconnector_net` value=385 d1=139.0 d12=-2077.0 z=-5.214548725971922
- **ROBUST_OUTLIER** `interconnector_net` value=385 d1=139.0 d12=-2077.0 z=-5.214548725971922
- **REVERSAL** `ccgt_gen` value=3690 d1=-26.0 d12=1195.0 z=4.9462581666666665
- **ROBUST_OUTLIER** `ccgt_gen` value=3690 d1=-26.0 d12=1195.0 z=4.9462581666666665
- **REVERSAL** `thermal_base` value=7019 d1=-28.0 d12=1197.0 z=4.804442373076923
- **ROBUST_OUTLIER** `thermal_base` value=7019 d1=-28.0 d12=1197.0 z=4.804442373076923
- **PERSISTENT_DOWN** `wind_gen` value=9486 d1=-55.0 d12=-292.0 z=-1.311266094623656

## Nearest historical live analogues

- `2026-09-16T02:51:04.821431Z` distance=1.398 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:21:42.296151Z` distance=1.398 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:25:54.871254Z` distance=1.398 → {'next30m_imbalance_delta': 20.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:30:06.645142Z` distance=1.398 → {'next30m_imbalance_delta': 20.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:34:18.082313Z` distance=1.398 → {'next30m_imbalance_delta': 20.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

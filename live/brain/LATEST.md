# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T03:16:12.455788Z`  
Memory snapshots: **423**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=1.0 z=18.091313961111112
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=1.0 z=18.091313961111112
- **CHANGE_POINT** `ccgt_gen` value=2509 d1=-23.0 d12=-462.0 z=-7.481647842307693
- **CHANGE_POINT** `thermal_base` value=5834 d1=-29.0 d12=-464.0 z=-6.786762381034483
- **PERSISTENT_DOWN** `ccgt_gen` value=2509 d1=-23.0 d12=-462.0 z=-7.481647842307693
- **ROBUST_OUTLIER** `ccgt_gen` value=2509 d1=-23.0 d12=-462.0 z=-7.481647842307693
- **PERSISTENT_DOWN** `thermal_base` value=5834 d1=-29.0 d12=-464.0 z=-6.786762381034483
- **ROBUST_OUTLIER** `thermal_base` value=5834 d1=-29.0 d12=-464.0 z=-6.786762381034483
- **CHANGE_POINT** `interconnector_net` value=2412 d1=9.0 d12=-1485.0 z=-2.2616529954103672
- **CHANGE_POINT** `imbalance` value=6027 d1=0.0 d12=20.0 z=1.2818836609947644
- **CHANGE_POINT** `ind_generation` value=2.515e+04 d1=0.0 d12=20.0 z=1.2783523010471205
- **CHANGE_POINT** `wind_gen` value=9751 d1=-37.0 d12=-416.0 z=-1.2062862717923604
- **REVERSAL** `interconnector_net` value=2412 d1=9.0 d12=-1485.0 z=-2.2616529954103672
- **PERSISTENT_DOWN** `wind_gen` value=9751 d1=-37.0 d12=-416.0 z=-1.2062862717923604
- **PERSISTENT_UP** `ps_gen` value=224 d1=0.0 d12=236.0 z=0.7634512278177459

## Nearest historical live analogues

- `2026-09-16T02:21:42.296151Z` distance=0.007 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:51:47.907050Z` distance=0.906 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:56:00.416093Z` distance=0.906 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:00:10.670180Z` distance=0.906 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:04:21.558749Z` distance=0.906 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

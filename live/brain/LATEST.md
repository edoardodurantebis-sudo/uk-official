# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T03:20:25.023279Z`  
Memory snapshots: **424**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=1.0 z=15.565148076923078
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=1.0 z=15.565148076923078
- **CHANGE_POINT** `ccgt_gen` value=2509 d1=0.0 d12=-462.0 z=-7.481647842307693
- **CHANGE_POINT** `thermal_base` value=5834 d1=0.0 d12=-464.0 z=-6.915894901408451
- **PERSISTENT_DOWN** `ccgt_gen` value=2509 d1=0.0 d12=-462.0 z=-7.481647842307693
- **ROBUST_OUTLIER** `ccgt_gen` value=2509 d1=0.0 d12=-462.0 z=-7.481647842307693
- **PERSISTENT_DOWN** `thermal_base` value=5834 d1=0.0 d12=-464.0 z=-6.915894901408451
- **ROBUST_OUTLIER** `thermal_base` value=5834 d1=0.0 d12=-464.0 z=-6.915894901408451
- **CHANGE_POINT** `interconnector_net` value=2412 d1=0.0 d12=-1485.0 z=-2.2616529954103672
- **CHANGE_POINT** `wind_gen` value=9751 d1=0.0 d12=-416.0 z=-1.216911576923077
- **CHANGE_POINT** `imbalance` value=6027 d1=0.0 d12=20.0 z=1.138201453125
- **CHANGE_POINT** `ind_generation` value=2.515e+04 d1=0.0 d12=20.0 z=1.138201453125
- **PERSISTENT_DOWN** `interconnector_net` value=2412 d1=0.0 d12=-1485.0 z=-2.2616529954103672
- **PERSISTENT_DOWN** `wind_gen` value=9751 d1=0.0 d12=-416.0 z=-1.216911576923077
- **PERSISTENT_UP** `ps_gen` value=224 d1=0.0 d12=236.0 z=0.7634512278177459

## Nearest historical live analogues

- `2026-09-16T02:21:42.296151Z` distance=0.007 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:25:54.871254Z` distance=0.007 → {'next30m_imbalance_delta': 20.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:51:47.907050Z` distance=0.887 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:56:00.416093Z` distance=0.887 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:00:10.670180Z` distance=0.887 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T03:07:47.035181Z`  
Memory snapshots: **421**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=1462.0 z=36.12487749264706
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=1462.0 z=36.12487749264706
- **CHANGE_POINT** `ccgt_gen` value=2600 d1=-76.0 d12=-459.0 z=-6.405116949248121
- **CHANGE_POINT** `thermal_base` value=5930 d1=-80.0 d12=-455.0 z=-5.753533370805369
- **PERSISTENT_DOWN** `ccgt_gen` value=2600 d1=-76.0 d12=-459.0 z=-6.405116949248121
- **ROBUST_OUTLIER** `ccgt_gen` value=2600 d1=-76.0 d12=-459.0 z=-6.405116949248121
- **PERSISTENT_DOWN** `thermal_base` value=5930 d1=-80.0 d12=-455.0 z=-5.753533370805369
- **ROBUST_OUTLIER** `thermal_base` value=5930 d1=-80.0 d12=-455.0 z=-5.753533370805369
- **CHANGE_POINT** `imbalance` value=6027 d1=0.0 d12=58.0 z=2.378463855263158
- **CHANGE_POINT** `ind_generation` value=2.515e+04 d1=0.0 d12=58.0 z=2.325826724137931
- **CHANGE_POINT** `interconnector_net` value=2628 d1=-636.0 d12=-1269.0 z=-1.9469882308315334
- **CHANGE_POINT** `wind_gen` value=9849 d1=-86.0 d12=-193.0 z=-1.0031011562
- **PERSISTENT_DOWN** `interconnector_net` value=2628 d1=-636.0 d12=-1269.0 z=-1.9469882308315334
- **PERSISTENT_DOWN** `wind_gen` value=9849 d1=-86.0 d12=-193.0 z=-1.0031011562
- **PERSISTENT_UP** `ps_gen` value=222 d1=116.0 d12=234.0 z=0.7569813021582734

## Nearest historical live analogues

- `2026-09-16T01:51:47.907050Z` distance=0.980 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:56:00.416093Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:00:10.670180Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:04:21.558749Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:08:33.939552Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T03:24:36.410956Z`  
Memory snapshots: **425**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=1.0 z=15.565148076923078
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=1.0 z=15.565148076923078
- **CHANGE_POINT** `ccgt_gen` value=2503 d1=-6.0 d12=-363.0 z=-7.597159742248062
- **CHANGE_POINT** `thermal_base` value=5826 d1=-8.0 d12=-363.0 z=-7.036698030141844
- **PERSISTENT_DOWN** `ccgt_gen` value=2503 d1=-6.0 d12=-363.0 z=-7.597159742248062
- **ROBUST_OUTLIER** `ccgt_gen` value=2503 d1=-6.0 d12=-363.0 z=-7.597159742248062
- **PERSISTENT_DOWN** `thermal_base` value=5826 d1=-8.0 d12=-363.0 z=-7.036698030141844
- **ROBUST_OUTLIER** `thermal_base` value=5826 d1=-8.0 d12=-363.0 z=-7.036698030141844
- **CHANGE_POINT** `wind_gen` value=9760 d1=9.0 d12=-433.0 z=-1.2186567117163412
- **CHANGE_POINT** `imbalance` value=6025 d1=-2.0 d12=18.0 z=1.1241495833333335
- **CHANGE_POINT** `ind_generation` value=2.515e+04 d1=-2.0 d12=18.0 z=1.1241495833333335
- **REVERSAL** `interconnector_net` value=2437 d1=25.0 d12=-923.0 z=-2.2252334624730024
- **REVERSAL** `wind_gen` value=9760 d1=9.0 d12=-433.0 z=-1.2186567117163412
- **REVERSAL** `imbalance` value=6025 d1=-2.0 d12=18.0 z=1.1241495833333335
- **REVERSAL** `ind_generation` value=2.515e+04 d1=-2.0 d12=18.0 z=1.1241495833333335

## Nearest historical live analogues

- `2026-09-16T02:21:42.296151Z` distance=0.009 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:25:54.871254Z` distance=0.009 → {'next30m_imbalance_delta': 20.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:30:06.645142Z` distance=0.009 → {'next30m_imbalance_delta': 20.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:51:47.907050Z` distance=0.887 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:56:00.416093Z` distance=0.887 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

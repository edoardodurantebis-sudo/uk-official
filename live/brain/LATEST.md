# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T03:28:46.443654Z`  
Memory snapshots: **426**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=1.0 z=15.565148076923078
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=1.0 z=15.565148076923078
- **CHANGE_POINT** `ccgt_gen` value=2495 d1=-8.0 d12=-299.0 z=-7.7355543203125
- **CHANGE_POINT** `thermal_base` value=5822 d1=-4.0 d12=-301.0 z=-7.167060149280576
- **PERSISTENT_DOWN** `ccgt_gen` value=2495 d1=-8.0 d12=-299.0 z=-7.7355543203125
- **ROBUST_OUTLIER** `ccgt_gen` value=2495 d1=-8.0 d12=-299.0 z=-7.7355543203125
- **PERSISTENT_DOWN** `thermal_base` value=5822 d1=-4.0 d12=-301.0 z=-7.167060149280576
- **ROBUST_OUTLIER** `thermal_base` value=5822 d1=-4.0 d12=-301.0 z=-7.167060149280576
- **CHANGE_POINT** `interconnector_net` value=2462 d1=25.0 d12=-907.0 z=-2.188813929535637
- **CHANGE_POINT** `wind_gen` value=9778 d1=18.0 d12=-391.0 z=-1.1969024791231733
- **CHANGE_POINT** `imbalance` value=6025 d1=0.0 d12=18.0 z=1.1241495833333335
- **CHANGE_POINT** `ind_generation` value=2.515e+04 d1=0.0 d12=18.0 z=1.1241495833333335
- **REVERSAL** `interconnector_net` value=2462 d1=25.0 d12=-907.0 z=-2.188813929535637
- **REVERSAL** `wind_gen` value=9778 d1=18.0 d12=-391.0 z=-1.1969024791231733
- **PERSISTENT_DOWN** `ind_demand` value=-1.221e+04 d1=0.0 d12=-4.0 z=-0.6966041680327869

## Nearest historical live analogues

- `2026-09-16T02:21:42.296151Z` distance=0.009 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:25:54.871254Z` distance=0.009 → {'next30m_imbalance_delta': 20.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:30:06.645142Z` distance=0.009 → {'next30m_imbalance_delta': 20.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:34:18.082313Z` distance=0.009 → {'next30m_imbalance_delta': 20.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:51:47.907050Z` distance=0.887 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

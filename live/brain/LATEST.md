# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T06:29:00.658838Z`  
Memory snapshots: **469**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **ROBUST_OUTLIER** `imbalance` value=7190 d1=0.0 d12=17.0 z=11.707934018656717
- **ROBUST_OUTLIER** `ind_generation` value=2.631e+04 d1=0.0 d12=17.0 z=11.707934018656717
- **PERSISTENT_UP** `ccgt_gen` value=8444 d1=1.0 d12=819.0 z=7.416535284883721
- **ROBUST_OUTLIER** `ccgt_gen` value=8444 d1=1.0 d12=819.0 z=7.416535284883721
- **REVERSAL** `thermal_base` value=1.177e+04 d1=-3.0 d12=818.0 z=7.393800705216017
- **ROBUST_OUTLIER** `thermal_base` value=1.177e+04 d1=-3.0 d12=818.0 z=7.393800705216017
- **CHANGE_POINT** `margin` value=3.745e+04 d1=0.0 d12=-100.0 z=-3.330293140625
- **CHANGE_POINT** `wind_gen` value=7707 d1=-56.0 d12=-887.0 z=-3.07567326
- **PERSISTENT_DOWN** `margin` value=3.745e+04 d1=0.0 d12=-100.0 z=-3.330293140625
- **ROBUST_OUTLIER** `margin` value=3.745e+04 d1=0.0 d12=-100.0 z=-3.330293140625
- **PERSISTENT_DOWN** `wind_gen` value=7707 d1=-56.0 d12=-887.0 z=-3.07567326
- **ROBUST_OUTLIER** `wind_gen` value=7707 d1=-56.0 d12=-887.0 z=-3.07567326
- **CHANGE_POINT** `interconnector_net` value=904 d1=-19.0 d12=2661.0 z=-0.9987730743292241
- **REVERSAL** `interconnector_net` value=904 d1=-19.0 d12=2661.0 z=-0.9987730743292241
- **PERSISTENT_DOWN** `nuclear_gen` value=3329 d1=-4.0 d12=-1.0 z=0.0

## Nearest historical live analogues

- `2026-09-16T05:34:36.913190Z` distance=0.060 → {'next30m_imbalance_delta': 41.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:22:04.416358Z` distance=0.289 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -157.0}
- `2026-09-16T05:26:14.079375Z` distance=0.289 → {'next30m_imbalance_delta': 41.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -157.0}
- `2026-09-16T05:30:25.684923Z` distance=0.289 → {'next30m_imbalance_delta': 41.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -157.0}
- `2026-09-16T03:32:58.473492Z` distance=0.290 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

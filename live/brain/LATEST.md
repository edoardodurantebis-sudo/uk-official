# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T03:03:36.001895Z`  
Memory snapshots: **420**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=1462.0 z=36.12487749264706
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=1462.0 z=36.12487749264706
- **CHANGE_POINT** `ccgt_gen` value=2676 d1=-14.0 d12=-473.0 z=-5.287433634615384
- **CHANGE_POINT** `thermal_base` value=6010 d1=-13.0 d12=-465.0 z=-4.9715701440397355
- **PERSISTENT_DOWN** `ccgt_gen` value=2676 d1=-14.0 d12=-473.0 z=-5.287433634615384
- **ROBUST_OUTLIER** `ccgt_gen` value=2676 d1=-14.0 d12=-473.0 z=-5.287433634615384
- **PERSISTENT_DOWN** `thermal_base` value=6010 d1=-13.0 d12=-465.0 z=-4.9715701440397355
- **ROBUST_OUTLIER** `thermal_base` value=6010 d1=-13.0 d12=-465.0 z=-4.9715701440397355
- **CHANGE_POINT** `imbalance` value=6027 d1=0.0 d12=58.0 z=2.378463855263158
- **CHANGE_POINT** `ind_generation` value=2.515e+04 d1=0.0 d12=58.0 z=2.325826724137931
- **CHANGE_POINT** `interconnector_net` value=3264 d1=-193.0 d12=-661.0 z=-1.0204753129049677
- **CHANGE_POINT** `wind_gen` value=9935 d1=-28.0 d12=-212.0 z=-0.9151900137254902
- **PERSISTENT_UP** `nuclear_gen` value=3334 d1=1.0 d12=8.0 z=1.5738094166666665
- **ACCELERATION** `nuclear_gen` value=3334 d1=1.0 d12=8.0 z=1.5738094166666665
- **PERSISTENT_DOWN** `interconnector_net` value=3264 d1=-193.0 d12=-661.0 z=-1.0204753129049677

## Nearest historical live analogues

- `2026-09-16T01:51:47.907050Z` distance=0.980 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:56:00.416093Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:00:10.670180Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:04:21.558749Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:08:33.939552Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

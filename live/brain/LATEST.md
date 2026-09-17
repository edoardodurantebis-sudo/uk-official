# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T10:18:50.084900Z`  
Memory snapshots: **828**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.441e+04 d1=0.0 d12=-57.0 z=-12.560092912162162
- **ROBUST_OUTLIER** `margin` value=3.441e+04 d1=0.0 d12=-57.0 z=-12.560092912162162
- **CHANGE_POINT** `imbalance` value=6663 d1=0.0 d12=26.0 z=-4.428171836956522
- **ROBUST_OUTLIER** `imbalance` value=6663 d1=0.0 d12=26.0 z=-4.428171836956522
- **REVERSAL** `wind_gen` value=1.558e+04 d1=81.0 d12=-163.0 z=3.6216910218914187
- **ACCELERATION** `wind_gen` value=1.558e+04 d1=81.0 d12=-163.0 z=3.6216910218914187
- **ROBUST_OUTLIER** `wind_gen` value=1.558e+04 d1=81.0 d12=-163.0 z=3.6216910218914187
- **CHANGE_POINT** `ind_demand` value=-1.301e+04 d1=0.0 d12=-23.0 z=-0.9531776370578777
- **CHANGE_POINT** `interconnector_net` value=810 d1=-19.0 d12=-3067.0 z=0.7922293466065496
- **PERSISTENT_DOWN** `ccgt_gen` value=1832 d1=-4.0 d12=-16.0 z=-2.471499881038647
- **ACCELERATION** `ccgt_gen` value=1832 d1=-4.0 d12=-16.0 z=-2.471499881038647
- **PERSISTENT_DOWN** `thermal_base` value=5145 d1=-5.0 d12=-20.0 z=-2.445126315269461
- **ACCELERATION** `thermal_base` value=5145 d1=-5.0 d12=-20.0 z=-2.445126315269461
- **REVERSAL** `biomass_gen` value=1999 d1=-2.0 d12=171.0 z=-1.4914016384462152
- **REVERSAL** `ps_gen` value=-935 d1=-274.0 d12=11.0 z=-0.8528562852595495

## Nearest historical live analogues

- `2026-09-17T09:19:56.543683Z` distance=0.054 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:24:08.362874Z` distance=0.054 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:52:24.970739Z` distance=1.072 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=1.072 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=1.072 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

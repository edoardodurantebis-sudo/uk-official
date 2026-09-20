# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T03:38:17.578686Z`  
Memory snapshots: **1703**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=-61.0 z=28.579094264285715
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=-61.0 z=28.579094264285715
- **ROBUST_OUTLIER** `ind_demand` value=-1.229e+04 d1=0.0 d12=-90.0 z=-17.896461366666664
- **CHANGE_POINT** `ps_gen` value=-695 d1=4.0 d12=2.0 z=-0.8756533596491228
- **CHANGE_POINT** `imbalance` value=-3815 d1=0.0 d12=-60.0 z=-0.6376994
- **CHANGE_POINT** `ind_generation` value=1.614e+04 d1=0.0 d12=-60.0 z=-0.6376994
- **CHANGE_POINT** `ccgt_gen` value=3701 d1=15.0 d12=-265.0 z=-0.5166871135241856
- **CHANGE_POINT** `thermal_base` value=7036 d1=18.0 d12=-261.0 z=-0.5143399669950739
- **PERSISTENT_DOWN** `interconnector_net` value=-1.188e+04 d1=0.0 d12=-832.0 z=-1.7765990718107876
- **ACCELERATION** `interconnector_net` value=-1.188e+04 d1=0.0 d12=-832.0 z=-1.7765990718107876
- **PERSISTENT_UP** `ps_gen` value=-695 d1=4.0 d12=2.0 z=-0.8756533596491228
- **ACCELERATION** `ps_gen` value=-695 d1=4.0 d12=2.0 z=-0.8756533596491228
- **PERSISTENT_DOWN** `wind_gen` value=1.512e+04 d1=-81.0 d12=-203.0 z=-0.6444517449392713
- **REVERSAL** `ccgt_gen` value=3701 d1=15.0 d12=-265.0 z=-0.5166871135241856
- **REVERSAL** `thermal_base` value=7036 d1=18.0 d12=-261.0 z=-0.5143399669950739

## Nearest historical live analogues

- `2026-09-20T02:20:49.967105Z` distance=1.035 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:25:01.524399Z` distance=1.035 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:29:13.820300Z` distance=1.035 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:33:25.726465Z` distance=1.035 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:37:39.122581Z` distance=1.035 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

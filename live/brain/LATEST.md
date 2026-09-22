# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T21:49:59.633660Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.687e+04 d1=0.0 d12=-1423.0 z=-3.731719777939042
- **CHANGE_POINT** `ccgt_gen` value=1.313e+04 d1=0.0 d12=-1430.0 z=-3.720384384726225
- **CHANGE_POINT** `interconnector_net` value=4760 d1=0.0 d12=-1914.0 z=-2.583152234042553
- **PERSISTENT_DOWN** `thermal_base` value=1.687e+04 d1=0.0 d12=-1423.0 z=-3.731719777939042
- **ROBUST_OUTLIER** `thermal_base` value=1.687e+04 d1=0.0 d12=-1423.0 z=-3.731719777939042
- **PERSISTENT_DOWN** `ccgt_gen` value=1.313e+04 d1=0.0 d12=-1430.0 z=-3.720384384726225
- **ROBUST_OUTLIER** `ccgt_gen` value=1.313e+04 d1=0.0 d12=-1430.0 z=-3.720384384726225
- **CHANGE_POINT** `margin` value=3.721e+04 d1=-1.0 d12=-1.0 z=1.6267105735294118
- **CHANGE_POINT** `imbalance` value=-8019 d1=0.0 d12=22.0 z=-0.9563660634328358
- **CHANGE_POINT** `ind_generation` value=1.315e+04 d1=0.0 d12=22.0 z=-0.657195141025641
- **PERSISTENT_UP** `nuclear_gen` value=3740 d1=0.0 d12=7.0 z=2.56306105
- **PERSISTENT_UP** `wind_gen` value=2465 d1=0.0 d12=145.0 z=1.994249477436823
- **PERSISTENT_DOWN** `margin` value=3.721e+04 d1=-1.0 d12=-1.0 z=1.6267105735294118
- **ACCELERATION** `margin` value=3.721e+04 d1=-1.0 d12=-1.0 z=1.6267105735294118

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.001 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:55:13.117327Z` distance=0.001 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:22:55.061007Z` distance=0.020 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:27:09.876357Z` distance=0.020 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:31:30.036637Z` distance=0.020 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

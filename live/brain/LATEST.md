# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T21:45:44.692302Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.687e+04 d1=-155.0 d12=-1547.0 z=-3.731719777939042
- **CHANGE_POINT** `ccgt_gen` value=1.313e+04 d1=-155.0 d12=-1556.0 z=-3.720384384726225
- **CHANGE_POINT** `interconnector_net` value=4760 d1=0.0 d12=-1890.0 z=-2.5773684083333332
- **CHANGE_POINT** `imbalance` value=-8019 d1=0.0 d12=22.0 z=-1.7782002499999998
- **PERSISTENT_DOWN** `thermal_base` value=1.687e+04 d1=-155.0 d12=-1547.0 z=-3.731719777939042
- **ROBUST_OUTLIER** `thermal_base` value=1.687e+04 d1=-155.0 d12=-1547.0 z=-3.731719777939042
- **PERSISTENT_DOWN** `ccgt_gen` value=1.313e+04 d1=-155.0 d12=-1556.0 z=-3.720384384726225
- **ROBUST_OUTLIER** `ccgt_gen` value=1.313e+04 d1=-155.0 d12=-1556.0 z=-3.720384384726225
- **CHANGE_POINT** `margin` value=3.721e+04 d1=0.0 d12=0.0 z=1.4239228055555555
- **PERSISTENT_UP** `nuclear_gen` value=3740 d1=0.0 d12=9.0 z=3.37244875
- **ACCELERATION** `nuclear_gen` value=3740 d1=0.0 d12=9.0 z=3.37244875
- **ROBUST_OUTLIER** `nuclear_gen` value=3740 d1=0.0 d12=9.0 z=3.37244875
- **CHANGE_POINT** `ind_generation` value=1.315e+04 d1=0.0 d12=22.0 z=-0.9961694769230768
- **PERSISTENT_UP** `wind_gen` value=2465 d1=9.0 d12=143.0 z=2.0210076085766424

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.001 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:22:55.061007Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:27:09.876357Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:31:30.036637Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:35:44.591045Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

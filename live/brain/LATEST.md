# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T15:56:21.179145Z`  
Memory snapshots: **2218**  
Current physical regime: **BALANCED**

## Active patterns

- **PERSISTENT_UP** `thermal_base` value=1.53e+04 d1=415.0 d12=2331.0 z=5.7203096220508165
- **ROBUST_OUTLIER** `thermal_base` value=1.53e+04 d1=415.0 d12=2331.0 z=5.7203096220508165
- **PERSISTENT_UP** `ccgt_gen` value=1.18e+04 d1=415.0 d12=2314.0 z=5.577970543141594
- **ROBUST_OUTLIER** `ccgt_gen` value=1.18e+04 d1=415.0 d12=2314.0 z=5.577970543141594
- **CHANGE_POINT** `interconnector_net` value=1.087e+04 d1=-26.0 d12=-371.0 z=-1.2302429180929095
- **CHANGE_POINT** `imbalance` value=-3079 d1=28.0 d12=128.0 z=0.67448975
- **CHANGE_POINT** `ind_generation` value=1.838e+04 d1=28.0 d12=83.0 z=0.4354973188976378
- **PERSISTENT_DOWN** `interconnector_net` value=1.087e+04 d1=-26.0 d12=-371.0 z=-1.2302429180929095
- **REVERSAL** `ps_gen` value=-126 d1=28.0 d12=-255.0 z=-1.2200329301470587
- **PERSISTENT_DOWN** `margin` value=3.621e+04 d1=0.0 d12=-47.0 z=-0.854945341008772
- **ACCELERATION** `margin` value=3.621e+04 d1=0.0 d12=-47.0 z=-0.854945341008772
- **PERSISTENT_UP** `imbalance` value=-3079 d1=28.0 d12=128.0 z=0.67448975
- **PERSISTENT_UP** `nuclear_gen` value=3506 d1=0.0 d12=17.0 z=0.5707220961538462
- **PERSISTENT_UP** `ind_generation` value=1.838e+04 d1=28.0 d12=83.0 z=0.4354973188976378
- **PERSISTENT_DOWN** `wind_gen` value=3357 d1=-12.0 d12=-82.0 z=-0.37009340178571426

## Nearest historical live analogues

- `2026-09-21T14:23:01.446169Z` distance=0.033 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:27:16.085310Z` distance=0.033 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:31:28.406523Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:35:41.380076Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:39:54.228512Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

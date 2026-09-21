# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T16:13:17.779921Z`  
Memory snapshots: **2222**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.596e+04 d1=79.0 d12=2534.0 z=6.525780140199637
- **CHANGE_POINT** `ccgt_gen` value=1.245e+04 d1=80.0 d12=2523.0 z=6.363482499778761
- **PERSISTENT_UP** `thermal_base` value=1.596e+04 d1=79.0 d12=2534.0 z=6.525780140199637
- **ROBUST_OUTLIER** `thermal_base` value=1.596e+04 d1=79.0 d12=2534.0 z=6.525780140199637
- **PERSISTENT_UP** `ccgt_gen` value=1.245e+04 d1=80.0 d12=2523.0 z=6.363482499778761
- **ROBUST_OUTLIER** `ccgt_gen` value=1.245e+04 d1=80.0 d12=2523.0 z=6.363482499778761
- **CHANGE_POINT** `interconnector_net` value=1.02e+04 d1=-137.0 d12=-1007.0 z=-3.430167921760391
- **PERSISTENT_DOWN** `interconnector_net` value=1.02e+04 d1=-137.0 d12=-1007.0 z=-3.430167921760391
- **ROBUST_OUTLIER** `interconnector_net` value=1.02e+04 d1=-137.0 d12=-1007.0 z=-3.430167921760391
- **CHANGE_POINT** `margin` value=3.621e+04 d1=0.0 d12=-51.0 z=-0.854945341008772
- **CHANGE_POINT** `imbalance` value=-3079 d1=0.0 d12=128.0 z=0.67448975
- **CHANGE_POINT** `ind_generation` value=1.838e+04 d1=0.0 d12=83.0 z=0.4354973188976378
- **CHANGE_POINT** `nuclear_gen` value=3506 d1=-1.0 d12=11.0 z=0.3147618833333333
- **PERSISTENT_DOWN** `wind_gen` value=3197 d1=-107.0 d12=-139.0 z=-1.149330534
- **ACCELERATION** `wind_gen` value=3197 d1=-107.0 d12=-139.0 z=-1.149330534

## Nearest historical live analogues

- `2026-09-21T14:23:01.446169Z` distance=0.033 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:27:16.085310Z` distance=0.033 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:31:28.406523Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:35:41.380076Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:39:54.228512Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

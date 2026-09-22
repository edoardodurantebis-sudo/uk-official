# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T04:29:08.128499Z`  
Memory snapshots: **2395**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.779e+04 d1=0.0 d12=0.0 z=21.259916920000002
- **PERSISTENT_DOWN** `interconnector_net` value=-3178 d1=-43.0 d12=-1717.0 z=-5.942061729707252
- **ROBUST_OUTLIER** `interconnector_net` value=-3178 d1=-43.0 d12=-1717.0 z=-5.942061729707252
- **CHANGE_POINT** `ccgt_gen` value=1.264e+04 d1=109.0 d12=1333.0 z=3.792997139940239
- **CHANGE_POINT** `thermal_base` value=1.629e+04 d1=108.0 d12=1331.0 z=3.7110058618677044
- **CHANGE_POINT** `imbalance` value=-3324 d1=0.0 d12=-680.0 z=-3.5011681679389315
- **CHANGE_POINT** `ind_generation` value=1.814e+04 d1=0.0 d12=-680.0 z=-3.5011681679389315
- **CHANGE_POINT** `ps_gen` value=-700 d1=5.0 d12=-292.0 z=-2.4790456600877193
- **PERSISTENT_UP** `ccgt_gen` value=1.264e+04 d1=109.0 d12=1333.0 z=3.792997139940239
- **ROBUST_OUTLIER** `ccgt_gen` value=1.264e+04 d1=109.0 d12=1333.0 z=3.792997139940239
- **CHANGE_POINT** `biomass_gen` value=3029 d1=1.0 d12=-14.0 z=-1.7536733500000001
- **PERSISTENT_UP** `thermal_base` value=1.629e+04 d1=108.0 d12=1331.0 z=3.7110058618677044
- **ROBUST_OUTLIER** `thermal_base` value=1.629e+04 d1=108.0 d12=1331.0 z=3.7110058618677044
- **CHANGE_POINT** `wind_gen` value=3430 d1=-46.0 d12=-425.0 z=-1.7081233928571427
- **PERSISTENT_DOWN** `imbalance` value=-3324 d1=0.0 d12=-680.0 z=-3.5011681679389315

## Nearest historical live analogues

- `2026-09-22T03:33:35.816390Z` distance=0.023 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:20:28.289850Z` distance=0.199 → {'next30m_imbalance_delta': 15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -2141.0}
- `2026-09-22T03:24:38.283330Z` distance=0.199 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': -2141.0}
- `2026-09-22T03:29:25.727103Z` distance=0.199 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': -2141.0}
- `2026-09-22T02:20:47.392507Z` distance=0.200 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

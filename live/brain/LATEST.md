# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T12:03:10.360318Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-13 d1=0.0 d12=151.0 z=35.073467
- **ROBUST_OUTLIER** `ps_gen` value=-13 d1=0.0 d12=151.0 z=35.073467
- **CHANGE_POINT** `nuclear_gen` value=3705 d1=21.0 d12=55.0 z=12.1408155
- **PERSISTENT_UP** `nuclear_gen` value=3705 d1=21.0 d12=55.0 z=12.1408155
- **ROBUST_OUTLIER** `nuclear_gen` value=3705 d1=21.0 d12=55.0 z=12.1408155
- **ROBUST_OUTLIER** `wind_forecast` value=1.301e+04 d1=0.0 d12=0.0 z=7.81390012264151
- **CHANGE_POINT** `biomass_gen` value=3005 d1=1.0 d12=-37.0 z=-2.1920916875
- **CHANGE_POINT** `ind_generation` value=1.411e+04 d1=0.0 d12=-848.0 z=-2.0409129504310344
- **CHANGE_POINT** `imbalance` value=-7049 d1=0.0 d12=-819.0 z=-1.4770758726890756
- **CHANGE_POINT** `margin` value=3.703e+04 d1=0.0 d12=27.0 z=-0.67448975
- **REVERSAL** `biomass_gen` value=3005 d1=1.0 d12=-37.0 z=-2.1920916875
- **PERSISTENT_DOWN** `ind_generation` value=1.411e+04 d1=0.0 d12=-848.0 z=-2.0409129504310344
- **PERSISTENT_DOWN** `wind_gen` value=3318 d1=-79.0 d12=-361.0 z=-1.8012385231213872
- **REVERSAL** `ccgt_gen` value=7867 d1=134.0 d12=-849.0 z=-1.6371822417776571
- **REVERSAL** `thermal_base` value=1.157e+04 d1=155.0 d12=-794.0 z=-1.621641659901934

## Nearest historical live analogues

- `2026-09-22T10:54:49.977311Z` distance=0.014 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 27.0, 'next30m_residual_proxy_delta': -29.0}
- `2026-09-22T10:59:02.930644Z` distance=0.014 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 27.0, 'next30m_residual_proxy_delta': -29.0}
- `2026-09-22T11:03:15.730589Z` distance=0.014 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 27.0, 'next30m_residual_proxy_delta': -29.0}
- `2026-09-22T11:08:05.212103Z` distance=0.014 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 27.0, 'next30m_residual_proxy_delta': -29.0}
- `2026-09-22T05:53:47.929906Z` distance=0.387 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 41.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

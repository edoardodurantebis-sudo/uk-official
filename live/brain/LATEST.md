# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T12:54:37.550737Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `nuclear_gen` value=3731 d1=9.0 d12=26.0 z=17.986393333333336
- **PERSISTENT_UP** `nuclear_gen` value=3731 d1=9.0 d12=26.0 z=17.986393333333336
- **ROBUST_OUTLIER** `nuclear_gen` value=3731 d1=9.0 d12=26.0 z=17.986393333333336
- **ROBUST_OUTLIER** `wind_forecast` value=1.308e+04 d1=0.0 d12=75.0 z=8.76836675
- **CHANGE_POINT** `wind_gen` value=2499 d1=-50.0 d12=-819.0 z=-6.647615324519231
- **PERSISTENT_DOWN** `ps_gen` value=-126 d1=0.0 d12=-113.0 z=8.190232678571428
- **ROBUST_OUTLIER** `ps_gen` value=-126 d1=0.0 d12=-113.0 z=8.190232678571428
- **PERSISTENT_DOWN** `wind_gen` value=2499 d1=-50.0 d12=-819.0 z=-6.647615324519231
- **ROBUST_OUTLIER** `wind_gen` value=2499 d1=-50.0 d12=-819.0 z=-6.647615324519231
- **CHANGE_POINT** `biomass_gen` value=2964 d1=-15.0 d12=-41.0 z=-2.824425828125
- **CHANGE_POINT** `imbalance` value=-7090 d1=-15.0 d12=-41.0 z=-0.8622118163430421
- **CHANGE_POINT** `ind_generation` value=1.407e+04 d1=-15.0 d12=-41.0 z=-0.8527362980826396
- **PERSISTENT_DOWN** `biomass_gen` value=2964 d1=-15.0 d12=-41.0 z=-2.824425828125
- **ACCELERATION** `biomass_gen` value=2964 d1=-15.0 d12=-41.0 z=-2.824425828125
- **CHANGE_POINT** `interconnector_net` value=1.111e+04 d1=18.0 d12=171.0 z=0.8042323643312101

## Nearest historical live analogues

- `2026-09-22T11:20:45.669526Z` distance=0.095 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:25:00.789915Z` distance=0.095 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:29:14.531873Z` distance=0.095 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:33:26.711703Z` distance=0.095 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:37:39.590020Z` distance=0.095 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

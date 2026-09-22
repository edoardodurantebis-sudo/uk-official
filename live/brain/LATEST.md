# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T12:58:50.504318Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **PERSISTENT_UP** `nuclear_gen` value=3732 d1=1.0 d12=25.0 z=15.60961992857143
- **ROBUST_OUTLIER** `nuclear_gen` value=3732 d1=1.0 d12=25.0 z=15.60961992857143
- **ROBUST_OUTLIER** `wind_forecast` value=1.308e+04 d1=0.0 d12=75.0 z=8.76836675
- **CHANGE_POINT** `wind_gen` value=2471 d1=-28.0 d12=-802.0 z=-6.456706425
- **REVERSAL** `ps_gen` value=-125 d1=1.0 d12=-89.0 z=7.2507648125
- **ROBUST_OUTLIER** `ps_gen` value=-125 d1=1.0 d12=-89.0 z=7.2507648125
- **PERSISTENT_DOWN** `wind_gen` value=2471 d1=-28.0 d12=-802.0 z=-6.456706425
- **ROBUST_OUTLIER** `wind_gen` value=2471 d1=-28.0 d12=-802.0 z=-6.456706425
- **CHANGE_POINT** `biomass_gen` value=2966 d1=2.0 d12=-37.0 z=-2.740114609375
- **CHANGE_POINT** `imbalance` value=-7090 d1=0.0 d12=-41.0 z=-0.8622118163430421
- **CHANGE_POINT** `ind_generation` value=1.407e+04 d1=0.0 d12=-41.0 z=-0.8527362980826396
- **CHANGE_POINT** `interconnector_net` value=1.111e+04 d1=-1.0 d12=195.0 z=0.8072384355670102
- **REVERSAL** `biomass_gen` value=2966 d1=2.0 d12=-37.0 z=-2.740114609375
- **ACCELERATION** `biomass_gen` value=2966 d1=2.0 d12=-37.0 z=-2.740114609375
- **PERSISTENT_DOWN** `imbalance` value=-7090 d1=0.0 d12=-41.0 z=-0.8622118163430421

## Nearest historical live analogues

- `2026-09-22T11:20:45.669526Z` distance=0.095 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:25:00.789915Z` distance=0.095 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:29:14.531873Z` distance=0.095 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:33:26.711703Z` distance=0.095 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:37:39.590020Z` distance=0.095 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

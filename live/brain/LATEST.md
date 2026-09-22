# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T12:41:52.346468Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

Regime read: wind rising.

## Active patterns

- **CHANGE_POINT** `nuclear_gen` value=3728 d1=-9.0 d12=50.0 z=17.311903583333333
- **REVERSAL** `nuclear_gen` value=3728 d1=-9.0 d12=50.0 z=17.311903583333333
- **ROBUST_OUTLIER** `nuclear_gen` value=3728 d1=-9.0 d12=50.0 z=17.311903583333333
- **CHANGE_POINT** `ps_gen` value=-125 d1=1.0 d12=-118.0 z=9.892516333333333
- **REVERSAL** `ps_gen` value=-125 d1=1.0 d12=-118.0 z=9.892516333333333
- **ROBUST_OUTLIER** `ps_gen` value=-125 d1=1.0 d12=-118.0 z=9.892516333333333
- **PERSISTENT_UP** `wind_forecast` value=1.308e+04 d1=0.0 d12=75.0 z=8.76836675
- **ROBUST_OUTLIER** `wind_forecast` value=1.308e+04 d1=0.0 d12=75.0 z=8.76836675
- **CHANGE_POINT** `wind_gen` value=2587 d1=-56.0 d12=-964.0 z=-6.286506407766991
- **PERSISTENT_DOWN** `wind_gen` value=2587 d1=-56.0 d12=-964.0 z=-6.286506407766991
- **ROBUST_OUTLIER** `wind_gen` value=2587 d1=-56.0 d12=-964.0 z=-6.286506407766991
- **CHANGE_POINT** `ind_generation` value=1.408e+04 d1=0.0 d12=-851.0 z=-1.0482169272093877
- **CHANGE_POINT** `imbalance` value=-7075 d1=0.0 d12=-851.0 z=-0.8606086790693904
- **CHANGE_POINT** `interconnector_net` value=1.107e+04 d1=24.0 d12=123.0 z=0.7678476963492064
- **PERSISTENT_DOWN** `biomass_gen` value=2986 d1=-1.0 d12=-16.0 z=-2.0234692499999998

## Nearest historical live analogues

- `2026-09-22T11:20:45.669526Z` distance=0.019 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:25:00.789915Z` distance=0.019 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:29:14.531873Z` distance=0.019 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:33:26.711703Z` distance=0.019 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:37:39.590020Z` distance=0.019 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

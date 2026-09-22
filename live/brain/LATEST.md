# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T12:24:58.085132Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `nuclear_gen` value=3730 d1=0.0 d12=75.0 z=17.761563416666664
- **PERSISTENT_UP** `nuclear_gen` value=3730 d1=0.0 d12=75.0 z=17.761563416666664
- **ROBUST_OUTLIER** `nuclear_gen` value=3730 d1=0.0 d12=75.0 z=17.761563416666664
- **CHANGE_POINT** `ps_gen` value=-125 d1=0.0 d12=-106.0 z=9.892516333333333
- **ROBUST_OUTLIER** `ps_gen` value=-125 d1=0.0 d12=-106.0 z=9.892516333333333
- **ROBUST_OUTLIER** `wind_forecast` value=1.301e+04 d1=0.0 d12=0.0 z=7.81390012264151
- **CHANGE_POINT** `wind_gen` value=2816 d1=0.0 d12=-1009.0 z=-5.493344297222222
- **PERSISTENT_DOWN** `wind_gen` value=2816 d1=0.0 d12=-1009.0 z=-5.493344297222222
- **ROBUST_OUTLIER** `wind_gen` value=2816 d1=0.0 d12=-1009.0 z=-5.493344297222222
- **CHANGE_POINT** `biomass_gen` value=3000 d1=0.0 d12=-15.0 z=-1.3939454833333333
- **CHANGE_POINT** `ind_generation` value=1.408e+04 d1=-26.0 d12=-851.0 z=-1.0482169272093877
- **CHANGE_POINT** `imbalance` value=-7075 d1=-26.0 d12=-851.0 z=-0.8606086790693904
- **CHANGE_POINT** `margin` value=3.706e+04 d1=0.0 d12=33.0 z=-0.6451254205145119
- **CHANGE_POINT** `demand_forecast` value=2.066e+04 d1=0.0 d12=0.0 z=0.0
- **PERSISTENT_DOWN** `biomass_gen` value=3000 d1=0.0 d12=-15.0 z=-1.3939454833333333

## Nearest historical live analogues

- `2026-09-22T11:20:45.669526Z` distance=0.017 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:25:00.789915Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:29:14.531873Z` distance=0.017 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T10:54:49.977311Z` distance=0.031 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 27.0, 'next30m_residual_proxy_delta': -29.0}
- `2026-09-22T10:59:02.930644Z` distance=0.031 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 27.0, 'next30m_residual_proxy_delta': -29.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

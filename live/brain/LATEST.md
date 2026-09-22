# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T12:29:09.664290Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `nuclear_gen` value=3733 d1=3.0 d12=75.0 z=18.436053166666667
- **PERSISTENT_UP** `nuclear_gen` value=3733 d1=3.0 d12=75.0 z=18.436053166666667
- **ROBUST_OUTLIER** `nuclear_gen` value=3733 d1=3.0 d12=75.0 z=18.436053166666667
- **PERSISTENT_DOWN** `ps_gen` value=-126 d1=-1.0 d12=-119.0 z=9.667686416666667
- **ROBUST_OUTLIER** `ps_gen` value=-126 d1=-1.0 d12=-119.0 z=9.667686416666667
- **CHANGE_POINT** `wind_gen` value=2750 d1=-66.0 d12=-979.0 z=-5.987970113888889
- **ROBUST_OUTLIER** `wind_forecast` value=1.301e+04 d1=0.0 d12=0.0 z=7.81390012264151
- **PERSISTENT_DOWN** `wind_gen` value=2750 d1=-66.0 d12=-979.0 z=-5.987970113888889
- **ROBUST_OUTLIER** `wind_gen` value=2750 d1=-66.0 d12=-979.0 z=-5.987970113888889
- **CHANGE_POINT** `ind_generation` value=1.408e+04 d1=0.0 d12=-851.0 z=-1.0482169272093877
- **CHANGE_POINT** `imbalance` value=-7075 d1=0.0 d12=-851.0 z=-0.8606086790693904
- **CHANGE_POINT** `margin` value=3.706e+04 d1=0.0 d12=33.0 z=-0.6451254205145119
- **CHANGE_POINT** `demand_forecast` value=2.066e+04 d1=0.0 d12=0.0 z=0.0
- **REVERSAL** `biomass_gen` value=3001 d1=1.0 d12=-7.0 z=-1.3489795
- **PERSISTENT_DOWN** `ind_generation` value=1.408e+04 d1=0.0 d12=-851.0 z=-1.0482169272093877

## Nearest historical live analogues

- `2026-09-22T11:20:45.669526Z` distance=0.017 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:25:00.789915Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:29:14.531873Z` distance=0.017 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:33:26.711703Z` distance=0.017 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T10:54:49.977311Z` distance=0.032 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 27.0, 'next30m_residual_proxy_delta': -29.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

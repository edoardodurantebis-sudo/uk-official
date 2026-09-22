# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T13:20:01.731737Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **PERSISTENT_UP** `ps_gen` value=-6 d1=0.0 d12=120.0 z=24.13174438888889
- **ROBUST_OUTLIER** `ps_gen` value=-6 d1=0.0 d12=120.0 z=24.13174438888889
- **ROBUST_OUTLIER** `nuclear_gen` value=3732 d1=0.0 d12=-1.0 z=13.57410621875
- **ROBUST_OUTLIER** `wind_forecast` value=1.308e+04 d1=0.0 d12=75.0 z=8.76836675
- **PERSISTENT_DOWN** `wind_gen` value=2426 d1=-43.0 d12=-324.0 z=-5.631861182509506
- **ROBUST_OUTLIER** `wind_gen` value=2426 d1=-43.0 d12=-324.0 z=-5.631861182509506
- **CHANGE_POINT** `biomass_gen` value=2948 d1=-6.0 d12=-53.0 z=-3.2930970147058822
- **PERSISTENT_DOWN** `biomass_gen` value=2948 d1=-6.0 d12=-53.0 z=-3.2930970147058822
- **ROBUST_OUTLIER** `biomass_gen` value=2948 d1=-6.0 d12=-53.0 z=-3.2930970147058822
- **CHANGE_POINT** `ind_generation` value=1.407e+04 d1=0.0 d12=-15.0 z=-0.859071239492811
- **CHANGE_POINT** `imbalance` value=-7090 d1=0.0 d12=-15.0 z=-0.7015432993435291
- **CHANGE_POINT** `ccgt_gen` value=9097 d1=13.0 d12=597.0 z=-0.36819971859903383
- **CHANGE_POINT** `thermal_base` value=1.283e+04 d1=13.0 d12=596.0 z=-0.3470368741804558
- **CHANGE_POINT** `interconnector_net` value=1.064e+04 d1=-25.0 d12=-343.0 z=-0.30699367358803986
- **PERSISTENT_UP** `ccgt_gen` value=9097 d1=13.0 d12=597.0 z=-0.36819971859903383

## Nearest historical live analogues

- `2026-09-22T12:20:45.067431Z` distance=0.078 → {'next30m_imbalance_delta': -26.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -75.0}
- `2026-09-22T12:24:58.085132Z` distance=0.078 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -75.0}
- `2026-09-22T11:20:45.669526Z` distance=0.095 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:25:00.789915Z` distance=0.095 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:29:14.531873Z` distance=0.095 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

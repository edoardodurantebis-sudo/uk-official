# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T13:24:17.015287Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-6 d1=0.0 d12=120.0 z=24.13174438888889
- **ROBUST_OUTLIER** `ps_gen` value=-6 d1=0.0 d12=120.0 z=24.13174438888889
- **PERSISTENT_DOWN** `nuclear_gen` value=3730 d1=-2.0 d12=-7.0 z=11.691155666666667
- **ROBUST_OUTLIER** `nuclear_gen` value=3730 d1=-2.0 d12=-7.0 z=11.691155666666667
- **ROBUST_OUTLIER** `wind_forecast` value=1.308e+04 d1=0.0 d12=0.0 z=8.76836675
- **PERSISTENT_DOWN** `wind_gen` value=2375 d1=-51.0 d12=-331.0 z=-5.8934503631178705
- **ROBUST_OUTLIER** `wind_gen` value=2375 d1=-51.0 d12=-331.0 z=-5.8934503631178705
- **CHANGE_POINT** `biomass_gen` value=2946 d1=-2.0 d12=-48.0 z=-3.37244875
- **PERSISTENT_DOWN** `biomass_gen` value=2946 d1=-2.0 d12=-48.0 z=-3.37244875
- **ROBUST_OUTLIER** `biomass_gen` value=2946 d1=-2.0 d12=-48.0 z=-3.37244875
- **CHANGE_POINT** `ind_generation` value=1.406e+04 d1=-11.0 d12=-26.0 z=-0.8120669468001261
- **CHANGE_POINT** `imbalance` value=-7101 d1=-11.0 d12=-26.0 z=-0.6853889007147297
- **CHANGE_POINT** `interconnector_net` value=1.061e+04 d1=-27.0 d12=-405.0 z=-0.3993368916967509
- **CHANGE_POINT** `ccgt_gen` value=9076 d1=-21.0 d12=677.0 z=-0.3588073032283465
- **CHANGE_POINT** `thermal_base` value=1.281e+04 d1=-23.0 d12=670.0 z=-0.341457664365549

## Nearest historical live analogues

- `2026-09-22T12:20:45.067431Z` distance=0.081 → {'next30m_imbalance_delta': -26.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -75.0}
- `2026-09-22T12:24:58.085132Z` distance=0.081 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -75.0}
- `2026-09-22T12:29:09.664290Z` distance=0.081 → {'next30m_imbalance_delta': -15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 141.0, 'next30m_residual_proxy_delta': -75.0}
- `2026-09-22T11:20:45.669526Z` distance=0.097 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:25:00.789915Z` distance=0.097 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

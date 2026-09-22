# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T23:47:55.708752Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.365e+04 d1=81.0 d12=-170.0 z=-9.142288123342174
- **CHANGE_POINT** `ccgt_gen` value=9921 d1=85.0 d12=-161.0 z=-9.110964718253967
- **REVERSAL** `thermal_base` value=1.365e+04 d1=81.0 d12=-170.0 z=-9.142288123342174
- **ROBUST_OUTLIER** `thermal_base` value=1.365e+04 d1=81.0 d12=-170.0 z=-9.142288123342174
- **REVERSAL** `ccgt_gen` value=9921 d1=85.0 d12=-161.0 z=-9.110964718253967
- **ROBUST_OUTLIER** `ccgt_gen` value=9921 d1=85.0 d12=-161.0 z=-9.110964718253967
- **ROBUST_OUTLIER** `ind_demand` value=-1.248e+04 d1=0.0 d12=9.0 z=-8.76836675
- **PERSISTENT_UP** `wind_gen` value=3295 d1=90.0 d12=346.0 z=2.0932440517241377
- **REVERSAL** `interconnector_net` value=4203 d1=1.0 d12=-1121.0 z=-1.5923229757501745
- **PERSISTENT_DOWN** `nuclear_gen` value=3730 d1=-4.0 d12=-9.0 z=-0.5058673124999999
- **REVERSAL** `biomass_gen` value=2913 d1=-3.0 d12=5.0 z=0.40469384999999997
- **ACCELERATION** `biomass_gen` value=2913 d1=-3.0 d12=5.0 z=0.40469384999999997

## Nearest historical live analogues

- `2026-09-22T22:19:30.437012Z` distance=0.024 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:23:43.484966Z` distance=0.024 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:27:58.503394Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:32:11.198781Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:36:22.598490Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

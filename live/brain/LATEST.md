# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T23:35:16.889434Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

Regime read: wind rising.

## Active patterns

- **PERSISTENT_DOWN** `thermal_base` value=1.351e+04 d1=0.0 d12=-514.0 z=-10.0487540720339
- **ROBUST_OUTLIER** `thermal_base` value=1.351e+04 d1=0.0 d12=-514.0 z=-10.0487540720339
- **PERSISTENT_DOWN** `ccgt_gen` value=9767 d1=0.0 d12=-514.0 z=-10.019635357946555
- **ROBUST_OUTLIER** `ccgt_gen` value=9767 d1=0.0 d12=-514.0 z=-10.019635357946555
- **ROBUST_OUTLIER** `ind_demand` value=-1.248e+04 d1=0.0 d12=-6.0 z=-4.72142825
- **CHANGE_POINT** `wind_gen` value=3178 d1=0.0 d12=451.0 z=2.035287593554443
- **PERSISTENT_UP** `wind_gen` value=3178 d1=0.0 d12=451.0 z=2.035287593554443
- **PERSISTENT_DOWN** `interconnector_net` value=4134 d1=0.0 d12=-1227.0 z=-1.8800461507434942
- **ACCELERATION** `interconnector_net` value=4134 d1=0.0 d12=-1227.0 z=-1.8800461507434942
- **ACCELERATION** `nuclear_gen` value=3739 d1=0.0 d12=0.0 z=1.2526238214285714
- **ACCELERATION** `biomass_gen` value=2915 d1=0.0 d12=0.0 z=0.5395918
- **PERSISTENT_DOWN** `residual_proxy` value=6903 d1=0.0 d12=-158.0 z=None
- **ACCELERATION** `residual_proxy` value=6903 d1=0.0 d12=-158.0 z=None
- **PERSISTENT_UP** `wind_forecast` value=1.377e+04 d1=0.0 d12=158.0 z=None
- **ACCELERATION** `wind_forecast` value=1.377e+04 d1=0.0 d12=158.0 z=None

## Nearest historical live analogues

- `2026-09-22T22:19:30.437012Z` distance=0.024 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:23:43.484966Z` distance=0.024 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:27:58.503394Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:32:11.198781Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:36:22.598490Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

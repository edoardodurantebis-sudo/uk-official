# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T23:31:03.889259Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

Regime read: wind rising.

## Active patterns

- **PERSISTENT_DOWN** `thermal_base` value=1.351e+04 d1=-115.0 d12=-514.0 z=-10.163596975714286
- **ROBUST_OUTLIER** `thermal_base` value=1.351e+04 d1=-115.0 d12=-514.0 z=-10.163596975714286
- **PERSISTENT_DOWN** `ccgt_gen` value=9767 d1=-119.0 d12=-514.0 z=-10.10490885035461
- **ROBUST_OUTLIER** `ccgt_gen` value=9767 d1=-119.0 d12=-514.0 z=-10.10490885035461
- **ROBUST_OUTLIER** `ind_demand` value=-1.248e+04 d1=0.0 d12=-6.0 z=-4.72142825
- **CHANGE_POINT** `wind_gen` value=3178 d1=11.0 d12=451.0 z=2.045173128094059
- **PERSISTENT_UP** `wind_gen` value=3178 d1=11.0 d12=451.0 z=2.045173128094059
- **PERSISTENT_DOWN** `interconnector_net` value=4134 d1=-535.0 d12=-1227.0 z=-1.9451219670513777
- **ACCELERATION** `interconnector_net` value=4134 d1=-535.0 d12=-1227.0 z=-1.9451219670513777
- **PERSISTENT_UP** `nuclear_gen` value=3739 d1=4.0 d12=0.0 z=1.1803570625
- **ACCELERATION** `nuclear_gen` value=3739 d1=4.0 d12=0.0 z=1.1803570625
- **ACCELERATION** `biomass_gen` value=2915 d1=-1.0 d12=0.0 z=0.5395918
- **PERSISTENT_DOWN** `residual_proxy` value=6903 d1=-158.0 d12=-158.0 z=None
- **ACCELERATION** `residual_proxy` value=6903 d1=-158.0 d12=-158.0 z=None
- **PERSISTENT_UP** `wind_forecast` value=1.377e+04 d1=158.0 d12=158.0 z=None

## Nearest historical live analogues

- `2026-09-22T22:19:30.437012Z` distance=0.024 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:23:43.484966Z` distance=0.024 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:27:58.503394Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:32:11.198781Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:36:22.598490Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

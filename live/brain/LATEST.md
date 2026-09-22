# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T23:39:29.907531Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

Regime read: wind rising.

## Active patterns

- **REVERSAL** `ccgt_gen` value=9795 d1=28.0 d12=-438.0 z=-9.896912449022347
- **ROBUST_OUTLIER** `ccgt_gen` value=9795 d1=28.0 d12=-438.0 z=-9.896912449022347
- **REVERSAL** `thermal_base` value=1.354e+04 d1=29.0 d12=-439.0 z=-9.8818400523743
- **ROBUST_OUTLIER** `thermal_base` value=1.354e+04 d1=29.0 d12=-439.0 z=-9.8818400523743
- **ROBUST_OUTLIER** `ind_demand` value=-1.248e+04 d1=0.0 d12=-6.0 z=-4.72142825
- **CHANGE_POINT** `wind_gen` value=3182 d1=4.0 d12=384.0 z=2.0293784217772215
- **PERSISTENT_UP** `wind_gen` value=3182 d1=4.0 d12=384.0 z=2.0293784217772215
- **REVERSAL** `interconnector_net` value=4172 d1=38.0 d12=-1162.0 z=-1.7705355937499998
- **REVERSAL** `nuclear_gen` value=3740 d1=1.0 d12=-1.0 z=1.1803570625
- **ACCELERATION** `nuclear_gen` value=3740 d1=1.0 d12=-1.0 z=1.1803570625
- **PERSISTENT_UP** `biomass_gen` value=2917 d1=2.0 d12=6.0 z=0.67448975
- **PERSISTENT_DOWN** `residual_proxy` value=6903 d1=0.0 d12=-158.0 z=None
- **PERSISTENT_UP** `wind_forecast` value=1.377e+04 d1=0.0 d12=158.0 z=None

## Nearest historical live analogues

- `2026-09-22T22:19:30.437012Z` distance=0.024 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:23:43.484966Z` distance=0.024 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:27:58.503394Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:32:11.198781Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:36:22.598490Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

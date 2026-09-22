# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T23:43:42.870536Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.357e+04 d1=35.0 d12=-333.0 z=-9.750124052777778
- **CHANGE_POINT** `ccgt_gen` value=9836 d1=41.0 d12=-323.0 z=-9.614712792465752
- **REVERSAL** `thermal_base` value=1.357e+04 d1=35.0 d12=-333.0 z=-9.750124052777778
- **ROBUST_OUTLIER** `thermal_base` value=1.357e+04 d1=35.0 d12=-333.0 z=-9.750124052777778
- **REVERSAL** `ccgt_gen` value=9836 d1=41.0 d12=-323.0 z=-9.614712792465752
- **ROBUST_OUTLIER** `ccgt_gen` value=9836 d1=41.0 d12=-323.0 z=-9.614712792465752
- **ROBUST_OUTLIER** `ind_demand` value=-1.248e+04 d1=0.0 d12=9.0 z=-4.72142825
- **CHANGE_POINT** `wind_gen` value=3205 d1=23.0 d12=328.0 z=2.0386642631414267
- **PERSISTENT_UP** `wind_gen` value=3205 d1=23.0 d12=328.0 z=2.0386642631414267
- **REVERSAL** `interconnector_net` value=4202 d1=30.0 d12=-1110.0 z=-1.6622908677419355
- **REVERSAL** `biomass_gen` value=2916 d1=-1.0 d12=5.0 z=0.607040775
- **ACCELERATION** `biomass_gen` value=2916 d1=-1.0 d12=5.0 z=0.607040775
- **PERSISTENT_DOWN** `nuclear_gen` value=3734 d1=-6.0 d12=-10.0 z=0.1686224375
- **ACCELERATION** `nuclear_gen` value=3734 d1=-6.0 d12=-10.0 z=0.1686224375

## Nearest historical live analogues

- `2026-09-22T22:19:30.437012Z` distance=0.024 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:23:43.484966Z` distance=0.024 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:27:58.503394Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:32:11.198781Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:36:22.598490Z` distance=0.024 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

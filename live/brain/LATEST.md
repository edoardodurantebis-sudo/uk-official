# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T01:04:02.744778Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.244e+04 d1=0.0 d12=50.0 z=28.3285695
- **ROBUST_OUTLIER** `ind_demand` value=-1.244e+04 d1=0.0 d12=50.0 z=28.3285695
- **CHANGE_POINT** `interconnector_net` value=2225 d1=-54.0 d12=-978.0 z=-2.500537437688594
- **CHANGE_POINT** `thermal_base` value=1.342e+04 d1=-6.0 d12=-341.0 z=-1.2459231149675971
- **CHANGE_POINT** `ccgt_gen` value=9682 d1=-14.0 d12=-342.0 z=-1.238711887682957
- **CHANGE_POINT** `margin` value=3.724e+04 d1=0.0 d12=16.0 z=0.8874865131578948
- **PERSISTENT_DOWN** `interconnector_net` value=2225 d1=-54.0 d12=-978.0 z=-2.500537437688594
- **PERSISTENT_UP** `wind_gen` value=4446 d1=54.0 d12=536.0 z=2.221069356792144
- **PERSISTENT_DOWN** `thermal_base` value=1.342e+04 d1=-6.0 d12=-341.0 z=-1.2459231149675971
- **PERSISTENT_DOWN** `ccgt_gen` value=9682 d1=-14.0 d12=-342.0 z=-1.238711887682957
- **PERSISTENT_UP** `nuclear_gen` value=3734 d1=8.0 d12=1.0 z=-0.1686224375
- **ACCELERATION** `nuclear_gen` value=3734 d1=8.0 d12=1.0 z=-0.1686224375
- **PERSISTENT_DOWN** `biomass_gen` value=2910 d1=-6.0 d12=-5.0 z=0.09635567857142857
- **ACCELERATION** `biomass_gen` value=2910 d1=-6.0 d12=-5.0 z=0.09635567857142857

## Nearest historical live analogues

- `2026-09-23T00:04:41.945935Z` distance=0.058 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:08:54.862562Z` distance=0.058 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:00:29.286244Z` distance=0.287 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:55:13.117327Z` distance=0.467 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:59:27.826421Z` distance=0.467 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

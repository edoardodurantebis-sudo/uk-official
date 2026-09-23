# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T04:06:07.388688Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.855e+04 d1=0.0 d12=-134.0 z=88.96519802499999
- **ROBUST_OUTLIER** `margin` value=3.855e+04 d1=0.0 d12=-134.0 z=88.96519802499999
- **CHANGE_POINT** `imbalance` value=-8081 d1=0.0 d12=-101.0 z=-3.110147180555556
- **CHANGE_POINT** `ind_generation` value=1.309e+04 d1=0.0 d12=-101.0 z=-3.110147180555556
- **CHANGE_POINT** `ind_demand` value=-1.24e+04 d1=0.0 d12=15.0 z=3.077359484375
- **PERSISTENT_DOWN** `biomass_gen` value=2865 d1=-2.0 d12=-16.0 z=-4.239649857142857
- **ROBUST_OUTLIER** `biomass_gen` value=2865 d1=-2.0 d12=-16.0 z=-4.239649857142857
- **CHANGE_POINT** `wind_gen` value=7639 d1=266.0 d12=1799.0 z=2.0560183532171585
- **CHANGE_POINT** `ps_gen` value=144 d1=0.0 d12=155.0 z=-1.1241495833333335
- **ROBUST_OUTLIER** `imbalance` value=-8081 d1=0.0 d12=-101.0 z=-3.110147180555556
- **ROBUST_OUTLIER** `ind_generation` value=1.309e+04 d1=0.0 d12=-101.0 z=-3.110147180555556
- **ROBUST_OUTLIER** `ind_demand` value=-1.24e+04 d1=0.0 d12=15.0 z=3.077359484375
- **PERSISTENT_UP** `wind_gen` value=7639 d1=266.0 d12=1799.0 z=2.0560183532171585
- **PERSISTENT_DOWN** `interconnector_net` value=-4473 d1=-609.0 d12=-2229.0 z=-1.8634021243862522
- **PERSISTENT_DOWN** `thermal_base` value=1.253e+04 d1=-99.0 d12=-563.0 z=-1.7356750766182298

## Nearest historical live analogues

- `2026-09-21T07:19:16.764355Z` distance=0.389 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:53:56.422040Z` distance=0.414 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.414 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.414 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:06:37.268181Z` distance=0.414 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

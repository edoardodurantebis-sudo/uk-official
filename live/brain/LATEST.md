# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T03:53:29.874059Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.855e+04 d1=-23.0 d12=-134.0 z=88.96519802499999
- **PERSISTENT_DOWN** `margin` value=3.855e+04 d1=-23.0 d12=-134.0 z=88.96519802499999
- **ROBUST_OUTLIER** `margin` value=3.855e+04 d1=-23.0 d12=-134.0 z=88.96519802499999
- **CHANGE_POINT** `ind_demand` value=-1.24e+04 d1=11.0 d12=15.0 z=3.077359484375
- **CHANGE_POINT** `interconnector_net` value=-3713 d1=30.0 d12=-2877.0 z=-2.978870732353881
- **PERSISTENT_DOWN** `biomass_gen` value=2869 d1=-7.0 d12=-5.0 z=-4.202589980769231
- **ROBUST_OUTLIER** `biomass_gen` value=2869 d1=-7.0 d12=-5.0 z=-4.202589980769231
- **CHANGE_POINT** `wind_gen` value=7174 d1=208.0 d12=1646.0 z=1.7321032299079113
- **PERSISTENT_DOWN** `imbalance` value=-8081 d1=-89.0 d12=-101.0 z=-3.110147180555556
- **ACCELERATION** `imbalance` value=-8081 d1=-89.0 d12=-101.0 z=-3.110147180555556
- **ROBUST_OUTLIER** `imbalance` value=-8081 d1=-89.0 d12=-101.0 z=-3.110147180555556
- **PERSISTENT_DOWN** `ind_generation` value=1.309e+04 d1=-89.0 d12=-101.0 z=-3.110147180555556
- **ACCELERATION** `ind_generation` value=1.309e+04 d1=-89.0 d12=-101.0 z=-3.110147180555556
- **ROBUST_OUTLIER** `ind_generation` value=1.309e+04 d1=-89.0 d12=-101.0 z=-3.110147180555556
- **PERSISTENT_UP** `ind_demand` value=-1.24e+04 d1=11.0 d12=15.0 z=3.077359484375

## Nearest historical live analogues

- `2026-09-21T07:19:16.764355Z` distance=0.391 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:53:56.422040Z` distance=0.418 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.418 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.418 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:06:37.268181Z` distance=0.418 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T02:33:26.071895Z`  
Memory snapshots: **2368**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.782e+04 d1=0.0 d12=1654.0 z=22.312120930000003
- **ROBUST_OUTLIER** `margin` value=3.782e+04 d1=0.0 d12=1654.0 z=22.312120930000003
- **CHANGE_POINT** `wind_gen` value=4114 d1=15.0 d12=513.0 z=4.471049479166666
- **PERSISTENT_UP** `wind_gen` value=4114 d1=15.0 d12=513.0 z=4.471049479166666
- **ROBUST_OUTLIER** `wind_gen` value=4114 d1=15.0 d12=513.0 z=4.471049479166666
- **CHANGE_POINT** `ind_demand` value=-1.25e+04 d1=0.0 d12=-93.0 z=-2.0944681710526316
- **CHANGE_POINT** `ps_gen` value=-164 d1=0.0 d12=121.0 z=-0.35945860928143714
- **CHANGE_POINT** `imbalance` value=-2655 d1=0.0 d12=44.0 z=-0.3165972295918367
- **CHANGE_POINT** `ind_generation` value=1.88e+04 d1=0.0 d12=44.0 z=-0.3165972295918367
- **PERSISTENT_DOWN** `interconnector_net` value=2626 d1=-1157.0 d12=-2410.0 z=-1.1982879124597208
- **ACCELERATION** `interconnector_net` value=2626 d1=-1157.0 d12=-2410.0 z=-1.1982879124597208
- **PERSISTENT_UP** `nuclear_gen` value=3660 d1=1.0 d12=7.0 z=1.1506001617647057
- **ACCELERATION** `nuclear_gen` value=3660 d1=1.0 d12=7.0 z=1.1506001617647057
- **PERSISTENT_DOWN** `biomass_gen` value=3041 d1=-4.0 d12=-6.0 z=1.0698802931034483
- **ACCELERATION** `biomass_gen` value=3041 d1=-4.0 d12=-6.0 z=1.0698802931034483

## Nearest historical live analogues

- `2026-09-21T06:53:56.422040Z` distance=0.335 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.335 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.335 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:06:37.268181Z` distance=0.335 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:10:52.783726Z` distance=0.335 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T04:04:21.572514Z`  
Memory snapshots: **2050**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.755e+04 d1=0.0 d12=-9.0 z=33.53177614285714
- **ROBUST_OUTLIER** `margin` value=3.755e+04 d1=0.0 d12=-9.0 z=33.53177614285714
- **CHANGE_POINT** `imbalance` value=-4043 d1=0.0 d12=822.0 z=6.6299276562500005
- **CHANGE_POINT** `ind_generation` value=1.657e+04 d1=0.0 d12=822.0 z=6.6299276562500005
- **ROBUST_OUTLIER** `imbalance` value=-4043 d1=0.0 d12=822.0 z=6.6299276562500005
- **ROBUST_OUTLIER** `ind_generation` value=1.657e+04 d1=0.0 d12=822.0 z=6.6299276562500005
- **ROBUST_OUTLIER** `ind_demand` value=-1.176e+04 d1=0.0 d12=42.0 z=3.8221085833333333
- **CHANGE_POINT** `interconnector_net` value=9320 d1=-732.0 d12=-1980.0 z=-1.1101573395803865
- **CHANGE_POINT** `nuclear_gen` value=3335 d1=5.0 d12=-6.0 z=-0.4496598333333333
- **PERSISTENT_UP** `thermal_base` value=9822 d1=296.0 d12=1059.0 z=2.2731422513812154
- **PERSISTENT_UP** `ccgt_gen` value=6487 d1=291.0 d12=1065.0 z=2.2458420091074682
- **CHANGE_POINT** `ps_gen` value=-134 d1=-122.0 d12=-112.0 z=None
- **PERSISTENT_DOWN** `interconnector_net` value=9320 d1=-732.0 d12=-1980.0 z=-1.1101573395803865
- **ACCELERATION** `interconnector_net` value=9320 d1=-732.0 d12=-1980.0 z=-1.1101573395803865
- **PERSISTENT_UP** `wind_gen` value=3869 d1=19.0 d12=91.0 z=-0.7103905233160622

## Nearest historical live analogues

- `2026-09-21T02:22:39.819793Z` distance=0.587 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:26:51.602433Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:31:01.988533Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:35:13.346437Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:40:00.109498Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

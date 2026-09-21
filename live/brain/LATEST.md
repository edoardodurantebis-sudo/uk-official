# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T04:12:44.976997Z`  
Memory snapshots: **2052**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.755e+04 d1=0.0 d12=-17.0 z=33.53177614285714
- **ROBUST_OUTLIER** `margin` value=3.755e+04 d1=0.0 d12=-17.0 z=33.53177614285714
- **CHANGE_POINT** `imbalance` value=-4043 d1=0.0 d12=777.0 z=6.6299276562500005
- **CHANGE_POINT** `ind_generation` value=1.657e+04 d1=0.0 d12=777.0 z=6.6299276562500005
- **ROBUST_OUTLIER** `imbalance` value=-4043 d1=0.0 d12=777.0 z=6.6299276562500005
- **ROBUST_OUTLIER** `ind_generation` value=1.657e+04 d1=0.0 d12=777.0 z=6.6299276562500005
- **CHANGE_POINT** `thermal_base` value=1.033e+04 d1=304.0 d12=1378.0 z=3.52771802946593
- **CHANGE_POINT** `ccgt_gen` value=6995 d1=309.0 d12=1381.0 z=3.494078049180328
- **CHANGE_POINT** `interconnector_net` value=7217 d1=-573.0 d12=-4044.0 z=-2.3051573112199466
- **ROBUST_OUTLIER** `ind_demand` value=-1.176e+04 d1=0.0 d12=38.0 z=3.8221085833333333
- **PERSISTENT_UP** `thermal_base` value=1.033e+04 d1=304.0 d12=1378.0 z=3.52771802946593
- **ROBUST_OUTLIER** `thermal_base` value=1.033e+04 d1=304.0 d12=1378.0 z=3.52771802946593
- **PERSISTENT_UP** `ccgt_gen` value=6995 d1=309.0 d12=1381.0 z=3.494078049180328
- **ROBUST_OUTLIER** `ccgt_gen` value=6995 d1=309.0 d12=1381.0 z=3.494078049180328
- **PERSISTENT_DOWN** `interconnector_net` value=7217 d1=-573.0 d12=-4044.0 z=-2.3051573112199466

## Nearest historical live analogues

- `2026-09-21T02:22:39.819793Z` distance=0.587 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:26:51.602433Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:31:01.988533Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:35:13.346437Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:40:00.109498Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

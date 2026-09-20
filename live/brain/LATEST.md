# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T03:17:14.106655Z`  
Memory snapshots: **1698**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.761e+04 d1=0.0 d12=1.0 z=29.77390467857143
- **ROBUST_OUTLIER** `margin` value=3.761e+04 d1=0.0 d12=1.0 z=29.77390467857143
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=0.0 d12=-81.0 z=-18.118190181034485
- **REVERSAL** `biomass_gen` value=1223 d1=1.0 d12=-7.0 z=5.140927972560975
- **ACCELERATION** `biomass_gen` value=1223 d1=1.0 d12=-7.0 z=5.140927972560975
- **ROBUST_OUTLIER** `biomass_gen` value=1223 d1=1.0 d12=-7.0 z=5.140927972560975
- **CHANGE_POINT** `thermal_base` value=6945 d1=-16.0 d12=-666.0 z=-0.5929580219780219
- **CHANGE_POINT** `ccgt_gen` value=3616 d1=-17.0 d12=-663.0 z=-0.5862109444852941
- **CHANGE_POINT** `imbalance` value=-3749 d1=0.0 d12=6.0 z=0.48177839285714286
- **CHANGE_POINT** `ind_generation` value=1.62e+04 d1=0.0 d12=6.0 z=0.48177839285714286
- **PERSISTENT_DOWN** `interconnector_net` value=-1.152e+04 d1=-31.0 d12=-977.0 z=-1.4827450432843652
- **REVERSAL** `nuclear_gen` value=3329 d1=1.0 d12=-3.0 z=-1.1241495833333335
- **ACCELERATION** `nuclear_gen` value=3329 d1=1.0 d12=-3.0 z=-1.1241495833333335
- **PERSISTENT_UP** `ps_gen` value=-692 d1=1.0 d12=11.0 z=-0.9155236246246247
- **PERSISTENT_DOWN** `thermal_base` value=6945 d1=-16.0 d12=-666.0 z=-0.5929580219780219

## Nearest historical live analogues

- `2026-09-20T02:20:49.967105Z` distance=0.091 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:48:55.634175Z` distance=0.381 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.381 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.381 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.381 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

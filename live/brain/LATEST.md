# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T02:55:09.059110Z`  
Memory snapshots: **1693**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.761e+04 d1=0.0 d12=1589.0 z=29.77390467857143
- **PERSISTENT_UP** `margin` value=3.761e+04 d1=0.0 d12=1589.0 z=29.77390467857143
- **ROBUST_OUTLIER** `margin` value=3.761e+04 d1=0.0 d12=1589.0 z=29.77390467857143
- **CHANGE_POINT** `ind_demand` value=-1.228e+04 d1=-81.0 d12=-81.0 z=-18.78935732142857
- **PERSISTENT_DOWN** `ind_demand` value=-1.228e+04 d1=-81.0 d12=-81.0 z=-18.78935732142857
- **ACCELERATION** `ind_demand` value=-1.228e+04 d1=-81.0 d12=-81.0 z=-18.78935732142857
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=-81.0 d12=-81.0 z=-18.78935732142857
- **PERSISTENT_DOWN** `biomass_gen` value=1168 d1=0.0 d12=-55.0 z=5.263063958333333
- **ROBUST_OUTLIER** `biomass_gen` value=1168 d1=0.0 d12=-55.0 z=5.263063958333333
- **CHANGE_POINT** `interconnector_net` value=-1.105e+04 d1=0.0 d12=-910.0 z=-1.2664526456679894
- **CHANGE_POINT** `thermal_base` value=7184 d1=0.0 d12=-363.0 z=-0.3100271297288777
- **CHANGE_POINT** `ccgt_gen` value=3855 d1=0.0 d12=-362.0 z=-0.3076694569400631
- **PERSISTENT_DOWN** `nuclear_gen` value=3329 d1=0.0 d12=-1.0 z=-1.1241495833333335
- **ACCELERATION** `nuclear_gen` value=3329 d1=0.0 d12=-1.0 z=-1.1241495833333335
- **PERSISTENT_UP** `imbalance` value=-3749 d1=6.0 d12=8.0 z=0.6560105787671233

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.375 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.375 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.375 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.375 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.375 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

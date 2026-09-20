# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T15:57:48.628664Z`  
Memory snapshots: **1878**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1537 d1=125.0 d12=667.0 z=320.38263125
- **PERSISTENT_UP** `biomass_gen` value=1537 d1=125.0 d12=667.0 z=320.38263125
- **ROBUST_OUTLIER** `biomass_gen` value=1537 d1=125.0 d12=667.0 z=320.38263125
- **CHANGE_POINT** `ccgt_gen` value=3947 d1=113.0 d12=1239.0 z=59.586351628571435
- **PERSISTENT_UP** `ccgt_gen` value=3947 d1=113.0 d12=1239.0 z=59.586351628571435
- **ROBUST_OUTLIER** `ccgt_gen` value=3947 d1=113.0 d12=1239.0 z=59.586351628571435
- **CHANGE_POINT** `thermal_base` value=7284 d1=110.0 d12=1243.0 z=53.578698602564096
- **PERSISTENT_UP** `thermal_base` value=7284 d1=110.0 d12=1243.0 z=53.578698602564096
- **ROBUST_OUTLIER** `thermal_base` value=7284 d1=110.0 d12=1243.0 z=53.578698602564096
- **CHANGE_POINT** `imbalance` value=-5166 d1=-6.0 d12=-8.0 z=14.371820057692307
- **PERSISTENT_DOWN** `imbalance` value=-5166 d1=-6.0 d12=-8.0 z=14.371820057692307
- **ACCELERATION** `imbalance` value=-5166 d1=-6.0 d12=-8.0 z=14.371820057692307
- **ROBUST_OUTLIER** `imbalance` value=-5166 d1=-6.0 d12=-8.0 z=14.371820057692307
- **CHANGE_POINT** `interconnector_net` value=7946 d1=0.0 d12=3709.0 z=6.279566353663367
- **PERSISTENT_UP** `interconnector_net` value=7946 d1=0.0 d12=3709.0 z=6.279566353663367

## Nearest historical live analogues

- `2026-09-20T14:54:10.136499Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:58:25.329493Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:02:37.176302Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T10:57:55.935414Z` distance=0.060 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:02:06.579348Z` distance=0.060 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

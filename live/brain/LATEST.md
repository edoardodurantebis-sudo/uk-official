# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T04:01:33.750127Z`  
Memory snapshots: **1367**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.831e+04 d1=0.0 d12=1.0 z=7.507364173913043
- **CHANGE_POINT** `imbalance` value=9802 d1=0.0 d12=406.0 z=6.520067583333334
- **CHANGE_POINT** `ind_generation` value=2.7e+04 d1=0.0 d12=405.0 z=6.509361396825397
- **PERSISTENT_UP** `margin` value=3.831e+04 d1=0.0 d12=1.0 z=7.507364173913043
- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=1.0 z=7.507364173913043
- **PERSISTENT_UP** `imbalance` value=9802 d1=0.0 d12=406.0 z=6.520067583333334
- **ROBUST_OUTLIER** `imbalance` value=9802 d1=0.0 d12=406.0 z=6.520067583333334
- **PERSISTENT_UP** `ind_generation` value=2.7e+04 d1=0.0 d12=405.0 z=6.509361396825397
- **ROBUST_OUTLIER** `ind_generation` value=2.7e+04 d1=0.0 d12=405.0 z=6.509361396825397
- **ROBUST_OUTLIER** `biomass_gen` value=694 d1=0.0 d12=-119.0 z=-4.459685958955224
- **CHANGE_POINT** `thermal_base` value=6396 d1=1.0 d12=1.0 z=-2.0165157474226802
- **CHANGE_POINT** `ccgt_gen` value=3059 d1=1.0 d12=2.0 z=-1.9957978756410255
- **CHANGE_POINT** `wind_gen` value=1.577e+04 d1=56.0 d12=-375.0 z=-0.9862704631675875
- **PERSISTENT_UP** `ind_demand` value=-1.088e+04 d1=0.0 d12=3.0 z=2.697959
- **CHANGE_POINT** `interconnector_net` value=-1.106e+04 d1=49.0 d12=95.0 z=-0.6658303783840357

## Nearest historical live analogues

- `2026-09-19T02:54:16.089654Z` distance=0.313 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:58:27.254129Z` distance=0.313 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:02:39.982753Z` distance=0.313 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:06:52.906018Z` distance=0.313 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 748.0}
- `2026-09-19T02:20:35.608449Z` distance=0.313 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

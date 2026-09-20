# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T06:44:41.055483Z`  
Memory snapshots: **1747**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `imbalance` value=-6854 d1=0.0 d12=-80.0 z=-48.07700194767442
- **CHANGE_POINT** `ind_generation` value=1.31e+04 d1=0.0 d12=-80.0 z=-48.07700194767442
- **ROBUST_OUTLIER** `imbalance` value=-6854 d1=0.0 d12=-80.0 z=-48.07700194767442
- **ROBUST_OUTLIER** `ind_generation` value=1.31e+04 d1=0.0 d12=-80.0 z=-48.07700194767442
- **CHANGE_POINT** `biomass_gen` value=887 d1=-1.0 d12=-126.0 z=-7.7750273000000005
- **PERSISTENT_DOWN** `biomass_gen` value=887 d1=-1.0 d12=-126.0 z=-7.7750273000000005
- **ROBUST_OUTLIER** `biomass_gen` value=887 d1=-1.0 d12=-126.0 z=-7.7750273000000005
- **CHANGE_POINT** `wind_gen` value=1.584e+04 d1=-70.0 d12=164.0 z=1.5996207061933534
- **CHANGE_POINT** `interconnector_net` value=-9362 d1=0.0 d12=1886.0 z=1.0888652710526316
- **CHANGE_POINT** `ps_gen` value=-805 d1=-1.0 d12=13.0 z=-0.9355825564516129
- **CHANGE_POINT** `ind_demand` value=-1.231e+04 d1=0.0 d12=3.0 z=-0.766788347368421
- **CHANGE_POINT** `margin` value=3.748e+04 d1=0.0 d12=11.0 z=-0.3539875283687943
- **PERSISTENT_DOWN** `nuclear_gen` value=3327 d1=-5.0 d12=-9.0 z=-2.0234692499999998
- **ACCELERATION** `nuclear_gen` value=3327 d1=-5.0 d12=-9.0 z=-2.0234692499999998
- **REVERSAL** `wind_gen` value=1.584e+04 d1=-70.0 d12=164.0 z=1.5996207061933534

## Nearest historical live analogues

- `2026-09-20T05:49:39.839259Z` distance=0.015 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:32:50.061317Z` distance=0.022 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': -55.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:37:06.199540Z` distance=0.022 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': -55.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:41:17.937410Z` distance=0.022 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': -55.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:45:29.054412Z` distance=0.022 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': -55.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

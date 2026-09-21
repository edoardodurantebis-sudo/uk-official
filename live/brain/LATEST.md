# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T16:17:36.082823Z`  
Memory snapshots: **2223**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.606e+04 d1=103.0 d12=2409.0 z=6.6518644310344825
- **CHANGE_POINT** `ccgt_gen` value=1.255e+04 d1=100.0 d12=2394.0 z=6.48286121659292
- **PERSISTENT_UP** `thermal_base` value=1.606e+04 d1=103.0 d12=2409.0 z=6.6518644310344825
- **ROBUST_OUTLIER** `thermal_base` value=1.606e+04 d1=103.0 d12=2409.0 z=6.6518644310344825
- **PERSISTENT_UP** `ccgt_gen` value=1.255e+04 d1=100.0 d12=2394.0 z=6.48286121659292
- **ROBUST_OUTLIER** `ccgt_gen` value=1.255e+04 d1=100.0 d12=2394.0 z=6.48286121659292
- **CHANGE_POINT** `interconnector_net` value=1.02e+04 d1=-2.0 d12=-961.0 z=-3.4367643985330076
- **PERSISTENT_DOWN** `interconnector_net` value=1.02e+04 d1=-2.0 d12=-961.0 z=-3.4367643985330076
- **ROBUST_OUTLIER** `interconnector_net` value=1.02e+04 d1=-2.0 d12=-961.0 z=-3.4367643985330076
- **CHANGE_POINT** `wind_gen` value=3189 d1=-8.0 d12=-149.0 z=-1.1877468904382469
- **CHANGE_POINT** `margin` value=3.621e+04 d1=0.0 d12=-51.0 z=-0.8651064184782609
- **CHANGE_POINT** `imbalance` value=-3079 d1=0.0 d12=28.0 z=0.67448975
- **CHANGE_POINT** `nuclear_gen` value=3509 d1=3.0 d12=15.0 z=0.5058673124999999
- **CHANGE_POINT** `ind_generation` value=1.838e+04 d1=0.0 d12=28.0 z=0.4354973188976378
- **PERSISTENT_DOWN** `wind_gen` value=3189 d1=-8.0 d12=-149.0 z=-1.1877468904382469

## Nearest historical live analogues

- `2026-09-21T14:23:01.446169Z` distance=0.033 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:27:16.085310Z` distance=0.033 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:31:28.406523Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:35:41.380076Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:39:54.228512Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

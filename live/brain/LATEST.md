# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T00:37:54.376339Z`  
Memory snapshots: **690**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6554 d1=17.0 d12=-109.0 z=-5.016338565191025
- **CHANGE_POINT** `ccgt_gen` value=4627 d1=-21.0 d12=-729.0 z=-3.477934019121004
- **CHANGE_POINT** `thermal_base` value=7943 d1=-15.0 d12=-727.0 z=-3.4615612910022775
- **REVERSAL** `interconnector_net` value=-6554 d1=17.0 d12=-109.0 z=-5.016338565191025
- **ROBUST_OUTLIER** `interconnector_net` value=-6554 d1=17.0 d12=-109.0 z=-5.016338565191025
- **CHANGE_POINT** `margin` value=3.451e+04 d1=0.0 d12=23.0 z=1.6287678407407407
- **ROBUST_OUTLIER** `ccgt_gen` value=4627 d1=-21.0 d12=-729.0 z=-3.477934019121004
- **ROBUST_OUTLIER** `thermal_base` value=7943 d1=-15.0 d12=-727.0 z=-3.4615612910022775
- **CHANGE_POINT** `ps_gen` value=-251 d1=-1.0 d12=-1.0 z=-0.7715386348920863
- **CHANGE_POINT** `ind_generation` value=2.562e+04 d1=0.0 d12=-107.0 z=0.27836084920634924
- **PERSISTENT_UP** `wind_gen` value=1.237e+04 d1=394.0 d12=832.0 z=1.5134657339560753
- **ACCELERATION** `wind_gen` value=1.237e+04 d1=394.0 d12=832.0 z=1.5134657339560753
- **PERSISTENT_UP** `nuclear_gen` value=3316 d1=6.0 d12=2.0 z=1.3489795

## Nearest historical live analogues

- `2026-09-16T23:33:53.959539Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:38:04.318669Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:42:15.181563Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:21:30.462993Z` distance=0.247 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.249 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

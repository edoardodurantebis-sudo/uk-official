# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T00:33:42.368612Z`  
Memory snapshots: **689**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6571 d1=-2.0 d12=-135.0 z=-5.028200422528805
- **CHANGE_POINT** `ccgt_gen` value=4648 d1=25.0 d12=-747.0 z=-3.4617647442922377
- **CHANGE_POINT** `thermal_base` value=7958 d1=21.0 d12=-752.0 z=-3.450038117596811
- **ROBUST_OUTLIER** `interconnector_net` value=-6571 d1=-2.0 d12=-135.0 z=-5.028200422528805
- **REVERSAL** `ccgt_gen` value=4648 d1=25.0 d12=-747.0 z=-3.4617647442922377
- **ROBUST_OUTLIER** `ccgt_gen` value=4648 d1=25.0 d12=-747.0 z=-3.4617647442922377
- **REVERSAL** `thermal_base` value=7958 d1=21.0 d12=-752.0 z=-3.450038117596811
- **ROBUST_OUTLIER** `thermal_base` value=7958 d1=21.0 d12=-752.0 z=-3.450038117596811
- **CHANGE_POINT** `ps_gen` value=-250 d1=-3.0 d12=-3.0 z=-0.8181489804202483
- **CHANGE_POINT** `imbalance` value=6558 d1=0.0 d12=-45.0 z=0.4634761969273743
- **CHANGE_POINT** `ind_generation` value=2.562e+04 d1=0.0 d12=-107.0 z=0.27836084920634924
- **PERSISTENT_UP** `wind_gen` value=1.197e+04 d1=64.0 d12=485.0 z=1.354862781443444
- **PERSISTENT_DOWN** `ps_gen` value=-250 d1=-3.0 d12=-3.0 z=-0.8181489804202483

## Nearest historical live analogues

- `2026-09-16T23:33:53.959539Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:38:04.318669Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:21:30.462993Z` distance=0.247 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.249 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:29:54.321922Z` distance=0.249 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

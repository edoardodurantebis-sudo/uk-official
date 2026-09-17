# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T00:29:31.305684Z`  
Memory snapshots: **688**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6569 d1=19.0 d12=-132.0 z=-5.072784644936325
- **CHANGE_POINT** `ccgt_gen` value=4623 d1=94.0 d12=-765.0 z=-3.481013880993151
- **CHANGE_POINT** `thermal_base` value=7937 d1=93.0 d12=-767.0 z=-3.4661705603644646
- **REVERSAL** `interconnector_net` value=-6569 d1=19.0 d12=-132.0 z=-5.072784644936325
- **ROBUST_OUTLIER** `interconnector_net` value=-6569 d1=19.0 d12=-132.0 z=-5.072784644936325
- **REVERSAL** `ccgt_gen` value=4623 d1=94.0 d12=-765.0 z=-3.481013880993151
- **ROBUST_OUTLIER** `ccgt_gen` value=4623 d1=94.0 d12=-765.0 z=-3.481013880993151
- **REVERSAL** `thermal_base` value=7937 d1=93.0 d12=-767.0 z=-3.4661705603644646
- **ROBUST_OUTLIER** `thermal_base` value=7937 d1=93.0 d12=-767.0 z=-3.4661705603644646
- **CHANGE_POINT** `ps_gen` value=-247 d1=-1.0 d12=2.0 z=-0.8166236053639846
- **CHANGE_POINT** `imbalance` value=6558 d1=0.0 d12=-45.0 z=0.4634761969273743
- **CHANGE_POINT** `ind_generation` value=2.562e+04 d1=0.0 d12=-107.0 z=0.27836084920634924
- **PERSISTENT_UP** `wind_gen` value=1.191e+04 d1=96.0 d12=504.0 z=1.3186088289364641

## Nearest historical live analogues

- `2026-09-16T23:33:53.959539Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:21:30.462993Z` distance=0.247 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.249 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:29:54.321922Z` distance=0.249 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:34:06.314775Z` distance=0.249 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

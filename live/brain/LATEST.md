# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T04:04:06.794649Z`  
Memory snapshots: **739**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.15e+04 d1=0.0 d12=11.0 z=34.8036711
- **CHANGE_POINT** `ind_generation` value=2.639e+04 d1=0.0 d12=760.0 z=25.5294370375
- **ROBUST_OUTLIER** `ind_generation` value=2.639e+04 d1=0.0 d12=760.0 z=25.5294370375
- **CHANGE_POINT** `biomass_gen` value=2910 d1=146.0 d12=876.0 z=-23.28973430882353
- **PERSISTENT_UP** `biomass_gen` value=2910 d1=146.0 d12=876.0 z=-23.28973430882353
- **ROBUST_OUTLIER** `biomass_gen` value=2910 d1=146.0 d12=876.0 z=-23.28973430882353
- **CHANGE_POINT** `imbalance` value=7273 d1=0.0 d12=760.0 z=16.231269467741935
- **CHANGE_POINT** `interconnector_net` value=-9961 d1=-203.0 d12=-1691.0 z=-14.247298873076923
- **ROBUST_OUTLIER** `imbalance` value=7273 d1=0.0 d12=760.0 z=16.231269467741935
- **PERSISTENT_DOWN** `interconnector_net` value=-9961 d1=-203.0 d12=-1691.0 z=-14.247298873076923
- **ROBUST_OUTLIER** `interconnector_net` value=-9961 d1=-203.0 d12=-1691.0 z=-14.247298873076923
- **CHANGE_POINT** `margin` value=3.584e+04 d1=0.0 d12=-19.0 z=9.095392083333333
- **ROBUST_OUTLIER** `margin` value=3.584e+04 d1=0.0 d12=-19.0 z=9.095392083333333
- **CHANGE_POINT** `nuclear_gen` value=3320 d1=4.0 d12=12.0 z=2.1583672
- **CHANGE_POINT** `wind_gen` value=1.37e+04 d1=-32.0 d12=384.0 z=0.8417424455964088

## Nearest historical live analogues

- `2026-09-17T02:52:02.690108Z` distance=0.591 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:56:14.879410Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T03:00:26.007200Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T03:04:39.344891Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T03:08:48.749095Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 1126.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

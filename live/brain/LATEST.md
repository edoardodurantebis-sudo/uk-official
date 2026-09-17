# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T03:59:54.984364Z`  
Memory snapshots: **738**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2764 d1=0.0 d12=730.0 z=-34.8750876617647
- **PERSISTENT_UP** `biomass_gen` value=2764 d1=0.0 d12=730.0 z=-34.8750876617647
- **ROBUST_OUTLIER** `biomass_gen` value=2764 d1=0.0 d12=730.0 z=-34.8750876617647
- **PERSISTENT_UP** `ind_demand` value=-1.15e+04 d1=0.0 d12=11.0 z=34.8036711
- **ROBUST_OUTLIER** `ind_demand` value=-1.15e+04 d1=0.0 d12=11.0 z=34.8036711
- **CHANGE_POINT** `ind_generation` value=2.639e+04 d1=0.0 d12=760.0 z=25.5294370375
- **PERSISTENT_UP** `ind_generation` value=2.639e+04 d1=0.0 d12=760.0 z=25.5294370375
- **ROBUST_OUTLIER** `ind_generation` value=2.639e+04 d1=0.0 d12=760.0 z=25.5294370375
- **CHANGE_POINT** `imbalance` value=7273 d1=0.0 d12=760.0 z=16.231269467741935
- **PERSISTENT_UP** `imbalance` value=7273 d1=0.0 d12=760.0 z=16.231269467741935
- **ROBUST_OUTLIER** `imbalance` value=7273 d1=0.0 d12=760.0 z=16.231269467741935
- **CHANGE_POINT** `interconnector_net` value=-9758 d1=0.0 d12=-1931.0 z=-12.495404397142858
- **ROBUST_OUTLIER** `interconnector_net` value=-9758 d1=0.0 d12=-1931.0 z=-12.495404397142858
- **CHANGE_POINT** `margin` value=3.584e+04 d1=0.0 d12=-19.0 z=9.095392083333333
- **PERSISTENT_DOWN** `margin` value=3.584e+04 d1=0.0 d12=-19.0 z=9.095392083333333

## Nearest historical live analogues

- `2026-09-17T02:52:02.690108Z` distance=0.591 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:56:14.879410Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T03:00:26.007200Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T03:04:39.344891Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:22:41.615797Z` distance=0.592 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T00:12:06.744150Z`  
Memory snapshots: **684**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=-657.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=657.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6541 d1=-34.0 d12=-785.0 z=-5.142933215054578
- **PERSISTENT_DOWN** `interconnector_net` value=-6541 d1=-34.0 d12=-785.0 z=-5.142933215054578
- **ROBUST_OUTLIER** `interconnector_net` value=-6541 d1=-34.0 d12=-785.0 z=-5.142933215054578
- **PERSISTENT_DOWN** `ccgt_gen` value=4574 d1=-70.0 d12=-1182.0 z=-3.5187421889269404
- **ROBUST_OUTLIER** `ccgt_gen` value=4574 d1=-70.0 d12=-1182.0 z=-3.5187421889269404
- **PERSISTENT_DOWN** `thermal_base` value=7886 d1=-74.0 d12=-1183.0 z=-3.505349349943052
- **ROBUST_OUTLIER** `thermal_base` value=7886 d1=-74.0 d12=-1183.0 z=-3.505349349943052
- **CHANGE_POINT** `imbalance` value=6451 d1=0.0 d12=-152.0 z=-0.607040775
- **CHANGE_POINT** `ind_generation` value=2.557e+04 d1=0.0 d12=-152.0 z=-0.16429878525641026
- **REVERSAL** `wind_gen` value=1.173e+04 d1=-6.0 d12=737.0 z=1.2094743355624553
- **PERSISTENT_UP** `ps_gen` value=-246 d1=1.0 d12=3.0 z=-0.8168964150671785
- **PERSISTENT_DOWN** `nuclear_gen` value=3312 d1=-4.0 d12=-1.0 z=0.7494330555555556
- **ACCELERATION** `nuclear_gen` value=3312 d1=-4.0 d12=-1.0 z=0.7494330555555556

## Nearest historical live analogues

- `2026-09-16T14:21:30.462993Z` distance=0.331 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.332 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:29:54.321922Z` distance=0.332 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:34:06.314775Z` distance=0.332 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:38:16.233128Z` distance=0.332 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

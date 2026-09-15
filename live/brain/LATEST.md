# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T17:25:00.411600Z`  
Memory snapshots: **283**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3006 d1=0.0 d12=900.0 z=39.273698625
- **PERSISTENT_UP** `biomass_gen` value=3006 d1=0.0 d12=900.0 z=39.273698625
- **ROBUST_OUTLIER** `biomass_gen` value=3006 d1=0.0 d12=900.0 z=39.273698625
- **ROBUST_OUTLIER** `ccgt_gen` value=1.039e+04 d1=0.0 d12=790.0 z=21.97670174154135
- **ROBUST_OUTLIER** `thermal_base` value=1.371e+04 d1=0.0 d12=787.0 z=21.90509863508443
- **ROBUST_OUTLIER** `interconnector_net` value=-749 d1=0.0 d12=-1426.0 z=-6.1297718939647945
- **ROBUST_OUTLIER** `ps_gen` value=501 d1=0.0 d12=376.0 z=3.063079869529984
- **PERSISTENT_DOWN** `nuclear_gen` value=3319 d1=0.0 d12=-3.0 z=-2.02346925
- **ACCELERATION** `nuclear_gen` value=3319 d1=0.0 d12=-3.0 z=-2.02346925
- **PERSISTENT_DOWN** `margin` value=3.482e+04 d1=0.0 d12=-94.0 z=-1.1917150505181346
- **PERSISTENT_DOWN** `imbalance` value=5772 d1=-63.0 d12=-55.0 z=0.6969727416666667
- **ACCELERATION** `imbalance` value=5772 d1=-63.0 d12=-55.0 z=0.6969727416666667
- **PERSISTENT_DOWN** `ind_generation` value=2.489e+04 d1=-63.0 d12=-55.0 z=0.5361328782051282
- **ACCELERATION** `ind_generation` value=2.489e+04 d1=-63.0 d12=-55.0 z=0.5361328782051282
- **PERSISTENT_UP** `wind_gen` value=1.054e+04 d1=0.0 d12=338.0 z=0.4025907639198218

## Nearest historical live analogues

- `2026-09-15T16:21:57.402275Z` distance=0.096 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 53.0}
- `2026-09-15T16:26:08.230608Z` distance=0.096 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 53.0}
- `2026-09-15T16:30:22.410859Z` distance=0.096 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 53.0}
- `2026-09-15T15:52:27.365496Z` distance=0.142 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:56:36.878520Z` distance=0.142 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -54.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

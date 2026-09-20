# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T04:38:07.201517Z`  
Memory snapshots: **1717**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-6763 d1=0.0 d12=-2948.0 z=-38.91287019230769
- **CHANGE_POINT** `ind_generation` value=1.319e+04 d1=0.0 d12=-2948.0 z=-38.91287019230769
- **ROBUST_OUTLIER** `imbalance` value=-6763 d1=0.0 d12=-2948.0 z=-38.91287019230769
- **ROBUST_OUTLIER** `ind_generation` value=1.319e+04 d1=0.0 d12=-2948.0 z=-38.91287019230769
- **CHANGE_POINT** `margin` value=3.751e+04 d1=0.0 d12=-32.0 z=19.904330173469386
- **ROBUST_OUTLIER** `margin` value=3.751e+04 d1=0.0 d12=-32.0 z=19.904330173469386
- **CHANGE_POINT** `ind_demand` value=-1.232e+04 d1=0.0 d12=-28.0 z=-3.29150998
- **CHANGE_POINT** `biomass_gen` value=1230 d1=-2.0 d12=4.0 z=1.9311706526315788
- **ROBUST_OUTLIER** `ind_demand` value=-1.232e+04 d1=0.0 d12=-28.0 z=-3.29150998
- **CHANGE_POINT** `thermal_base` value=7511 d1=33.0 d12=490.0 z=0.6109643995844874
- **CHANGE_POINT** `ccgt_gen` value=4173 d1=31.0 d12=482.0 z=0.5991277667597765
- **REVERSAL** `biomass_gen` value=1230 d1=-2.0 d12=4.0 z=1.9311706526315788
- **ACCELERATION** `biomass_gen` value=1230 d1=-2.0 d12=4.0 z=1.9311706526315788
- **PERSISTENT_DOWN** `interconnector_net` value=-1.266e+04 d1=0.0 d12=-774.0 z=-1.426552852067408
- **ACCELERATION** `interconnector_net` value=-1.266e+04 d1=0.0 d12=-774.0 z=-1.426552852067408

## Nearest historical live analogues

- `2026-09-20T03:34:04.391029Z` distance=0.034 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:38:17.578686Z` distance=0.034 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:42:30.347706Z` distance=0.034 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:21:25.229596Z` distance=1.029 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 3696.0}
- `2026-09-20T03:25:39.544534Z` distance=1.029 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 3696.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

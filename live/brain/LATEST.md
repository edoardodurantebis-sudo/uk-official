# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T04:33:18.594038Z`  
Memory snapshots: **1716**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-6763 d1=0.0 d12=-2948.0 z=-38.91287019230769
- **CHANGE_POINT** `ind_generation` value=1.319e+04 d1=0.0 d12=-2948.0 z=-38.91287019230769
- **PERSISTENT_DOWN** `imbalance` value=-6763 d1=0.0 d12=-2948.0 z=-38.91287019230769
- **ROBUST_OUTLIER** `imbalance` value=-6763 d1=0.0 d12=-2948.0 z=-38.91287019230769
- **ROBUST_OUTLIER** `ind_generation` value=1.319e+04 d1=0.0 d12=-2948.0 z=-38.91287019230769
- **ROBUST_OUTLIER** `margin` value=3.751e+04 d1=0.0 d12=-32.0 z=19.904330173469386
- **CHANGE_POINT** `ind_demand` value=-1.232e+04 d1=0.0 d12=-28.0 z=-3.29150998
- **CHANGE_POINT** `biomass_gen` value=1232 d1=1.0 d12=13.0 z=2.653584674342105
- **ROBUST_OUTLIER** `ind_demand` value=-1.232e+04 d1=0.0 d12=-28.0 z=-3.29150998
- **CHANGE_POINT** `ps_gen` value=-697 d1=3.0 d12=-2.0 z=-0.7285713789712557
- **CHANGE_POINT** `thermal_base` value=7478 d1=9.0 d12=441.0 z=0.5477900179558011
- **CHANGE_POINT** `ccgt_gen` value=4142 d1=9.0 d12=439.0 z=0.5392160396935933
- **PERSISTENT_DOWN** `interconnector_net` value=-1.266e+04 d1=-333.0 d12=-773.0 z=-1.4216654770749666
- **ACCELERATION** `interconnector_net` value=-1.266e+04 d1=-333.0 d12=-773.0 z=-1.4216654770749666
- **REVERSAL** `ps_gen` value=-697 d1=3.0 d12=-2.0 z=-0.7285713789712557

## Nearest historical live analogues

- `2026-09-20T03:34:04.391029Z` distance=0.034 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:38:17.578686Z` distance=0.034 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:21:25.229596Z` distance=1.029 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 3696.0}
- `2026-09-20T03:25:39.544534Z` distance=1.029 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 3696.0}
- `2026-09-20T03:29:52.472014Z` distance=1.029 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 3696.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

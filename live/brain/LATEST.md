# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T13:22:29.547136Z`  
Memory snapshots: **1500**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=1.679e+04 d1=0.0 d12=30.0 z=-32.61569215487805
- **CHANGE_POINT** `imbalance` value=-3220 d1=0.0 d12=30.0 z=-6.041823017318664
- **ROBUST_OUTLIER** `imbalance` value=-3220 d1=0.0 d12=30.0 z=-6.041823017318664
- **CHANGE_POINT** `wind_gen` value=1.501e+04 d1=-13.0 d12=-336.0 z=-3.0520100980066447
- **CHANGE_POINT** `residual_proxy` value=1.285e+04 d1=0.0 d12=0.0 z=2.954730270344828
- **ROBUST_OUTLIER** `demand_forecast` value=1.951e+04 d1=0.0 d12=0.0 z=3.2718281479508198
- **CHANGE_POINT** `interconnector_net` value=-2604 d1=-9.0 d12=-892.0 z=-1.1714205128149435
- **PERSISTENT_DOWN** `wind_gen` value=1.501e+04 d1=-13.0 d12=-336.0 z=-3.0520100980066447
- **ROBUST_OUTLIER** `wind_gen` value=1.501e+04 d1=-13.0 d12=-336.0 z=-3.0520100980066447
- **CHANGE_POINT** `thermal_base` value=6512 d1=14.0 d12=209.0 z=0.25452443396226415
- **CHANGE_POINT** `ccgt_gen` value=3183 d1=17.0 d12=209.0 z=0.2346051304347826
- **PERSISTENT_DOWN** `interconnector_net` value=-2604 d1=-9.0 d12=-892.0 z=-1.1714205128149435
- **PERSISTENT_DOWN** `biomass_gen` value=475 d1=-1.0 d12=-3.0 z=-0.67448975
- **ACCELERATION** `nuclear_gen` value=3329 d1=-3.0 d12=0.0 z=-0.67448975
- **PERSISTENT_UP** `thermal_base` value=6512 d1=14.0 d12=209.0 z=0.25452443396226415

## Nearest historical live analogues

- `2026-09-19T12:23:39.094440Z` distance=0.085 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1.0}
- `2026-09-19T12:27:49.601950Z` distance=0.085 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1.0}
- `2026-09-19T11:54:18.195696Z` distance=0.085 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:58:27.853052Z` distance=0.085 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T12:02:38.156173Z` distance=0.085 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

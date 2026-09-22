# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T09:46:43.408904Z`  
Memory snapshots: **2470**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=4.033e+04 d1=0.0 d12=1386.0 z=155.745815
- **ROBUST_OUTLIER** `margin` value=4.033e+04 d1=0.0 d12=1386.0 z=155.745815
- **CHANGE_POINT** `imbalance` value=2430 d1=0.0 d12=2450.0 z=19.209331819444444
- **ROBUST_OUTLIER** `imbalance` value=2430 d1=0.0 d12=2450.0 z=19.209331819444444
- **ROBUST_OUTLIER** `ind_generation` value=2.35e+04 d1=0.0 d12=2450.0 z=17.87738488888889
- **CHANGE_POINT** `ind_demand` value=-1.28e+04 d1=0.0 d12=0.0 z=-4.25913752247191
- **CHANGE_POINT** `biomass_gen` value=3048 d1=2.0 d12=1.0 z=3.8221085833333333
- **ROBUST_OUTLIER** `ind_demand` value=-1.28e+04 d1=0.0 d12=0.0 z=-4.25913752247191
- **ACCELERATION** `biomass_gen` value=3048 d1=2.0 d12=1.0 z=3.8221085833333333
- **ROBUST_OUTLIER** `biomass_gen` value=3048 d1=2.0 d12=1.0 z=3.8221085833333333
- **CHANGE_POINT** `residual_proxy` value=7927 d1=0.0 d12=0.0 z=-0.67448975
- **PERSISTENT_DOWN** `thermal_base` value=1.376e+04 d1=-238.0 d12=-1502.0 z=-2.156138632937532
- **PERSISTENT_DOWN** `ccgt_gen` value=1.01e+04 d1=-239.0 d12=-1510.0 z=-2.145883070951157
- **PERSISTENT_UP** `interconnector_net` value=1.081e+04 d1=25.0 d12=1371.0 z=1.8628459793643264
- **PERSISTENT_UP** `wind_gen` value=3718 d1=75.0 d12=144.0 z=1.7203757547468357

## Nearest historical live analogues

- `2026-09-21T09:51:38.826991Z` distance=0.472 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T09:55:50.935902Z` distance=0.472 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:00:02.533283Z` distance=0.472 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:04:15.522994Z` distance=0.472 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:08:28.408864Z` distance=0.472 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 354.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

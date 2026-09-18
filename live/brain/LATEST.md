# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T14:55:13.529164Z`  
Memory snapshots: **1235**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=-22.0 z=-14.8387745
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-6.528097223214285
- **CHANGE_POINT** `imbalance` value=8537 d1=-13.0 d12=-391.0 z=-4.32978904032258
- **CHANGE_POINT** `wind_gen` value=1.688e+04 d1=0.0 d12=986.0 z=3.1597651022601987
- **CHANGE_POINT** `biomass_gen` value=1484 d1=0.0 d12=326.0 z=3.111083971875
- **PERSISTENT_DOWN** `imbalance` value=8537 d1=-13.0 d12=-391.0 z=-4.32978904032258
- **ROBUST_OUTLIER** `imbalance` value=8537 d1=-13.0 d12=-391.0 z=-4.32978904032258
- **CHANGE_POINT** `margin` value=3.83e+04 d1=0.0 d12=104.0 z=1.4716139999999998
- **ROBUST_OUTLIER** `residual_proxy` value=9748 d1=0.0 d12=380.0 z=3.3488416087500004
- **PERSISTENT_UP** `wind_gen` value=1.688e+04 d1=0.0 d12=986.0 z=3.1597651022601987
- **ROBUST_OUTLIER** `wind_gen` value=1.688e+04 d1=0.0 d12=986.0 z=3.1597651022601987
- **PERSISTENT_UP** `biomass_gen` value=1484 d1=0.0 d12=326.0 z=3.111083971875
- **ROBUST_OUTLIER** `biomass_gen` value=1484 d1=0.0 d12=326.0 z=3.111083971875
- **CHANGE_POINT** `ps_gen` value=-465 d1=0.0 d12=253.0 z=1.0977664808673468
- **CHANGE_POINT** `interconnector_net` value=5020 d1=0.0 d12=-1487.0 z=-0.4261584483159117

## Nearest historical live analogues

- `2026-09-18T13:55:43.928319Z` distance=0.144 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 380.0}
- `2026-09-18T13:59:56.236821Z` distance=0.144 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 380.0}
- `2026-09-18T13:22:08.039057Z` distance=0.147 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:26:20.440549Z` distance=0.147 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:30:31.422218Z` distance=0.147 → {'next30m_imbalance_delta': -7.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

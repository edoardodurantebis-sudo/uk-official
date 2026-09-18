# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T15:16:12.629356Z`  
Memory snapshots: **1240**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=0.0 z=-14.8387745
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-6.528097223214285
- **CHANGE_POINT** `imbalance` value=8537 d1=0.0 d12=-13.0 z=-3.8221085833333333
- **ROBUST_OUTLIER** `imbalance` value=8537 d1=0.0 d12=-13.0 z=-3.8221085833333333
- **CHANGE_POINT** `margin` value=3.83e+04 d1=0.0 d12=0.0 z=1.4716139999999998
- **ROBUST_OUTLIER** `residual_proxy` value=9748 d1=0.0 d12=0.0 z=3.3488416087500004
- **PERSISTENT_UP** `biomass_gen` value=1488 d1=3.0 d12=126.0 z=3.144808459375
- **ROBUST_OUTLIER** `biomass_gen` value=1488 d1=3.0 d12=126.0 z=3.144808459375
- **PERSISTENT_UP** `ps_gen` value=-173 d1=2.0 d12=295.0 z=3.1074706339285716
- **ROBUST_OUTLIER** `ps_gen` value=-173 d1=2.0 d12=295.0 z=3.1074706339285716
- **CHANGE_POINT** `ind_generation` value=2.559e+04 d1=0.0 d12=-13.0 z=-0.8118858101851851
- **CHANGE_POINT** `ccgt_gen` value=2553 d1=11.0 d12=64.0 z=0.697353809322034
- **CHANGE_POINT** `thermal_base` value=5883 d1=9.0 d12=58.0 z=0.5838020525210084
- **REVERSAL** `wind_gen` value=1.642e+04 d1=-67.0 d12=396.0 z=1.7951643732612057
- **PERSISTENT_DOWN** `nuclear_gen` value=3330 d1=-2.0 d12=-6.0 z=-1.48387745

## Nearest historical live analogues

- `2026-09-18T14:21:00.093276Z` distance=0.047 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:55:43.928319Z` distance=0.144 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 380.0}
- `2026-09-18T13:59:56.236821Z` distance=0.144 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 380.0}
- `2026-09-18T14:04:09.224702Z` distance=0.144 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 380.0}
- `2026-09-18T14:08:23.149664Z` distance=0.144 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 380.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

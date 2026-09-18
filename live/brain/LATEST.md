# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T15:12:01.212365Z`  
Memory snapshots: **1239**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=-22.0 z=-14.8387745
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-6.528097223214285
- **CHANGE_POINT** `imbalance` value=8537 d1=0.0 d12=-391.0 z=-4.062384830152672
- **CHANGE_POINT** `biomass_gen` value=1485 d1=-1.0 d12=123.0 z=3.11951509375
- **CHANGE_POINT** `ps_gen` value=-175 d1=-5.0 d12=293.0 z=3.093705536989796
- **ROBUST_OUTLIER** `imbalance` value=8537 d1=0.0 d12=-391.0 z=-4.062384830152672
- **CHANGE_POINT** `margin` value=3.83e+04 d1=0.0 d12=104.0 z=1.4716139999999998
- **ROBUST_OUTLIER** `residual_proxy` value=9748 d1=0.0 d12=0.0 z=3.3488416087500004
- **REVERSAL** `biomass_gen` value=1485 d1=-1.0 d12=123.0 z=3.11951509375
- **ROBUST_OUTLIER** `biomass_gen` value=1485 d1=-1.0 d12=123.0 z=3.11951509375
- **REVERSAL** `ps_gen` value=-175 d1=-5.0 d12=293.0 z=3.093705536989796
- **ROBUST_OUTLIER** `ps_gen` value=-175 d1=-5.0 d12=293.0 z=3.093705536989796
- **CHANGE_POINT** `ind_generation` value=2.559e+04 d1=0.0 d12=-11.0 z=-0.8118858101851851
- **CHANGE_POINT** `ccgt_gen` value=2542 d1=25.0 d12=53.0 z=0.5716014830508475
- **CHANGE_POINT** `thermal_base` value=5874 d1=21.0 d12=49.0 z=0.48177839285714286

## Nearest historical live analogues

- `2026-09-18T13:55:43.928319Z` distance=0.144 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 380.0}
- `2026-09-18T13:59:56.236821Z` distance=0.144 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 380.0}
- `2026-09-18T14:04:09.224702Z` distance=0.144 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 380.0}
- `2026-09-18T14:08:23.149664Z` distance=0.144 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 380.0}
- `2026-09-18T14:12:37.215300Z` distance=0.144 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 380.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

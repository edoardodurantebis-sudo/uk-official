# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T18:50:45.390519Z`  
Memory snapshots: **1578**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.62e+04 d1=0.0 d12=-611.0 z=-38.918058574999996
- **ROBUST_OUTLIER** `ind_generation` value=1.62e+04 d1=0.0 d12=-611.0 z=-38.918058574999996
- **CHANGE_POINT** `imbalance` value=-3750 d1=0.0 d12=-611.0 z=-10.223844631578947
- **ROBUST_OUTLIER** `imbalance` value=-3750 d1=0.0 d12=-611.0 z=-10.223844631578947
- **CHANGE_POINT** `biomass_gen` value=991 d1=12.0 d12=261.0 z=2.288552557860262
- **CHANGE_POINT** `margin` value=3.62e+04 d1=0.0 d12=-100.0 z=-2.228225066964286
- **PERSISTENT_DOWN** `ccgt_gen` value=6983 d1=-87.0 d12=-2.0 z=3.8440050621739132
- **ACCELERATION** `ccgt_gen` value=6983 d1=-87.0 d12=-2.0 z=3.8440050621739132
- **ROBUST_OUTLIER** `ccgt_gen` value=6983 d1=-87.0 d12=-2.0 z=3.8440050621739132
- **REVERSAL** `thermal_base` value=1.032e+04 d1=-82.0 d12=8.0 z=3.8087465986218776
- **ACCELERATION** `thermal_base` value=1.032e+04 d1=-82.0 d12=8.0 z=3.8087465986218776
- **ROBUST_OUTLIER** `thermal_base` value=1.032e+04 d1=-82.0 d12=8.0 z=3.8087465986218776
- **PERSISTENT_UP** `biomass_gen` value=991 d1=12.0 d12=261.0 z=2.288552557860262
- **PERSISTENT_UP** `nuclear_gen` value=3334 d1=5.0 d12=10.0 z=1.3489795
- **ACCELERATION** `nuclear_gen` value=3334 d1=5.0 d12=10.0 z=1.3489795

## Nearest historical live analogues

- `2026-09-19T17:22:38.318939Z` distance=0.017 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:26:48.291042Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:31:01.384129Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:35:13.165368Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:39:26.231429Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

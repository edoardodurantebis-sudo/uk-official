# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T18:25:36.560673Z`  
Memory snapshots: **1572**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.62e+04 d1=-611.0 d12=-614.0 z=-38.918058574999996
- **PERSISTENT_DOWN** `ind_generation` value=1.62e+04 d1=-611.0 d12=-614.0 z=-38.918058574999996
- **ACCELERATION** `ind_generation` value=1.62e+04 d1=-611.0 d12=-614.0 z=-38.918058574999996
- **ROBUST_OUTLIER** `ind_generation` value=1.62e+04 d1=-611.0 d12=-614.0 z=-38.918058574999996
- **CHANGE_POINT** `imbalance` value=-3750 d1=-611.0 d12=-614.0 z=-10.223844631578947
- **PERSISTENT_DOWN** `imbalance` value=-3750 d1=-611.0 d12=-614.0 z=-10.223844631578947
- **ACCELERATION** `imbalance` value=-3750 d1=-611.0 d12=-614.0 z=-10.223844631578947
- **ROBUST_OUTLIER** `imbalance` value=-3750 d1=-611.0 d12=-614.0 z=-10.223844631578947
- **CHANGE_POINT** `margin` value=3.62e+04 d1=0.0 d12=-50.0 z=-2.712010869791667
- **ROBUST_OUTLIER** `ccgt_gen` value=6753 d1=0.0 d12=57.0 z=3.9057952745370375
- **ROBUST_OUTLIER** `thermal_base` value=1.008e+04 d1=0.0 d12=58.0 z=3.898438444033302
- **CHANGE_POINT** `biomass_gen` value=835 d1=0.0 d12=227.0 z=1.534618880733945
- **PERSISTENT_DOWN** `margin` value=3.62e+04 d1=0.0 d12=-50.0 z=-2.712010869791667
- **ACCELERATION** `margin` value=3.62e+04 d1=0.0 d12=-50.0 z=-2.712010869791667
- **PERSISTENT_UP** `biomass_gen` value=835 d1=0.0 d12=227.0 z=1.534618880733945

## Nearest historical live analogues

- `2026-09-19T17:22:38.318939Z` distance=0.017 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:26:48.291042Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:31:01.384129Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T16:52:42.433757Z` distance=0.020 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T16:56:53.146650Z` distance=0.020 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

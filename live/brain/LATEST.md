# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T03:04:06.415873Z`  
Memory snapshots: **1695**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.761e+04 d1=0.0 d12=1589.0 z=29.77390467857143
- **ROBUST_OUTLIER** `margin` value=3.761e+04 d1=0.0 d12=1589.0 z=29.77390467857143
- **CHANGE_POINT** `ind_demand` value=-1.228e+04 d1=0.0 d12=-81.0 z=-18.78935732142857
- **PERSISTENT_DOWN** `ind_demand` value=-1.228e+04 d1=0.0 d12=-81.0 z=-18.78935732142857
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=0.0 d12=-81.0 z=-18.78935732142857
- **REVERSAL** `biomass_gen` value=1207 d1=10.0 d12=-24.0 z=6.060188208333334
- **ACCELERATION** `biomass_gen` value=1207 d1=10.0 d12=-24.0 z=6.060188208333334
- **ROBUST_OUTLIER** `biomass_gen` value=1207 d1=10.0 d12=-24.0 z=6.060188208333334
- **CHANGE_POINT** `interconnector_net` value=-1.124e+04 d1=-163.0 d12=-725.0 z=-1.3503950083945435
- **CHANGE_POINT** `thermal_base` value=6967 d1=-19.0 d12=-647.0 z=-0.5172577023178808
- **CHANGE_POINT** `ccgt_gen` value=3637 d1=-21.0 d12=-649.0 z=-0.5137697501650165
- **PERSISTENT_DOWN** `interconnector_net` value=-1.124e+04 d1=-163.0 d12=-725.0 z=-1.3503950083945435
- **PERSISTENT_UP** `ps_gen` value=-693 d1=1.0 d12=2.0 z=-1.0684484778528527
- **PERSISTENT_UP** `nuclear_gen` value=3330 d1=2.0 d12=2.0 z=-0.8993196666666666
- **ACCELERATION** `nuclear_gen` value=3330 d1=2.0 d12=2.0 z=-0.8993196666666666

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.375 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.375 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.375 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.375 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.375 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

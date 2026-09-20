# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T10:49:30.773763Z`  
Memory snapshots: **1805**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.603e+04 d1=0.0 d12=14.0 z=24.0118351
- **ROBUST_OUTLIER** `ind_generation` value=1.603e+04 d1=0.0 d12=14.0 z=24.0118351
- **ROBUST_OUTLIER** `margin` value=3.978e+04 d1=0.0 d12=490.0 z=22.731311276119403
- **CHANGE_POINT** `ind_demand` value=-1.247e+04 d1=0.0 d12=-107.0 z=-15.127841535714285
- **ROBUST_OUTLIER** `ind_demand` value=-1.247e+04 d1=0.0 d12=-107.0 z=-15.127841535714285
- **CHANGE_POINT** `imbalance` value=-4140 d1=0.0 d12=14.0 z=6.483963509124088
- **ROBUST_OUTLIER** `imbalance` value=-4140 d1=0.0 d12=14.0 z=6.483963509124088
- **PERSISTENT_UP** `residual_proxy` value=1.824e+04 d1=938.0 d12=1031.0 z=6.057839618012422
- **ACCELERATION** `residual_proxy` value=1.824e+04 d1=938.0 d12=1031.0 z=6.057839618012422
- **ROBUST_OUTLIER** `residual_proxy` value=1.824e+04 d1=938.0 d12=1031.0 z=6.057839618012422
- **CHANGE_POINT** `wind_gen` value=1.38e+04 d1=-130.0 d12=-624.0 z=-3.0190981139652675
- **PERSISTENT_DOWN** `wind_gen` value=1.38e+04 d1=-130.0 d12=-624.0 z=-3.0190981139652675
- **ROBUST_OUTLIER** `wind_gen` value=1.38e+04 d1=-130.0 d12=-624.0 z=-3.0190981139652675
- **CHANGE_POINT** `ps_gen` value=-924 d1=3.0 d12=3.0 z=-0.6565829424778761
- **PERSISTENT_UP** `nuclear_gen` value=3343 d1=8.0 d12=3.0 z=2.360714125

## Nearest historical live analogues

- `2026-09-20T09:49:28.570363Z` distance=0.220 → {'next30m_imbalance_delta': 33.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:53:43.269871Z` distance=0.229 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 490.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:20:07.153673Z` distance=0.347 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:24:18.809197Z` distance=0.347 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:28:32.169507Z` distance=0.347 → {'next30m_imbalance_delta': 33.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

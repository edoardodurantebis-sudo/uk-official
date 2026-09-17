# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T06:39:57.616616Z`  
Memory snapshots: **776**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.648e+04 d1=0.0 d12=96.0 z=28.4297429625
- **ROBUST_OUTLIER** `ind_generation` value=2.648e+04 d1=0.0 d12=96.0 z=28.4297429625
- **CHANGE_POINT** `imbalance` value=7359 d1=0.0 d12=96.0 z=18.102434580645163
- **ROBUST_OUTLIER** `imbalance` value=7359 d1=0.0 d12=96.0 z=18.102434580645163
- **CHANGE_POINT** `ps_gen` value=224 d1=0.0 d12=-2.0 z=5.879302320833333
- **PERSISTENT_DOWN** `ps_gen` value=224 d1=0.0 d12=-2.0 z=5.879302320833333
- **ACCELERATION** `ps_gen` value=224 d1=0.0 d12=-2.0 z=5.879302320833333
- **ROBUST_OUTLIER** `ps_gen` value=224 d1=0.0 d12=-2.0 z=5.879302320833333
- **CHANGE_POINT** `margin` value=3.577e+04 d1=0.0 d12=-19.0 z=-2.052794891304348
- **CHANGE_POINT** `thermal_base` value=8429 d1=0.0 d12=1205.0 z=1.9173614015401539
- **CHANGE_POINT** `ccgt_gen` value=5120 d1=0.0 d12=1211.0 z=1.9168539656970363
- **ROBUST_OUTLIER** `ind_demand` value=-1.182e+04 d1=0.0 d12=-364.0 z=-3.285417814516129
- **CHANGE_POINT** `biomass_gen` value=3130 d1=0.0 d12=-82.0 z=-1.1205232943548387
- **PERSISTENT_UP** `interconnector_net` value=-5401 d1=0.0 d12=2881.0 z=2.9753091852
- **PERSISTENT_UP** `thermal_base` value=8429 d1=0.0 d12=1205.0 z=1.9173614015401539

## Nearest historical live analogues

- `2026-09-16T12:53:12.066274Z` distance=0.540 → {'next30m_imbalance_delta': 110.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T12:57:22.882714Z` distance=0.540 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T13:01:39.157044Z` distance=0.540 → {'next30m_imbalance_delta': 304.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T13:05:52.763174Z` distance=0.540 → {'next30m_imbalance_delta': 304.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T13:10:06.628440Z` distance=0.540 → {'next30m_imbalance_delta': 304.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T06:44:07.871858Z`  
Memory snapshots: **777**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.648e+04 d1=0.0 d12=75.0 z=22.15235943627451
- **ROBUST_OUTLIER** `ind_generation` value=2.648e+04 d1=0.0 d12=75.0 z=22.15235943627451
- **CHANGE_POINT** `imbalance` value=7359 d1=0.0 d12=75.0 z=14.685890156666668
- **ROBUST_OUTLIER** `imbalance` value=7359 d1=0.0 d12=75.0 z=14.685890156666668
- **CHANGE_POINT** `ps_gen` value=226 d1=2.0 d12=0.0 z=5.447801826923077
- **ACCELERATION** `ps_gen` value=226 d1=2.0 d12=0.0 z=5.447801826923077
- **ROBUST_OUTLIER** `ps_gen` value=226 d1=2.0 d12=0.0 z=5.447801826923077
- **CHANGE_POINT** `interconnector_net` value=-5402 d1=-1.0 d12=2916.0 z=2.973150818
- **CHANGE_POINT** `margin` value=3.577e+04 d1=0.0 d12=-19.0 z=-2.052794891304348
- **CHANGE_POINT** `ccgt_gen` value=5188 d1=68.0 d12=1127.0 z=2.0175461786498357
- **CHANGE_POINT** `thermal_base` value=8495 d1=66.0 d12=1116.0 z=2.015307107810781
- **ROBUST_OUTLIER** `ind_demand` value=-1.182e+04 d1=0.0 d12=-363.0 z=-3.285417814516129
- **REVERSAL** `interconnector_net` value=-5402 d1=-1.0 d12=2916.0 z=2.973150818
- **CHANGE_POINT** `biomass_gen` value=3156 d1=26.0 d12=-62.0 z=-0.19607260174418606
- **PERSISTENT_UP** `ccgt_gen` value=5188 d1=68.0 d12=1127.0 z=2.0175461786498357

## Nearest historical live analogues

- `2026-09-16T12:53:12.066274Z` distance=0.540 → {'next30m_imbalance_delta': 110.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T12:57:22.882714Z` distance=0.540 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T13:01:39.157044Z` distance=0.540 → {'next30m_imbalance_delta': 304.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T13:05:52.763174Z` distance=0.540 → {'next30m_imbalance_delta': 304.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T13:10:06.628440Z` distance=0.540 → {'next30m_imbalance_delta': 304.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

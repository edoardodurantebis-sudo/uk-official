# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T06:48:19.283938Z`  
Memory snapshots: **778**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.648e+04 d1=0.0 d12=75.0 z=18.102434580645163
- **ROBUST_OUTLIER** `ind_generation` value=2.648e+04 d1=0.0 d12=75.0 z=18.102434580645163
- **CHANGE_POINT** `imbalance` value=7359 d1=0.0 d12=75.0 z=10.19370358018868
- **ROBUST_OUTLIER** `imbalance` value=7359 d1=0.0 d12=75.0 z=10.19370358018868
- **CHANGE_POINT** `ps_gen` value=226 d1=0.0 d12=0.0 z=5.095066456834532
- **ACCELERATION** `ps_gen` value=226 d1=0.0 d12=0.0 z=5.095066456834532
- **ROBUST_OUTLIER** `ps_gen` value=226 d1=0.0 d12=0.0 z=5.095066456834532
- **CHANGE_POINT** `ccgt_gen` value=5252 d1=64.0 d12=1085.0 z=2.11231532025247
- **CHANGE_POINT** `thermal_base` value=8559 d1=64.0 d12=1077.0 z=2.1102847623762377
- **CHANGE_POINT** `margin` value=3.577e+04 d1=0.0 d12=-19.0 z=-2.052794891304348
- **ROBUST_OUTLIER** `ind_demand` value=-1.182e+04 d1=0.0 d12=-363.0 z=-3.285417814516129
- **CHANGE_POINT** `biomass_gen` value=3173 d1=17.0 d12=-42.0 z=0.20660046396396395
- **PERSISTENT_UP** `ccgt_gen` value=5252 d1=64.0 d12=1085.0 z=2.11231532025247
- **PERSISTENT_UP** `thermal_base` value=8559 d1=64.0 d12=1077.0 z=2.1102847623762377
- **PERSISTENT_DOWN** `nuclear_gen` value=3307 d1=0.0 d12=-8.0 z=-1.3489794999999998

## Nearest historical live analogues

- `2026-09-16T12:53:12.066274Z` distance=0.539 → {'next30m_imbalance_delta': 110.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T12:57:22.882714Z` distance=0.539 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T13:01:39.157044Z` distance=0.539 → {'next30m_imbalance_delta': 304.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T13:05:52.763174Z` distance=0.539 → {'next30m_imbalance_delta': 304.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T13:10:06.628440Z` distance=0.539 → {'next30m_imbalance_delta': 304.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

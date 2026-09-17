# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T08:50:21.688970Z`  
Memory snapshots: **807**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **PERSISTENT_UP** `margin` value=3.606e+04 d1=10.0 d12=481.0 z=7.869047083333332
- **ROBUST_OUTLIER** `margin` value=3.606e+04 d1=10.0 d12=481.0 z=7.869047083333332
- **PERSISTENT_UP** `ind_demand` value=-1.213e+04 d1=14.0 d12=11.0 z=-6.646987697580645
- **ACCELERATION** `ind_demand` value=-1.213e+04 d1=14.0 d12=11.0 z=-6.646987697580645
- **ROBUST_OUTLIER** `ind_demand` value=-1.213e+04 d1=14.0 d12=11.0 z=-6.646987697580645
- **ACCELERATION** `wind_gen` value=1.557e+04 d1=0.0 d12=-77.0 z=6.014945728116711
- **ROBUST_OUTLIER** `wind_gen` value=1.557e+04 d1=0.0 d12=-77.0 z=6.014945728116711
- **CHANGE_POINT** `interconnector_net` value=5464 d1=0.0 d12=1502.0 z=2.9134292658758154
- **CHANGE_POINT** `ccgt_gen` value=2419 d1=0.0 d12=-755.0 z=-2.556092152214022
- **CHANGE_POINT** `thermal_base` value=5737 d1=0.0 d12=-750.0 z=-2.5411587998154985
- **CHANGE_POINT** `ps_gen` value=-714 d1=0.0 d12=-940.0 z=-1.1076243670212766
- **PERSISTENT_UP** `interconnector_net` value=5464 d1=0.0 d12=1502.0 z=2.9134292658758154
- **PERSISTENT_DOWN** `ccgt_gen` value=2419 d1=0.0 d12=-755.0 z=-2.556092152214022
- **PERSISTENT_DOWN** `thermal_base` value=5737 d1=0.0 d12=-750.0 z=-2.5411587998154985
- **ACCELERATION** `nuclear_gen` value=3318 d1=0.0 d12=5.0 z=1.686224375

## Nearest historical live analogues

- `2026-09-17T06:52:29.952634Z` distance=0.229 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:56:43.028097Z` distance=0.229 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:00:51.548981Z` distance=0.229 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:05:06.905847Z` distance=0.229 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:09:19.225959Z` distance=0.229 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

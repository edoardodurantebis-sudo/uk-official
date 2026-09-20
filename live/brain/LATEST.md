# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T17:56:46.494195Z`  
Memory snapshots: **1906**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=2259 d1=0.0 d12=124.0 z=204.86093225000002
- **ROBUST_OUTLIER** `biomass_gen` value=2259 d1=0.0 d12=124.0 z=204.86093225000002
- **PERSISTENT_UP** `thermal_base` value=1.224e+04 d1=58.0 d12=1769.0 z=59.14862154591837
- **ROBUST_OUTLIER** `thermal_base` value=1.224e+04 d1=58.0 d12=1769.0 z=59.14862154591837
- **PERSISTENT_UP** `ccgt_gen` value=8898 d1=56.0 d12=1770.0 z=57.13638171710526
- **ROBUST_OUTLIER** `ccgt_gen` value=8898 d1=56.0 d12=1770.0 z=57.13638171710526
- **CHANGE_POINT** `margin` value=3.546e+04 d1=0.0 d12=-424.0 z=-15.657797767857144
- **PERSISTENT_DOWN** `margin` value=3.546e+04 d1=0.0 d12=-424.0 z=-15.657797767857144
- **ACCELERATION** `margin` value=3.546e+04 d1=0.0 d12=-424.0 z=-15.657797767857144
- **ROBUST_OUTLIER** `margin` value=3.546e+04 d1=0.0 d12=-424.0 z=-15.657797767857144
- **PERSISTENT_UP** `imbalance` value=-5165 d1=7.0 d12=25.0 z=3.989360106707317
- **ROBUST_OUTLIER** `imbalance` value=-5165 d1=7.0 d12=25.0 z=3.989360106707317
- **PERSISTENT_UP** `ps_gen` value=288 d1=299.0 d12=123.0 z=3.6499287104430382
- **ACCELERATION** `ps_gen` value=288 d1=299.0 d12=123.0 z=3.6499287104430382
- **ROBUST_OUTLIER** `ps_gen` value=288 d1=299.0 d12=123.0 z=3.6499287104430382

## Nearest historical live analogues

- `2026-09-20T14:49:59.741529Z` distance=0.041 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:24:12.719546Z` distance=0.046 → {'next30m_imbalance_delta': 81.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:28:27.793665Z` distance=0.046 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:32:40.592900Z` distance=0.046 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:36:50.929973Z` distance=0.046 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

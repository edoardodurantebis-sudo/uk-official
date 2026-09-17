# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T10:14:35.004711Z`  
Memory snapshots: **827**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.441e+04 d1=0.0 d12=-57.0 z=-12.999257
- **ROBUST_OUTLIER** `margin` value=3.441e+04 d1=0.0 d12=-57.0 z=-12.999257
- **CHANGE_POINT** `imbalance` value=6663 d1=0.0 d12=26.0 z=-4.428171836956522
- **ROBUST_OUTLIER** `imbalance` value=6663 d1=0.0 d12=26.0 z=-4.428171836956522
- **PERSISTENT_DOWN** `wind_gen` value=1.55e+04 d1=-29.0 d12=-235.0 z=3.6276944140767826
- **ROBUST_OUTLIER** `wind_gen` value=1.55e+04 d1=-29.0 d12=-235.0 z=3.6276944140767826
- **CHANGE_POINT** `ind_demand` value=-1.301e+04 d1=0.0 d12=-23.0 z=-1.491091244117647
- **CHANGE_POINT** `interconnector_net` value=829 d1=-321.0 d12=-3072.0 z=0.8034552853728489
- **ACCELERATION** `thermal_base` value=5150 d1=-20.0 d12=-39.0 z=-2.526620215923172
- **ACCELERATION** `ccgt_gen` value=1836 d1=-24.0 d12=-44.0 z=-2.5214258802469134
- **REVERSAL** `biomass_gen` value=2001 d1=-16.0 d12=229.0 z=-1.487818691567065
- **PERSISTENT_DOWN** `interconnector_net` value=829 d1=-321.0 d12=-3072.0 z=0.8034552853728489
- **PERSISTENT_UP** `ps_gen` value=-661 d1=270.0 d12=281.0 z=-0.4908382803623898
- **ACCELERATION** `ps_gen` value=-661 d1=270.0 d12=281.0 z=-0.4908382803623898
- **ACCELERATION** `nuclear_gen` value=3314 d1=4.0 d12=5.0 z=0.22482991666666666

## Nearest historical live analogues

- `2026-09-17T09:19:56.543683Z` distance=0.054 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:52:24.970739Z` distance=1.072 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=1.072 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=1.072 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:05:03.473837Z` distance=1.072 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

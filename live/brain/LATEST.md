# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T19:15:39.927936Z`  
Memory snapshots: **1268**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.088e+04 d1=0.0 d12=-149.0 z=-94.428565
- **ROBUST_OUTLIER** `ind_demand` value=-1.088e+04 d1=0.0 d12=-149.0 z=-94.428565
- **CHANGE_POINT** `ccgt_gen` value=4809 d1=0.0 d12=-28.0 z=26.488012724576272
- **CHANGE_POINT** `thermal_base` value=8148 d1=0.0 d12=-21.0 z=26.259756401260503
- **PERSISTENT_DOWN** `ccgt_gen` value=4809 d1=0.0 d12=-28.0 z=26.488012724576272
- **ACCELERATION** `ccgt_gen` value=4809 d1=0.0 d12=-28.0 z=26.488012724576272
- **ROBUST_OUTLIER** `ccgt_gen` value=4809 d1=0.0 d12=-28.0 z=26.488012724576272
- **PERSISTENT_DOWN** `thermal_base` value=8148 d1=0.0 d12=-21.0 z=26.259756401260503
- **ACCELERATION** `thermal_base` value=8148 d1=0.0 d12=-21.0 z=26.259756401260503
- **ROBUST_OUTLIER** `thermal_base` value=8148 d1=0.0 d12=-21.0 z=26.259756401260503
- **CHANGE_POINT** `ind_generation` value=2.623e+04 d1=0.0 d12=5.0 z=18.240548891304346
- **ROBUST_OUTLIER** `ind_generation` value=2.623e+04 d1=0.0 d12=5.0 z=18.240548891304346
- **ACCELERATION** `interconnector_net` value=-807 d1=0.0 d12=65.0 z=-9.555663148083624
- **ROBUST_OUTLIER** `interconnector_net` value=-807 d1=0.0 d12=65.0 z=-9.555663148083624
- **ROBUST_OUTLIER** `margin` value=3.753e+04 d1=0.0 d12=-241.0 z=-4.87318844375

## Nearest historical live analogues

- `2026-09-18T17:51:12.400587Z` distance=0.118 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:55:26.775797Z` distance=0.119 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:59:39.675441Z` distance=0.119 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:03:52.862865Z` distance=0.119 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:08:04.608022Z` distance=0.119 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

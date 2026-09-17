# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T09:41:00.316073Z`  
Memory snapshots: **819**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.298e+04 d1=0.0 d12=-856.0 z=-15.959297794354839
- **CHANGE_POINT** `margin` value=3.447e+04 d1=0.0 d12=-1587.0 z=-14.715653355158729
- **ROBUST_OUTLIER** `ind_demand` value=-1.298e+04 d1=0.0 d12=-856.0 z=-15.959297794354839
- **ROBUST_OUTLIER** `margin` value=3.447e+04 d1=0.0 d12=-1587.0 z=-14.715653355158729
- **CHANGE_POINT** `imbalance` value=6637 d1=0.0 d12=-804.0 z=-4.618788505434782
- **CHANGE_POINT** `thermal_base` value=5128 d1=-15.0 d12=-609.0 z=-4.009322725480769
- **CHANGE_POINT** `ccgt_gen` value=1816 d1=-14.0 d12=-603.0 z=-3.9647149876190477
- **REVERSAL** `wind_gen` value=1.57e+04 d1=-32.0 d12=124.0 z=5.757960292279411
- **ROBUST_OUTLIER** `wind_gen` value=1.57e+04 d1=-32.0 d12=124.0 z=5.757960292279411
- **ROBUST_OUTLIER** `imbalance` value=6637 d1=0.0 d12=-804.0 z=-4.618788505434782
- **PERSISTENT_DOWN** `thermal_base` value=5128 d1=-15.0 d12=-609.0 z=-4.009322725480769
- **ROBUST_OUTLIER** `thermal_base` value=5128 d1=-15.0 d12=-609.0 z=-4.009322725480769
- **PERSISTENT_DOWN** `ccgt_gen` value=1816 d1=-14.0 d12=-603.0 z=-3.9647149876190477
- **ROBUST_OUTLIER** `ccgt_gen` value=1816 d1=-14.0 d12=-603.0 z=-3.9647149876190477
- **CHANGE_POINT** `residual_proxy` value=-999 d1=0.0 d12=0.0 z=-0.8285254714532871

## Nearest historical live analogues

- `2026-09-16T08:52:24.970739Z` distance=1.054 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=1.054 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=1.054 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:05:03.473837Z` distance=1.054 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:09:50.095639Z` distance=1.054 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T09:45:11.477564Z`  
Memory snapshots: **820**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.447e+04 d1=0.0 d12=-1587.0 z=-13.2199991
- **ROBUST_OUTLIER** `margin` value=3.447e+04 d1=0.0 d12=-1587.0 z=-13.2199991
- **CHANGE_POINT** `imbalance` value=6637 d1=0.0 d12=-804.0 z=-4.618788505434782
- **CHANGE_POINT** `ind_demand` value=-1.298e+04 d1=0.0 d12=-856.0 z=-4.167270004694836
- **CHANGE_POINT** `ccgt_gen` value=1816 d1=0.0 d12=-547.0 z=-3.3944549408646
- **CHANGE_POINT** `thermal_base` value=5128 d1=0.0 d12=-551.0 z=-3.3900250301302934
- **ACCELERATION** `wind_gen` value=1.57e+04 d1=0.0 d12=88.0 z=5.331092898169336
- **ROBUST_OUTLIER** `wind_gen` value=1.57e+04 d1=0.0 d12=88.0 z=5.331092898169336
- **ROBUST_OUTLIER** `imbalance` value=6637 d1=0.0 d12=-804.0 z=-4.618788505434782
- **ROBUST_OUTLIER** `ind_demand` value=-1.298e+04 d1=0.0 d12=-856.0 z=-4.167270004694836
- **CHANGE_POINT** `interconnector_net` value=2422 d1=0.0 d12=-3047.0 z=1.6118211750746656
- **PERSISTENT_DOWN** `ccgt_gen` value=1816 d1=0.0 d12=-547.0 z=-3.3944549408646
- **ROBUST_OUTLIER** `ccgt_gen` value=1816 d1=0.0 d12=-547.0 z=-3.3944549408646
- **PERSISTENT_DOWN** `thermal_base` value=5128 d1=0.0 d12=-551.0 z=-3.3900250301302934
- **ROBUST_OUTLIER** `thermal_base` value=5128 d1=0.0 d12=-551.0 z=-3.3900250301302934

## Nearest historical live analogues

- `2026-09-16T08:52:24.970739Z` distance=1.054 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=1.054 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=1.054 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:05:03.473837Z` distance=1.054 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:09:50.095639Z` distance=1.054 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

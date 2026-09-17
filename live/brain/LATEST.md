# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T09:36:45.320295Z`  
Memory snapshots: **818**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.447e+04 d1=0.0 d12=-1577.0 z=-16.585221174107144
- **CHANGE_POINT** `ind_demand` value=-1.298e+04 d1=0.0 d12=-842.0 z=-15.959297794354839
- **ROBUST_OUTLIER** `margin` value=3.447e+04 d1=0.0 d12=-1577.0 z=-16.585221174107144
- **ROBUST_OUTLIER** `ind_demand` value=-1.298e+04 d1=0.0 d12=-842.0 z=-15.959297794354839
- **CHANGE_POINT** `imbalance` value=6637 d1=0.0 d12=-888.0 z=-4.618788505434782
- **CHANGE_POINT** `thermal_base` value=5143 d1=-2.0 d12=-594.0 z=-4.329151784518829
- **CHANGE_POINT** `ccgt_gen` value=1830 d1=1.0 d12=-589.0 z=-4.284336548654244
- **REVERSAL** `wind_gen` value=1.573e+04 d1=-40.0 d12=156.0 z=6.044923250629722
- **ACCELERATION** `wind_gen` value=1.573e+04 d1=-40.0 d12=156.0 z=6.044923250629722
- **ROBUST_OUTLIER** `wind_gen` value=1.573e+04 d1=-40.0 d12=156.0 z=6.044923250629722
- **ROBUST_OUTLIER** `imbalance` value=6637 d1=0.0 d12=-888.0 z=-4.618788505434782
- **PERSISTENT_DOWN** `thermal_base` value=5143 d1=-2.0 d12=-594.0 z=-4.329151784518829
- **ROBUST_OUTLIER** `thermal_base` value=5143 d1=-2.0 d12=-594.0 z=-4.329151784518829
- **REVERSAL** `ccgt_gen` value=1830 d1=1.0 d12=-589.0 z=-4.284336548654244
- **ROBUST_OUTLIER** `ccgt_gen` value=1830 d1=1.0 d12=-589.0 z=-4.284336548654244

## Nearest historical live analogues

- `2026-09-16T08:52:24.970739Z` distance=1.054 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=1.054 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=1.054 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:05:03.473837Z` distance=1.054 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:09:50.095639Z` distance=1.054 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T09:32:33.001998Z`  
Memory snapshots: **817**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.447e+04 d1=0.0 d12=-1577.0 z=-16.585221174107144
- **CHANGE_POINT** `ind_demand` value=-1.298e+04 d1=0.0 d12=-842.0 z=-15.959297794354839
- **ROBUST_OUTLIER** `margin` value=3.447e+04 d1=0.0 d12=-1577.0 z=-16.585221174107144
- **ROBUST_OUTLIER** `ind_demand` value=-1.298e+04 d1=0.0 d12=-842.0 z=-15.959297794354839
- **CHANGE_POINT** `thermal_base` value=5145 d1=-20.0 d12=-663.0 z=-4.588619427544248
- **CHANGE_POINT** `ccgt_gen` value=1829 d1=-19.0 d12=-663.0 z=-4.548747066739606
- **PERSISTENT_UP** `wind_gen` value=1.577e+04 d1=29.0 d12=324.0 z=6.468728468503937
- **ROBUST_OUTLIER** `wind_gen` value=1.577e+04 d1=29.0 d12=324.0 z=6.468728468503937
- **ROBUST_OUTLIER** `imbalance` value=6637 d1=0.0 d12=-888.0 z=-4.618788505434782
- **PERSISTENT_DOWN** `thermal_base` value=5145 d1=-20.0 d12=-663.0 z=-4.588619427544248
- **ROBUST_OUTLIER** `thermal_base` value=5145 d1=-20.0 d12=-663.0 z=-4.588619427544248
- **PERSISTENT_DOWN** `ccgt_gen` value=1829 d1=-19.0 d12=-663.0 z=-4.548747066739606
- **ROBUST_OUTLIER** `ccgt_gen` value=1829 d1=-19.0 d12=-663.0 z=-4.548747066739606
- **CHANGE_POINT** `biomass_gen` value=1883 d1=55.0 d12=-76.0 z=-1.699212557436919
- **CHANGE_POINT** `ind_generation` value=2.65e+04 d1=0.0 d12=-32.0 z=1.174111787037037

## Nearest historical live analogues

- `2026-09-16T08:52:24.970739Z` distance=1.053 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=1.053 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=1.053 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:05:03.473837Z` distance=1.053 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:09:50.095639Z` distance=1.053 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

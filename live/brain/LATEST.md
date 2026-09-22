# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T22:53:13.778957Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.249e+04 d1=-15.0 d12=-15.0 z=-10.791836
- **CHANGE_POINT** `thermal_base` value=1.39e+04 d1=-71.0 d12=-2472.0 z=-9.548582034107403
- **CHANGE_POINT** `ccgt_gen` value=1.016e+04 d1=-74.0 d12=-2474.0 z=-9.503113509365994
- **PERSISTENT_DOWN** `ind_demand` value=-1.249e+04 d1=-15.0 d12=-15.0 z=-10.791836
- **ACCELERATION** `ind_demand` value=-1.249e+04 d1=-15.0 d12=-15.0 z=-10.791836
- **ROBUST_OUTLIER** `ind_demand` value=-1.249e+04 d1=-15.0 d12=-15.0 z=-10.791836
- **PERSISTENT_DOWN** `thermal_base` value=1.39e+04 d1=-71.0 d12=-2472.0 z=-9.548582034107403
- **ROBUST_OUTLIER** `thermal_base` value=1.39e+04 d1=-71.0 d12=-2472.0 z=-9.548582034107403
- **PERSISTENT_DOWN** `ccgt_gen` value=1.016e+04 d1=-74.0 d12=-2474.0 z=-9.503113509365994
- **ROBUST_OUTLIER** `ccgt_gen` value=1.016e+04 d1=-74.0 d12=-2474.0 z=-9.503113509365994
- **CHANGE_POINT** `wind_gen` value=2877 d1=79.0 d12=413.0 z=1.841686036890244
- **PERSISTENT_UP** `nuclear_gen` value=3744 d1=3.0 d12=2.0 z=2.9227889166666667
- **ACCELERATION** `nuclear_gen` value=3744 d1=3.0 d12=2.0 z=2.9227889166666667
- **PERSISTENT_UP** `ps_gen` value=148 d1=0.0 d12=5.0 z=-2.4395951296610168
- **ACCELERATION** `ps_gen` value=148 d1=0.0 d12=5.0 z=-2.4395951296610168

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.020 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:54:12.694588Z` distance=0.020 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:58:28.957668Z` distance=0.020 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:24:47.718083Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:28:58.806773Z` distance=0.021 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

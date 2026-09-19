# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T23:57:34.023150Z`  
Memory snapshots: **1651**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **PERSISTENT_DOWN** `ps_gen` value=-253 d1=-2.0 d12=-120.0 z=-85.3824671764706
- **ROBUST_OUTLIER** `ps_gen` value=-253 d1=-2.0 d12=-120.0 z=-85.3824671764706
- **PERSISTENT_DOWN** `ind_demand` value=-1.189e+04 d1=0.0 d12=-1.0 z=-10.791836
- **ACCELERATION** `ind_demand` value=-1.189e+04 d1=0.0 d12=-1.0 z=-10.791836
- **ROBUST_OUTLIER** `ind_demand` value=-1.189e+04 d1=0.0 d12=-1.0 z=-10.791836
- **CHANGE_POINT** `wind_gen` value=1.618e+04 d1=77.0 d12=480.0 z=3.330913905957162
- **CHANGE_POINT** `margin` value=3.599e+04 d1=0.0 d12=-65.0 z=-2.80587736
- **PERSISTENT_UP** `wind_gen` value=1.618e+04 d1=77.0 d12=480.0 z=3.330913905957162
- **ROBUST_OUTLIER** `wind_gen` value=1.618e+04 d1=77.0 d12=480.0 z=3.330913905957162
- **ROBUST_OUTLIER** `thermal_base` value=6479 d1=-1.0 d12=-419.0 z=-3.2601302851931333
- **ROBUST_OUTLIER** `ccgt_gen` value=3146 d1=-2.0 d12=-416.0 z=-3.244001940222032
- **PERSISTENT_DOWN** `margin` value=3.599e+04 d1=0.0 d12=-65.0 z=-2.80587736
- **ACCELERATION** `margin` value=3.599e+04 d1=0.0 d12=-65.0 z=-2.80587736
- **CHANGE_POINT** `biomass_gen` value=886 d1=0.0 d12=-23.0 z=-0.319861118556701
- **PERSISTENT_DOWN** `interconnector_net` value=-8390 d1=-10.0 d12=-359.0 z=-1.1346778182036121

## Nearest historical live analogues

- `2026-09-19T19:24:22.442601Z` distance=0.125 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -119.0}
- `2026-09-19T19:28:35.593770Z` distance=0.125 → {'next30m_imbalance_delta': -36.0, 'next30m_margin_delta': 40.0, 'next30m_residual_proxy_delta': -119.0}
- `2026-09-19T18:21:25.144867Z` distance=0.132 → {'next30m_imbalance_delta': -611.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T18:25:36.560673Z` distance=0.132 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T18:29:47.180961Z` distance=0.132 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

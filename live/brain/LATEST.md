# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T09:18:14.749183Z`  
Memory snapshots: **509**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.574e+04 d1=0.0 d12=-815.0 z=-46.07283830769231
- **ROBUST_OUTLIER** `ind_demand` value=-1.268e+04 d1=0.0 d12=-15.0 z=-15.945629474358975
- **CHANGE_POINT** `interconnector_net` value=1.028e+04 d1=1.0 d12=179.0 z=1.468643972683751
- **CHANGE_POINT** `ccgt_gen` value=7055 d1=-160.0 d12=-1025.0 z=-0.3986802374793616
- **CHANGE_POINT** `thermal_base` value=1.039e+04 d1=-158.0 d12=-1024.0 z=-0.3969769155665567
- **REVERSAL** `biomass_gen` value=3238 d1=-2.0 d12=5.0 z=2.0234692499999998
- **CHANGE_POINT** `demand_forecast` value=1.851e+04 d1=0.0 d12=0.0 z=None
- **PERSISTENT_UP** `nuclear_gen` value=3334 d1=2.0 d12=1.0 z=1.686224375
- **PERSISTENT_UP** `interconnector_net` value=1.028e+04 d1=1.0 d12=179.0 z=1.468643972683751
- **PERSISTENT_DOWN** `wind_gen` value=5924 d1=-341.0 d12=-913.0 z=-1.3325359575620768
- **ACCELERATION** `wind_gen` value=5924 d1=-341.0 d12=-913.0 z=-1.3325359575620768
- **PERSISTENT_DOWN** `ccgt_gen` value=7055 d1=-160.0 d12=-1025.0 z=-0.3986802374793616
- **PERSISTENT_DOWN** `thermal_base` value=1.039e+04 d1=-158.0 d12=-1024.0 z=-0.3969769155665567
- **PERSISTENT_UP** `ts_demand_forecast` value=2.064e+04 d1=1180.0 d12=1180.0 z=None
- **ACCELERATION** `ts_demand_forecast` value=2.064e+04 d1=1180.0 d12=1180.0 z=None

## Nearest historical live analogues

- `2026-09-16T08:17:56.653795Z` distance=0.514 → {'next30m_imbalance_delta': 235.0, 'next30m_margin_delta': 235.0, 'next30m_residual_proxy_delta': -321.0}
- `2026-09-16T07:23:21.620957Z` distance=0.528 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:27:32.881343Z` distance=0.528 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:31:44.991160Z` distance=0.528 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:35:56.436252Z` distance=0.528 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T11:41:03.979554Z`  
Memory snapshots: **2158**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=0.0 d12=587.0 z=14.786890673076924
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=587.0 z=14.786890673076924
- **CHANGE_POINT** `nuclear_gen` value=3517 d1=2.0 d12=22.0 z=3.2225621388888888
- **ROBUST_OUTLIER** `nuclear_gen` value=3517 d1=2.0 d12=22.0 z=3.2225621388888888
- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=1004.0 z=1.0682912189440994
- **REVERSAL** `ccgt_gen` value=7005 d1=-122.0 d12=47.0 z=-3.050989805319149
- **ACCELERATION** `ccgt_gen` value=7005 d1=-122.0 d12=47.0 z=-3.050989805319149
- **ROBUST_OUTLIER** `ccgt_gen` value=7005 d1=-122.0 d12=47.0 z=-3.050989805319149
- **REVERSAL** `thermal_base` value=1.052e+04 d1=-120.0 d12=69.0 z=-2.8014473331090177
- **ACCELERATION** `thermal_base` value=1.052e+04 d1=-120.0 d12=69.0 z=-2.8014473331090177
- **PERSISTENT_UP** `interconnector_net` value=1.134e+04 d1=41.0 d12=343.0 z=1.1553057890137328
- **REVERSAL** `wind_gen` value=3407 d1=28.0 d12=-3.0 z=-0.48146856752411576
- **ACCELERATION** `wind_gen` value=3407 d1=28.0 d12=-3.0 z=-0.48146856752411576
- **PERSISTENT_UP** `biomass_gen` value=3017 d1=3.0 d12=15.0 z=0.14988661111111112
- **ACCELERATION** `biomass_gen` value=3017 d1=3.0 d12=15.0 z=0.14988661111111112

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.474 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.474 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.474 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.474 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.474 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

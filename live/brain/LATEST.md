# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T11:36:50.598890Z`  
Memory snapshots: **2157**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=0.0 d12=587.0 z=14.786890673076924
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=587.0 z=14.786890673076924
- **CHANGE_POINT** `nuclear_gen` value=3515 d1=0.0 d12=20.0 z=2.697959
- **CHANGE_POINT** `margin` value=3.668e+04 d1=0.0 d12=-4335.0 z=-1.5156412114825584
- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=1004.0 z=1.0682912189440994
- **REVERSAL** `ccgt_gen` value=7127 d1=-13.0 d12=169.0 z=-2.8175493812056738
- **ACCELERATION** `ccgt_gen` value=7127 d1=-13.0 d12=169.0 z=-2.8175493812056738
- **REVERSAL** `thermal_base` value=1.064e+04 d1=-13.0 d12=189.0 z=-2.583577158142665
- **ACCELERATION** `thermal_base` value=1.064e+04 d1=-13.0 d12=189.0 z=-2.583577158142665
- **PERSISTENT_UP** `interconnector_net` value=1.13e+04 d1=49.0 d12=302.0 z=1.0862569007490637
- **REVERSAL** `wind_gen` value=3379 d1=64.0 d12=-31.0 z=-0.5364546383720931
- **ACCELERATION** `wind_gen` value=3379 d1=64.0 d12=-31.0 z=-0.5364546383720931
- **REVERSAL** `biomass_gen` value=3014 d1=-3.0 d12=12.0 z=-0.07494330555555556
- **ACCELERATION** `biomass_gen` value=3014 d1=-3.0 d12=12.0 z=-0.07494330555555556
- **PERSISTENT_UP** `ps_gen` value=-8 d1=0.0 d12=3.0 z=0.067448975

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.474 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.474 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.474 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.474 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.474 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

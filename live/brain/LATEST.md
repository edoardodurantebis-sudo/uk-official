# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T02:46:43.224866Z`  
Memory snapshots: **1691**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.761e+04 d1=0.0 d12=1588.0 z=29.754633542857146
- **ROBUST_OUTLIER** `margin` value=3.761e+04 d1=0.0 d12=1588.0 z=29.754633542857146
- **CHANGE_POINT** `ind_demand` value=-1.22e+04 d1=0.0 d12=0.0 z=-14.886952339285713
- **ROBUST_OUTLIER** `ind_demand` value=-1.22e+04 d1=0.0 d12=0.0 z=-14.886952339285713
- **PERSISTENT_DOWN** `biomass_gen` value=1152 d1=-29.0 d12=-70.0 z=4.936038625
- **ROBUST_OUTLIER** `biomass_gen` value=1152 d1=-29.0 d12=-70.0 z=4.936038625
- **CHANGE_POINT** `interconnector_net` value=-1.105e+04 d1=0.0 d12=-1092.0 z=-1.2529800346580406
- **REVERSAL** `ps_gen` value=-697 d1=-2.0 d12=118.0 z=-1.1403535412912913
- **PERSISTENT_DOWN** `nuclear_gen` value=3331 d1=-1.0 d12=-1.0 z=-0.6744897499999999
- **ACCELERATION** `nuclear_gen` value=3331 d1=-1.0 d12=-1.0 z=-0.6744897499999999
- **PERSISTENT_DOWN** `thermal_base` value=7297 d1=-79.0 d12=-248.0 z=-0.21349859941610327
- **PERSISTENT_DOWN** `ccgt_gen` value=3966 d1=-78.0 d12=-247.0 z=-0.21233936574074075
- **ACCELERATION** `wind_gen` value=1.533e+04 d1=66.0 d12=43.0 z=0.043109864181091875

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.329 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.329 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T02:37:39.122581Z`  
Memory snapshots: **1689**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.761e+04 d1=0.0 d12=1562.0 z=29.754633542857146
- **ROBUST_OUTLIER** `margin` value=3.761e+04 d1=0.0 d12=1562.0 z=29.754633542857146
- **CHANGE_POINT** `ind_demand` value=-1.22e+04 d1=0.0 d12=1.0 z=-14.886952339285713
- **ROBUST_OUTLIER** `ind_demand` value=-1.22e+04 d1=0.0 d12=1.0 z=-14.886952339285713
- **REVERSAL** `biomass_gen` value=1226 d1=-4.0 d12=15.0 z=6.448530791666667
- **ROBUST_OUTLIER** `biomass_gen` value=1226 d1=-4.0 d12=15.0 z=6.448530791666667
- **CHANGE_POINT** `interconnector_net` value=-1.105e+04 d1=1.0 d12=-1119.0 z=-1.2450699578395623
- **CHANGE_POINT** `ccgt_gen` value=4146 d1=-90.0 d12=-136.0 z=-0.06508948130277444
- **CHANGE_POINT** `thermal_base` value=7481 d1=-91.0 d12=-137.0 z=-0.0619429362244898
- **REVERSAL** `interconnector_net` value=-1.105e+04 d1=1.0 d12=-1119.0 z=-1.2450699578395623
- **ACCELERATION** `interconnector_net` value=-1.105e+04 d1=1.0 d12=-1119.0 z=-1.2450699578395623
- **PERSISTENT_UP** `ps_gen` value=-700 d1=3.0 d12=120.0 z=-1.1464300255255255
- **ACCELERATION** `nuclear_gen` value=3335 d1=-1.0 d12=-1.0 z=0.13489795
- **REVERSAL** `wind_gen` value=1.533e+04 d1=-22.0 d12=11.0 z=0.07666509854897219
- **ACCELERATION** `wind_gen` value=1.533e+04 d1=-22.0 d12=11.0 z=0.07666509854897219

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.329 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.329 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

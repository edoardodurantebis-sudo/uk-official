# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T02:33:25.726465Z`  
Memory snapshots: **1688**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.761e+04 d1=0.0 d12=1562.0 z=29.754633542857146
- **ROBUST_OUTLIER** `margin` value=3.761e+04 d1=0.0 d12=1562.0 z=29.754633542857146
- **ROBUST_OUTLIER** `ind_demand` value=-1.22e+04 d1=0.0 d12=1.0 z=-14.886952339285713
- **ROBUST_OUTLIER** `biomass_gen` value=1230 d1=0.0 d12=33.0 z=6.530287125
- **CHANGE_POINT** `interconnector_net` value=-1.105e+04 d1=-507.0 d12=-1120.0 z=-1.2453064096294044
- **CHANGE_POINT** `thermal_base` value=7572 d1=-27.0 d12=22.0 z=0.011458818248388986
- **CHANGE_POINT** `ccgt_gen` value=4236 d1=-30.0 d12=21.0 z=0.007967982870643828
- **PERSISTENT_DOWN** `interconnector_net` value=-1.105e+04 d1=-507.0 d12=-1120.0 z=-1.2453064096294044
- **ACCELERATION** `interconnector_net` value=-1.105e+04 d1=-507.0 d12=-1120.0 z=-1.2453064096294044
- **PERSISTENT_UP** `nuclear_gen` value=3336 d1=3.0 d12=1.0 z=0.40469384999999997
- **ACCELERATION** `nuclear_gen` value=3336 d1=3.0 d12=1.0 z=0.40469384999999997
- **REVERSAL** `wind_gen` value=1.535e+04 d1=-90.0 d12=37.0 z=0.1148411804556355
- **ACCELERATION** `wind_gen` value=1.535e+04 d1=-90.0 d12=37.0 z=0.1148411804556355
- **REVERSAL** `thermal_base` value=7572 d1=-27.0 d12=22.0 z=0.011458818248388986
- **ACCELERATION** `thermal_base` value=7572 d1=-27.0 d12=22.0 z=0.011458818248388986

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.329 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.329 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

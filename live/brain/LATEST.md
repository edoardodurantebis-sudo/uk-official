# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T02:41:53.579517Z`  
Memory snapshots: **1690**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.761e+04 d1=0.0 d12=1588.0 z=29.754633542857146
- **ROBUST_OUTLIER** `margin` value=3.761e+04 d1=0.0 d12=1588.0 z=29.754633542857146
- **CHANGE_POINT** `ind_demand` value=-1.22e+04 d1=0.0 d12=0.0 z=-14.886952339285713
- **ROBUST_OUTLIER** `ind_demand` value=-1.22e+04 d1=0.0 d12=0.0 z=-14.886952339285713
- **PERSISTENT_DOWN** `biomass_gen` value=1181 d1=-45.0 d12=-35.0 z=5.528772041666667
- **ACCELERATION** `biomass_gen` value=1181 d1=-45.0 d12=-35.0 z=5.528772041666667
- **ROBUST_OUTLIER** `biomass_gen` value=1181 d1=-45.0 d12=-35.0 z=5.528772041666667
- **CHANGE_POINT** `interconnector_net` value=-1.105e+04 d1=0.0 d12=-1120.0 z=-1.2482078874885425
- **CHANGE_POINT** `ccgt_gen` value=4044 d1=-102.0 d12=-200.0 z=-0.14832145608108108
- **CHANGE_POINT** `thermal_base` value=7376 d1=-105.0 d12=-204.0 z=-0.14832145608108108
- **PERSISTENT_DOWN** `interconnector_net` value=-1.105e+04 d1=0.0 d12=-1120.0 z=-1.2482078874885425
- **PERSISTENT_UP** `ps_gen` value=-695 d1=5.0 d12=124.0 z=-1.1363025518018017
- **PERSISTENT_DOWN** `nuclear_gen` value=3332 d1=-3.0 d12=-4.0 z=-0.67448975
- **ACCELERATION** `nuclear_gen` value=3332 d1=-3.0 d12=-4.0 z=-0.67448975
- **PERSISTENT_DOWN** `ccgt_gen` value=4044 d1=-102.0 d12=-200.0 z=-0.14832145608108108

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.329 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.329 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

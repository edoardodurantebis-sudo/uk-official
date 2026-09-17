# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T00:54:40.714610Z`  
Memory snapshots: **694**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6616 d1=-24.0 d12=-1.0 z=-5.017361139099455
- **PERSISTENT_DOWN** `interconnector_net` value=-6616 d1=-24.0 d12=-1.0 z=-5.017361139099455
- **ACCELERATION** `interconnector_net` value=-6616 d1=-24.0 d12=-1.0 z=-5.017361139099455
- **ROBUST_OUTLIER** `interconnector_net` value=-6616 d1=-24.0 d12=-1.0 z=-5.017361139099455
- **PERSISTENT_DOWN** `ccgt_gen` value=4401 d1=-43.0 d12=-331.0 z=-3.65194621489726
- **ROBUST_OUTLIER** `ccgt_gen` value=4401 d1=-43.0 d12=-331.0 z=-3.65194621489726
- **PERSISTENT_DOWN** `thermal_base` value=7712 d1=-50.0 d12=-341.0 z=-3.639018161446469
- **ROBUST_OUTLIER** `thermal_base` value=7712 d1=-50.0 d12=-341.0 z=-3.639018161446469
- **PERSISTENT_UP** `ind_demand` value=-1.175e+04 d1=16.0 d12=16.0 z=2.83285695
- **ACCELERATION** `ind_demand` value=-1.175e+04 d1=16.0 d12=16.0 z=2.83285695
- **CHANGE_POINT** `ps_gen` value=-288 d1=-44.0 d12=-41.0 z=-0.7216718628775836
- **PERSISTENT_UP** `margin` value=3.451e+04 d1=0.0 d12=3.0 z=1.6437565018518518
- **ACCELERATION** `margin` value=3.451e+04 d1=0.0 d12=3.0 z=1.6437565018518518

## Nearest historical live analogues

- `2026-09-16T23:51:11.579176Z` distance=0.054 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:55:23.288978Z` distance=0.054 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:59:33.595851Z` distance=0.054 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:33:53.959539Z` distance=0.056 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:38:04.318669Z` distance=0.056 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

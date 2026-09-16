# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T23:29:42.981994Z`  
Memory snapshots: **674**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=-5742 d1=14.0 d12=-11026.0 z=-4.6290771057500715
- **CHANGE_POINT** `ccgt_gen` value=5559 d1=-197.0 d12=-3065.0 z=-2.760326202910959
- **CHANGE_POINT** `thermal_base` value=8870 d1=-199.0 d12=-3065.0 z=-2.749429174544419
- **REVERSAL** `interconnector_net` value=-5742 d1=14.0 d12=-11026.0 z=-4.6290771057500715
- **ROBUST_OUTLIER** `interconnector_net` value=-5742 d1=14.0 d12=-11026.0 z=-4.6290771057500715
- **CHANGE_POINT** `ps_gen` value=-250 d1=-1.0 d12=-478.0 z=-1.7517422955010225
- **CHANGE_POINT** `margin` value=3.448e+04 d1=0.0 d12=76.0 z=1.5138547722222222
- **CHANGE_POINT** `ind_generation` value=2.572e+04 d1=0.0 d12=-37.0 z=1.2069816578947368
- **PERSISTENT_DOWN** `ccgt_gen` value=5559 d1=-197.0 d12=-3065.0 z=-2.760326202910959
- **PERSISTENT_DOWN** `thermal_base` value=8870 d1=-199.0 d12=-3065.0 z=-2.749429174544419
- **CHANGE_POINT** `imbalance` value=6603 d1=0.0 d12=-37.0 z=0.3118608521505376
- **PERSISTENT_UP** `margin` value=3.448e+04 d1=0.0 d12=76.0 z=1.5138547722222222
- **PERSISTENT_UP** `wind_gen` value=1.106e+04 d1=59.0 d12=932.0 z=1.49337457579023
- **PERSISTENT_DOWN** `ind_generation` value=2.572e+04 d1=0.0 d12=-37.0 z=1.2069816578947368
- **PERSISTENT_DOWN** `nuclear_gen` value=3311 d1=-2.0 d12=0.0 z=0.67448975

## Nearest historical live analogues

- `2026-09-16T19:55:48.790004Z` distance=0.049 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -56.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T19:59:58.980702Z` distance=0.049 → {'next30m_imbalance_delta': 5.0, 'next30m_margin_delta': -56.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T19:51:38.678882Z` distance=0.051 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T15:24:31.150364Z` distance=0.130 → {'next30m_imbalance_delta': -339.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T15:28:42.332391Z` distance=0.130 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -80.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

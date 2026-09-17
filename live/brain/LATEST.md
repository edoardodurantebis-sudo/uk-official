# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T19:52:34.655680Z`  
Memory snapshots: **964**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=2.65e+04 d1=0.0 d12=-17.0 z=-27.81193905319149
- **ROBUST_OUTLIER** `ind_demand` value=-1.116e+04 d1=0.0 d12=0.0 z=26.97959
- **ROBUST_OUTLIER** `imbalance` value=9684 d1=0.0 d12=-17.0 z=-4.136585871835443
- **CHANGE_POINT** `wind_gen` value=1.604e+04 d1=35.0 d12=785.0 z=1.528743564408662
- **CHANGE_POINT** `ps_gen` value=500 d1=-1.0 d12=223.0 z=0.9562145373941674
- **CHANGE_POINT** `biomass_gen` value=2632 d1=36.0 d12=-410.0 z=-0.6778370936724566
- **PERSISTENT_UP** `wind_gen` value=1.604e+04 d1=35.0 d12=785.0 z=1.528743564408662
- **PERSISTENT_UP** `interconnector_net` value=-310 d1=1.0 d12=198.0 z=-1.3872857107461023
- **PERSISTENT_UP** `nuclear_gen` value=3325 d1=1.0 d12=1.0 z=1.1562681428571426
- **ACCELERATION** `nuclear_gen` value=3325 d1=1.0 d12=1.0 z=1.1562681428571426
- **REVERSAL** `ps_gen` value=500 d1=-1.0 d12=223.0 z=0.9562145373941674
- **REVERSAL** `biomass_gen` value=2632 d1=36.0 d12=-410.0 z=-0.6778370936724566
- **PERSISTENT_DOWN** `thermal_base` value=9080 d1=-294.0 d12=-1151.0 z=0.44637678891786176
- **PERSISTENT_DOWN** `ccgt_gen` value=5755 d1=-295.0 d12=-1152.0 z=0.4441244713200629
- **REVERSAL** `margin` value=3.652e+04 d1=26.0 d12=-65.0 z=-0.41659661029411765

## Nearest historical live analogues

- `2026-09-17T18:57:56.745109Z` distance=0.131 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:24:17.596696Z` distance=0.191 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:28:33.240401Z` distance=0.191 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:32:46.898081Z` distance=0.191 → {'next30m_imbalance_delta': 19.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:37:00.976118Z` distance=0.191 → {'next30m_imbalance_delta': 19.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

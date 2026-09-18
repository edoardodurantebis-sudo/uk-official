# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T03:23:46.426083Z`  
Memory snapshots: **1071**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.817e+04 d1=-14.0 d12=-46.0 z=11.292488185567011
- **PERSISTENT_DOWN** `margin` value=3.817e+04 d1=-14.0 d12=-46.0 z=11.292488185567011
- **ROBUST_OUTLIER** `margin` value=3.817e+04 d1=-14.0 d12=-46.0 z=11.292488185567011
- **CHANGE_POINT** `wind_gen` value=1.363e+04 d1=11.0 d12=-522.0 z=-1.511422057591623
- **CHANGE_POINT** `interconnector_net` value=-6209 d1=-14.0 d12=-812.0 z=-1.0432701743674369
- **PERSISTENT_DOWN** `ind_demand` value=-1.125e+04 d1=-6.0 d12=-45.0 z=-2.0234692499999998
- **REVERSAL** `wind_gen` value=1.363e+04 d1=11.0 d12=-522.0 z=-1.511422057591623
- **PERSISTENT_DOWN** `interconnector_net` value=-6209 d1=-14.0 d12=-812.0 z=-1.0432701743674369
- **PERSISTENT_UP** `biomass_gen` value=1790 d1=36.0 d12=8.0 z=-0.9701564897260274
- **ACCELERATION** `biomass_gen` value=1790 d1=36.0 d12=8.0 z=-0.9701564897260274
- **PERSISTENT_DOWN** `imbalance` value=1.017e+04 d1=-3.0 d12=-7.0 z=0.5983376814516129
- **ACCELERATION** `imbalance` value=1.017e+04 d1=-3.0 d12=-7.0 z=0.5983376814516129
- **PERSISTENT_DOWN** `ind_generation` value=2.698e+04 d1=-3.0 d12=-7.0 z=0.5983376814516129
- **ACCELERATION** `ind_generation` value=2.698e+04 d1=-3.0 d12=-7.0 z=0.5983376814516129
- **PERSISTENT_UP** `thermal_base` value=6805 d1=27.0 d12=165.0 z=-0.581085044274301

## Nearest historical live analogues

- `2026-09-18T02:20:05.299900Z` distance=0.040 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T02:24:14.818372Z` distance=0.060 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T02:28:26.564879Z` distance=0.060 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': -32.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:54:53.197905Z` distance=0.660 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:59:03.576885Z` distance=0.660 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T07:32:11.773694Z`  
Memory snapshots: **1417**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **PERSISTENT_DOWN** `ind_demand` value=-1.208e+04 d1=0.0 d12=-1215.0 z=-161.47284615
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-1215.0 z=-161.47284615
- **CHANGE_POINT** `margin` value=3.703e+04 d1=0.0 d12=-1257.0 z=-26.4948004921875
- **ROBUST_OUTLIER** `margin` value=3.703e+04 d1=0.0 d12=-1257.0 z=-26.4948004921875
- **CHANGE_POINT** `ps_gen` value=-420 d1=0.0 d12=10.0 z=20.7405598125
- **CHANGE_POINT** `interconnector_net` value=-3937 d1=2033.0 d12=4389.0 z=18.85056924549098
- **ROBUST_OUTLIER** `ps_gen` value=-420 d1=0.0 d12=10.0 z=20.7405598125
- **PERSISTENT_UP** `interconnector_net` value=-3937 d1=2033.0 d12=4389.0 z=18.85056924549098
- **ACCELERATION** `interconnector_net` value=-3937 d1=2033.0 d12=4389.0 z=18.85056924549098
- **ROBUST_OUTLIER** `interconnector_net` value=-3937 d1=2033.0 d12=4389.0 z=18.85056924549098
- **CHANGE_POINT** `imbalance` value=8458 d1=0.0 d12=-1267.0 z=-2.902867278481013
- **CHANGE_POINT** `biomass_gen` value=1005 d1=-22.0 d12=272.0 z=1.0791836
- **CHANGE_POINT** `wind_gen` value=1.574e+04 d1=-9.0 d12=-97.0 z=-0.9506337888235293
- **PERSISTENT_DOWN** `imbalance` value=8458 d1=0.0 d12=-1267.0 z=-2.902867278481013
- **PERSISTENT_DOWN** `nuclear_gen` value=3333 d1=-5.0 d12=-2.0 z=-1.1241495833333335

## Nearest historical live analogues

- `2026-09-18T08:34:36.525091Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:38:47.543853Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:43:00.251145Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:47:16.640835Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:51:27.785288Z` distance=1.030 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

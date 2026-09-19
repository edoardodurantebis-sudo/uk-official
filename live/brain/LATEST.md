# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T07:36:22.503128Z`  
Memory snapshots: **1418**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.208e+04 d1=0.0 d12=-1215.0 z=-161.47284615
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-1215.0 z=-161.47284615
- **CHANGE_POINT** `margin` value=3.703e+04 d1=0.0 d12=-1257.0 z=-26.4948004921875
- **ROBUST_OUTLIER** `margin` value=3.703e+04 d1=0.0 d12=-1257.0 z=-26.4948004921875
- **CHANGE_POINT** `interconnector_net` value=-3927 d1=10.0 d12=4374.0 z=18.877602902805613
- **PERSISTENT_DOWN** `ps_gen` value=-421 d1=-1.0 d12=-120.0 z=20.571937375
- **ROBUST_OUTLIER** `ps_gen` value=-421 d1=-1.0 d12=-120.0 z=20.571937375
- **PERSISTENT_UP** `interconnector_net` value=-3927 d1=10.0 d12=4374.0 z=18.877602902805613
- **ACCELERATION** `interconnector_net` value=-3927 d1=10.0 d12=4374.0 z=18.877602902805613
- **ROBUST_OUTLIER** `interconnector_net` value=-3927 d1=10.0 d12=4374.0 z=18.877602902805613
- **CHANGE_POINT** `imbalance` value=8458 d1=0.0 d12=-1267.0 z=-2.902867278481013
- **REVERSAL** `biomass_gen` value=954 d1=-51.0 d12=161.0 z=0.79252545625
- **ACCELERATION** `nuclear_gen` value=3335 d1=2.0 d12=2.0 z=-0.6744897499999999
- **REVERSAL** `thermal_base` value=6530 d1=13.0 d12=-65.0 z=-0.2390596582278481
- **REVERSAL** `ccgt_gen` value=3195 d1=11.0 d12=-67.0 z=-0.2259293294621027

## Nearest historical live analogues

- `2026-09-18T08:34:36.525091Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:38:47.543853Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:43:00.251145Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:47:16.640835Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:51:27.785288Z` distance=1.030 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

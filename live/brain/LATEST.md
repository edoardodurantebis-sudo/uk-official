# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T07:40:34.209614Z`  
Memory snapshots: **1419**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.208e+04 d1=0.0 d12=-1215.0 z=-161.47284615
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-1215.0 z=-161.47284615
- **CHANGE_POINT** `margin` value=3.703e+04 d1=0.0 d12=-1004.0 z=-26.4948004921875
- **ROBUST_OUTLIER** `margin` value=3.703e+04 d1=0.0 d12=-1004.0 z=-26.4948004921875
- **PERSISTENT_DOWN** `ps_gen` value=-421 d1=0.0 d12=-120.0 z=23.41442989285714
- **ROBUST_OUTLIER** `ps_gen` value=-421 d1=0.0 d12=-120.0 z=23.41442989285714
- **CHANGE_POINT** `interconnector_net` value=-3903 d1=24.0 d12=4398.0 z=18.94248368036072
- **PERSISTENT_UP** `interconnector_net` value=-3903 d1=24.0 d12=4398.0 z=18.94248368036072
- **ROBUST_OUTLIER** `interconnector_net` value=-3903 d1=24.0 d12=4398.0 z=18.94248368036072
- **CHANGE_POINT** `imbalance` value=8458 d1=0.0 d12=-1267.0 z=-2.902867278481013
- **CHANGE_POINT** `ind_generation` value=2.687e+04 d1=0.0 d12=-45.0 z=-0.11138362844036698
- **PERSISTENT_DOWN** `wind_gen` value=1.569e+04 d1=-13.0 d12=-194.0 z=-1.150600161764706
- **REVERSAL** `nuclear_gen` value=3334 d1=-1.0 d12=1.0 z=-0.8993196666666666
- **ACCELERATION** `nuclear_gen` value=3334 d1=-1.0 d12=1.0 z=-0.8993196666666666
- **REVERSAL** `biomass_gen` value=902 d1=-52.0 d12=109.0 z=0.5002465645833333

## Nearest historical live analogues

- `2026-09-18T08:34:36.525091Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:38:47.543853Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:43:00.251145Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:47:16.640835Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:51:27.785288Z` distance=1.030 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

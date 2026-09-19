# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T07:44:44.985777Z`  
Memory snapshots: **1420**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.208e+04 d1=0.0 d12=-726.0 z=-94.98402714705882
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-726.0 z=-94.98402714705882
- **CHANGE_POINT** `margin` value=3.703e+04 d1=0.0 d12=-1004.0 z=-26.4948004921875
- **ROBUST_OUTLIER** `margin` value=3.703e+04 d1=0.0 d12=-1004.0 z=-26.4948004921875
- **CHANGE_POINT** `interconnector_net` value=-3903 d1=0.0 d12=4392.0 z=18.94248368036072
- **PERSISTENT_DOWN** `ps_gen` value=-421 d1=0.0 d12=-122.0 z=20.4033149375
- **ROBUST_OUTLIER** `ps_gen` value=-421 d1=0.0 d12=-122.0 z=20.4033149375
- **PERSISTENT_UP** `interconnector_net` value=-3903 d1=0.0 d12=4392.0 z=18.94248368036072
- **ROBUST_OUTLIER** `interconnector_net` value=-3903 d1=0.0 d12=4392.0 z=18.94248368036072
- **CHANGE_POINT** `imbalance` value=8458 d1=0.0 d12=-1020.0 z=-2.902867278481013
- **CHANGE_POINT** `ind_generation` value=2.687e+04 d1=0.0 d12=-38.0 z=-0.13415265745856353
- **PERSISTENT_DOWN** `wind_gen` value=1.569e+04 d1=0.0 d12=-203.0 z=-1.149330534
- **PERSISTENT_UP** `nuclear_gen` value=3334 d1=0.0 d12=2.0 z=-0.8993196666666666
- **ACCELERATION** `nuclear_gen` value=3334 d1=0.0 d12=2.0 z=-0.8993196666666666
- **ACCELERATION** `biomass_gen` value=902 d1=0.0 d12=53.0 z=0.5002465645833333

## Nearest historical live analogues

- `2026-09-18T08:34:36.525091Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:38:47.543853Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:43:00.251145Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:47:16.640835Z` distance=1.028 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:51:27.785288Z` distance=1.030 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

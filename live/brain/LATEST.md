# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T00:26:37.805564Z`  
Memory snapshots: **41**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2919 d1=34.0 d12=232.0 z=8.781592039215687
- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=0.0 z=8.733777532051281
- **PERSISTENT_UP** `biomass_gen` value=2919 d1=34.0 d12=232.0 z=8.781592039215687
- **ROBUST_OUTLIER** `biomass_gen` value=2919 d1=34.0 d12=232.0 z=8.781592039215687
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=0.0 z=8.733777532051281
- **CHANGE_POINT** `margin` value=3.27e+04 d1=0.0 d12=216.0 z=3.035203875
- **CHANGE_POINT** `imbalance` value=264 d1=0.0 d12=77.0 z=2.727284641304348
- **CHANGE_POINT** `ind_generation` value=2.075e+04 d1=0.0 d12=76.0 z=2.727284641304348
- **CHANGE_POINT** `wind_gen` value=1.19e+04 d1=37.0 d12=-390.0 z=-1.0608272333860758
- **ROBUST_OUTLIER** `margin` value=3.27e+04 d1=0.0 d12=216.0 z=3.035203875
- **CHANGE_POINT** `ind_demand` value=-1.227e+04 d1=0.0 d12=-1.0 z=-0.8993196666666666
- **PERSISTENT_UP** `imbalance` value=264 d1=0.0 d12=77.0 z=2.727284641304348
- **ACCELERATION** `imbalance` value=264 d1=0.0 d12=77.0 z=2.727284641304348
- **PERSISTENT_UP** `ind_generation` value=2.075e+04 d1=0.0 d12=76.0 z=2.727284641304348
- **ACCELERATION** `ind_generation` value=2.075e+04 d1=0.0 d12=76.0 z=2.727284641304348

## Nearest historical live analogues

- `2026-09-14T23:28:00.797408Z` distance=7.648 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 4389.0}
- `2026-09-14T23:23:50.457848Z` distance=7.753 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 4457.0}
- `2026-09-14T23:19:39.979677Z` distance=7.920 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 4546.0}
- `2026-09-14T22:54:28.088906Z` distance=7.941 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': -8.0}
- `2026-09-14T23:11:14.299399Z` distance=7.950 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 4544.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

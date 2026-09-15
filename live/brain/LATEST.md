# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T00:22:28.991704Z`  
Memory snapshots: **40**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=4389.0 z=8.887624357971015
- **CHANGE_POINT** `biomass_gen` value=2885 d1=30.0 d12=205.0 z=8.374914395833333
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=4389.0 z=8.887624357971015
- **PERSISTENT_UP** `biomass_gen` value=2885 d1=30.0 d12=205.0 z=8.374914395833333
- **ROBUST_OUTLIER** `biomass_gen` value=2885 d1=30.0 d12=205.0 z=8.374914395833333
- **CHANGE_POINT** `margin` value=3.27e+04 d1=-23.0 d12=216.0 z=3.035203875
- **CHANGE_POINT** `imbalance` value=264 d1=54.0 d12=77.0 z=2.727284641304348
- **CHANGE_POINT** `ind_generation` value=2.075e+04 d1=53.0 d12=76.0 z=2.727284641304348
- **CHANGE_POINT** `ind_demand` value=-1.227e+04 d1=-1.0 d12=-1.0 z=-1.3489795
- **CHANGE_POINT** `wind_gen` value=1.186e+04 d1=-64.0 d12=-378.0 z=-1.1455619563492063
- **REVERSAL** `margin` value=3.27e+04 d1=-23.0 d12=216.0 z=3.035203875
- **ROBUST_OUTLIER** `margin` value=3.27e+04 d1=-23.0 d12=216.0 z=3.035203875
- **PERSISTENT_UP** `imbalance` value=264 d1=54.0 d12=77.0 z=2.727284641304348
- **ACCELERATION** `imbalance` value=264 d1=54.0 d12=77.0 z=2.727284641304348
- **PERSISTENT_UP** `ind_generation` value=2.075e+04 d1=53.0 d12=76.0 z=2.727284641304348

## Nearest historical live analogues

- `2026-09-14T23:23:50.457848Z` distance=7.886 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 4457.0}
- `2026-09-14T23:19:39.979677Z` distance=8.089 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 4546.0}
- `2026-09-14T22:54:28.088906Z` distance=8.109 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': -8.0}
- `2026-09-14T23:11:14.299399Z` distance=8.118 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 4544.0}
- `2026-09-14T23:15:27.902002Z` distance=8.118 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 4544.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

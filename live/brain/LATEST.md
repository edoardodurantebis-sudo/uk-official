# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T11:06:18.746524Z`  
Memory snapshots: **1809**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=546.0 z=47.792416571428575
- **PERSISTENT_UP** `ind_demand` value=-1.181e+04 d1=0.0 d12=546.0 z=47.792416571428575
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=546.0 z=47.792416571428575
- **CHANGE_POINT** `ind_generation` value=1.536e+04 d1=0.0 d12=-654.0 z=18.3798456875
- **CHANGE_POINT** `margin` value=3.579e+04 d1=0.0 d12=-3495.0 z=-17.385728332089553
- **PERSISTENT_DOWN** `ind_generation` value=1.536e+04 d1=0.0 d12=-654.0 z=18.3798456875
- **ROBUST_OUTLIER** `ind_generation` value=1.536e+04 d1=0.0 d12=-654.0 z=18.3798456875
- **ROBUST_OUTLIER** `margin` value=3.579e+04 d1=0.0 d12=-3495.0 z=-17.385728332089553
- **ROBUST_OUTLIER** `residual_proxy` value=1.824e+04 d1=0.0 d12=1031.0 z=6.057839618012422
- **CHANGE_POINT** `imbalance` value=-5746 d1=0.0 d12=-1592.0 z=2.530567383211679
- **PERSISTENT_DOWN** `wind_gen` value=1.37e+04 d1=-97.0 d12=-253.0 z=-2.983913604643338
- **ACCELERATION** `wind_gen` value=1.37e+04 d1=-97.0 d12=-253.0 z=-2.983913604643338
- **CHANGE_POINT** `biomass_gen` value=585 d1=-2.0 d12=-9.0 z=-0.6952788176369863
- **CHANGE_POINT** `ps_gen` value=-718 d1=79.0 d12=-133.0 z=0.6187979357798166
- **PERSISTENT_DOWN** `imbalance` value=-5746 d1=0.0 d12=-1592.0 z=2.530567383211679

## Nearest historical live analogues

- `2026-09-20T04:50:36.902238Z` distance=0.754 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:54:47.005275Z` distance=0.754 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:58:57.948602Z` distance=0.754 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:03:10.294370Z` distance=0.754 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:07:21.689505Z` distance=0.754 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 161.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

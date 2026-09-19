# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T09:47:44.451200Z`  
Memory snapshots: **1449**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.893e+04 d1=0.0 d12=1130.0 z=293.065796375
- **CHANGE_POINT** `ind_demand` value=-1.322e+04 d1=0.0 d12=-1130.0 z=-92.64315095588235
- **ROBUST_OUTLIER** `ind_demand` value=-1.322e+04 d1=0.0 d12=-1130.0 z=-92.64315095588235
- **CHANGE_POINT** `margin` value=3.648e+04 d1=0.0 d12=-1114.0 z=-14.452176716463413
- **ROBUST_OUTLIER** `margin` value=3.648e+04 d1=0.0 d12=-1114.0 z=-14.452176716463413
- **CHANGE_POINT** `ps_gen` value=-701 d1=-1.0 d12=-4.0 z=-4.524702072916667
- **CHANGE_POINT** `imbalance` value=7771 d1=0.0 d12=-1161.0 z=-4.320277685741088
- **ROBUST_OUTLIER** `ind_generation` value=2.67e+04 d1=0.0 d12=-32.0 z=-4.621503842592593
- **PERSISTENT_DOWN** `ps_gen` value=-701 d1=-1.0 d12=-4.0 z=-4.524702072916667
- **ACCELERATION** `ps_gen` value=-701 d1=-1.0 d12=-4.0 z=-4.524702072916667
- **ROBUST_OUTLIER** `ps_gen` value=-701 d1=-1.0 d12=-4.0 z=-4.524702072916667
- **ROBUST_OUTLIER** `imbalance` value=7771 d1=0.0 d12=-1161.0 z=-4.320277685741088
- **PERSISTENT_DOWN** `interconnector_net` value=-1019 d1=-7.0 d12=-1093.0 z=3.7564328530509576
- **ROBUST_OUTLIER** `interconnector_net` value=-1019 d1=-7.0 d12=-1093.0 z=3.7564328530509576
- **PERSISTENT_DOWN** `biomass_gen` value=477 d1=0.0 d12=-7.0 z=-3.484863708333333

## Nearest historical live analogues

- `2026-09-18T09:21:34.020078Z` distance=0.927 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:25:46.604177Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:30:05.383319Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:34:18.274964Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:39:05.140398Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

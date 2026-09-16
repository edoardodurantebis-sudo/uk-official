# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T08:17:56.653795Z`  
Memory snapshots: **495**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.632e+04 d1=0.0 d12=0.0 z=-50.628886859375
- **ROBUST_OUTLIER** `margin` value=3.632e+04 d1=0.0 d12=0.0 z=-50.628886859375
- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=0.0 z=-23.710908903846153
- **CHANGE_POINT** `wind_gen` value=6995 d1=-42.0 d12=-1008.0 z=-1.6389334044396318
- **PERSISTENT_UP** `biomass_gen` value=3242 d1=2.0 d12=13.0 z=3.37244875
- **ROBUST_OUTLIER** `biomass_gen` value=3242 d1=2.0 d12=13.0 z=3.37244875
- **CHANGE_POINT** `ps_gen` value=230 d1=0.0 d12=8.0 z=1.3489795
- **CHANGE_POINT** `ind_generation` value=2.644e+04 d1=0.0 d12=0.0 z=0.67448975
- **PERSISTENT_UP** `interconnector_net` value=1.01e+04 d1=0.0 d12=3149.0 z=2.482937651474531
- **PERSISTENT_DOWN** `wind_gen` value=6995 d1=-42.0 d12=-1008.0 z=-1.6389334044396318
- **REVERSAL** `thermal_base` value=1.183e+04 d1=-114.0 d12=382.0 z=1.3139823903301886
- **ACCELERATION** `thermal_base` value=1.183e+04 d1=-114.0 d12=382.0 z=1.3139823903301886
- **REVERSAL** `ccgt_gen` value=8502 d1=-118.0 d12=378.0 z=1.3070846899901014
- **ACCELERATION** `ccgt_gen` value=8502 d1=-118.0 d12=378.0 z=1.3070846899901014
- **PERSISTENT_DOWN** `residual_proxy` value=-492 d1=-1356.0 d12=-107.0 z=-1.134173847133758

## Nearest historical live analogues

- `2026-09-16T07:23:21.620957Z` distance=0.074 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:19:10.764986Z` distance=0.511 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:54:08.413156Z` distance=0.729 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:58:18.248300Z` distance=0.729 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T07:02:28.186045Z` distance=0.729 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T09:17:10.091657Z`  
Memory snapshots: **1442**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.78e+04 d1=0.0 d12=0.0 z=102.522442
- **ROBUST_OUTLIER** `ind_demand` value=-1.209e+04 d1=0.0 d12=-5.0 z=-50.797509296875
- **ROBUST_OUTLIER** `interconnector_net` value=-483 d1=32.0 d12=1258.0 z=20.70833419111111
- **CHANGE_POINT** `ps_gen` value=-423 d1=2.0 d12=0.0 z=15.917958100000002
- **PERSISTENT_UP** `ps_gen` value=-423 d1=2.0 d12=0.0 z=15.917958100000002
- **ACCELERATION** `ps_gen` value=-423 d1=2.0 d12=0.0 z=15.917958100000002
- **ROBUST_OUTLIER** `ps_gen` value=-423 d1=2.0 d12=0.0 z=15.917958100000002
- **ROBUST_OUTLIER** `margin` value=3.759e+04 d1=0.0 d12=-23.0 z=-7.31987236885246
- **CHANGE_POINT** `wind_gen` value=1.493e+04 d1=-43.0 d12=-328.0 z=-4.618058173371648
- **PERSISTENT_DOWN** `wind_gen` value=1.493e+04 d1=-43.0 d12=-328.0 z=-4.618058173371648
- **ROBUST_OUTLIER** `wind_gen` value=1.493e+04 d1=-43.0 d12=-328.0 z=-4.618058173371648
- **CHANGE_POINT** `nuclear_gen` value=3328 d1=-3.0 d12=-11.0 z=-2.248299166666667
- **ROBUST_OUTLIER** `ind_generation` value=2.673e+04 d1=0.0 d12=-59.0 z=-3.8221085833333337
- **PERSISTENT_DOWN** `biomass_gen` value=476 d1=-1.0 d12=-214.0 z=-3.5250119077380955
- **ROBUST_OUTLIER** `biomass_gen` value=476 d1=-1.0 d12=-214.0 z=-3.5250119077380955

## Nearest historical live analogues

- `2026-09-19T08:22:32.362085Z` distance=0.042 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -115.0}
- `2026-09-19T08:18:19.086544Z` distance=0.190 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -115.0}
- `2026-09-19T07:23:46.754706Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:27:59.733660Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:32:11.773694Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

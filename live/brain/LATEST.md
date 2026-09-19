# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T09:08:46.152718Z`  
Memory snapshots: **1440**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.78e+04 d1=0.0 d12=0.0 z=102.522442
- **ROBUST_OUTLIER** `ind_demand` value=-1.209e+04 d1=0.0 d12=-8.0 z=-50.797509296875
- **REVERSAL** `interconnector_net` value=-396 d1=-435.0 d12=1344.0 z=21.338774057488656
- **ROBUST_OUTLIER** `interconnector_net` value=-396 d1=-435.0 d12=1344.0 z=21.338774057488656
- **CHANGE_POINT** `ps_gen` value=-680 d1=17.0 d12=-256.0 z=-18.75081505
- **REVERSAL** `ps_gen` value=-680 d1=17.0 d12=-256.0 z=-18.75081505
- **ROBUST_OUTLIER** `ps_gen` value=-680 d1=17.0 d12=-256.0 z=-18.75081505
- **ROBUST_OUTLIER** `margin` value=3.759e+04 d1=0.0 d12=566.0 z=-14.5647630390625
- **CHANGE_POINT** `wind_gen` value=1.507e+04 d1=-20.0 d12=-226.0 z=-3.8776749125475285
- **CHANGE_POINT** `nuclear_gen` value=3327 d1=-2.0 d12=-9.0 z=-2.4731290833333333
- **PERSISTENT_DOWN** `wind_gen` value=1.507e+04 d1=-20.0 d12=-226.0 z=-3.8776749125475285
- **ROBUST_OUTLIER** `wind_gen` value=1.507e+04 d1=-20.0 d12=-226.0 z=-3.8776749125475285
- **ROBUST_OUTLIER** `ind_generation` value=2.673e+04 d1=0.0 d12=-135.0 z=-3.8221085833333337
- **PERSISTENT_DOWN** `biomass_gen` value=476 d1=-2.0 d12=-215.0 z=-3.7638193456790123
- **ROBUST_OUTLIER** `biomass_gen` value=476 d1=-2.0 d12=-215.0 z=-3.7638193456790123

## Nearest historical live analogues

- `2026-09-19T07:23:46.754706Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:27:59.733660Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:32:11.773694Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:36:22.503128Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:40:34.209614Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

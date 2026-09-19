# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T09:00:21.792182Z`  
Memory snapshots: **1438**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.78e+04 d1=0.0 d12=-1758.0 z=102.522442
- **PERSISTENT_DOWN** `ind_demand` value=-1.209e+04 d1=0.0 d12=-8.0 z=-50.797509296875
- **ROBUST_OUTLIER** `ind_demand` value=-1.209e+04 d1=0.0 d12=-8.0 z=-50.797509296875
- **PERSISTENT_UP** `interconnector_net` value=74 d1=0.0 d12=2244.0 z=23.352073132515823
- **ROBUST_OUTLIER** `interconnector_net` value=74 d1=0.0 d12=2244.0 z=23.352073132515823
- **CHANGE_POINT** `ps_gen` value=-697 d1=0.0 d12=-8.0 z=-21.0440802
- **PERSISTENT_DOWN** `ps_gen` value=-697 d1=0.0 d12=-8.0 z=-21.0440802
- **ACCELERATION** `ps_gen` value=-697 d1=0.0 d12=-8.0 z=-21.0440802
- **ROBUST_OUTLIER** `ps_gen` value=-697 d1=0.0 d12=-8.0 z=-21.0440802
- **ROBUST_OUTLIER** `margin` value=3.759e+04 d1=0.0 d12=566.0 z=-14.5647630390625
- **CHANGE_POINT** `wind_gen` value=1.514e+04 d1=0.0 d12=-396.0 z=-3.427003068014706
- **PERSISTENT_DOWN** `biomass_gen` value=484 d1=0.0 d12=-270.0 z=-5.241117073770492
- **ACCELERATION** `biomass_gen` value=484 d1=0.0 d12=-270.0 z=-5.241117073770492
- **ROBUST_OUTLIER** `biomass_gen` value=484 d1=0.0 d12=-270.0 z=-5.241117073770492
- **CHANGE_POINT** `residual_proxy` value=8953 d1=0.0 d12=-3235.0 z=-3.094968789556962

## Nearest historical live analogues

- `2026-09-19T07:23:46.754706Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:27:59.733660Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:32:11.773694Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:36:22.503128Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:40:34.209614Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T09:04:34.188608Z`  
Memory snapshots: **1439**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.78e+04 d1=0.0 d12=-1758.0 z=102.522442
- **ROBUST_OUTLIER** `ind_demand` value=-1.209e+04 d1=0.0 d12=-8.0 z=-50.797509296875
- **CHANGE_POINT** `ps_gen` value=-697 d1=0.0 d12=-105.0 z=-21.0440802
- **REVERSAL** `interconnector_net` value=39 d1=-35.0 d12=1778.0 z=22.94106946879875
- **ROBUST_OUTLIER** `interconnector_net` value=39 d1=-35.0 d12=1778.0 z=22.94106946879875
- **PERSISTENT_DOWN** `ps_gen` value=-697 d1=0.0 d12=-105.0 z=-21.0440802
- **ROBUST_OUTLIER** `ps_gen` value=-697 d1=0.0 d12=-105.0 z=-21.0440802
- **ROBUST_OUTLIER** `margin` value=3.759e+04 d1=0.0 d12=566.0 z=-14.5647630390625
- **CHANGE_POINT** `wind_gen` value=1.509e+04 d1=-50.0 d12=-337.0 z=-3.71976063619403
- **PERSISTENT_DOWN** `biomass_gen` value=478 d1=-6.0 d12=-231.0 z=-4.147200489864865
- **ROBUST_OUTLIER** `biomass_gen` value=478 d1=-6.0 d12=-231.0 z=-4.147200489864865
- **ROBUST_OUTLIER** `ind_generation` value=2.673e+04 d1=0.0 d12=-135.0 z=-3.8221085833333337
- **ROBUST_OUTLIER** `wind_gen` value=1.509e+04 d1=-50.0 d12=-337.0 z=-3.71976063619403
- **ROBUST_OUTLIER** `residual_proxy` value=8953 d1=0.0 d12=-3235.0 z=-3.094968789556962
- **PERSISTENT_DOWN** `nuclear_gen` value=3329 d1=-2.0 d12=-2.0 z=-2.02346925

## Nearest historical live analogues

- `2026-09-19T07:23:46.754706Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:27:59.733660Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:32:11.773694Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:36:22.503128Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:40:34.209614Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

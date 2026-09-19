# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T09:12:57.512519Z`  
Memory snapshots: **1441**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.78e+04 d1=0.0 d12=0.0 z=102.522442
- **ROBUST_OUTLIER** `ind_demand` value=-1.209e+04 d1=0.0 d12=-5.0 z=-50.797509296875
- **REVERSAL** `interconnector_net` value=-515 d1=-119.0 d12=1224.0 z=20.64438257037037
- **ROBUST_OUTLIER** `interconnector_net` value=-515 d1=-119.0 d12=1224.0 z=20.64438257037037
- **CHANGE_POINT** `ps_gen` value=-425 d1=255.0 d12=-2.0 z=17.461790194444447
- **REVERSAL** `ps_gen` value=-425 d1=255.0 d12=-2.0 z=17.461790194444447
- **ACCELERATION** `ps_gen` value=-425 d1=255.0 d12=-2.0 z=17.461790194444447
- **ROBUST_OUTLIER** `ps_gen` value=-425 d1=255.0 d12=-2.0 z=17.461790194444447
- **ROBUST_OUTLIER** `margin` value=3.759e+04 d1=0.0 d12=-23.0 z=-10.489478525862069
- **CHANGE_POINT** `wind_gen` value=1.497e+04 d1=-99.0 d12=-399.0 z=-4.370078076045627
- **PERSISTENT_DOWN** `wind_gen` value=1.497e+04 d1=-99.0 d12=-399.0 z=-4.370078076045627
- **ROBUST_OUTLIER** `wind_gen` value=1.497e+04 d1=-99.0 d12=-399.0 z=-4.370078076045627
- **ROBUST_OUTLIER** `ind_generation` value=2.673e+04 d1=0.0 d12=-59.0 z=-3.8221085833333337
- **CHANGE_POINT** `nuclear_gen` value=3331 d1=4.0 d12=-7.0 z=-1.5738094166666665
- **REVERSAL** `biomass_gen` value=477 d1=1.0 d12=-214.0 z=-3.573189747023809

## Nearest historical live analogues

- `2026-09-19T08:18:19.086544Z` distance=0.190 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -115.0}
- `2026-09-19T07:23:46.754706Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:27:59.733660Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:32:11.773694Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:36:22.503128Z` distance=0.222 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

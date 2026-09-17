# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T02:10:10.548653Z`  
Memory snapshots: **712**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2022 d1=0.0 d12=-972.0 z=-319.16854969999997
- **PERSISTENT_DOWN** `biomass_gen` value=2022 d1=0.0 d12=-972.0 z=-319.16854969999997
- **ROBUST_OUTLIER** `biomass_gen` value=2022 d1=0.0 d12=-972.0 z=-319.16854969999997
- **CHANGE_POINT** `ind_demand` value=-1.153e+04 d1=0.0 d12=220.0 z=31.835916200000003
- **ROBUST_OUTLIER** `ind_demand` value=-1.153e+04 d1=0.0 d12=220.0 z=31.835916200000003
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `ccgt_gen` value=4089 d1=0.0 d12=-496.0 z=-1.9126907119462024
- **CHANGE_POINT** `thermal_base` value=7403 d1=0.0 d12=-501.0 z=-1.9042412638888888
- **CHANGE_POINT** `ps_gen` value=-581 d1=0.0 d12=-269.0 z=-1.034430725592417
- **PERSISTENT_UP** `interconnector_net` value=-6584 d1=0.0 d12=84.0 z=-3.0034411997922437
- **ACCELERATION** `interconnector_net` value=-6584 d1=0.0 d12=84.0 z=-3.0034411997922437
- **ROBUST_OUTLIER** `interconnector_net` value=-6584 d1=0.0 d12=84.0 z=-3.0034411997922437
- **CHANGE_POINT** `margin` value=3.456e+04 d1=0.0 d12=69.0 z=0.8528502613981763
- **PERSISTENT_UP** `wind_gen` value=1.349e+04 d1=0.0 d12=849.0 z=1.2876448253765274

## Nearest historical live analogues

- `2026-09-17T00:54:40.714610Z` distance=0.483 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:58:51.888099Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:03:09.320399Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:07:19.944210Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:11:31.123687Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

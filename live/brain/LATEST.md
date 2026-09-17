# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T01:53:23.110162Z`  
Memory snapshots: **708**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2244 d1=-145.0 d12=-958.0 z=-324.42956975
- **PERSISTENT_DOWN** `biomass_gen` value=2244 d1=-145.0 d12=-958.0 z=-324.42956975
- **ROBUST_OUTLIER** `biomass_gen` value=2244 d1=-145.0 d12=-958.0 z=-324.42956975
- **PERSISTENT_UP** `ind_demand` value=-1.153e+04 d1=120.0 d12=220.0 z=64.34632215
- **ACCELERATION** `ind_demand` value=-1.153e+04 d1=120.0 d12=220.0 z=64.34632215
- **ROBUST_OUTLIER** `ind_demand` value=-1.153e+04 d1=120.0 d12=220.0 z=64.34632215
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `thermal_base` value=7368 d1=-9.0 d12=-754.0 z=-2.428522690879665
- **CHANGE_POINT** `ccgt_gen` value=4057 d1=-8.0 d12=-751.0 z=-2.42457266026616
- **ROBUST_OUTLIER** `interconnector_net` value=-6663 d1=0.0 d12=110.0 z=-3.3065222603811755
- **CHANGE_POINT** `ps_gen` value=-364 d1=-56.0 d12=-54.0 z=-0.7595948596986818
- **PERSISTENT_DOWN** `thermal_base` value=7368 d1=-9.0 d12=-754.0 z=-2.428522690879665
- **PERSISTENT_DOWN** `ccgt_gen` value=4057 d1=-8.0 d12=-751.0 z=-2.42457266026616
- **PERSISTENT_UP** `wind_gen` value=1.312e+04 d1=53.0 d12=835.0 z=1.1796585437033968

## Nearest historical live analogues

- `2026-09-17T00:54:40.714610Z` distance=0.483 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:58:51.888099Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:50:29.902043Z` distance=0.518 → {'next30m_imbalance_delta': -43.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:03:44.260171Z` distance=0.518 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:07:55.537385Z` distance=0.518 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

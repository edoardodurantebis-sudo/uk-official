# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T13:05:25.405882Z`  
Memory snapshots: **1209**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=-813.0 z=-8.175909537162163
- **ROBUST_OUTLIER** `residual_proxy` value=9368 d1=0.0 d12=813.0 z=4.35206481547619
- **PERSISTENT_UP** `wind_gen` value=1.499e+04 d1=0.0 d12=704.0 z=4.178921488295318
- **ROBUST_OUTLIER** `wind_gen` value=1.499e+04 d1=0.0 d12=704.0 z=4.178921488295318
- **CHANGE_POINT** `thermal_base` value=5772 d1=0.0 d12=2.0 z=-0.6755163706240487
- **CHANGE_POINT** `ccgt_gen` value=2434 d1=0.0 d12=1.0 z=-0.67448975
- **CHANGE_POINT** `ps_gen` value=-711 d1=0.0 d12=12.0 z=-0.6517029341216216
- **PERSISTENT_DOWN** `biomass_gen` value=1035 d1=0.0 d12=-3.0 z=-0.8942827438900204
- **ACCELERATION** `biomass_gen` value=1035 d1=0.0 d12=-3.0 z=-0.8942827438900204
- **PERSISTENT_UP** `interconnector_net` value=5816 d1=0.0 d12=502.0 z=0.6879512050945379
- **ACCELERATION** `thermal_base` value=5772 d1=0.0 d12=2.0 z=-0.6755163706240487
- **PERSISTENT_UP** `ccgt_gen` value=2434 d1=0.0 d12=1.0 z=-0.67448975
- **ACCELERATION** `ccgt_gen` value=2434 d1=0.0 d12=1.0 z=-0.67448975
- **ACCELERATION** `nuclear_gen` value=3338 d1=0.0 d12=1.0 z=0.6744897499999999
- **PERSISTENT_DOWN** `ind_demand` value=-1.074e+04 d1=0.0 d12=-1.0 z=0.6738091347124117

## Nearest historical live analogues

- `2026-09-18T11:53:30.754266Z` distance=0.518 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:57:41.506573Z` distance=0.518 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:01:54.588988Z` distance=0.518 → {'next30m_imbalance_delta': -33.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:06:06.838501Z` distance=0.518 → {'next30m_imbalance_delta': -33.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 813.0}
- `2026-09-18T12:10:18.933990Z` distance=0.518 → {'next30m_imbalance_delta': -33.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 813.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

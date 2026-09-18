# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T13:01:14.855580Z`  
Memory snapshots: **1208**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=-813.0 z=-8.175909537162163
- **ROBUST_OUTLIER** `residual_proxy` value=9368 d1=0.0 d12=813.0 z=4.35206481547619
- **ROBUST_OUTLIER** `wind_gen` value=1.499e+04 d1=44.0 d12=1107.0 z=4.178921488295318
- **CHANGE_POINT** `biomass_gen` value=1035 d1=-2.0 d12=-5.0 z=-1.0128427680722891
- **CHANGE_POINT** `thermal_base` value=5772 d1=1.0 d12=-1.0 z=-0.6754679802393039
- **CHANGE_POINT** `margin` value=3.81e+04 d1=0.0 d12=0.0 z=0.67448975
- **CHANGE_POINT** `ccgt_gen` value=2434 d1=5.0 d12=2.0 z=-0.6740041562275018
- **CHANGE_POINT** `ps_gen` value=-711 d1=5.0 d12=8.0 z=-0.6506039409780775
- **ACCELERATION** `ind_generation` value=2.561e+04 d1=0.0 d12=-10.0 z=-2.4617321751152073
- **PERSISTENT_DOWN** `biomass_gen` value=1035 d1=-2.0 d12=-5.0 z=-1.0128427680722891
- **ACCELERATION** `biomass_gen` value=1035 d1=-2.0 d12=-5.0 z=-1.0128427680722891
- **PERSISTENT_UP** `interconnector_net` value=5816 d1=129.0 d12=524.0 z=0.7156965192926045
- **REVERSAL** `thermal_base` value=5772 d1=1.0 d12=-1.0 z=-0.6754679802393039
- **ACCELERATION** `thermal_base` value=5772 d1=1.0 d12=-1.0 z=-0.6754679802393039
- **PERSISTENT_DOWN** `nuclear_gen` value=3338 d1=-4.0 d12=-3.0 z=0.6744897499999999

## Nearest historical live analogues

- `2026-09-18T11:53:30.754266Z` distance=0.518 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:57:41.506573Z` distance=0.518 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:01:54.588988Z` distance=0.518 → {'next30m_imbalance_delta': -33.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:06:06.838501Z` distance=0.518 → {'next30m_imbalance_delta': -33.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 813.0}
- `2026-09-18T11:24:04.514292Z` distance=0.518 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

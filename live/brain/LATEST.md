# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T21:47:14.880667Z`  
Memory snapshots: **345**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=8309 d1=-281.0 d12=-2893.0 z=-8.04363284255079
- **CHANGE_POINT** `ccgt_gen` value=4980 d1=-285.0 d12=-2899.0 z=-7.997845387612108
- **PERSISTENT_DOWN** `thermal_base` value=8309 d1=-281.0 d12=-2893.0 z=-8.04363284255079
- **ROBUST_OUTLIER** `thermal_base` value=8309 d1=-281.0 d12=-2893.0 z=-8.04363284255079
- **PERSISTENT_DOWN** `ccgt_gen` value=4980 d1=-285.0 d12=-2899.0 z=-7.997845387612108
- **ROBUST_OUTLIER** `ccgt_gen` value=4980 d1=-285.0 d12=-2899.0 z=-7.997845387612108
- **PERSISTENT_DOWN** `wind_gen` value=1.215e+04 d1=-125.0 d12=-140.0 z=4.8740083837209305
- **ROBUST_OUTLIER** `wind_gen` value=1.215e+04 d1=-125.0 d12=-140.0 z=4.8740083837209305
- **CHANGE_POINT** `ps_gen` value=-256 d1=0.0 d12=8.0 z=-0.6762647230263158
- **CHANGE_POINT** `interconnector_net` value=1313 d1=0.0 d12=1150.0 z=0.5818768845980127
- **PERSISTENT_UP** `nuclear_gen` value=3329 d1=4.0 d12=6.0 z=2.360714125
- **PERSISTENT_UP** `ps_gen` value=-256 d1=0.0 d12=8.0 z=-0.6762647230263158
- **PERSISTENT_UP** `interconnector_net` value=1313 d1=0.0 d12=1150.0 z=0.5818768845980127
- **REVERSAL** `biomass_gen` value=3258 d1=3.0 d12=-5.0 z=0.08126382530120482
- **ACCELERATION** `biomass_gen` value=3258 d1=3.0 d12=-5.0 z=0.08126382530120482

## Nearest historical live analogues

- `2026-09-15T20:52:49.933053Z` distance=0.003 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:22:50.211969Z` distance=0.016 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:27:39.367678Z` distance=0.016 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:31:49.811988Z` distance=0.016 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:36:00.984640Z` distance=0.016 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

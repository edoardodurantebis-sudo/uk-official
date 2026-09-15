# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T07:46:47.163241Z`  
Memory snapshots: **146**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=6484 d1=19.0 d12=7145.0 z=2.655470407928515
- **CHANGE_POINT** `thermal_base` value=6340 d1=-86.0 d12=-988.0 z=-1.9132161177884617
- **CHANGE_POINT** `ccgt_gen` value=3022 d1=-86.0 d12=-983.0 z=-1.9036693673965936
- **CHANGE_POINT** `wind_gen` value=1.255e+04 d1=14.0 d12=-935.0 z=-1.8310667251602564
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=0.0 d12=144.0 z=3.1074706339285716
- **CHANGE_POINT** `margin` value=3.413e+04 d1=0.0 d12=158.0 z=0.67448975
- **REVERSAL** `biomass_gen` value=3244 d1=-10.0 d12=8.0 z=2.662459539473684
- **ACCELERATION** `biomass_gen` value=3244 d1=-10.0 d12=8.0 z=2.662459539473684
- **PERSISTENT_UP** `interconnector_net` value=6484 d1=19.0 d12=7145.0 z=2.655470407928515
- **CHANGE_POINT** `imbalance` value=-454 d1=0.0 d12=249.0 z=0.0
- **CHANGE_POINT** `ind_generation` value=2.003e+04 d1=0.0 d12=249.0 z=0.0
- **PERSISTENT_DOWN** `thermal_base` value=6340 d1=-86.0 d12=-988.0 z=-1.9132161177884617
- **PERSISTENT_DOWN** `ccgt_gen` value=3022 d1=-86.0 d12=-983.0 z=-1.9036693673965936
- **PERSISTENT_DOWN** `residual_proxy` value=1664 d1=-1211.0 d12=-1211.0 z=-1.8917879426229507
- **ACCELERATION** `residual_proxy` value=1664 d1=-1211.0 d12=-1211.0 z=-1.8917879426229507

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=1.113 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=1.113 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=1.113 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=1.113 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=1.113 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

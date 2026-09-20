# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T13:38:01.505393Z`  
Memory snapshots: **1845**  
Current physical regime: **BALANCED**

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.182e+04 d1=0.0 d12=0.0 z=4.438871733108108
- **CHANGE_POINT** `wind_gen` value=1.067e+04 d1=-328.0 d12=-1430.0 z=-2.162741573199809
- **CHANGE_POINT** `ps_gen` value=-392 d1=249.0 d12=283.0 z=2.149443989299611
- **CHANGE_POINT** `interconnector_net` value=-2242 d1=0.0 d12=1510.0 z=1.839798128146453
- **PERSISTENT_DOWN** `wind_gen` value=1.067e+04 d1=-328.0 d12=-1430.0 z=-2.162741573199809
- **PERSISTENT_UP** `ps_gen` value=-392 d1=249.0 d12=283.0 z=2.149443989299611
- **ACCELERATION** `ps_gen` value=-392 d1=249.0 d12=283.0 z=2.149443989299611
- **CHANGE_POINT** `imbalance` value=-5731 d1=0.0 d12=-11.0 z=0.0010672306170886076
- **CHANGE_POINT** `ind_generation` value=1.537e+04 d1=0.0 d12=-11.0 z=0.001053890234375
- **PERSISTENT_UP** `interconnector_net` value=-2242 d1=0.0 d12=1510.0 z=1.839798128146453
- **ACCELERATION** `interconnector_net` value=-2242 d1=0.0 d12=1510.0 z=1.839798128146453
- **PERSISTENT_UP** `biomass_gen` value=585 d1=1.0 d12=2.0 z=-0.67448975
- **ACCELERATION** `biomass_gen` value=585 d1=1.0 d12=2.0 z=-0.67448975
- **REVERSAL** `thermal_base` value=5739 d1=-4.0 d12=23.0 z=-0.02086050773195876
- **ACCELERATION** `thermal_base` value=5739 d1=-4.0 d12=23.0 z=-0.02086050773195876

## Nearest historical live analogues

- `2026-09-20T12:34:29.670242Z` distance=0.003 → {'next30m_imbalance_delta': -11.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T12:38:40.894482Z` distance=0.003 → {'next30m_imbalance_delta': -11.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T12:42:54.105261Z` distance=0.003 → {'next30m_imbalance_delta': -11.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T12:26:00.831842Z` distance=0.014 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 73.0}
- `2026-09-20T12:30:16.008395Z` distance=0.014 → {'next30m_imbalance_delta': -11.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 73.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

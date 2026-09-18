# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T14:08:23.149664Z`  
Memory snapshots: **1224**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `wind_gen` value=1.603e+04 d1=135.0 d12=1118.0 z=4.5649516756314314
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-6.528097223214285
- **PERSISTENT_UP** `wind_gen` value=1.603e+04 d1=135.0 d12=1118.0 z=4.5649516756314314
- **ROBUST_OUTLIER** `wind_gen` value=1.603e+04 d1=135.0 d12=1118.0 z=4.5649516756314314
- **CHANGE_POINT** `biomass_gen` value=1210 d1=52.0 d12=175.0 z=0.800956578125
- **CHANGE_POINT** `thermal_base` value=5823 d1=6.0 d12=18.0 z=-0.619473107256356
- **PERSISTENT_UP** `nuclear_gen` value=3339 d1=2.0 d12=7.0 z=0.8993196666666666
- **ACCELERATION** `nuclear_gen` value=3339 d1=2.0 d12=7.0 z=0.8993196666666666
- **PERSISTENT_UP** `biomass_gen` value=1210 d1=52.0 d12=175.0 z=0.800956578125
- **PERSISTENT_UP** `ps_gen` value=-512 d1=206.0 d12=190.0 z=0.7742867028061226
- **ACCELERATION** `ps_gen` value=-512 d1=206.0 d12=190.0 z=0.7742867028061226
- **PERSISTENT_DOWN** `interconnector_net` value=5875 d1=-632.0 d12=-159.0 z=0.6902383432288193
- **ACCELERATION** `interconnector_net` value=5875 d1=-632.0 d12=-159.0 z=0.6902383432288193
- **PERSISTENT_UP** `thermal_base` value=5823 d1=6.0 d12=18.0 z=-0.619473107256356
- **PERSISTENT_UP** `ccgt_gen` value=2484 d1=4.0 d12=11.0 z=-0.6155945951143452

## Nearest historical live analogues

- `2026-09-18T12:57:04.108111Z` distance=0.037 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:01:14.855580Z` distance=0.037 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:05:25.405882Z` distance=0.037 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:09:36.028376Z` distance=0.037 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:13:45.560848Z` distance=0.037 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

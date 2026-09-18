# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T13:59:56.236821Z`  
Memory snapshots: **1222**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `wind_gen` value=1.569e+04 d1=0.0 d12=677.0 z=4.908037080833333
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-6.528097223214285
- **PERSISTENT_UP** `wind_gen` value=1.569e+04 d1=0.0 d12=677.0 z=4.908037080833333
- **ROBUST_OUTLIER** `wind_gen` value=1.569e+04 d1=0.0 d12=677.0 z=4.908037080833333
- **CHANGE_POINT** `ccgt_gen` value=2472 d1=0.0 d12=30.0 z=-0.6480862366548042
- **CHANGE_POINT** `thermal_base` value=5810 d1=0.0 d12=25.0 z=-0.6477049584837545
- **CHANGE_POINT** `biomass_gen` value=1102 d1=0.0 d12=66.0 z=-0.2691909764573991
- **PERSISTENT_UP** `interconnector_net` value=6531 d1=0.0 d12=561.0 z=1.2557678646833015
- **PERSISTENT_UP** `margin` value=3.819e+04 d1=0.0 d12=88.0 z=0.8495785346607669
- **PERSISTENT_DOWN** `ind_generation` value=2.56e+04 d1=0.0 d12=-11.0 z=-0.8131698855140187
- **ACCELERATION** `ind_generation` value=2.56e+04 d1=0.0 d12=-11.0 z=-0.8131698855140187
- **PERSISTENT_DOWN** `ps_gen` value=-714 d1=0.0 d12=-4.0 z=-0.6645707830882354
- **ACCELERATION** `ps_gen` value=-714 d1=0.0 d12=-4.0 z=-0.6645707830882354
- **PERSISTENT_UP** `ccgt_gen` value=2472 d1=0.0 d12=30.0 z=-0.6480862366548042
- **ACCELERATION** `ccgt_gen` value=2472 d1=0.0 d12=30.0 z=-0.6480862366548042

## Nearest historical live analogues

- `2026-09-18T12:57:04.108111Z` distance=0.037 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:01:14.855580Z` distance=0.037 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:05:25.405882Z` distance=0.037 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:31:54.164710Z` distance=0.037 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:36:05.963399Z` distance=0.037 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

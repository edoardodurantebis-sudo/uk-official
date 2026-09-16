# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T11:37:14.795574Z`  
Memory snapshots: **542**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **ROBUST_OUTLIER** `ps_gen` value=-5 d1=0.0 d12=0.0 z=-20.45952241666667
- **CHANGE_POINT** `ind_generation` value=2.48e+04 d1=0.0 d12=-1211.0 z=-8.088523906746031
- **ROBUST_OUTLIER** `ind_generation` value=2.48e+04 d1=0.0 d12=-1211.0 z=-8.088523906746031
- **CHANGE_POINT** `interconnector_net` value=1.119e+04 d1=25.0 d12=874.0 z=2.4873920830550915
- **CHANGE_POINT** `imbalance` value=6020 d1=0.0 d12=647.0 z=-1.736148842900302
- **ROBUST_OUTLIER** `wind_forecast` value=1.976e+04 d1=0.0 d12=0.0 z=3.2392692452229297
- **CHANGE_POINT** `thermal_base` value=9942 d1=-120.0 d12=519.0 z=-0.778775937095826
- **CHANGE_POINT** `ccgt_gen` value=6621 d1=-124.0 d12=515.0 z=-0.7705053497058824
- **CHANGE_POINT** `margin` value=3.544e+04 d1=0.0 d12=1211.0 z=-0.5019196300167224
- **PERSISTENT_UP** `interconnector_net` value=1.119e+04 d1=25.0 d12=874.0 z=2.4873920830550915
- **ACCELERATION** `interconnector_net` value=1.119e+04 d1=25.0 d12=874.0 z=2.4873920830550915
- **PERSISTENT_DOWN** `wind_gen` value=4166 d1=-16.0 d12=-715.0 z=-1.8970431519323672
- **PERSISTENT_UP** `nuclear_gen` value=3321 d1=4.0 d12=4.0 z=-1.5738094166666665
- **ACCELERATION** `nuclear_gen` value=3321 d1=4.0 d12=4.0 z=-1.5738094166666665
- **REVERSAL** `thermal_base` value=9942 d1=-120.0 d12=519.0 z=-0.778775937095826

## Nearest historical live analogues

- `2026-09-16T06:49:55.430272Z` distance=1.591 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:20:37.850603Z` distance=1.605 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:24:49.356241Z` distance=1.605 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:29:00.658838Z` distance=1.605 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:33:09.371452Z` distance=1.605 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

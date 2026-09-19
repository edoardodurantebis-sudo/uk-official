# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T13:05:41.840763Z`  
Memory snapshots: **1496**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.679e+04 d1=0.0 d12=40.0 z=-36.61779052595629
- **PERSISTENT_UP** `ind_generation` value=1.679e+04 d1=0.0 d12=40.0 z=-36.61779052595629
- **ROBUST_OUTLIER** `ind_generation` value=1.679e+04 d1=0.0 d12=40.0 z=-36.61779052595629
- **CHANGE_POINT** `imbalance` value=-3220 d1=0.0 d12=40.0 z=-6.164444495228216
- **PERSISTENT_UP** `imbalance` value=-3220 d1=0.0 d12=40.0 z=-6.164444495228216
- **ROBUST_OUTLIER** `imbalance` value=-3220 d1=0.0 d12=40.0 z=-6.164444495228216
- **CHANGE_POINT** `wind_gen` value=1.507e+04 d1=-10.0 d12=-572.0 z=-3.5396776136363637
- **CHANGE_POINT** `residual_proxy` value=1.285e+04 d1=0.0 d12=1.0 z=2.954730270344828
- **PERSISTENT_DOWN** `wind_gen` value=1.507e+04 d1=-10.0 d12=-572.0 z=-3.5396776136363637
- **ROBUST_OUTLIER** `wind_gen` value=1.507e+04 d1=-10.0 d12=-572.0 z=-3.5396776136363637
- **ROBUST_OUTLIER** `demand_forecast` value=1.951e+04 d1=0.0 d12=0.0 z=3.2718281479508198
- **CHANGE_POINT** `interconnector_net` value=-2512 d1=-352.0 d12=-908.0 z=-1.0635959133362294
- **PERSISTENT_DOWN** `nuclear_gen` value=3321 d1=-7.0 d12=-8.0 z=-2.6979589999999996
- **ACCELERATION** `nuclear_gen` value=3321 d1=-7.0 d12=-8.0 z=-2.6979589999999996
- **CHANGE_POINT** `thermal_base` value=6452 d1=11.0 d12=241.0 z=-0.10799414536516853

## Nearest historical live analogues

- `2026-09-19T11:54:18.195696Z` distance=0.085 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:58:27.853052Z` distance=0.085 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T12:02:38.156173Z` distance=0.085 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T12:06:51.129462Z` distance=0.085 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 1.0}
- `2026-09-19T12:11:04.601097Z` distance=0.085 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 1.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

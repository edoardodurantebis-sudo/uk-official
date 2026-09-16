# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T11:33:04.123714Z`  
Memory snapshots: **541**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **ROBUST_OUTLIER** `ps_gen` value=-5 d1=0.0 d12=0.0 z=-21.969094714285713
- **CHANGE_POINT** `ind_generation` value=2.48e+04 d1=0.0 d12=-1211.0 z=-8.088523906746031
- **ROBUST_OUTLIER** `ind_generation` value=2.48e+04 d1=0.0 d12=-1211.0 z=-8.088523906746031
- **CHANGE_POINT** `interconnector_net` value=1.116e+04 d1=336.0 d12=874.0 z=2.4283762089257506
- **CHANGE_POINT** `ind_demand` value=-1.177e+04 d1=0.0 d12=3343.0 z=1.3611324684684685
- **ROBUST_OUTLIER** `wind_forecast` value=1.976e+04 d1=0.0 d12=0.0 z=3.2392692452229297
- **CHANGE_POINT** `thermal_base` value=1.006e+04 d1=-88.0 d12=607.0 z=-0.6836098348030569
- **CHANGE_POINT** `ccgt_gen` value=6745 d1=-88.0 d12=607.0 z=-0.6713194103995299
- **CHANGE_POINT** `margin` value=3.544e+04 d1=0.0 d12=1211.0 z=-0.5019196300167224
- **PERSISTENT_UP** `interconnector_net` value=1.116e+04 d1=336.0 d12=874.0 z=2.4283762089257506
- **ACCELERATION** `interconnector_net` value=1.116e+04 d1=336.0 d12=874.0 z=2.4283762089257506
- **PERSISTENT_DOWN** `wind_gen` value=4182 d1=-51.0 d12=-731.0 z=-2.1499585371603622
- **PERSISTENT_UP** `imbalance` value=6020 d1=0.0 d12=647.0 z=-1.736148842900302
- **REVERSAL** `thermal_base` value=1.006e+04 d1=-88.0 d12=607.0 z=-0.6836098348030569
- **ACCELERATION** `thermal_base` value=1.006e+04 d1=-88.0 d12=607.0 z=-0.6836098348030569

## Nearest historical live analogues

- `2026-09-16T06:49:55.430272Z` distance=1.608 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:20:37.850603Z` distance=1.622 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:24:49.356241Z` distance=1.622 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:29:00.658838Z` distance=1.622 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:33:09.371452Z` distance=1.622 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

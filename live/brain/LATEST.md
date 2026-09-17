# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T19:35:51.852732Z`  
Memory snapshots: **960**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=2.65e+04 d1=0.0 d12=2.0 z=-48.91299742592592
- **CHANGE_POINT** `ind_demand` value=-1.116e+04 d1=0.0 d12=94.0 z=26.97959
- **ROBUST_OUTLIER** `ind_demand` value=-1.116e+04 d1=0.0 d12=94.0 z=26.97959
- **ROBUST_OUTLIER** `imbalance` value=9684 d1=0.0 d12=2.0 z=-4.4767828152542375
- **CHANGE_POINT** `margin` value=3.649e+04 d1=0.0 d12=-91.0 z=-0.545723525
- **PERSISTENT_UP** `residual_proxy` value=-2399 d1=0.0 d12=191.0 z=2.2649532345679013
- **ACCELERATION** `residual_proxy` value=-2399 d1=0.0 d12=191.0 z=2.2649532345679013
- **PERSISTENT_UP** `wind_gen` value=1.576e+04 d1=172.0 d12=710.0 z=1.4051206185064935
- **PERSISTENT_UP** `interconnector_net` value=-310 d1=0.0 d12=133.0 z=-1.3872857107461023
- **ACCELERATION** `interconnector_net` value=-310 d1=0.0 d12=133.0 z=-1.3872857107461023
- **PERSISTENT_DOWN** `thermal_base` value=9797 d1=-86.0 d12=-619.0 z=1.2705116330445545
- **PERSISTENT_DOWN** `ccgt_gen` value=6477 d1=-80.0 d12=-615.0 z=1.2686432518610422
- **PERSISTENT_UP** `ps_gen` value=480 d1=53.0 d12=198.0 z=0.9301125070356473
- **PERSISTENT_DOWN** `nuclear_gen` value=3320 d1=-6.0 d12=-4.0 z=0.7708454285714286
- **ACCELERATION** `nuclear_gen` value=3320 d1=-6.0 d12=-4.0 z=0.7708454285714286

## Nearest historical live analogues

- `2026-09-17T18:24:17.596696Z` distance=0.193 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:28:33.240401Z` distance=0.193 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:32:46.898081Z` distance=0.193 → {'next30m_imbalance_delta': 19.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:37:00.976118Z` distance=0.193 → {'next30m_imbalance_delta': 19.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:41:13.121776Z` distance=0.193 → {'next30m_imbalance_delta': 19.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

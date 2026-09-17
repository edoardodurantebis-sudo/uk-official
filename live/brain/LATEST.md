# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T19:40:05.244843Z`  
Memory snapshots: **961**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=2.65e+04 d1=0.0 d12=2.0 z=-48.91299742592592
- **CHANGE_POINT** `ind_demand` value=-1.116e+04 d1=0.0 d12=94.0 z=26.97959
- **ROBUST_OUTLIER** `ind_demand` value=-1.116e+04 d1=0.0 d12=94.0 z=26.97959
- **ROBUST_OUTLIER** `imbalance` value=9684 d1=0.0 d12=2.0 z=-4.4767828152542375
- **CHANGE_POINT** `wind_gen` value=1.576e+04 d1=0.0 d12=688.0 z=1.3501272420589903
- **CHANGE_POINT** `ps_gen` value=480 d1=0.0 d12=200.0 z=0.9303525284037558
- **PERSISTENT_UP** `residual_proxy` value=-2399 d1=0.0 d12=191.0 z=2.2649532345679013
- **PERSISTENT_UP** `interconnector_net` value=-310 d1=0.0 d12=158.0 z=-1.3872857107461023
- **PERSISTENT_UP** `wind_gen` value=1.576e+04 d1=0.0 d12=688.0 z=1.3501272420589903
- **PERSISTENT_DOWN** `ccgt_gen` value=6477 d1=0.0 d12=-610.0 z=1.0584932003682357
- **PERSISTENT_DOWN** `thermal_base` value=9797 d1=0.0 d12=-609.0 z=1.0545865786213469
- **PERSISTENT_UP** `ps_gen` value=480 d1=0.0 d12=200.0 z=0.9303525284037558
- **ACCELERATION** `nuclear_gen` value=3320 d1=0.0 d12=1.0 z=0.67448975
- **PERSISTENT_DOWN** `biomass_gen` value=2747 d1=0.0 d12=-184.0 z=-0.2851104015700483
- **ACCELERATION** `biomass_gen` value=2747 d1=0.0 d12=-184.0 z=-0.2851104015700483

## Nearest historical live analogues

- `2026-09-17T18:24:17.596696Z` distance=0.193 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:28:33.240401Z` distance=0.193 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:32:46.898081Z` distance=0.193 → {'next30m_imbalance_delta': 19.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:37:00.976118Z` distance=0.193 → {'next30m_imbalance_delta': 19.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:41:13.121776Z` distance=0.193 → {'next30m_imbalance_delta': 19.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

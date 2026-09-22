# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T00:30:29.689236Z`  
Memory snapshots: **2339**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.238e+04 d1=0.0 d12=-1.0 z=-11.562681428571429
- **ROBUST_OUTLIER** `ind_demand` value=-1.238e+04 d1=0.0 d12=-1.0 z=-11.562681428571429
- **CHANGE_POINT** `imbalance` value=-1960 d1=0.0 d12=56.0 z=3.098156251666667
- **CHANGE_POINT** `ind_generation` value=1.95e+04 d1=0.0 d12=56.0 z=3.098156251666667
- **PERSISTENT_UP** `imbalance` value=-1960 d1=0.0 d12=56.0 z=3.098156251666667
- **ROBUST_OUTLIER** `imbalance` value=-1960 d1=0.0 d12=56.0 z=3.098156251666667
- **PERSISTENT_UP** `ind_generation` value=1.95e+04 d1=0.0 d12=56.0 z=3.098156251666667
- **ROBUST_OUTLIER** `ind_generation` value=1.95e+04 d1=0.0 d12=56.0 z=3.098156251666667
- **CHANGE_POINT** `biomass_gen` value=3005 d1=0.0 d12=0.0 z=-0.337244875
- **PERSISTENT_DOWN** `thermal_base` value=1.488e+04 d1=0.0 d12=-144.0 z=-1.324730201398136
- **PERSISTENT_DOWN** `ccgt_gen` value=1.122e+04 d1=0.0 d12=-148.0 z=-1.2694831382138516
- **PERSISTENT_UP** `interconnector_net` value=3685 d1=0.0 d12=338.0 z=-1.0035258247971603
- **PERSISTENT_DOWN** `ps_gen` value=-285 d1=0.0 d12=-3.0 z=-0.9438440855155483
- **PERSISTENT_UP** `nuclear_gen` value=3653 d1=0.0 d12=4.0 z=0.7012022153465346
- **ACCELERATION** `biomass_gen` value=3005 d1=0.0 d12=0.0 z=-0.337244875

## Nearest historical live analogues

- `2026-09-21T23:31:08.892013Z` distance=0.266 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 51.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T23:35:23.461931Z` distance=0.266 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 51.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T22:52:30.792878Z` distance=0.277 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T22:56:44.809172Z` distance=0.277 → {'next30m_imbalance_delta': 477.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -67.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T23:00:57.207752Z` distance=0.277 → {'next30m_imbalance_delta': 477.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -67.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

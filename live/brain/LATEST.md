# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T02:33:15.620122Z`  
Memory snapshots: **1346**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.831e+04 d1=0.0 d12=1189.0 z=6.338578373493975
- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=1189.0 z=6.338578373493975
- **CHANGE_POINT** `ccgt_gen` value=3094 d1=-24.0 d12=-455.0 z=-1.9627044076576576
- **CHANGE_POINT** `thermal_base` value=6442 d1=-14.0 d12=-441.0 z=-1.9382064373589165
- **CHANGE_POINT** `biomass_gen` value=1045 d1=-54.0 d12=-94.0 z=-1.6263397710280374
- **PERSISTENT_UP** `nuclear_gen` value=3348 d1=10.0 d12=14.0 z=3.37244875
- **ACCELERATION** `nuclear_gen` value=3348 d1=10.0 d12=14.0 z=3.37244875
- **ROBUST_OUTLIER** `nuclear_gen` value=3348 d1=10.0 d12=14.0 z=3.37244875
- **CHANGE_POINT** `ps_gen` value=-672 d1=-3.0 d12=155.0 z=-0.41269768386897404
- **PERSISTENT_UP** `ind_generation` value=2.645e+04 d1=0.0 d12=50.0 z=2.1198249285714286
- **PERSISTENT_DOWN** `ccgt_gen` value=3094 d1=-24.0 d12=-455.0 z=-1.9627044076576576
- **PERSISTENT_DOWN** `thermal_base` value=6442 d1=-14.0 d12=-441.0 z=-1.9382064373589165
- **PERSISTENT_DOWN** `biomass_gen` value=1045 d1=-54.0 d12=-94.0 z=-1.6263397710280374
- **REVERSAL** `interconnector_net` value=-1.118e+04 d1=12.0 d12=-81.0 z=-1.083512348886706
- **PERSISTENT_UP** `imbalance` value=9256 d1=0.0 d12=50.0 z=0.8602188115942029

## Nearest historical live analogues

- `2026-09-19T00:22:06.996302Z` distance=0.276 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:26:19.516071Z` distance=0.276 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:30:34.705011Z` distance=0.276 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:34:45.510432Z` distance=0.276 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:38:55.391009Z` distance=0.276 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

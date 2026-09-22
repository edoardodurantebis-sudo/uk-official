# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T06:11:17.063153Z`  
Memory snapshots: **2419**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.783e+04 d1=16.0 d12=674.0 z=4.745023186972255
- **CHANGE_POINT** `ccgt_gen` value=1.418e+04 d1=14.0 d12=683.0 z=4.701282200119474
- **PERSISTENT_UP** `thermal_base` value=1.783e+04 d1=16.0 d12=674.0 z=4.745023186972255
- **ROBUST_OUTLIER** `thermal_base` value=1.783e+04 d1=16.0 d12=674.0 z=4.745023186972255
- **PERSISTENT_UP** `ccgt_gen` value=1.418e+04 d1=14.0 d12=683.0 z=4.701282200119474
- **ROBUST_OUTLIER** `ccgt_gen` value=1.418e+04 d1=14.0 d12=683.0 z=4.701282200119474
- **CHANGE_POINT** `wind_gen` value=3477 d1=15.0 d12=38.0 z=-0.948420453065134
- **CHANGE_POINT** `imbalance` value=-3209 d1=0.0 d12=103.0 z=-0.6406398926579925
- **CHANGE_POINT** `ind_generation` value=1.825e+04 d1=0.0 d12=103.0 z=-0.6406398926579925
- **CHANGE_POINT** `ind_demand` value=-1.248e+04 d1=0.0 d12=46.0 z=-0.028103739583333332
- **PERSISTENT_UP** `interconnector_net` value=-441 d1=357.0 d12=2608.0 z=-0.9552589438195864
- **ACCELERATION** `wind_gen` value=3477 d1=15.0 d12=38.0 z=-0.948420453065134
- **ACCELERATION** `biomass_gen` value=3029 d1=0.0 d12=-1.0 z=-0.912544955882353
- **PERSISTENT_DOWN** `ps_gen` value=-174 d1=0.0 d12=-1.0 z=0.6682444745370371
- **ACCELERATION** `ps_gen` value=-174 d1=0.0 d12=-1.0 z=0.6682444745370371

## Nearest historical live analogues

- `2026-09-22T03:33:35.816390Z` distance=0.074 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:37:48.990972Z` distance=0.074 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:42:37.215255Z` distance=0.074 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:46:49.421565Z` distance=0.074 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:51:00.662974Z` distance=0.075 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

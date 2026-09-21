# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T13:05:39.062581Z`  
Memory snapshots: **2178**  
Current physical regime: **BALANCED**

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=1.0 z=14.812832586538462
- **CHANGE_POINT** `biomass_gen` value=2860 d1=-54.0 d12=-153.0 z=-12.1408155
- **PERSISTENT_DOWN** `biomass_gen` value=2860 d1=-54.0 d12=-153.0 z=-12.1408155
- **ROBUST_OUTLIER** `biomass_gen` value=2860 d1=-54.0 d12=-153.0 z=-12.1408155
- **ROBUST_OUTLIER** `ps_gen` value=228 d1=0.0 d12=0.0 z=7.001845976190476
- **ROBUST_OUTLIER** `demand_forecast` value=2.1e+04 d1=0.0 d12=0.0 z=5.481762150000001
- **CHANGE_POINT** `ccgt_gen` value=6123 d1=128.0 d12=-525.0 z=-0.9243806532663317
- **CHANGE_POINT** `margin` value=3.627e+04 d1=0.0 d12=-402.0 z=-0.9042609835164835
- **CHANGE_POINT** `thermal_base` value=9631 d1=128.0 d12=-530.0 z=-0.897295995049505
- **CHANGE_POINT** `ind_generation` value=1.826e+04 d1=0.0 d12=-234.0 z=-0.2089841911569149
- **CHANGE_POINT** `imbalance` value=-3248 d1=0.0 d12=-234.0 z=-0.1844555302230047
- **PERSISTENT_UP** `interconnector_net` value=1.144e+04 d1=1.0 d12=142.0 z=1.3936416591216216
- **ACCELERATION** `interconnector_net` value=1.144e+04 d1=1.0 d12=142.0 z=1.3936416591216216
- **ACCELERATION** `nuclear_gen` value=3508 d1=0.0 d12=-5.0 z=1.21408155
- **REVERSAL** `ccgt_gen` value=6123 d1=128.0 d12=-525.0 z=-0.9243806532663317

## Nearest historical live analogues

- `2026-09-21T11:24:15.280087Z` distance=0.101 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 182.0, 'next30m_residual_proxy_delta': -104.0}
- `2026-09-21T11:28:26.888729Z` distance=0.101 → {'next30m_imbalance_delta': 1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 178.0, 'next30m_residual_proxy_delta': -104.0}
- `2026-09-21T10:54:44.355248Z` distance=0.101 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:58:55.909932Z` distance=0.101 → {'next30m_imbalance_delta': 856.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T11:03:12.814990Z` distance=0.101 → {'next30m_imbalance_delta': 856.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

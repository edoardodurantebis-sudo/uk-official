# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T00:42:27.190881Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=2247 d1=25.0 d12=-1955.0 z=-2.749163719240838
- **CHANGE_POINT** `wind_gen` value=4243 d1=30.0 d12=593.0 z=2.327413464093357
- **ROBUST_OUTLIER** `ind_demand` value=-1.248e+04 d1=0.0 d12=2.0 z=-4.0469384999999996
- **CHANGE_POINT** `imbalance` value=-8007 d1=0.0 d12=-9.0 z=1.1506001617647057
- **CHANGE_POINT** `ind_generation` value=1.317e+04 d1=0.0 d12=-9.0 z=1.1506001617647057
- **REVERSAL** `interconnector_net` value=2247 d1=25.0 d12=-1955.0 z=-2.749163719240838
- **PERSISTENT_UP** `wind_gen` value=4243 d1=30.0 d12=593.0 z=2.327413464093357
- **PERSISTENT_DOWN** `thermal_base` value=1.356e+04 d1=-64.0 d12=-155.0 z=-2.1915744407592026
- **PERSISTENT_DOWN** `ccgt_gen` value=9818 d1=-71.0 d12=-165.0 z=-2.187325430672269
- **PERSISTENT_UP** `nuclear_gen` value=3739 d1=7.0 d12=10.0 z=0.67448975
- **ACCELERATION** `nuclear_gen` value=3739 d1=7.0 d12=10.0 z=0.67448975
- **PERSISTENT_UP** `biomass_gen` value=2910 d1=6.0 d12=1.0 z=0.17749730263157895
- **ACCELERATION** `biomass_gen` value=2910 d1=6.0 d12=1.0 z=0.17749730263157895

## Nearest historical live analogues

- `2026-09-22T23:31:03.889259Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:35:16.889434Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:39:29.907531Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:43:42.870536Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:47:55.708752Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

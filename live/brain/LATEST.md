# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T00:21:31.120572Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `wind_gen` value=4070 d1=54.0 d12=892.0 z=2.1822090538003662
- **PERSISTENT_UP** `ind_demand` value=-1.248e+04 d1=2.0 d12=0.0 z=-4.0469384999999996
- **ACCELERATION** `ind_demand` value=-1.248e+04 d1=2.0 d12=0.0 z=-4.0469384999999996
- **ROBUST_OUTLIER** `ind_demand` value=-1.248e+04 d1=2.0 d12=0.0 z=-4.0469384999999996
- **PERSISTENT_UP** `thermal_base` value=1.376e+04 d1=10.0 d12=256.0 z=-3.788800447530864
- **ROBUST_OUTLIER** `thermal_base` value=1.376e+04 d1=10.0 d12=256.0 z=-3.788800447530864
- **PERSISTENT_UP** `ccgt_gen` value=1.003e+04 d1=10.0 d12=260.0 z=-3.760941620710784
- **ROBUST_OUTLIER** `ccgt_gen` value=1.003e+04 d1=10.0 d12=260.0 z=-3.760941620710784
- **CHANGE_POINT** `imbalance` value=-8007 d1=-9.0 d12=42.0 z=1.1506001617647057
- **CHANGE_POINT** `ind_generation` value=1.317e+04 d1=-9.0 d12=42.0 z=1.1506001617647057
- **PERSISTENT_UP** `wind_gen` value=4070 d1=54.0 d12=892.0 z=2.1822090538003662
- **REVERSAL** `interconnector_net` value=3202 d1=1.0 d12=-932.0 z=-1.9243621897679952
- **REVERSAL** `imbalance` value=-8007 d1=-9.0 d12=42.0 z=1.1506001617647057
- **REVERSAL** `ind_generation` value=1.317e+04 d1=-9.0 d12=42.0 z=1.1506001617647057
- **PERSISTENT_UP** `margin` value=3.723e+04 d1=11.0 d12=1.0 z=0.7082142375

## Nearest historical live analogues

- `2026-09-22T23:22:42.187473Z` distance=0.464 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -158.0}
- `2026-09-22T23:26:53.201699Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': -158.0}
- `2026-09-22T22:19:30.437012Z` distance=0.464 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:23:43.484966Z` distance=0.464 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:27:58.503394Z` distance=0.464 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

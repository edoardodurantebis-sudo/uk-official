# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T00:34:05.411449Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=2211 d1=-990.0 d12=-1991.0 z=-2.8503784862491717
- **CHANGE_POINT** `wind_gen` value=4182 d1=39.0 d12=977.0 z=2.2960831816530427
- **ROBUST_OUTLIER** `ind_demand` value=-1.248e+04 d1=0.0 d12=0.0 z=-4.0469384999999996
- **REVERSAL** `thermal_base` value=1.366e+04 d1=-75.0 d12=93.0 z=-3.263752963180363
- **ACCELERATION** `thermal_base` value=1.366e+04 d1=-75.0 d12=93.0 z=-3.263752963180363
- **ROBUST_OUTLIER** `thermal_base` value=1.366e+04 d1=-75.0 d12=93.0 z=-3.263752963180363
- **REVERSAL** `ccgt_gen` value=9934 d1=-70.0 d12=98.0 z=-3.24213332059448
- **ACCELERATION** `ccgt_gen` value=9934 d1=-70.0 d12=98.0 z=-3.24213332059448
- **ROBUST_OUTLIER** `ccgt_gen` value=9934 d1=-70.0 d12=98.0 z=-3.24213332059448
- **CHANGE_POINT** `imbalance` value=-8007 d1=0.0 d12=42.0 z=1.1506001617647057
- **CHANGE_POINT** `ind_generation` value=1.317e+04 d1=0.0 d12=42.0 z=1.1506001617647057
- **PERSISTENT_DOWN** `interconnector_net` value=2211 d1=-990.0 d12=-1991.0 z=-2.8503784862491717
- **ACCELERATION** `interconnector_net` value=2211 d1=-990.0 d12=-1991.0 z=-2.8503784862491717
- **PERSISTENT_UP** `wind_gen` value=4182 d1=39.0 d12=977.0 z=2.2960831816530427
- **PERSISTENT_DOWN** `nuclear_gen` value=3729 d1=-5.0 d12=-5.0 z=-1.0117346249999999

## Nearest historical live analogues

- `2026-09-22T23:31:03.889259Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:35:16.889434Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:39:29.907531Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:22:42.187473Z` distance=0.464 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -158.0}
- `2026-09-22T23:26:53.201699Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': -158.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

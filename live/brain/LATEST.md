# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T00:17:19.207901Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.249e+04 d1=0.0 d12=-2.0 z=-5.395918
- **CHANGE_POINT** `wind_gen` value=4016 d1=106.0 d12=849.0 z=2.123187202020202
- **REVERSAL** `thermal_base` value=1.375e+04 d1=-5.0 d12=131.0 z=-4.0202736427414125
- **ROBUST_OUTLIER** `thermal_base` value=1.375e+04 d1=-5.0 d12=131.0 z=-4.0202736427414125
- **REVERSAL** `ccgt_gen` value=1.002e+04 d1=-7.0 d12=131.0 z=-4.019435034466019
- **ROBUST_OUTLIER** `ccgt_gen` value=1.002e+04 d1=-7.0 d12=131.0 z=-4.019435034466019
- **CHANGE_POINT** `imbalance` value=-7998 d1=0.0 d12=51.0 z=1.5076829705882353
- **CHANGE_POINT** `ind_generation` value=1.318e+04 d1=0.0 d12=51.0 z=1.5076829705882353
- **PERSISTENT_UP** `wind_gen` value=4016 d1=106.0 d12=849.0 z=2.123187202020202
- **PERSISTENT_DOWN** `interconnector_net` value=3201 d1=-2.0 d12=-1468.0 z=-1.9507108804664723
- **ACCELERATION** `biomass_gen` value=2910 d1=-5.0 d12=-6.0 z=0.20234692499999998
- **ACCELERATION** `nuclear_gen` value=3735 d1=2.0 d12=0.0 z=0.1686224375

## Nearest historical live analogues

- `2026-09-22T23:22:42.187473Z` distance=0.464 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -158.0}
- `2026-09-22T22:53:13.778957Z` distance=0.464 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:57:26.907882Z` distance=0.464 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:01:39.891099Z` distance=0.464 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:05:56.234014Z` distance=0.464 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -158.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

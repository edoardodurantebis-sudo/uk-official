# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T23:56:18.566481Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.373e+04 d1=22.0 d12=-147.0 z=-8.4505134553125
- **CHANGE_POINT** `ccgt_gen` value=1e+04 d1=19.0 d12=-139.0 z=-8.244587163919414
- **REVERSAL** `thermal_base` value=1.373e+04 d1=22.0 d12=-147.0 z=-8.4505134553125
- **ROBUST_OUTLIER** `thermal_base` value=1.373e+04 d1=22.0 d12=-147.0 z=-8.4505134553125
- **REVERSAL** `ccgt_gen` value=1e+04 d1=19.0 d12=-139.0 z=-8.244587163919414
- **ROBUST_OUTLIER** `ccgt_gen` value=1e+04 d1=19.0 d12=-139.0 z=-8.244587163919414
- **ROBUST_OUTLIER** `ind_demand` value=-1.249e+04 d1=0.0 d12=7.0 z=-5.395918
- **CHANGE_POINT** `interconnector_net` value=4200 d1=-2.0 d12=-523.0 z=-1.539062975
- **CHANGE_POINT** `imbalance` value=-7998 d1=0.0 d12=58.0 z=1.5076829705882353
- **CHANGE_POINT** `ind_generation` value=1.318e+04 d1=0.0 d12=58.0 z=1.5076829705882353
- **PERSISTENT_UP** `wind_gen` value=3731 d1=81.0 d12=686.0 z=2.867235858344114
- **ACCELERATION** `wind_gen` value=3731 d1=81.0 d12=686.0 z=2.867235858344114
- **PERSISTENT_DOWN** `interconnector_net` value=4200 d1=-2.0 d12=-523.0 z=-1.539062975
- **PERSISTENT_UP** `imbalance` value=-7998 d1=0.0 d12=58.0 z=1.5076829705882353
- **ACCELERATION** `imbalance` value=-7998 d1=0.0 d12=58.0 z=1.5076829705882353

## Nearest historical live analogues

- `2026-09-22T22:53:13.778957Z` distance=0.025 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:57:26.907882Z` distance=0.025 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:01:39.891099Z` distance=0.025 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:50:58.019212Z` distance=0.025 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:19:30.437012Z` distance=0.025 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

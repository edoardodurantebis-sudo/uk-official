# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T06:23:57.986998Z`  
Memory snapshots: **2422**  
Current physical regime: **BALANCED**

## Active patterns

- **PERSISTENT_UP** `thermal_base` value=1.787e+04 d1=12.0 d12=559.0 z=4.055858506866734
- **ROBUST_OUTLIER** `thermal_base` value=1.787e+04 d1=12.0 d12=559.0 z=4.055858506866734
- **PERSISTENT_UP** `ccgt_gen` value=1.422e+04 d1=13.0 d12=560.0 z=4.017672042633703
- **ROBUST_OUTLIER** `ccgt_gen` value=1.422e+04 d1=13.0 d12=560.0 z=4.017672042633703
- **CHANGE_POINT** `ps_gen` value=-174 d1=-2.0 d12=-26.0 z=0.6682444745370371
- **CHANGE_POINT** `imbalance` value=-3011 d1=198.0 d12=251.0 z=-0.41288549828599413
- **CHANGE_POINT** `ind_generation` value=1.845e+04 d1=198.0 d12=251.0 z=-0.41288549828599413
- **CHANGE_POINT** `ind_demand` value=-1.248e+04 d1=1.0 d12=-1.0 z=0.015685808139534883
- **PERSISTENT_DOWN** `biomass_gen` value=3024 d1=-3.0 d12=-4.0 z=-1.3093036323529412
- **PERSISTENT_DOWN** `wind_gen` value=3436 d1=-34.0 d12=-35.0 z=-1.1515053146387833
- **ACCELERATION** `wind_gen` value=3436 d1=-34.0 d12=-35.0 z=-1.1515053146387833
- **REVERSAL** `interconnector_net` value=-594 d1=-76.0 d12=1072.0 z=-0.9789216101351352
- **PERSISTENT_DOWN** `ps_gen` value=-174 d1=-2.0 d12=-26.0 z=0.6682444745370371
- **PERSISTENT_UP** `imbalance` value=-3011 d1=198.0 d12=251.0 z=-0.41288549828599413
- **ACCELERATION** `imbalance` value=-3011 d1=198.0 d12=251.0 z=-0.41288549828599413

## Nearest historical live analogues

- `2026-09-22T05:24:23.506139Z` distance=0.065 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': -696.0}
- `2026-09-22T05:28:36.987525Z` distance=0.065 → {'next30m_imbalance_delta': 53.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': -696.0}
- `2026-09-22T03:33:35.816390Z` distance=0.070 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:37:48.990972Z` distance=0.070 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:42:37.215255Z` distance=0.070 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

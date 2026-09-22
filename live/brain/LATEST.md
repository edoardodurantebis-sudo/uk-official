# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T22:36:22.598490Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.412e+04 d1=-84.0 d12=-2758.0 z=-9.131553538461539
- **CHANGE_POINT** `ccgt_gen` value=1.038e+04 d1=-82.0 d12=-2755.0 z=-9.075483120317003
- **PERSISTENT_DOWN** `thermal_base` value=1.412e+04 d1=-84.0 d12=-2758.0 z=-9.131553538461539
- **ROBUST_OUTLIER** `thermal_base` value=1.412e+04 d1=-84.0 d12=-2758.0 z=-9.131553538461539
- **PERSISTENT_DOWN** `ccgt_gen` value=1.038e+04 d1=-82.0 d12=-2755.0 z=-9.075483120317003
- **ROBUST_OUTLIER** `ccgt_gen` value=1.038e+04 d1=-82.0 d12=-2755.0 z=-9.075483120317003
- **CHANGE_POINT** `wind_gen` value=2694 d1=88.0 d12=229.0 z=1.7048126751968504
- **REVERSAL** `interconnector_net` value=5387 d1=-25.0 d12=627.0 z=-1.7986393333333333
- **ACCELERATION** `interconnector_net` value=5387 d1=-25.0 d12=627.0 z=-1.7986393333333333
- **PERSISTENT_UP** `wind_gen` value=2694 d1=88.0 d12=229.0 z=1.7048126751968504
- **ACCELERATION** `wind_gen` value=2694 d1=88.0 d12=229.0 z=1.7048126751968504
- **PERSISTENT_DOWN** `nuclear_gen` value=3737 d1=-2.0 d12=-3.0 z=1.3489794999999998
- **ACCELERATION** `nuclear_gen` value=3737 d1=-2.0 d12=-3.0 z=1.3489794999999998
- **PERSISTENT_UP** `biomass_gen` value=2915 d1=7.0 d12=3.0 z=0.498535902173913
- **ACCELERATION** `biomass_gen` value=2915 d1=7.0 d12=3.0 z=0.498535902173913

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.011 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:24:47.718083Z` distance=0.011 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:28:58.806773Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:33:11.512074Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:37:22.236065Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

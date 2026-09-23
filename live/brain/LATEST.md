# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T04:48:12.196905Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.853e+04 d1=0.0 d12=-21.0 z=54.4650473125
- **ROBUST_OUTLIER** `margin` value=3.853e+04 d1=0.0 d12=-21.0 z=54.4650473125
- **CHANGE_POINT** `nuclear_gen` value=3791 d1=15.0 d12=63.0 z=6.520067583333333
- **PERSISTENT_UP** `nuclear_gen` value=3791 d1=15.0 d12=63.0 z=6.520067583333333
- **ROBUST_OUTLIER** `nuclear_gen` value=3791 d1=15.0 d12=63.0 z=6.520067583333333
- **CHANGE_POINT** `ccgt_gen` value=7589 d1=-73.0 d12=-1435.0 z=-3.8581923971193417
- **CHANGE_POINT** `thermal_base` value=1.138e+04 d1=-58.0 d12=-1372.0 z=-3.7569449673763735
- **CHANGE_POINT** `wind_gen` value=9110 d1=-53.0 d12=1817.0 z=2.6929184413825316
- **PERSISTENT_DOWN** `ccgt_gen` value=7589 d1=-73.0 d12=-1435.0 z=-3.8581923971193417
- **ROBUST_OUTLIER** `ccgt_gen` value=7589 d1=-73.0 d12=-1435.0 z=-3.8581923971193417
- **PERSISTENT_DOWN** `thermal_base` value=1.138e+04 d1=-58.0 d12=-1372.0 z=-3.7569449673763735
- **ROBUST_OUTLIER** `thermal_base` value=1.138e+04 d1=-58.0 d12=-1372.0 z=-3.7569449673763735
- **CHANGE_POINT** `ps_gen` value=144 d1=0.0 d12=0.0 z=-1.1241495833333335
- **REVERSAL** `wind_gen` value=9110 d1=-53.0 d12=1817.0 z=2.6929184413825316
- **PERSISTENT_DOWN** `interconnector_net` value=-5629 d1=-25.0 d12=-1968.0 z=-2.1189610223623854

## Nearest historical live analogues

- `2026-09-23T03:53:29.874059Z` distance=0.020 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T03:32:33.216215Z` distance=0.024 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T03:36:43.352003Z` distance=0.024 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T03:40:54.258660Z` distance=0.024 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T03:45:06.650607Z` distance=0.024 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

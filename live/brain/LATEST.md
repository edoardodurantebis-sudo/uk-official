# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T13:53:50.893520Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-22 d1=1.0 d12=102.0 z=21.73355861111111
- **PERSISTENT_UP** `ps_gen` value=-22 d1=1.0 d12=102.0 z=21.73355861111111
- **ROBUST_OUTLIER** `ps_gen` value=-22 d1=1.0 d12=102.0 z=21.73355861111111
- **PERSISTENT_UP** `nuclear_gen` value=3734 d1=2.0 d12=8.0 z=9.87207725
- **ROBUST_OUTLIER** `nuclear_gen` value=3734 d1=2.0 d12=8.0 z=9.87207725
- **ROBUST_OUTLIER** `wind_forecast` value=1.308e+04 d1=0.0 d12=0.0 z=8.76836675
- **PERSISTENT_DOWN** `wind_gen` value=2199 d1=-57.0 d12=-273.0 z=-6.306359994699647
- **ROBUST_OUTLIER** `wind_gen` value=2199 d1=-57.0 d12=-273.0 z=-6.306359994699647
- **CHANGE_POINT** `interconnector_net` value=1.014e+04 d1=-4.0 d12=-1027.0 z=-1.9215463544444444
- **REVERSAL** `biomass_gen` value=2946 d1=2.0 d12=-21.0 z=-3.37244875
- **ROBUST_OUTLIER** `biomass_gen` value=2946 d1=2.0 d12=-21.0 z=-3.37244875
- **CHANGE_POINT** `ind_generation` value=1.406e+04 d1=-2.0 d12=-13.0 z=-0.6841585704141226
- **CHANGE_POINT** `imbalance` value=-7103 d1=-2.0 d12=-13.0 z=-0.6803114864364981
- **CHANGE_POINT** `margin` value=3.723e+04 d1=21.0 d12=25.0 z=-0.4957634380825566
- **CHANGE_POINT** `thermal_base` value=1.353e+04 d1=71.0 d12=985.0 z=0.038021429922779924

## Nearest historical live analogues

- `2026-09-22T12:54:37.550737Z` distance=0.013 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T12:58:50.504318Z` distance=0.013 → {'next30m_imbalance_delta': -11.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T12:33:23.497533Z` distance=0.091 → {'next30m_imbalance_delta': -15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 141.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T12:37:39.628217Z` distance=0.091 → {'next30m_imbalance_delta': -15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 141.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T12:41:52.346468Z` distance=0.091 → {'next30m_imbalance_delta': -15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 141.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

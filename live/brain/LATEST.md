# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T00:04:41.945935Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.249e+04 d1=0.0 d12=7.0 z=-5.395918
- **ROBUST_OUTLIER** `thermal_base` value=1.374e+04 d1=0.0 d12=-149.0 z=-4.9532188452012385
- **ROBUST_OUTLIER** `ccgt_gen` value=1e+04 d1=0.0 d12=-143.0 z=-4.9177658961213515
- **CHANGE_POINT** `imbalance` value=-7998 d1=0.0 d12=58.0 z=1.5076829705882353
- **CHANGE_POINT** `ind_generation` value=1.318e+04 d1=0.0 d12=58.0 z=1.5076829705882353
- **CHANGE_POINT** `interconnector_net` value=4019 d1=62.0 d12=-575.0 z=-1.3200841057805164
- **CHANGE_POINT** `nuclear_gen` value=3737 d1=0.0 d12=-6.0 z=0.67448975
- **PERSISTENT_UP** `wind_gen` value=3800 d1=0.0 d12=713.0 z=2.1598752055386177
- **REVERSAL** `interconnector_net` value=4019 d1=62.0 d12=-575.0 z=-1.3200841057805164
- **ACCELERATION** `interconnector_net` value=4019 d1=62.0 d12=-575.0 z=-1.3200841057805164
- **ACCELERATION** `nuclear_gen` value=3737 d1=0.0 d12=-6.0 z=0.67448975
- **PERSISTENT_DOWN** `biomass_gen` value=2905 d1=0.0 d12=-14.0 z=-0.13489795
- **PERSISTENT_UP** `frequency` value=50.12 d1=0.016999999999995907 d12=0.027999999999998693 z=None
- **PERSISTENT_UP** `frequency_abs_dev` value=0.117 d1=0.016999999999995907 d12=0.027999999999998693 z=None

## Nearest historical live analogues

- `2026-09-22T22:53:13.778957Z` distance=0.464 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:57:26.907882Z` distance=0.464 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:01:39.891099Z` distance=0.464 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:05:56.234014Z` distance=0.464 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -158.0}
- `2026-09-22T23:10:06.870136Z` distance=0.464 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -158.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

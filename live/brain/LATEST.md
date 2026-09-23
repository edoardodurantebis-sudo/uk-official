# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T00:13:08.250701Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.249e+04 d1=0.0 d12=-2.0 z=-5.395918
- **ACCELERATION** `thermal_base` value=1.376e+04 d1=0.0 d12=-24.0 z=-4.344424963938973
- **ROBUST_OUTLIER** `thermal_base` value=1.376e+04 d1=0.0 d12=-24.0 z=-4.344424963938973
- **REVERSAL** `ccgt_gen` value=1.002e+04 d1=4.0 d12=-27.0 z=-4.337739271107266
- **ACCELERATION** `ccgt_gen` value=1.002e+04 d1=4.0 d12=-27.0 z=-4.337739271107266
- **ROBUST_OUTLIER** `ccgt_gen` value=1.002e+04 d1=4.0 d12=-27.0 z=-4.337739271107266
- **CHANGE_POINT** `wind_gen` value=3910 d1=46.0 d12=774.0 z=2.0316410736253494
- **CHANGE_POINT** `interconnector_net` value=3203 d1=-178.0 d12=-1442.0 z=-1.9491377265306122
- **CHANGE_POINT** `imbalance` value=-7998 d1=0.0 d12=51.0 z=1.5076829705882353
- **CHANGE_POINT** `ind_generation` value=1.318e+04 d1=0.0 d12=51.0 z=1.5076829705882353
- **PERSISTENT_UP** `wind_gen` value=3910 d1=46.0 d12=774.0 z=2.0316410736253494
- **PERSISTENT_DOWN** `interconnector_net` value=3203 d1=-178.0 d12=-1442.0 z=-1.9491377265306122
- **PERSISTENT_UP** `biomass_gen` value=2915 d1=2.0 d12=0.0 z=0.5395918
- **ACCELERATION** `biomass_gen` value=2915 d1=2.0 d12=0.0 z=0.5395918
- **REVERSAL** `nuclear_gen` value=3733 d1=-4.0 d12=3.0 z=-0.1686224375

## Nearest historical live analogues

- `2026-09-22T22:53:13.778957Z` distance=0.464 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:57:26.907882Z` distance=0.464 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:01:39.891099Z` distance=0.464 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:05:56.234014Z` distance=0.464 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -158.0}
- `2026-09-22T23:10:06.870136Z` distance=0.464 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -158.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

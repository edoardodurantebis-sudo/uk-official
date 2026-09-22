# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T03:29:25.727103Z`  
Memory snapshots: **2381**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **PERSISTENT_DOWN** `margin` value=3.779e+04 d1=0.0 d12=-28.0 z=22.368282525510203
- **ROBUST_OUTLIER** `margin` value=3.779e+04 d1=0.0 d12=-28.0 z=22.368282525510203
- **CHANGE_POINT** `ind_demand` value=-1.25e+04 d1=0.0 d12=-3.0 z=-2.2739940142857145
- **PERSISTENT_DOWN** `interconnector_net` value=408 d1=-2.0 d12=-2222.0 z=-2.694106974014849
- **CHANGE_POINT** `imbalance` value=-2644 d1=0.0 d12=11.0 z=-0.2459077213541667
- **CHANGE_POINT** `ind_generation` value=1.882e+04 d1=0.0 d12=11.0 z=-0.2459077213541667
- **CHANGE_POINT** `ps_gen` value=-169 d1=1.0 d12=-2.0 z=-0.019921638185654008
- **CHANGE_POINT** `ccgt_gen` value=1.123e+04 d1=4.0 d12=487.0 z=0.01087886693548387
- **CHANGE_POINT** `thermal_base` value=1.488e+04 d1=-5.0 d12=482.0 z=-0.002949663629737609
- **REVERSAL** `wind_gen` value=3969 d1=14.0 d12=-147.0 z=1.8565500694444443
- **PERSISTENT_UP** `biomass_gen` value=3045 d1=1.0 d12=2.0 z=0.5246031388888889
- **ACCELERATION** `biomass_gen` value=3045 d1=1.0 d12=2.0 z=0.5246031388888889
- **PERSISTENT_DOWN** `nuclear_gen` value=3648 d1=-9.0 d12=-5.0 z=-0.2697959
- **ACCELERATION** `nuclear_gen` value=3648 d1=-9.0 d12=-5.0 z=-0.2697959
- **PERSISTENT_UP** `imbalance` value=-2644 d1=0.0 d12=11.0 z=-0.2459077213541667

## Nearest historical live analogues

- `2026-09-22T02:20:47.392507Z` distance=0.016 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:24:59.358718Z` distance=0.016 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:29:12.426907Z` distance=0.016 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:33:26.071895Z` distance=0.016 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:53:56.422040Z` distance=0.341 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

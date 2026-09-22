# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T23:05:56.234014Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.249e+04 d1=0.0 d12=-15.0 z=-10.791836
- **ROBUST_OUTLIER** `ind_demand` value=-1.249e+04 d1=0.0 d12=-15.0 z=-10.791836
- **REVERSAL** `thermal_base` value=1.388e+04 d1=94.0 d12=-1213.0 z=-9.591655399854861
- **ROBUST_OUTLIER** `thermal_base` value=1.388e+04 d1=94.0 d12=-1213.0 z=-9.591655399854861
- **REVERSAL** `ccgt_gen` value=1.014e+04 d1=91.0 d12=-1217.0 z=-9.538101450288185
- **ROBUST_OUTLIER** `ccgt_gen` value=1.014e+04 d1=91.0 d12=-1217.0 z=-9.538101450288185
- **CHANGE_POINT** `wind_gen` value=3045 d1=38.0 d12=527.0 z=1.8683366075
- **CHANGE_POINT** `margin` value=3.723e+04 d1=0.0 d12=20.0 z=1.1428854097222223
- **PERSISTENT_DOWN** `interconnector_net` value=4723 d1=-426.0 d12=-448.0 z=-1.8734524159426584
- **ACCELERATION** `interconnector_net` value=4723 d1=-426.0 d12=-448.0 z=-1.8734524159426584
- **PERSISTENT_UP** `wind_gen` value=3045 d1=38.0 d12=527.0 z=1.8683366075
- **ACCELERATION** `nuclear_gen` value=3740 d1=3.0 d12=4.0 z=1.3489795
- **PERSISTENT_UP** `biomass_gen` value=2917 d1=12.0 d12=6.0 z=0.67448975
- **ACCELERATION** `biomass_gen` value=2917 d1=12.0 d12=6.0 z=0.67448975

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.020 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:54:12.694588Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:58:28.957668Z` distance=0.021 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:02:41.905609Z` distance=0.021 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:06:53.543524Z` distance=0.021 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

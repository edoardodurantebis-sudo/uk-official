# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T10:12:22.787147Z`  
Memory snapshots: **2476**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.107e+04 d1=0.0 d12=0.0 z=-263.72549225
- **CHANGE_POINT** `margin` value=4.027e+04 d1=0.0 d12=-65.0 z=151.76019374999998
- **ROBUST_OUTLIER** `margin` value=4.027e+04 d1=0.0 d12=-65.0 z=151.76019374999998
- **ROBUST_OUTLIER** `imbalance` value=3833 d1=0.0 d12=1403.0 z=23.988670805555557
- **ROBUST_OUTLIER** `ind_generation` value=2.49e+04 d1=0.0 d12=1403.0 z=22.656723874999997
- **ROBUST_OUTLIER** `ind_demand` value=-1.31e+04 d1=0.0 d12=-294.0 z=-8.618480138888888
- **ACCELERATION** `biomass_gen` value=3048 d1=0.0 d12=-6.0 z=3.8221085833333333
- **ROBUST_OUTLIER** `biomass_gen` value=3048 d1=0.0 d12=-6.0 z=3.8221085833333333
- **PERSISTENT_DOWN** `ccgt_gen` value=9837 d1=-3.0 d12=-843.0 z=-2.331757881233933
- **REVERSAL** `wind_gen` value=3776 d1=-53.0 d12=260.0 z=2.2155707610759494
- **REVERSAL** `interconnector_net` value=1.096e+04 d1=-24.0 d12=785.0 z=1.802846676803119
- **REVERSAL** `nuclear_gen` value=3657 d1=-2.0 d12=16.0 z=1.3489794999999998
- **ACCELERATION** `nuclear_gen` value=3657 d1=-2.0 d12=16.0 z=1.3489794999999998
- **PERSISTENT_UP** `ps_gen` value=-168 d1=2.0 d12=2.0 z=1.0117346249999999
- **ACCELERATION** `ps_gen` value=-168 d1=2.0 d12=2.0 z=1.0117346249999999

## Nearest historical live analogues

- `2026-09-21T09:51:38.826991Z` distance=0.560 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T09:55:50.935902Z` distance=0.560 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:00:02.533283Z` distance=0.560 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:04:15.522994Z` distance=0.560 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:08:28.408864Z` distance=0.560 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 354.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T10:08:07.452528Z`  
Memory snapshots: **2475**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=4.027e+04 d1=0.0 d12=1321.0 z=151.76019374999998
- **ROBUST_OUTLIER** `margin` value=4.027e+04 d1=0.0 d12=1321.0 z=151.76019374999998
- **CHANGE_POINT** `imbalance` value=3833 d1=0.0 d12=3853.0 z=23.988670805555557
- **ROBUST_OUTLIER** `imbalance` value=3833 d1=0.0 d12=3853.0 z=23.988670805555557
- **ROBUST_OUTLIER** `ind_generation` value=2.49e+04 d1=0.0 d12=3853.0 z=22.656723874999997
- **ROBUST_OUTLIER** `ind_demand` value=-1.31e+04 d1=0.0 d12=-294.0 z=-8.618480138888888
- **REVERSAL** `biomass_gen` value=3048 d1=8.0 d12=-1.0 z=3.8221085833333333
- **ACCELERATION** `biomass_gen` value=3048 d1=8.0 d12=-1.0 z=3.8221085833333333
- **ROBUST_OUTLIER** `biomass_gen` value=3048 d1=8.0 d12=-1.0 z=3.8221085833333333
- **PERSISTENT_UP** `wind_gen` value=3829 d1=29.0 d12=327.0 z=2.668076542721519
- **REVERSAL** `thermal_base` value=1.35e+04 d1=32.0 d12=-675.0 z=-2.335120425141972
- **REVERSAL** `ccgt_gen` value=9840 d1=25.0 d12=-688.0 z=-2.329677193059126
- **PERSISTENT_UP** `interconnector_net` value=1.098e+04 d1=11.0 d12=811.0 z=1.8302011430400524
- **PERSISTENT_UP** `nuclear_gen` value=3659 d1=7.0 d12=13.0 z=1.7986393333333333
- **ACCELERATION** `nuclear_gen` value=3659 d1=7.0 d12=13.0 z=1.7986393333333333

## Nearest historical live analogues

- `2026-09-21T09:51:38.826991Z` distance=0.558 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T09:55:50.935902Z` distance=0.558 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:00:02.533283Z` distance=0.558 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:04:15.522994Z` distance=0.558 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:08:28.408864Z` distance=0.558 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 354.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

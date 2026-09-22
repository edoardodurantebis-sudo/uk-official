# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T10:03:39.626379Z`  
Memory snapshots: **2474**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=4.027e+04 d1=0.0 d12=1321.0 z=151.76019374999998
- **ROBUST_OUTLIER** `margin` value=4.027e+04 d1=0.0 d12=1321.0 z=151.76019374999998
- **CHANGE_POINT** `imbalance` value=3833 d1=0.0 d12=3853.0 z=23.988670805555557
- **CHANGE_POINT** `ind_generation` value=2.49e+04 d1=0.0 d12=3853.0 z=22.656723874999997
- **ROBUST_OUTLIER** `imbalance` value=3833 d1=0.0 d12=3853.0 z=23.988670805555557
- **ROBUST_OUTLIER** `ind_generation` value=2.49e+04 d1=0.0 d12=3853.0 z=22.656723874999997
- **CHANGE_POINT** `ind_demand` value=-1.31e+04 d1=0.0 d12=-294.0 z=-8.618480138888888
- **ROBUST_OUTLIER** `ind_demand` value=-1.31e+04 d1=0.0 d12=-294.0 z=-8.618480138888888
- **PERSISTENT_UP** `wind_gen` value=3800 d1=25.0 d12=294.0 z=2.420479039556962
- **PERSISTENT_DOWN** `thermal_base` value=1.347e+04 d1=-23.0 d12=-817.0 z=-2.3574060957666494
- **PERSISTENT_DOWN** `ccgt_gen` value=9815 d1=-25.0 d12=-818.0 z=-2.347016261182519
- **PERSISTENT_DOWN** `biomass_gen` value=3040 d1=-8.0 d12=-8.0 z=2.02346925
- **ACCELERATION** `biomass_gen` value=3040 d1=-8.0 d12=-8.0 z=2.02346925
- **PERSISTENT_UP** `interconnector_net` value=1.097e+04 d1=105.0 d12=796.0 z=1.8527645011618643
- **PERSISTENT_UP** `nuclear_gen` value=3652 d1=2.0 d12=1.0 z=0.22482991666666666

## Nearest historical live analogues

- `2026-09-21T09:51:38.826991Z` distance=0.555 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T09:55:50.935902Z` distance=0.555 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:00:02.533283Z` distance=0.555 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:04:15.522994Z` distance=0.555 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:08:28.408864Z` distance=0.555 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 354.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

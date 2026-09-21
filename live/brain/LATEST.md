# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T10:37:58.343383Z`  
Memory snapshots: **2143**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.473e+04 d1=0.0 d12=3043.0 z=32.28261420209581
- **ROBUST_OUTLIER** `ind_generation` value=2.473e+04 d1=0.0 d12=3043.0 z=32.28261420209581
- **CHANGE_POINT** `imbalance` value=3568 d1=0.0 d12=3153.0 z=10.213505684826883
- **ROBUST_OUTLIER** `imbalance` value=3568 d1=0.0 d12=3153.0 z=10.213505684826883
- **CHANGE_POINT** `margin` value=4.101e+04 d1=0.0 d12=1333.0 z=3.203266105066445
- **ROBUST_OUTLIER** `margin` value=4.101e+04 d1=0.0 d12=1333.0 z=3.203266105066445
- **PERSISTENT_DOWN** `ccgt_gen` value=6958 d1=0.0 d12=-549.0 z=-3.1409217719858153
- **ROBUST_OUTLIER** `ccgt_gen` value=6958 d1=0.0 d12=-549.0 z=-3.1409217719858153
- **PERSISTENT_DOWN** `thermal_base` value=1.045e+04 d1=0.0 d12=-543.0 z=-2.9267226837146705
- **CHANGE_POINT** `interconnector_net` value=1.099e+04 d1=0.0 d12=365.0 z=0.8622652928730512
- **PERSISTENT_UP** `biomass_gen` value=3002 d1=0.0 d12=59.0 z=-1.09604584375
- **ACCELERATION** `biomass_gen` value=3002 d1=0.0 d12=59.0 z=-1.09604584375
- **PERSISTENT_UP** `wind_gen` value=3410 d1=0.0 d12=99.0 z=-0.9395034479320532
- **ACCELERATION** `wind_gen` value=3410 d1=0.0 d12=99.0 z=-0.9395034479320532
- **PERSISTENT_UP** `interconnector_net` value=1.099e+04 d1=0.0 d12=365.0 z=0.8622652928730512

## Nearest historical live analogues

- `2026-09-21T09:22:16.225384Z` distance=0.603 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:26:26.475864Z` distance=0.603 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:30:39.158321Z` distance=0.603 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:34:50.037660Z` distance=0.603 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:39:02.425016Z` distance=0.603 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T16:34:47.779793Z`  
Memory snapshots: **2227**  
Current physical regime: **BALANCED**

Regime read: wind rising.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.652e+04 d1=185.0 d12=2375.0 z=6.21712774256651
- **CHANGE_POINT** `ccgt_gen` value=1.301e+04 d1=184.0 d12=2369.0 z=6.164595612684251
- **CHANGE_POINT** `interconnector_net` value=9728 d1=-475.0 d12=-1219.0 z=-5.000129393643032
- **PERSISTENT_UP** `thermal_base` value=1.652e+04 d1=185.0 d12=2375.0 z=6.21712774256651
- **ROBUST_OUTLIER** `thermal_base` value=1.652e+04 d1=185.0 d12=2375.0 z=6.21712774256651
- **PERSISTENT_UP** `ccgt_gen` value=1.301e+04 d1=184.0 d12=2369.0 z=6.164595612684251
- **ROBUST_OUTLIER** `ccgt_gen` value=1.301e+04 d1=184.0 d12=2369.0 z=6.164595612684251
- **PERSISTENT_DOWN** `interconnector_net` value=9728 d1=-475.0 d12=-1219.0 z=-5.000129393643032
- **ACCELERATION** `interconnector_net` value=9728 d1=-475.0 d12=-1219.0 z=-5.000129393643032
- **ROBUST_OUTLIER** `interconnector_net` value=9728 d1=-475.0 d12=-1219.0 z=-5.000129393643032
- **CHANGE_POINT** `ind_generation` value=1.839e+04 d1=0.0 d12=36.0 z=0.7402936280487804
- **CHANGE_POINT** `imbalance` value=-3071 d1=0.0 d12=36.0 z=0.7169772933070866
- **CHANGE_POINT** `wind_gen` value=3263 d1=117.0 d12=-123.0 z=-0.7082142375
- **PERSISTENT_UP** `ind_generation` value=1.839e+04 d1=0.0 d12=36.0 z=0.7402936280487804
- **PERSISTENT_UP** `imbalance` value=-3071 d1=0.0 d12=36.0 z=0.7169772933070866

## Nearest historical live analogues

- `2026-09-21T15:26:27.469405Z` distance=0.010 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -51.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T15:30:37.860005Z` distance=0.010 → {'next30m_imbalance_delta': 28.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -51.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T15:34:50.537935Z` distance=0.010 → {'next30m_imbalance_delta': 28.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -51.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T15:39:04.883699Z` distance=0.010 → {'next30m_imbalance_delta': 28.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -51.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T13:57:37.194603Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

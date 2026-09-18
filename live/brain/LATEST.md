# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T10:58:51.813919Z`  
Memory snapshots: **1179**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1084 d1=0.0 d12=-480.0 z=-45.485902515625
- **ROBUST_OUTLIER** `biomass_gen` value=1084 d1=0.0 d12=-480.0 z=-45.485902515625
- **CHANGE_POINT** `ind_generation` value=2.565e+04 d1=-1107.0 d12=-1242.0 z=-6.210783789340101
- **PERSISTENT_DOWN** `ind_generation` value=2.565e+04 d1=-1107.0 d12=-1242.0 z=-6.210783789340101
- **ACCELERATION** `ind_generation` value=2.565e+04 d1=-1107.0 d12=-1242.0 z=-6.210783789340101
- **ROBUST_OUTLIER** `ind_generation` value=2.565e+04 d1=-1107.0 d12=-1242.0 z=-6.210783789340101
- **CHANGE_POINT** `thermal_base` value=6052 d1=-101.0 d12=-313.0 z=-1.3284627015209125
- **CHANGE_POINT** `ccgt_gen` value=2719 d1=-98.0 d12=-314.0 z=-1.324890580357143
- **CHANGE_POINT** `ind_demand` value=-1.074e+04 d1=3052.0 d12=2445.0 z=1.1809529015017668
- **CHANGE_POINT** `margin` value=3.813e+04 d1=0.0 d12=1962.0 z=1.0145449989583333
- **CHANGE_POINT** `interconnector_net` value=5747 d1=23.0 d12=710.0 z=0.8260524094781683
- **PERSISTENT_UP** `ps_gen` value=-698 d1=17.0 d12=4.0 z=-2.39029700877193
- **ACCELERATION** `ps_gen` value=-698 d1=17.0 d12=4.0 z=-2.39029700877193
- **PERSISTENT_UP** `imbalance` value=8982 d1=1904.0 d12=1181.0 z=-1.60013307293666
- **ACCELERATION** `imbalance` value=8982 d1=1904.0 d12=1181.0 z=-1.60013307293666

## Nearest historical live analogues

- `2026-09-18T05:50:47.091039Z` distance=0.523 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T05:54:59.248868Z` distance=0.523 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T05:59:09.222653Z` distance=0.523 → {'next30m_imbalance_delta': -67.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T06:03:20.906831Z` distance=0.523 → {'next30m_imbalance_delta': -67.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T06:07:33.046654Z` distance=0.523 → {'next30m_imbalance_delta': -67.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

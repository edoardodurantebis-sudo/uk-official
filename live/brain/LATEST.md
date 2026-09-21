# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T17:51:24.666865Z`  
Memory snapshots: **2245**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=6620 d1=-1.0 d12=-2754.0 z=-14.08054448758465
- **ROBUST_OUTLIER** `interconnector_net` value=6620 d1=-1.0 d12=-2754.0 z=-14.08054448758465
- **CHANGE_POINT** `margin` value=3.617e+04 d1=0.0 d12=-106.0 z=-4.0469385
- **ROBUST_OUTLIER** `margin` value=3.617e+04 d1=0.0 d12=-106.0 z=-4.0469385
- **CHANGE_POINT** `ind_generation` value=1.844e+04 d1=0.0 d12=8.0 z=0.7411060216049382
- **CHANGE_POINT** `imbalance` value=-3018 d1=0.0 d12=8.0 z=0.645479438172043
- **CHANGE_POINT** `wind_gen` value=3585 d1=21.0 d12=238.0 z=0.5675821527377521
- **REVERSAL** `thermal_base` value=1.747e+04 d1=-85.0 d12=501.0 z=2.2441426471988795
- **REVERSAL** `ccgt_gen` value=1.396e+04 d1=-88.0 d12=494.0 z=2.228053818720379
- **PERSISTENT_UP** `wind_gen` value=3585 d1=21.0 d12=238.0 z=0.5675821527377521
- **PERSISTENT_UP** `nuclear_gen` value=3511 d1=3.0 d12=7.0 z=0.5620747916666667
- **REVERSAL** `biomass_gen` value=2974 d1=4.0 d12=-1.0 z=-0.2129967631578947
- **ACCELERATION** `biomass_gen` value=2974 d1=4.0 d12=-1.0 z=-0.2129967631578947

## Nearest historical live analogues

- `2026-09-21T15:52:07.020346Z` distance=0.019 → {'next30m_imbalance_delta': 28.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T15:56:21.179145Z` distance=0.020 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:00:35.791303Z` distance=0.020 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:04:50.781494Z` distance=0.020 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:09:03.909955Z` distance=0.020 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': -4.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

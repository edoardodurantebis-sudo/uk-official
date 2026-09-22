# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T03:42:37.215255Z`  
Memory snapshots: **2384**  
Current physical regime: **LOOSE**

Regime read: margin high, wind rising.

## Active patterns

- **CHANGE_POINT** `margin` value=3.779e+04 d1=0.0 d12=-43.0 z=22.368282525510203
- **ROBUST_OUTLIER** `margin` value=3.779e+04 d1=0.0 d12=-43.0 z=22.368282525510203
- **CHANGE_POINT** `interconnector_net` value=-1447 d1=14.0 d12=-4138.0 z=-4.46523334812936
- **CHANGE_POINT** `ps_gen` value=-712 d1=-304.0 d12=-547.0 z=-3.163124344827586
- **REVERSAL** `interconnector_net` value=-1447 d1=14.0 d12=-4138.0 z=-4.46523334812936
- **ROBUST_OUTLIER** `interconnector_net` value=-1447 d1=14.0 d12=-4138.0 z=-4.46523334812936
- **CHANGE_POINT** `ind_demand` value=-1.25e+04 d1=0.0 d12=-3.0 z=-2.2739940142857145
- **PERSISTENT_DOWN** `ps_gen` value=-712 d1=-304.0 d12=-547.0 z=-3.163124344827586
- **ROBUST_OUTLIER** `ps_gen` value=-712 d1=-304.0 d12=-547.0 z=-3.163124344827586
- **CHANGE_POINT** `thermal_base` value=1.501e+04 d1=51.0 d12=641.0 z=0.2842189512578616
- **CHANGE_POINT** `ccgt_gen` value=1.135e+04 d1=50.0 d12=637.0 z=0.2658648247699386
- **CHANGE_POINT** `imbalance` value=-2644 d1=0.0 d12=11.0 z=-0.2459077213541667
- **CHANGE_POINT** `ind_generation` value=1.882e+04 d1=0.0 d12=11.0 z=-0.2459077213541667
- **PERSISTENT_UP** `nuclear_gen` value=3658 d1=1.0 d12=4.0 z=0.8584415
- **ACCELERATION** `nuclear_gen` value=3658 d1=1.0 d12=4.0 z=0.8584415

## Nearest historical live analogues

- `2026-09-22T02:20:47.392507Z` distance=0.196 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:24:59.358718Z` distance=0.196 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:29:12.426907Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:33:26.071895Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:37:48.213453Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

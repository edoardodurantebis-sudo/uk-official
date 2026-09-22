# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T22:23:43.484966Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.453e+04 d1=-214.0 d12=-2849.0 z=-8.328822631349782
- **CHANGE_POINT** `ccgt_gen` value=1.078e+04 d1=-222.0 d12=-2861.0 z=-8.292141998559078
- **PERSISTENT_DOWN** `thermal_base` value=1.453e+04 d1=-214.0 d12=-2849.0 z=-8.328822631349782
- **ROBUST_OUTLIER** `thermal_base` value=1.453e+04 d1=-214.0 d12=-2849.0 z=-8.328822631349782
- **PERSISTENT_DOWN** `ccgt_gen` value=1.078e+04 d1=-222.0 d12=-2861.0 z=-8.292141998559078
- **ROBUST_OUTLIER** `ccgt_gen` value=1.078e+04 d1=-222.0 d12=-2861.0 z=-8.292141998559078
- **CHANGE_POINT** `wind_gen` value=2568 d1=4.0 d12=192.0 z=1.581917014216366
- **PERSISTENT_UP** `nuclear_gen` value=3744 d1=8.0 d12=12.0 z=2.9227889166666667
- **ACCELERATION** `nuclear_gen` value=3744 d1=8.0 d12=12.0 z=2.9227889166666667
- **CHANGE_POINT** `imbalance` value=-8047 d1=7.0 d12=-28.0 z=-0.79712425
- **CHANGE_POINT** `ind_generation` value=1.313e+04 d1=7.0 d12=-28.0 z=-0.79712425
- **PERSISTENT_UP** `ps_gen` value=145 d1=1.0 d12=2.0 z=-2.4464543474576272
- **ACCELERATION** `ps_gen` value=145 d1=1.0 d12=2.0 z=-2.4464543474576272
- **PERSISTENT_UP** `margin` value=3.723e+04 d1=0.0 d12=19.0 z=2.4202279264705884
- **ACCELERATION** `margin` value=3.723e+04 d1=0.0 d12=19.0 z=2.4202279264705884

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.011 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:24:47.718083Z` distance=0.011 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:28:58.806773Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:55:13.117327Z` distance=0.011 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:59:27.826421Z` distance=0.011 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

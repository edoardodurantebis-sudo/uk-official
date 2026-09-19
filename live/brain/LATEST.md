# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T06:33:12.092764Z`  
Memory snapshots: **1403**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-482 d1=2.0 d12=57.0 z=8.363672900000001
- **CHANGE_POINT** `interconnector_net` value=-8364 d1=1234.0 d12=2517.0 z=6.8827691523046095
- **PERSISTENT_UP** `ps_gen` value=-482 d1=2.0 d12=57.0 z=8.363672900000001
- **ROBUST_OUTLIER** `ps_gen` value=-482 d1=2.0 d12=57.0 z=8.363672900000001
- **PERSISTENT_UP** `interconnector_net` value=-8364 d1=1234.0 d12=2517.0 z=6.8827691523046095
- **ACCELERATION** `interconnector_net` value=-8364 d1=1234.0 d12=2517.0 z=6.8827691523046095
- **ROBUST_OUTLIER** `interconnector_net` value=-8364 d1=1234.0 d12=2517.0 z=6.8827691523046095
- **PERSISTENT_UP** `ind_demand` value=-1.086e+04 d1=0.0 d12=2.0 z=3.2038263125
- **ROBUST_OUTLIER** `ind_demand` value=-1.086e+04 d1=0.0 d12=2.0 z=3.2038263125
- **PERSISTENT_DOWN** `nuclear_gen` value=3332 d1=-3.0 d12=0.0 z=-2.360714125
- **ACCELERATION** `nuclear_gen` value=3332 d1=-3.0 d12=0.0 z=-2.360714125
- **PERSISTENT_UP** `imbalance` value=9725 d1=0.0 d12=13.0 z=1.0516925485781992
- **PERSISTENT_UP** `ind_generation` value=2.691e+04 d1=0.0 d12=13.0 z=1.0276424021226416
- **PERSISTENT_UP** `wind_gen` value=1.588e+04 d1=2.0 d12=83.0 z=-0.6187048834586466
- **ACCELERATION** `wind_gen` value=1.588e+04 d1=2.0 d12=83.0 z=-0.6187048834586466

## Nearest historical live analogues

- `2026-09-19T05:34:16.820829Z` distance=0.010 → {'next30m_imbalance_delta': -15.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T05:38:30.029474Z` distance=0.010 → {'next30m_imbalance_delta': -15.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T05:21:38.330521Z` distance=0.066 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -158.0}
- `2026-09-19T05:25:51.266434Z` distance=0.066 → {'next30m_imbalance_delta': -15.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': -158.0}
- `2026-09-19T05:30:03.154514Z` distance=0.066 → {'next30m_imbalance_delta': -15.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': -158.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T16:09:15.808095Z`  
Memory snapshots: **265**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=7374 d1=298.0 d12=3341.0 z=14.685422302504817
- **CHANGE_POINT** `thermal_base` value=1.07e+04 d1=294.0 d12=3335.0 z=14.547312390057362
- **PERSISTENT_UP** `ccgt_gen` value=7374 d1=298.0 d12=3341.0 z=14.685422302504817
- **ROBUST_OUTLIER** `ccgt_gen` value=7374 d1=298.0 d12=3341.0 z=14.685422302504817
- **PERSISTENT_UP** `thermal_base` value=1.07e+04 d1=294.0 d12=3335.0 z=14.547312390057362
- **ROBUST_OUTLIER** `thermal_base` value=1.07e+04 d1=294.0 d12=3335.0 z=14.547312390057362
- **PERSISTENT_DOWN** `interconnector_net` value=3215 d1=-1131.0 d12=-3205.0 z=-13.91578852631579
- **ACCELERATION** `interconnector_net` value=3215 d1=-1131.0 d12=-3205.0 z=-13.91578852631579
- **ROBUST_OUTLIER** `interconnector_net` value=3215 d1=-1131.0 d12=-3205.0 z=-13.91578852631579
- **PERSISTENT_UP** `ps_gen` value=225 d1=370.0 d12=238.0 z=3.4009684011627903
- **ACCELERATION** `ps_gen` value=225 d1=370.0 d12=238.0 z=3.4009684011627903
- **ROBUST_OUTLIER** `ps_gen` value=225 d1=370.0 d12=238.0 z=3.4009684011627903
- **CHANGE_POINT** `imbalance` value=5825 d1=0.0 d12=7.0 z=1.087886693548387
- **CHANGE_POINT** `ind_generation` value=2.495e+04 d1=0.0 d12=7.0 z=1.023998075
- **CHANGE_POINT** `margin` value=3.497e+04 d1=0.0 d12=344.0 z=-0.3646401169467787

## Nearest historical live analogues

- `2026-09-15T13:25:09.783150Z` distance=0.184 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:29:22.306019Z` distance=0.184 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:33:32.333732Z` distance=0.184 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:37:45.498739Z` distance=0.184 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:41:57.247780Z` distance=0.184 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

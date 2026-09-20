# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T08:42:17.599613Z`  
Memory snapshots: **1775**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=585 d1=2.0 d12=-301.0 z=-9.699804976190476
- **REVERSAL** `biomass_gen` value=585 d1=2.0 d12=-301.0 z=-9.699804976190476
- **ROBUST_OUTLIER** `biomass_gen` value=585 d1=2.0 d12=-301.0 z=-9.699804976190476
- **CHANGE_POINT** `interconnector_net` value=-3244 d1=1.0 d12=3510.0 z=5.037696171052632
- **CHANGE_POINT** `thermal_base` value=6028 d1=-66.0 d12=-1218.0 z=-4.434718539755352
- **CHANGE_POINT** `ccgt_gen` value=2693 d1=-61.0 d12=-1217.0 z=-4.415028942835366
- **PERSISTENT_UP** `interconnector_net` value=-3244 d1=1.0 d12=3510.0 z=5.037696171052632
- **ROBUST_OUTLIER** `interconnector_net` value=-3244 d1=1.0 d12=3510.0 z=5.037696171052632
- **PERSISTENT_DOWN** `thermal_base` value=6028 d1=-66.0 d12=-1218.0 z=-4.434718539755352
- **ROBUST_OUTLIER** `thermal_base` value=6028 d1=-66.0 d12=-1218.0 z=-4.434718539755352
- **PERSISTENT_DOWN** `ccgt_gen` value=2693 d1=-61.0 d12=-1217.0 z=-4.415028942835366
- **ROBUST_OUTLIER** `ccgt_gen` value=2693 d1=-61.0 d12=-1217.0 z=-4.415028942835366
- **CHANGE_POINT** `wind_gen` value=1.506e+04 d1=-30.0 d12=-380.0 z=-1.0508461750547045
- **ACCELERATION** `ps_gen` value=-934 d1=-1.0 d12=-4.0 z=-1.6467595492021276
- **PERSISTENT_DOWN** `wind_forecast` value=2453 d1=0.0 d12=-201.0 z=-1.5165545931677018

## Nearest historical live analogues

- `2026-09-20T05:53:50.250426Z` distance=0.063 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:58:00.386850Z` distance=0.063 → {'next30m_imbalance_delta': -80.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:02:09.934243Z` distance=0.063 → {'next30m_imbalance_delta': -80.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:06:21.393634Z` distance=0.063 → {'next30m_imbalance_delta': -80.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:11:07.730851Z` distance=0.063 → {'next30m_imbalance_delta': -80.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

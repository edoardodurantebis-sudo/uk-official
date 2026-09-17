# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T02:22:41.615797Z`  
Memory snapshots: **715**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2033 d1=0.0 d12=-807.0 z=-316.2007948
- **ROBUST_OUTLIER** `biomass_gen` value=2033 d1=0.0 d12=-807.0 z=-316.2007948
- **CHANGE_POINT** `ind_demand` value=-1.153e+04 d1=0.0 d12=120.0 z=31.835916200000003
- **ROBUST_OUTLIER** `ind_demand` value=-1.153e+04 d1=0.0 d12=120.0 z=31.835916200000003
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `margin` value=3.585e+04 d1=1290.0 d12=1359.0 z=6.4198958382838285
- **PERSISTENT_UP** `margin` value=3.585e+04 d1=1290.0 d12=1359.0 z=6.4198958382838285
- **ACCELERATION** `margin` value=3.585e+04 d1=1290.0 d12=1359.0 z=6.4198958382838285
- **ROBUST_OUTLIER** `margin` value=3.585e+04 d1=1290.0 d12=1359.0 z=6.4198958382838285
- **CHANGE_POINT** `ps_gen` value=-538 d1=2.0 d12=-222.0 z=-0.9768913156398104
- **PERSISTENT_UP** `interconnector_net` value=-6579 d1=0.0 d12=84.0 z=-2.639496004012841
- **PERSISTENT_DOWN** `ccgt_gen` value=3801 d1=-16.0 d12=-279.0 z=-1.7594388723464478
- **ACCELERATION** `ccgt_gen` value=3801 d1=-16.0 d12=-279.0 z=-1.7594388723464478
- **PERSISTENT_DOWN** `thermal_base` value=7116 d1=-13.0 d12=-288.0 z=-1.749071531012123

## Nearest historical live analogues

- `2026-09-16T12:23:49.836209Z` distance=0.593 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T12:28:01.597273Z` distance=0.593 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T11:54:04.473281Z` distance=0.600 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T11:58:14.719154Z` distance=0.600 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T12:02:46.560952Z` distance=0.600 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

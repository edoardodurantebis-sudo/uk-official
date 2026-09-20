# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T15:06:50.185709Z`  
Memory snapshots: **1866**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=870 d1=131.0 d12=282.0 z=191.555089
- **PERSISTENT_UP** `biomass_gen` value=870 d1=131.0 d12=282.0 z=191.555089
- **ROBUST_OUTLIER** `biomass_gen` value=870 d1=131.0 d12=282.0 z=191.555089
- **ROBUST_OUTLIER** `imbalance` value=-5158 d1=0.0 d12=573.0 z=25.765508450000002
- **CHANGE_POINT** `ccgt_gen` value=2708 d1=31.0 d12=312.0 z=13.468037266129032
- **CHANGE_POINT** `thermal_base` value=6041 d1=34.0 d12=312.0 z=12.220167235294117
- **PERSISTENT_UP** `ccgt_gen` value=2708 d1=31.0 d12=312.0 z=13.468037266129032
- **ROBUST_OUTLIER** `ccgt_gen` value=2708 d1=31.0 d12=312.0 z=13.468037266129032
- **PERSISTENT_UP** `thermal_base` value=6041 d1=34.0 d12=312.0 z=12.220167235294117
- **ROBUST_OUTLIER** `thermal_base` value=6041 d1=34.0 d12=312.0 z=12.220167235294117
- **CHANGE_POINT** `interconnector_net` value=4237 d1=1533.0 d12=4363.0 z=5.670334172288531
- **PERSISTENT_UP** `interconnector_net` value=4237 d1=1533.0 d12=4363.0 z=5.670334172288531
- **ROBUST_OUTLIER** `interconnector_net` value=4237 d1=1533.0 d12=4363.0 z=5.670334172288531
- **ROBUST_OUTLIER** `residual_proxy` value=1.782e+04 d1=0.0 d12=-494.0 z=-3.889865544520548
- **ROBUST_OUTLIER** `margin` value=3.591e+04 d1=0.0 d12=112.0 z=3.587059125

## Nearest historical live analogues

- `2026-09-20T10:57:55.935414Z` distance=0.055 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:02:06.579348Z` distance=0.055 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:06:18.746524Z` distance=0.055 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:10:29.817646Z` distance=0.055 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:14:40.539694Z` distance=0.055 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

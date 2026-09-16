# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T11:07:54.442982Z`  
Memory snapshots: **535**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-5 d1=0.0 d12=0.0 z=-27.960666
- **ROBUST_OUTLIER** `ps_gen` value=-5 d1=0.0 d12=0.0 z=-27.960666
- **CHANGE_POINT** `imbalance` value=4364 d1=0.0 d12=-1003.0 z=-8.937803788647344
- **CHANGE_POINT** `ind_generation` value=2.473e+04 d1=0.0 d12=-1271.0 z=-8.441828061507938
- **ROBUST_OUTLIER** `imbalance` value=4364 d1=0.0 d12=-1003.0 z=-8.937803788647344
- **ROBUST_OUTLIER** `ind_generation` value=2.473e+04 d1=0.0 d12=-1271.0 z=-8.441828061507938
- **CHANGE_POINT** `nuclear_gen` value=3312 d1=-3.0 d12=-13.0 z=-3.5972786666666665
- **CHANGE_POINT** `margin` value=3.34e+04 d1=0.0 d12=-757.0 z=-2.216481405306972
- **CHANGE_POINT** `wind_gen` value=4680 d1=-50.0 d12=-626.0 z=-1.7049436940528633
- **PERSISTENT_DOWN** `nuclear_gen` value=3312 d1=-3.0 d12=-13.0 z=-3.5972786666666665
- **ROBUST_OUTLIER** `nuclear_gen` value=3312 d1=-3.0 d12=-13.0 z=-3.5972786666666665
- **ROBUST_OUTLIER** `wind_forecast` value=1.976e+04 d1=0.0 d12=433.0 z=3.2392692452229297
- **CHANGE_POINT** `thermal_base` value=9430 d1=-42.0 d12=-225.0 z=-1.1827320264084507
- **CHANGE_POINT** `ccgt_gen` value=6118 d1=-39.0 d12=-212.0 z=-1.167584135642983
- **CHANGE_POINT** `interconnector_net` value=1.072e+04 d1=175.0 d12=489.0 z=1.1355025818304778

## Nearest historical live analogues

- `2026-09-15T14:53:30.277508Z` distance=1.506 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T14:57:40.419064Z` distance=1.506 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:01:51.072857Z` distance=1.506 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:06:01.576691Z` distance=1.506 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:10:11.843860Z` distance=1.506 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 24.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T16:34:05.712800Z`  
Memory snapshots: **612**  
Current physical regime: **BALANCED**

Regime read: wind falling.

## Active patterns

- **REVERSAL** `ps_gen` value=1060 d1=-39.0 d12=837.0 z=358.491302125
- **ROBUST_OUTLIER** `ps_gen` value=1060 d1=-39.0 d12=837.0 z=358.491302125
- **PERSISTENT_UP** `thermal_base` value=1.289e+04 d1=91.0 d12=1619.0 z=3.592476474271845
- **ROBUST_OUTLIER** `thermal_base` value=1.289e+04 d1=91.0 d12=1619.0 z=3.592476474271845
- **PERSISTENT_UP** `ccgt_gen` value=9587 d1=93.0 d12=1617.0 z=3.456838690709617
- **ROBUST_OUTLIER** `ccgt_gen` value=9587 d1=93.0 d12=1617.0 z=3.456838690709617
- **PERSISTENT_DOWN** `interconnector_net` value=8072 d1=-1342.0 d12=-2824.0 z=-3.3992664219804953
- **ACCELERATION** `interconnector_net` value=8072 d1=-1342.0 d12=-2824.0 z=-3.3992664219804953
- **ROBUST_OUTLIER** `interconnector_net` value=8072 d1=-1342.0 d12=-2824.0 z=-3.3992664219804953
- **CHANGE_POINT** `wind_gen` value=5739 d1=68.0 d12=213.0 z=0.9842288373226952
- **CHANGE_POINT** `biomass_gen` value=3220 d1=-1.0 d12=-16.0 z=-0.9197587500000001
- **CHANGE_POINT** `ind_generation` value=2.557e+04 d1=0.0 d12=56.0 z=0.23024157768052517
- **PERSISTENT_UP** `residual_proxy` value=-864 d1=76.0 d12=76.0 z=1.4133780188442213
- **ACCELERATION** `residual_proxy` value=-864 d1=76.0 d12=76.0 z=1.4133780188442213
- **PERSISTENT_UP** `wind_gen` value=5739 d1=68.0 d12=213.0 z=0.9842288373226952

## Nearest historical live analogues

- `2026-09-16T15:24:31.150364Z` distance=0.105 → {'next30m_imbalance_delta': -339.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T15:28:42.332391Z` distance=0.105 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -80.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T15:32:56.539709Z` distance=0.105 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -80.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T15:37:09.894991Z` distance=0.105 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -80.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.358 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

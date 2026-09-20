# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T16:44:37.866118Z`  
Memory snapshots: **1889**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `biomass_gen` value=2018 d1=0.0 d12=606.0 z=321.73161075
- **CHANGE_POINT** `ccgt_gen` value=5674 d1=0.0 d12=1840.0 z=81.55080699537038
- **CHANGE_POINT** `thermal_base` value=9008 d1=0.0 d12=1834.0 z=80.1048554
- **PERSISTENT_UP** `ccgt_gen` value=5674 d1=0.0 d12=1840.0 z=81.55080699537038
- **ROBUST_OUTLIER** `ccgt_gen` value=5674 d1=0.0 d12=1840.0 z=81.55080699537038
- **PERSISTENT_UP** `thermal_base` value=9008 d1=0.0 d12=1834.0 z=80.1048554
- **ROBUST_OUTLIER** `thermal_base` value=9008 d1=0.0 d12=1834.0 z=80.1048554
- **CHANGE_POINT** `imbalance` value=-5182 d1=0.0 d12=-22.0 z=13.956749442307693
- **ROBUST_OUTLIER** `imbalance` value=-5182 d1=0.0 d12=-22.0 z=13.956749442307693
- **PERSISTENT_UP** `ps_gen` value=632 d1=0.0 d12=644.0 z=8.06901101843318
- **ACCELERATION** `ps_gen` value=632 d1=0.0 d12=644.0 z=8.06901101843318
- **ROBUST_OUTLIER** `ps_gen` value=632 d1=0.0 d12=644.0 z=8.06901101843318
- **CHANGE_POINT** `interconnector_net` value=1.196e+04 d1=0.0 d12=4011.0 z=4.567254772504558
- **ROBUST_OUTLIER** `interconnector_net` value=1.196e+04 d1=0.0 d12=4011.0 z=4.567254772504558
- **CHANGE_POINT** `wind_gen` value=7918 d1=0.0 d12=-653.0 z=-1.2872764202565343

## Nearest historical live analogues

- `2026-09-20T14:54:10.136499Z` distance=0.032 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:58:25.329493Z` distance=0.032 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:02:37.176302Z` distance=0.032 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:06:50.185709Z` distance=0.032 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:11:00.797261Z` distance=0.032 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

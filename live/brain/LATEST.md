# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T21:17:56.167679Z`  
Memory snapshots: **338**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=9735 d1=-265.0 d12=-3527.0 z=-5.872476220654627
- **CHANGE_POINT** `ccgt_gen` value=6412 d1=-265.0 d12=-3526.0 z=-5.832219105100897
- **PERSISTENT_UP** `wind_gen` value=1.263e+04 d1=88.0 d12=872.0 z=7.274970953163017
- **ROBUST_OUTLIER** `wind_gen` value=1.263e+04 d1=88.0 d12=872.0 z=7.274970953163017
- **PERSISTENT_DOWN** `thermal_base` value=9735 d1=-265.0 d12=-3527.0 z=-5.872476220654627
- **ROBUST_OUTLIER** `thermal_base` value=9735 d1=-265.0 d12=-3527.0 z=-5.872476220654627
- **PERSISTENT_DOWN** `ccgt_gen` value=6412 d1=-265.0 d12=-3526.0 z=-5.832219105100897
- **ROBUST_OUTLIER** `ccgt_gen` value=6412 d1=-265.0 d12=-3526.0 z=-5.832219105100897
- **CHANGE_POINT** `imbalance` value=5722 d1=0.0 d12=-66.0 z=-0.9407357039473684
- **CHANGE_POINT** `ind_generation` value=2.484e+04 d1=0.0 d12=-66.0 z=-0.9407357039473684
- **PERSISTENT_DOWN** `ps_gen` value=-262 d1=0.0 d12=-5.0 z=-0.6869145611842105
- **ACCELERATION** `ps_gen` value=-262 d1=0.0 d12=-5.0 z=-0.6869145611842105
- **PERSISTENT_DOWN** `biomass_gen` value=3261 d1=-4.0 d12=-13.0 z=0.4069547094972067
- **ACCELERATION** `nuclear_gen` value=3323 d1=0.0 d12=-1.0 z=0.22482991666666666
- **PERSISTENT_UP** `interconnector_net` value=728 d1=1.0 d12=425.0 z=0.1309001875163913

## Nearest historical live analogues

- `2026-09-15T20:22:50.211969Z` distance=0.014 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:31:50.302711Z` distance=0.057 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:36:02.892054Z` distance=0.057 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:40:15.609389Z` distance=0.057 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:44:28.590533Z` distance=0.057 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

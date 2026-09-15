# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T23:32:16.606471Z`  
Memory snapshots: **370**  
Current physical regime: **BALANCED**

Regime read: wind rising.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-166.0 z=-37.546596083333334
- **PERSISTENT_UP** `thermal_base` value=6556 d1=2.0 d12=49.0 z=-9.039447392380952
- **ROBUST_OUTLIER** `thermal_base` value=6556 d1=2.0 d12=49.0 z=-9.039447392380952
- **PERSISTENT_UP** `ccgt_gen` value=3229 d1=2.0 d12=51.0 z=-8.96708327691218
- **ROBUST_OUTLIER** `ccgt_gen` value=3229 d1=2.0 d12=51.0 z=-8.96708327691218
- **CHANGE_POINT** `ind_generation` value=2.495e+04 d1=0.0 d12=12.0 z=1.8885713
- **CHANGE_POINT** `imbalance` value=5826 d1=0.0 d12=11.0 z=1.8548468125
- **CHANGE_POINT** `biomass_gen` value=3246 d1=-4.0 d12=-9.0 z=-0.8519870526315788
- **CHANGE_POINT** `wind_gen` value=1.04e+04 d1=15.0 d12=-1590.0 z=-0.325539584643091
- **PERSISTENT_DOWN** `interconnector_net` value=3938 d1=-123.0 d12=-192.0 z=2.2651719559099437
- **ACCELERATION** `interconnector_net` value=3938 d1=-123.0 d12=-192.0 z=2.2651719559099437
- **CHANGE_POINT** `ps_gen` value=25 d1=-47.0 d12=283.0 z=-0.17591541317169068
- **PERSISTENT_UP** `ind_generation` value=2.495e+04 d1=0.0 d12=12.0 z=1.8885713
- **PERSISTENT_UP** `imbalance` value=5826 d1=0.0 d12=11.0 z=1.8548468125
- **ACCELERATION** `nuclear_gen` value=3327 d1=0.0 d12=-2.0 z=1.1241495833333335

## Nearest historical live analogues

- `2026-09-15T17:50:55.506503Z` distance=0.725 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.725 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:59:22.215947Z` distance=0.725 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:03:35.364442Z` distance=0.725 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:07:47.333244Z` distance=0.725 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

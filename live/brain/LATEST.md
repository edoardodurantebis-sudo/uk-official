# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T03:40:33.171803Z`  
Memory snapshots: **1362**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `margin` value=3.831e+04 d1=0.0 d12=2.0 z=6.676159691082803
- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=2.0 z=6.676159691082803
- **CHANGE_POINT** `biomass_gen` value=693 d1=-9.0 d12=-206.0 z=-4.547696041666667
- **PERSISTENT_DOWN** `biomass_gen` value=693 d1=-9.0 d12=-206.0 z=-4.547696041666667
- **ROBUST_OUTLIER** `biomass_gen` value=693 d1=-9.0 d12=-206.0 z=-4.547696041666667
- **CHANGE_POINT** `imbalance` value=9422 d1=0.0 d12=166.0 z=2.2514657852112676
- **CHANGE_POINT** `ind_generation` value=2.662e+04 d1=0.0 d12=166.0 z=2.2295633402777777
- **CHANGE_POINT** `ccgt_gen` value=3061 d1=5.0 d12=3.0 z=-2.0474358908629444
- **CHANGE_POINT** `thermal_base` value=6407 d1=7.0 d12=6.0 z=-1.9913506904761904
- **CHANGE_POINT** `wind_gen` value=1.575e+04 d1=6.0 d12=-456.0 z=-1.1362558096153847
- **PERSISTENT_UP** `nuclear_gen` value=3346 d1=2.0 d12=3.0 z=2.360714125
- **PERSISTENT_UP** `ccgt_gen` value=3061 d1=5.0 d12=3.0 z=-2.0474358908629444
- **ACCELERATION** `ccgt_gen` value=3061 d1=5.0 d12=3.0 z=-2.0474358908629444
- **PERSISTENT_UP** `thermal_base` value=6407 d1=7.0 d12=6.0 z=-1.9913506904761904
- **ACCELERATION** `thermal_base` value=6407 d1=7.0 d12=6.0 z=-1.9913506904761904

## Nearest historical live analogues

- `2026-09-19T02:20:35.608449Z` distance=0.315 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:24:50.521130Z` distance=0.315 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:29:01.647315Z` distance=0.315 → {'next30m_imbalance_delta': 140.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:33:15.620122Z` distance=0.315 → {'next30m_imbalance_delta': 140.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:37:27.246722Z` distance=0.315 → {'next30m_imbalance_delta': 140.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

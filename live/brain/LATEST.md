# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T03:36:20.101769Z`  
Memory snapshots: **1361**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `margin` value=3.831e+04 d1=0.0 d12=2.0 z=6.718955586538462
- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=2.0 z=6.718955586538462
- **CHANGE_POINT** `biomass_gen` value=702 d1=-44.0 d12=-197.0 z=-4.494882074427481
- **PERSISTENT_DOWN** `biomass_gen` value=702 d1=-44.0 d12=-197.0 z=-4.494882074427481
- **ROBUST_OUTLIER** `biomass_gen` value=702 d1=-44.0 d12=-197.0 z=-4.494882074427481
- **CHANGE_POINT** `imbalance` value=9422 d1=0.0 d12=166.0 z=2.2514657852112676
- **CHANGE_POINT** `ind_generation` value=2.662e+04 d1=0.0 d12=166.0 z=2.2295633402777777
- **CHANGE_POINT** `wind_gen` value=1.574e+04 d1=-104.0 d12=-462.0 z=-1.162418505319149
- **PERSISTENT_DOWN** `ccgt_gen` value=3056 d1=-2.0 d12=-2.0 z=-2.07311443464467
- **ACCELERATION** `ccgt_gen` value=3056 d1=-2.0 d12=-2.0 z=-2.07311443464467
- **PERSISTENT_DOWN** `thermal_base` value=6400 d1=0.0 d12=-1.0 z=-2.0302310520050124
- **ACCELERATION** `thermal_base` value=6400 d1=0.0 d12=-1.0 z=-2.0302310520050124
- **PERSISTENT_UP** `nuclear_gen` value=3344 d1=2.0 d12=1.0 z=1.686224375
- **ACCELERATION** `nuclear_gen` value=3344 d1=2.0 d12=1.0 z=1.686224375
- **PERSISTENT_DOWN** `wind_gen` value=1.574e+04 d1=-104.0 d12=-462.0 z=-1.162418505319149

## Nearest historical live analogues

- `2026-09-19T02:20:35.608449Z` distance=0.315 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:24:50.521130Z` distance=0.315 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:29:01.647315Z` distance=0.315 → {'next30m_imbalance_delta': 140.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:33:15.620122Z` distance=0.315 → {'next30m_imbalance_delta': 140.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:37:27.246722Z` distance=0.315 → {'next30m_imbalance_delta': 140.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

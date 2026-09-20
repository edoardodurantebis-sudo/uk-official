# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T10:45:18.329775Z`  
Memory snapshots: **1804**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.978e+04 d1=0.0 d12=490.0 z=24.967177959016393
- **CHANGE_POINT** `ind_generation` value=1.603e+04 d1=0.0 d12=14.0 z=24.0118351
- **ROBUST_OUTLIER** `margin` value=3.978e+04 d1=0.0 d12=490.0 z=24.967177959016393
- **ROBUST_OUTLIER** `ind_generation` value=1.603e+04 d1=0.0 d12=14.0 z=24.0118351
- **CHANGE_POINT** `ind_demand` value=-1.247e+04 d1=0.0 d12=-107.0 z=-15.224197214285713
- **ROBUST_OUTLIER** `ind_demand` value=-1.247e+04 d1=0.0 d12=-107.0 z=-15.224197214285713
- **CHANGE_POINT** `imbalance` value=-4140 d1=0.0 d12=14.0 z=6.819984650671786
- **ROBUST_OUTLIER** `imbalance` value=-4140 d1=0.0 d12=14.0 z=6.819984650671786
- **CHANGE_POINT** `wind_gen` value=1.393e+04 d1=0.0 d12=-714.0 z=-2.781411152474527
- **PERSISTENT_DOWN** `wind_gen` value=1.393e+04 d1=0.0 d12=-714.0 z=-2.781411152474527
- **CHANGE_POINT** `ps_gen` value=-927 d1=0.0 d12=-2.0 z=-0.677448038377193
- **CHANGE_POINT** `interconnector_net` value=-5563 d1=0.0 d12=-1106.0 z=0.4929279537149817
- **PERSISTENT_UP** `ccgt_gen` value=2510 d1=0.0 d12=226.0 z=-2.123573636527378
- **ACCELERATION** `biomass_gen` value=588 d1=0.0 d12=1.0 z=-0.6883018267918088
- **PERSISTENT_DOWN** `ps_gen` value=-927 d1=0.0 d12=-2.0 z=-0.677448038377193

## Nearest historical live analogues

- `2026-09-20T09:49:28.570363Z` distance=0.204 → {'next30m_imbalance_delta': 33.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:20:07.153673Z` distance=0.336 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:24:18.809197Z` distance=0.336 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:28:32.169507Z` distance=0.336 → {'next30m_imbalance_delta': 33.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:32:44.320157Z` distance=0.336 → {'next30m_imbalance_delta': 33.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

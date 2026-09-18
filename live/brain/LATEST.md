# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T21:57:29.954779Z`  
Memory snapshots: **1281**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=7272 d1=-43.0 d12=-787.0 z=16.329453527310925
- **CHANGE_POINT** `ccgt_gen` value=3931 d1=-40.0 d12=-793.0 z=16.312449584033615
- **PERSISTENT_DOWN** `ind_generation` value=2.618e+04 d1=0.0 d12=-46.0 z=16.891569391304348
- **ACCELERATION** `ind_generation` value=2.618e+04 d1=0.0 d12=-46.0 z=16.891569391304348
- **ROBUST_OUTLIER** `ind_generation` value=2.618e+04 d1=0.0 d12=-46.0 z=16.891569391304348
- **PERSISTENT_DOWN** `thermal_base` value=7272 d1=-43.0 d12=-787.0 z=16.329453527310925
- **ROBUST_OUTLIER** `thermal_base` value=7272 d1=-43.0 d12=-787.0 z=16.329453527310925
- **PERSISTENT_DOWN** `ccgt_gen` value=3931 d1=-40.0 d12=-793.0 z=16.312449584033615
- **ROBUST_OUTLIER** `ccgt_gen` value=3931 d1=-40.0 d12=-793.0 z=16.312449584033615
- **CHANGE_POINT** `ind_demand` value=-1.089e+04 d1=0.0 d12=-4.0 z=-10.791836
- **ACCELERATION** `ind_demand` value=-1.089e+04 d1=0.0 d12=-4.0 z=-10.791836
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=0.0 d12=-4.0 z=-10.791836
- **CHANGE_POINT** `interconnector_net` value=-6518 d1=-87.0 d12=-5621.0 z=-8.501725070690592
- **PERSISTENT_DOWN** `interconnector_net` value=-6518 d1=-87.0 d12=-5621.0 z=-8.501725070690592
- **ROBUST_OUTLIER** `interconnector_net` value=-6518 d1=-87.0 d12=-5621.0 z=-8.501725070690592

## Nearest historical live analogues

- `2026-09-18T18:54:36.333288Z` distance=0.289 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:58:51.197302Z` distance=0.289 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:03:04.185551Z` distance=0.289 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:07:15.585093Z` distance=0.289 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -511.0}
- `2026-09-18T19:11:26.475262Z` distance=0.289 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -511.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

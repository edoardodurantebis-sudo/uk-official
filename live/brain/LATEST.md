# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T21:53:09.203702Z`  
Memory snapshots: **1280**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=3971 d1=15.0 d12=-838.0 z=16.90797186864407
- **CHANGE_POINT** `ind_generation` value=2.618e+04 d1=-58.0 d12=-46.0 z=16.891569391304348
- **CHANGE_POINT** `thermal_base` value=7315 d1=16.0 d12=-833.0 z=16.816899901260506
- **REVERSAL** `ccgt_gen` value=3971 d1=15.0 d12=-838.0 z=16.90797186864407
- **ROBUST_OUTLIER** `ccgt_gen` value=3971 d1=15.0 d12=-838.0 z=16.90797186864407
- **PERSISTENT_DOWN** `ind_generation` value=2.618e+04 d1=-58.0 d12=-46.0 z=16.891569391304348
- **ACCELERATION** `ind_generation` value=2.618e+04 d1=-58.0 d12=-46.0 z=16.891569391304348
- **ROBUST_OUTLIER** `ind_generation` value=2.618e+04 d1=-58.0 d12=-46.0 z=16.891569391304348
- **REVERSAL** `thermal_base` value=7315 d1=16.0 d12=-833.0 z=16.816899901260506
- **ROBUST_OUTLIER** `thermal_base` value=7315 d1=16.0 d12=-833.0 z=16.816899901260506
- **CHANGE_POINT** `interconnector_net` value=-6431 d1=-28.0 d12=-5624.0 z=-9.128226869558823
- **REVERSAL** `ind_demand` value=-1.089e+04 d1=2.0 d12=-4.0 z=-10.791836
- **ACCELERATION** `ind_demand` value=-1.089e+04 d1=2.0 d12=-4.0 z=-10.791836
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=2.0 d12=-4.0 z=-10.791836
- **PERSISTENT_DOWN** `interconnector_net` value=-6431 d1=-28.0 d12=-5624.0 z=-9.128226869558823

## Nearest historical live analogues

- `2026-09-18T18:54:36.333288Z` distance=0.289 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:58:51.197302Z` distance=0.289 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:03:04.185551Z` distance=0.289 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T19:07:15.585093Z` distance=0.289 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -511.0}
- `2026-09-18T19:11:26.475262Z` distance=0.289 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -511.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T08:21:01.012290Z`  
Memory snapshots: **800**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.214e+04 d1=-3.0 d12=-3.0 z=-6.79929183467742
- **CHANGE_POINT** `wind_gen` value=1.563e+04 d1=107.0 d12=1286.0 z=6.0895298820876285
- **PERSISTENT_DOWN** `ind_demand` value=-1.214e+04 d1=-3.0 d12=-3.0 z=-6.79929183467742
- **ACCELERATION** `ind_demand` value=-1.214e+04 d1=-3.0 d12=-3.0 z=-6.79929183467742
- **ROBUST_OUTLIER** `ind_demand` value=-1.214e+04 d1=-3.0 d12=-3.0 z=-6.79929183467742
- **PERSISTENT_UP** `wind_gen` value=1.563e+04 d1=107.0 d12=1286.0 z=6.0895298820876285
- **ROBUST_OUTLIER** `wind_gen` value=1.563e+04 d1=107.0 d12=1286.0 z=6.0895298820876285
- **PERSISTENT_UP** `margin` value=3.605e+04 d1=471.0 d12=471.0 z=6.011756467391304
- **ACCELERATION** `margin` value=3.605e+04 d1=471.0 d12=471.0 z=6.011756467391304
- **ROBUST_OUTLIER** `margin` value=3.605e+04 d1=471.0 d12=471.0 z=6.011756467391304
- **PERSISTENT_UP** `interconnector_net` value=4898 d1=0.0 d12=5278.0 z=5.144581355731548
- **ROBUST_OUTLIER** `interconnector_net` value=4898 d1=0.0 d12=5278.0 z=5.144581355731548
- **CHANGE_POINT** `biomass_gen` value=2031 d1=2.0 d12=-703.0 z=-1.4436605477941178
- **PERSISTENT_UP** `imbalance` value=7525 d1=368.0 d12=368.0 z=2.3524886402439025
- **ACCELERATION** `imbalance` value=7525 d1=368.0 d12=368.0 z=2.3524886402439025

## Nearest historical live analogues

- `2026-09-17T06:52:29.952634Z` distance=0.218 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:56:43.028097Z` distance=0.218 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:00:51.548981Z` distance=0.218 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:05:06.905847Z` distance=0.218 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:09:19.225959Z` distance=0.218 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

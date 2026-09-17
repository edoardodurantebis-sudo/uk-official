# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T12:42:21.058328Z`  
Memory snapshots: **862**  
Current physical regime: **BALANCED**

Regime read: residual low, wind falling.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.848e+04 d1=0.0 d12=-38.0 z=27.45735357291667
- **ROBUST_OUTLIER** `ind_generation` value=2.848e+04 d1=0.0 d12=-38.0 z=27.45735357291667
- **PERSISTENT_DOWN** `wind_forecast` value=1.898e+04 d1=0.0 d12=-47.0 z=-18.21122325
- **ROBUST_OUTLIER** `wind_forecast` value=1.898e+04 d1=0.0 d12=-47.0 z=-18.21122325
- **CHANGE_POINT** `imbalance` value=1.194e+04 d1=0.0 d12=-38.0 z=7.442031989808154
- **ROBUST_OUTLIER** `imbalance` value=1.194e+04 d1=0.0 d12=-38.0 z=7.442031989808154
- **ROBUST_OUTLIER** `demand_forecast` value=1.604e+04 d1=0.0 d12=0.0 z=-4.089440593835617
- **CHANGE_POINT** `wind_gen` value=1.414e+04 d1=-75.0 d12=-1028.0 z=-2.0053794865900385
- **PERSISTENT_UP** `residual_proxy` value=-2942 d1=0.0 d12=47.0 z=-3.6916438992957747
- **ROBUST_OUTLIER** `residual_proxy` value=-2942 d1=0.0 d12=47.0 z=-3.6916438992957747
- **CHANGE_POINT** `ps_gen` value=-650 d1=265.0 d12=294.0 z=0.272933061627907
- **PERSISTENT_DOWN** `wind_gen` value=1.414e+04 d1=-75.0 d12=-1028.0 z=-2.0053794865900385
- **PERSISTENT_DOWN** `biomass_gen` value=1972 d1=-16.0 d12=-50.0 z=-1.006847018115942
- **PERSISTENT_UP** `nuclear_gen` value=3308 d1=4.0 d12=4.0 z=-0.8993196666666666
- **ACCELERATION** `nuclear_gen` value=3308 d1=4.0 d12=4.0 z=-0.8993196666666666

## Nearest historical live analogues

- `2026-09-17T10:57:20.878127Z` distance=0.215 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:01:31.274983Z` distance=0.215 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:05:43.396655Z` distance=0.215 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:09:56.284661Z` distance=0.215 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:14:08.992825Z` distance=0.215 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

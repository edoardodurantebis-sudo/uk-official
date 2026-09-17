# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T13:11:56.026063Z`  
Memory snapshots: **869**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=2.848e+04 d1=0.0 d12=-27.0 z=27.41519796354167
- **ROBUST_OUTLIER** `wind_forecast` value=1.898e+04 d1=0.0 d12=-47.0 z=-18.21122325
- **CHANGE_POINT** `biomass_gen` value=1905 d1=1.0 d12=-113.0 z=-2.697959
- **ROBUST_OUTLIER** `imbalance` value=1.194e+04 d1=0.0 d12=-27.0 z=4.6214664457335335
- **ROBUST_OUTLIER** `demand_forecast` value=1.604e+04 d1=0.0 d12=0.0 z=-4.089440593835617
- **ROBUST_OUTLIER** `residual_proxy` value=-2942 d1=0.0 d12=47.0 z=-3.6916438992957747
- **PERSISTENT_DOWN** `wind_gen` value=1.346e+04 d1=-67.0 d12=-705.0 z=-3.1786298563218387
- **ACCELERATION** `wind_gen` value=1.346e+04 d1=-67.0 d12=-705.0 z=-3.1786298563218387
- **ROBUST_OUTLIER** `wind_gen` value=1.346e+04 d1=-67.0 d12=-705.0 z=-3.1786298563218387
- **REVERSAL** `biomass_gen` value=1905 d1=1.0 d12=-113.0 z=-2.697959
- **CHANGE_POINT** `ps_gen` value=-686 d1=2.0 d12=261.0 z=0.6898773488593156
- **CHANGE_POINT** `thermal_base` value=5242 d1=30.0 d12=123.0 z=0.31555076023391815
- **CHANGE_POINT** `ccgt_gen` value=1936 d1=31.0 d12=128.0 z=0.29014363547486033
- **PERSISTENT_UP** `ps_gen` value=-686 d1=2.0 d12=261.0 z=0.6898773488593156
- **PERSISTENT_UP** `thermal_base` value=5242 d1=30.0 d12=123.0 z=0.31555076023391815

## Nearest historical live analogues

- `2026-09-17T11:51:58.101795Z` distance=0.174 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T11:56:11.138716Z` distance=0.174 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T12:00:23.510142Z` distance=0.174 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T12:04:34.286599Z` distance=0.174 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T12:08:43.971933Z` distance=0.174 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 47.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

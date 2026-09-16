# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T10:38:18.420163Z`  
Memory snapshots: **528**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low, wind rising.

## Active patterns

- **ROBUST_OUTLIER** `ps_gen` value=-5 d1=0.0 d12=-235.0 z=-30.7567326
- **ROBUST_OUTLIER** `margin` value=3.422e+04 d1=0.0 d12=-284.0 z=-14.78295465862069
- **CHANGE_POINT** `imbalance` value=5373 d1=0.0 d12=9.0 z=-10.93051613551402
- **ROBUST_OUTLIER** `imbalance` value=5373 d1=0.0 d12=9.0 z=-10.93051613551402
- **ROBUST_OUTLIER** `ind_demand` value=-1.511e+04 d1=0.0 d12=-1226.0 z=-7.156634214859437
- **PERSISTENT_DOWN** `residual_proxy` value=-1246 d1=0.0 d12=-433.0 z=-3.6989533423566883
- **ACCELERATION** `residual_proxy` value=-1246 d1=0.0 d12=-433.0 z=-3.6989533423566883
- **ROBUST_OUTLIER** `residual_proxy` value=-1246 d1=0.0 d12=-433.0 z=-3.6989533423566883
- **CHANGE_POINT** `ind_generation` value=2.601e+04 d1=0.0 d12=9.0 z=-1.6059279761904761
- **PERSISTENT_UP** `wind_forecast` value=1.976e+04 d1=0.0 d12=433.0 z=3.2392692452229297
- **ACCELERATION** `wind_forecast` value=1.976e+04 d1=0.0 d12=433.0 z=3.2392692452229297
- **ROBUST_OUTLIER** `wind_forecast` value=1.976e+04 d1=0.0 d12=433.0 z=3.2392692452229297
- **PERSISTENT_DOWN** `nuclear_gen` value=3323 d1=-1.0 d12=-1.0 z=-2.0234692499999998
- **ACCELERATION** `nuclear_gen` value=3323 d1=-1.0 d12=-1.0 z=-2.0234692499999998
- **PERSISTENT_DOWN** `wind_gen` value=4929 d1=-151.0 d12=-728.0 z=-1.6144459049831081

## Nearest historical live analogues

- `2026-09-16T09:22:28.850484Z` distance=2.957 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:26:41.423464Z` distance=2.957 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:30:50.292124Z` distance=2.957 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:35:00.318078Z` distance=2.957 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:39:12.760497Z` distance=2.957 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

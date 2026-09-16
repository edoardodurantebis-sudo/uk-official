# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T10:21:27.701459Z`  
Memory snapshots: **524**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **PERSISTENT_DOWN** `ps_gen` value=-5 d1=0.0 d12=-235.0 z=-30.7567326
- **ROBUST_OUTLIER** `ps_gen` value=-5 d1=0.0 d12=-235.0 z=-30.7567326
- **REVERSAL** `margin` value=3.422e+04 d1=65.0 d12=-284.0 z=-14.78295465862069
- **ROBUST_OUTLIER** `margin` value=3.422e+04 d1=65.0 d12=-284.0 z=-14.78295465862069
- **PERSISTENT_UP** `imbalance` value=5373 d1=6.0 d12=9.0 z=-10.93051613551402
- **ACCELERATION** `imbalance` value=5373 d1=6.0 d12=9.0 z=-10.93051613551402
- **ROBUST_OUTLIER** `imbalance` value=5373 d1=6.0 d12=9.0 z=-10.93051613551402
- **CHANGE_POINT** `ind_demand` value=-1.511e+04 d1=-1226.0 d12=-1226.0 z=-7.156634214859437
- **PERSISTENT_DOWN** `ind_demand` value=-1.511e+04 d1=-1226.0 d12=-1226.0 z=-7.156634214859437
- **ACCELERATION** `ind_demand` value=-1.511e+04 d1=-1226.0 d12=-1226.0 z=-7.156634214859437
- **ROBUST_OUTLIER** `ind_demand` value=-1.511e+04 d1=-1226.0 d12=-1226.0 z=-7.156634214859437
- **PERSISTENT_UP** `ind_generation` value=2.601e+04 d1=6.0 d12=9.0 z=-1.6059279761904761
- **ACCELERATION** `ind_generation` value=2.601e+04 d1=6.0 d12=9.0 z=-1.6059279761904761
- **PERSISTENT_DOWN** `wind_gen` value=5248 d1=-58.0 d12=-428.0 z=-1.46490742578125
- **ACCELERATION** `nuclear_gen` value=3325 d1=0.0 d12=1.0 z=-1.3489795

## Nearest historical live analogues

- `2026-09-16T09:22:28.850484Z` distance=3.163 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:26:41.423464Z` distance=3.163 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:52:24.970739Z` distance=6.308 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=6.308 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=6.308 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

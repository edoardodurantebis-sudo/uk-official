# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T10:25:37.865190Z`  
Memory snapshots: **525**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ps_gen` value=-5 d1=0.0 d12=-235.0 z=-30.7567326
- **ROBUST_OUTLIER** `margin` value=3.422e+04 d1=0.0 d12=-284.0 z=-14.78295465862069
- **PERSISTENT_UP** `imbalance` value=5373 d1=0.0 d12=9.0 z=-10.93051613551402
- **ACCELERATION** `imbalance` value=5373 d1=0.0 d12=9.0 z=-10.93051613551402
- **ROBUST_OUTLIER** `imbalance` value=5373 d1=0.0 d12=9.0 z=-10.93051613551402
- **CHANGE_POINT** `ind_demand` value=-1.511e+04 d1=0.0 d12=-1226.0 z=-7.156634214859437
- **PERSISTENT_DOWN** `ind_demand` value=-1.511e+04 d1=0.0 d12=-1226.0 z=-7.156634214859437
- **ACCELERATION** `ind_demand` value=-1.511e+04 d1=0.0 d12=-1226.0 z=-7.156634214859437
- **ROBUST_OUTLIER** `ind_demand` value=-1.511e+04 d1=0.0 d12=-1226.0 z=-7.156634214859437
- **PERSISTENT_UP** `ind_generation` value=2.601e+04 d1=0.0 d12=9.0 z=-1.6059279761904761
- **ACCELERATION** `ind_generation` value=2.601e+04 d1=0.0 d12=9.0 z=-1.6059279761904761
- **PERSISTENT_DOWN** `wind_gen` value=5248 d1=0.0 d12=-428.0 z=-1.4560775346283783
- **PERSISTENT_UP** `biomass_gen` value=3227 d1=0.0 d12=79.0 z=-1.1241495833333335
- **ACCELERATION** `interconnector_net` value=1.026e+04 d1=0.0 d12=-50.0 z=0.7458806661729059

## Nearest historical live analogues

- `2026-09-16T09:22:28.850484Z` distance=3.163 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:26:41.423464Z` distance=3.163 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:30:50.292124Z` distance=3.163 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:52:24.970739Z` distance=6.308 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=6.308 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

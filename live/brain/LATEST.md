# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T11:16:19.678566Z`  
Memory snapshots: **537**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-5 d1=0.0 d12=0.0 z=-23.659025076923076
- **ROBUST_OUTLIER** `ps_gen` value=-5 d1=0.0 d12=0.0 z=-23.659025076923076
- **CHANGE_POINT** `ind_generation` value=2.473e+04 d1=0.0 d12=-1277.0 z=-8.441828061507938
- **CHANGE_POINT** `imbalance` value=4364 d1=0.0 d12=-1009.0 z=-8.086177345319635
- **ROBUST_OUTLIER** `ind_generation` value=2.473e+04 d1=0.0 d12=-1277.0 z=-8.441828061507938
- **ROBUST_OUTLIER** `imbalance` value=4364 d1=0.0 d12=-1009.0 z=-8.086177345319635
- **ROBUST_OUTLIER** `demand_forecast` value=1.987e+04 d1=0.0 d12=1356.0 z=7.873249511682243
- **CHANGE_POINT** `nuclear_gen` value=3318 d1=2.0 d12=-7.0 z=-2.248299166666667
- **CHANGE_POINT** `wind_gen` value=4463 d1=-131.0 d12=-785.0 z=-1.8125791864481842
- **CHANGE_POINT** `margin` value=3.34e+04 d1=0.0 d12=-822.0 z=-1.648439414088629
- **ROBUST_OUTLIER** `wind_forecast` value=1.976e+04 d1=0.0 d12=433.0 z=3.2392692452229297
- **CHANGE_POINT** `interconnector_net` value=1.078e+04 d1=27.0 d12=522.0 z=1.2074952124773959
- **CHANGE_POINT** `thermal_base` value=9589 d1=133.0 d12=-85.0 z=-1.0568589392605634
- **CHANGE_POINT** `ccgt_gen` value=6271 d1=131.0 d12=-78.0 z=-1.0463898529066353
- **REVERSAL** `nuclear_gen` value=3318 d1=2.0 d12=-7.0 z=-2.248299166666667

## Nearest historical live analogues

- `2026-09-15T14:53:30.277508Z` distance=1.506 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T14:57:40.419064Z` distance=1.506 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:01:51.072857Z` distance=1.506 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:06:01.576691Z` distance=1.506 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:10:11.843860Z` distance=1.506 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 24.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

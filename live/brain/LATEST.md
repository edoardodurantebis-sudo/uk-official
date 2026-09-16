# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T11:12:08.786488Z`  
Memory snapshots: **536**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-5 d1=0.0 d12=0.0 z=-25.6306105
- **ROBUST_OUTLIER** `ps_gen` value=-5 d1=0.0 d12=0.0 z=-25.6306105
- **ROBUST_OUTLIER** `demand_forecast` value=1.987e+04 d1=0.0 d12=1356.0 z=15.746499023364485
- **CHANGE_POINT** `imbalance` value=4364 d1=0.0 d12=-1009.0 z=-8.937803788647344
- **CHANGE_POINT** `ind_generation` value=2.473e+04 d1=0.0 d12=-1277.0 z=-8.441828061507938
- **ROBUST_OUTLIER** `imbalance` value=4364 d1=0.0 d12=-1009.0 z=-8.937803788647344
- **ROBUST_OUTLIER** `ind_generation` value=2.473e+04 d1=0.0 d12=-1277.0 z=-8.441828061507938
- **CHANGE_POINT** `nuclear_gen` value=3316 d1=4.0 d12=-9.0 z=-2.6979589999999996
- **CHANGE_POINT** `margin` value=3.34e+04 d1=0.0 d12=-822.0 z=-1.9015170003477053
- **CHANGE_POINT** `wind_gen` value=4594 d1=-86.0 d12=-654.0 z=-1.7548618781938325
- **ROBUST_OUTLIER** `wind_forecast` value=1.976e+04 d1=0.0 d12=433.0 z=3.2392692452229297
- **CHANGE_POINT** `interconnector_net` value=1.075e+04 d1=31.0 d12=495.0 z=1.1745635248643762
- **CHANGE_POINT** `thermal_base` value=9456 d1=26.0 d12=-218.0 z=-1.1621490058685446
- **CHANGE_POINT** `ccgt_gen` value=6140 d1=22.0 d12=-209.0 z=-1.1501575067527892
- **REVERSAL** `nuclear_gen` value=3316 d1=4.0 d12=-9.0 z=-2.6979589999999996

## Nearest historical live analogues

- `2026-09-15T14:53:30.277508Z` distance=1.506 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T14:57:40.419064Z` distance=1.506 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:01:51.072857Z` distance=1.506 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:06:01.576691Z` distance=1.506 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:10:11.843860Z` distance=1.506 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 24.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T02:58:27.254129Z`  
Memory snapshots: **1352**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.831e+04 d1=0.0 d12=1197.0 z=6.354831138554217
- **PERSISTENT_UP** `margin` value=3.831e+04 d1=0.0 d12=1197.0 z=6.354831138554217
- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=1197.0 z=6.354831138554217
- **CHANGE_POINT** `biomass_gen` value=882 d1=3.0 d12=-260.0 z=-2.7729023055555557
- **CHANGE_POINT** `imbalance` value=9396 d1=0.0 d12=155.0 z=2.2828883846153847
- **CHANGE_POINT** `ccgt_gen` value=3057 d1=2.0 d12=-414.0 z=-2.1607103405707195
- **CHANGE_POINT** `thermal_base` value=6395 d1=-1.0 d12=-413.0 z=-2.1467093524691356
- **CHANGE_POINT** `ind_generation` value=2.659e+04 d1=0.0 d12=156.0 z=1.7354848623595507
- **CHANGE_POINT** `interconnector_net` value=-1.118e+04 d1=1.0 d12=13.0 z=-1.07130111686587
- **REVERSAL** `biomass_gen` value=882 d1=3.0 d12=-260.0 z=-2.7729023055555557
- **PERSISTENT_UP** `imbalance` value=9396 d1=0.0 d12=155.0 z=2.2828883846153847
- **ACCELERATION** `imbalance` value=9396 d1=0.0 d12=155.0 z=2.2828883846153847
- **REVERSAL** `ccgt_gen` value=3057 d1=2.0 d12=-414.0 z=-2.1607103405707195
- **PERSISTENT_DOWN** `thermal_base` value=6395 d1=-1.0 d12=-413.0 z=-2.1467093524691356
- **CHANGE_POINT** `ps_gen` value=-542 d1=0.0 d12=211.0 z=-0.1360315462184874

## Nearest historical live analogues

- `2026-09-19T00:22:06.996302Z` distance=0.274 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:26:19.516071Z` distance=0.274 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:30:34.705011Z` distance=0.274 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:34:45.510432Z` distance=0.274 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:38:55.391009Z` distance=0.274 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

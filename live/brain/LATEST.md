# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T02:50:02.239464Z`  
Memory snapshots: **1350**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.831e+04 d1=0.0 d12=1195.0 z=6.338578373493975
- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=1195.0 z=6.338578373493975
- **CHANGE_POINT** `biomass_gen` value=899 d1=0.0 d12=-241.0 z=-2.61702023
- **CHANGE_POINT** `ccgt_gen` value=3058 d1=0.0 d12=-582.0 z=-2.0939622404988123
- **CHANGE_POINT** `thermal_base` value=6401 d1=0.0 d12=-576.0 z=-2.0782011151551316
- **CHANGE_POINT** `interconnector_net` value=-1.118e+04 d1=0.0 d12=-44.0 z=-1.076675537184595
- **CHANGE_POINT** `ind_generation` value=2.645e+04 d1=0.0 d12=16.0 z=1.0168703337563452
- **CHANGE_POINT** `imbalance` value=9256 d1=0.0 d12=15.0 z=0.8211179565217391
- **PERSISTENT_DOWN** `biomass_gen` value=899 d1=0.0 d12=-241.0 z=-2.61702023
- **CHANGE_POINT** `ps_gen` value=-543 d1=0.0 d12=288.0 z=-0.18159339423076923
- **PERSISTENT_DOWN** `ccgt_gen` value=3058 d1=0.0 d12=-582.0 z=-2.0939622404988123
- **PERSISTENT_DOWN** `thermal_base` value=6401 d1=0.0 d12=-576.0 z=-2.0782011151551316
- **PERSISTENT_UP** `nuclear_gen` value=3343 d1=0.0 d12=6.0 z=1.686224375
- **PERSISTENT_DOWN** `interconnector_net` value=-1.118e+04 d1=0.0 d12=-44.0 z=-1.076675537184595
- **PERSISTENT_DOWN** `wind_gen` value=1.62e+04 d1=0.0 d12=-335.0 z=-0.29568300660211266

## Nearest historical live analogues

- `2026-09-19T00:22:06.996302Z` distance=0.276 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:26:19.516071Z` distance=0.276 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:30:34.705011Z` distance=0.276 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:34:45.510432Z` distance=0.276 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:38:55.391009Z` distance=0.276 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

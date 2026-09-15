# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T20:31:49.811988Z`  
Memory snapshots: **327**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `wind_gen` value=1.186e+04 d1=107.0 d12=1351.0 z=5.615173621212121
- **PERSISTENT_UP** `wind_gen` value=1.186e+04 d1=107.0 d12=1351.0 z=5.615173621212121
- **ROBUST_OUTLIER** `wind_gen` value=1.186e+04 d1=107.0 d12=1351.0 z=5.615173621212121
- **CHANGE_POINT** `thermal_base` value=1.297e+04 d1=-288.0 d12=-859.0 z=-0.9409360395033859
- **CHANGE_POINT** `ccgt_gen` value=9653 d1=-285.0 d12=-857.0 z=-0.9308261011771299
- **CHANGE_POINT** `ps_gen` value=-258 d1=-1.0 d12=-681.0 z=-0.6798146690789474
- **CHANGE_POINT** `imbalance` value=5788 d1=0.0 d12=32.0 z=0.30833817142857145
- **CHANGE_POINT** `ind_generation` value=2.491e+04 d1=0.0 d12=32.0 z=0.30833817142857145
- **PERSISTENT_UP** `margin` value=3.57e+04 d1=0.0 d12=52.0 z=1.4484617640117994
- **PERSISTENT_DOWN** `thermal_base` value=1.297e+04 d1=-288.0 d12=-859.0 z=-0.9409360395033859
- **PERSISTENT_DOWN** `ccgt_gen` value=9653 d1=-285.0 d12=-857.0 z=-0.9308261011771299
- **PERSISTENT_DOWN** `ps_gen` value=-258 d1=-1.0 d12=-681.0 z=-0.6798146690789474
- **PERSISTENT_DOWN** `ind_demand` value=-1.191e+04 d1=0.0 d12=-3.0 z=0.67448975
- **PERSISTENT_UP** `biomass_gen` value=3274 d1=0.0 d12=8.0 z=0.6449334575842696
- **PERSISTENT_UP** `imbalance` value=5788 d1=0.0 d12=32.0 z=0.30833817142857145

## Nearest historical live analogues

- `2026-09-15T19:31:50.302711Z` distance=0.034 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:36:02.892054Z` distance=0.034 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:50:55.506503Z` distance=0.086 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.086 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:59:22.215947Z` distance=0.086 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T20:27:39.367678Z`  
Memory snapshots: **326**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `wind_gen` value=1.175e+04 d1=267.0 d12=1244.0 z=5.241695825757576
- **PERSISTENT_UP** `wind_gen` value=1.175e+04 d1=267.0 d12=1244.0 z=5.241695825757576
- **ROBUST_OUTLIER** `wind_gen` value=1.175e+04 d1=267.0 d12=1244.0 z=5.241695825757576
- **CHANGE_POINT** `ps_gen` value=-257 d1=0.0 d12=-680.0 z=-0.6780396960526316
- **CHANGE_POINT** `imbalance` value=5788 d1=0.0 d12=32.0 z=0.30833817142857145
- **CHANGE_POINT** `ind_generation` value=2.491e+04 d1=0.0 d12=32.0 z=0.30833817142857145
- **PERSISTENT_UP** `margin` value=3.57e+04 d1=0.0 d12=52.0 z=1.4484617640117994
- **ACCELERATION** `margin` value=3.57e+04 d1=0.0 d12=52.0 z=1.4484617640117994
- **PERSISTENT_DOWN** `ps_gen` value=-257 d1=0.0 d12=-680.0 z=-0.6780396960526316
- **PERSISTENT_DOWN** `ind_demand` value=-1.191e+04 d1=0.0 d12=-3.0 z=0.67448975
- **ACCELERATION** `ind_demand` value=-1.191e+04 d1=0.0 d12=-3.0 z=0.67448975
- **REVERSAL** `biomass_gen` value=3274 d1=-1.0 d12=8.0 z=0.6498364226804123
- **ACCELERATION** `biomass_gen` value=3274 d1=-1.0 d12=8.0 z=0.6498364226804123
- **PERSISTENT_DOWN** `thermal_base` value=1.326e+04 d1=-480.0 d12=-571.0 z=-0.4622671183800623
- **ACCELERATION** `thermal_base` value=1.326e+04 d1=-480.0 d12=-571.0 z=-0.4622671183800623

## Nearest historical live analogues

- `2026-09-15T19:31:50.302711Z` distance=0.034 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:50:55.506503Z` distance=0.086 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.086 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:59:22.215947Z` distance=0.086 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:03:35.364442Z` distance=0.086 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

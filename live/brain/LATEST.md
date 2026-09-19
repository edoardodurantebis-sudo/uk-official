# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T22:29:16.794263Z`  
Memory snapshots: **1630**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-16 d1=-3.0 d12=-633.0 z=-75.542852
- **PERSISTENT_DOWN** `ps_gen` value=-16 d1=-3.0 d12=-633.0 z=-75.542852
- **ROBUST_OUTLIER** `ps_gen` value=-16 d1=-3.0 d12=-633.0 z=-75.542852
- **CHANGE_POINT** `wind_gen` value=1.518e+04 d1=99.0 d12=538.0 z=2.9250149554455445
- **CHANGE_POINT** `thermal_base` value=7941 d1=-286.0 d12=-1431.0 z=-1.8784400753600823
- **CHANGE_POINT** `ccgt_gen` value=4601 d1=-285.0 d12=-1434.0 z=-1.8772608379345603
- **PERSISTENT_UP** `wind_gen` value=1.518e+04 d1=99.0 d12=538.0 z=2.9250149554455445
- **REVERSAL** `interconnector_net` value=-7077 d1=26.0 d12=-821.0 z=-2.597637780866426
- **PERSISTENT_UP** `margin` value=3.607e+04 d1=0.0 d12=6.0 z=-2.495612075
- **PERSISTENT_DOWN** `thermal_base` value=7941 d1=-286.0 d12=-1431.0 z=-1.8784400753600823
- **PERSISTENT_DOWN** `ccgt_gen` value=4601 d1=-285.0 d12=-1434.0 z=-1.8772608379345603
- **REVERSAL** `nuclear_gen` value=3340 d1=-1.0 d12=3.0 z=1.7986393333333333
- **PERSISTENT_DOWN** `imbalance` value=-3915 d1=0.0 d12=-16.0 z=-0.7782574038461538
- **ACCELERATION** `imbalance` value=-3915 d1=0.0 d12=-16.0 z=-0.7782574038461538
- **PERSISTENT_DOWN** `ind_generation` value=1.604e+04 d1=0.0 d12=-16.0 z=-0.7782574038461538

## Nearest historical live analogues

- `2026-09-19T21:22:12.336443Z` distance=0.002 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:26:23.241124Z` distance=0.002 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:30:37.100220Z` distance=0.002 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:34:48.991316Z` distance=0.002 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T19:32:46.079639Z` distance=0.039 → {'next30m_imbalance_delta': -36.0, 'next30m_margin_delta': 40.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

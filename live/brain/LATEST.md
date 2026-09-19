# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T22:25:06.371138Z`  
Memory snapshots: **1629**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-13 d1=0.0 d12=-687.0 z=-75.2730561
- **PERSISTENT_DOWN** `ps_gen` value=-13 d1=0.0 d12=-687.0 z=-75.2730561
- **ROBUST_OUTLIER** `ps_gen` value=-13 d1=0.0 d12=-687.0 z=-75.2730561
- **CHANGE_POINT** `wind_gen` value=1.508e+04 d1=0.0 d12=614.0 z=2.7365012714285712
- **CHANGE_POINT** `ccgt_gen` value=4886 d1=0.0 d12=-1171.0 z=-1.4841533149284254
- **CHANGE_POINT** `thermal_base` value=8227 d1=0.0 d12=-1167.0 z=-1.4815181237139918
- **PERSISTENT_UP** `wind_gen` value=1.508e+04 d1=0.0 d12=614.0 z=2.7365012714285712
- **PERSISTENT_DOWN** `interconnector_net` value=-7103 d1=0.0 d12=-847.0 z=-2.611242369086313
- **PERSISTENT_UP** `margin` value=3.607e+04 d1=0.0 d12=6.0 z=-2.495612075
- **PERSISTENT_DOWN** `ccgt_gen` value=4886 d1=0.0 d12=-1171.0 z=-1.4841533149284254
- **PERSISTENT_DOWN** `thermal_base` value=8227 d1=0.0 d12=-1167.0 z=-1.4815181237139918
- **PERSISTENT_DOWN** `imbalance` value=-3915 d1=-22.0 d12=-16.0 z=-0.7782574038461538
- **ACCELERATION** `imbalance` value=-3915 d1=-22.0 d12=-16.0 z=-0.7782574038461538
- **PERSISTENT_DOWN** `ind_generation` value=1.604e+04 d1=-22.0 d12=-16.0 z=-0.7782574038461538
- **ACCELERATION** `ind_generation` value=1.604e+04 d1=-22.0 d12=-16.0 z=-0.7782574038461538

## Nearest historical live analogues

- `2026-09-19T21:22:12.336443Z` distance=0.002 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:26:23.241124Z` distance=0.002 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:30:37.100220Z` distance=0.002 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T19:32:46.079639Z` distance=0.039 → {'next30m_imbalance_delta': -36.0, 'next30m_margin_delta': 40.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T19:36:58.290416Z` distance=0.039 → {'next30m_imbalance_delta': -36.0, 'next30m_margin_delta': 40.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

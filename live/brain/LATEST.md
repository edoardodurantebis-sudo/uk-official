# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T18:16:13.545561Z`  
Memory snapshots: **295**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=3261 d1=11.0 d12=255.0 z=46.570451375
- **ROBUST_OUTLIER** `biomass_gen` value=3261 d1=11.0 d12=255.0 z=46.570451375
- **CHANGE_POINT** `ccgt_gen` value=1.07e+04 d1=83.0 d12=304.0 z=5.8527620265846
- **CHANGE_POINT** `thermal_base` value=1.401e+04 d1=80.0 d12=300.0 z=5.852419457240294
- **PERSISTENT_UP** `ccgt_gen` value=1.07e+04 d1=83.0 d12=304.0 z=5.8527620265846
- **ROBUST_OUTLIER** `ccgt_gen` value=1.07e+04 d1=83.0 d12=304.0 z=5.8527620265846
- **PERSISTENT_UP** `thermal_base` value=1.401e+04 d1=80.0 d12=300.0 z=5.852419457240294
- **ROBUST_OUTLIER** `thermal_base` value=1.401e+04 d1=80.0 d12=300.0 z=5.852419457240294
- **CHANGE_POINT** `margin` value=3.567e+04 d1=0.0 d12=851.0 z=2.2579347345238094
- **CHANGE_POINT** `ps_gen` value=804 d1=-2.0 d12=303.0 z=1.087902858283804
- **CHANGE_POINT** `imbalance` value=5775 d1=0.0 d12=3.0 z=0.05764869658119658
- **CHANGE_POINT** `ind_generation` value=2.49e+04 d1=0.0 d12=3.0 z=0.05764869658119658
- **ACCELERATION** `nuclear_gen` value=3315 d1=-3.0 d12=-4.0 z=-2.0234692499999998
- **REVERSAL** `ps_gen` value=804 d1=-2.0 d12=303.0 z=1.087902858283804
- **PERSISTENT_DOWN** `wind_gen` value=1.004e+04 d1=-97.0 d12=-503.0 z=-1.0028384772182255

## Nearest historical live analogues

- `2026-09-15T11:22:30.581865Z` distance=0.186 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:26:42.593420Z` distance=0.186 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:30:55.285075Z` distance=0.186 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:35:06.452199Z` distance=0.186 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:39:18.571623Z` distance=0.186 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

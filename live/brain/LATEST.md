# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T16:51:21.952148Z`  
Memory snapshots: **275**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2614 d1=112.0 d12=866.0 z=25.558856271276593
- **PERSISTENT_UP** `biomass_gen` value=2614 d1=112.0 d12=866.0 z=25.558856271276593
- **ROBUST_OUTLIER** `biomass_gen` value=2614 d1=112.0 d12=866.0 z=25.558856271276593
- **PERSISTENT_UP** `ccgt_gen` value=1.024e+04 d1=73.0 d12=3159.0 z=22.036784116122842
- **ROBUST_OUTLIER** `ccgt_gen` value=1.024e+04 d1=73.0 d12=3159.0 z=22.036784116122842
- **PERSISTENT_UP** `thermal_base` value=1.356e+04 d1=74.0 d12=3154.0 z=21.79909838403042
- **ROBUST_OUTLIER** `thermal_base` value=1.356e+04 d1=74.0 d12=3154.0 z=21.79909838403042
- **PERSISTENT_DOWN** `interconnector_net` value=505 d1=-15.0 d12=-3841.0 z=-12.243246891873891
- **ROBUST_OUTLIER** `interconnector_net` value=505 d1=-15.0 d12=-3841.0 z=-12.243246891873891
- **CHANGE_POINT** `ps_gen` value=432 d1=5.0 d12=577.0 z=3.6367225116959063
- **PERSISTENT_UP** `ps_gen` value=432 d1=5.0 d12=577.0 z=3.6367225116959063
- **ROBUST_OUTLIER** `ps_gen` value=432 d1=5.0 d12=577.0 z=3.6367225116959063
- **CHANGE_POINT** `imbalance` value=5827 d1=0.0 d12=2.0 z=1.2429882535714287
- **CHANGE_POINT** `ind_generation` value=2.495e+04 d1=0.0 d12=2.0 z=1.2429882535714287
- **CHANGE_POINT** `margin` value=3.483e+04 d1=-85.0 d12=-139.0 z=-1.1602621606217618

## Nearest historical live analogues

- `2026-09-15T15:56:36.878520Z` distance=0.136 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:52:27.365496Z` distance=0.136 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:22:47.712669Z` distance=0.174 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:27:19.632279Z` distance=0.174 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 320.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:31:31.060425Z` distance=0.174 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 320.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

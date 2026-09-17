# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T07:13:31.884291Z`  
Memory snapshots: **784**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.213e+04 d1=0.0 d12=-311.0 z=-6.668745431451613
- **ROBUST_OUTLIER** `ind_demand` value=-1.213e+04 d1=0.0 d12=-311.0 z=-6.668745431451613
- **CHANGE_POINT** `margin` value=3.573e+04 d1=0.0 d12=-42.0 z=-3.2844718260869565
- **CHANGE_POINT** `interconnector_net` value=-452 d1=1310.0 d12=6333.0 z=3.106138204603348
- **CHANGE_POINT** `biomass_gen` value=3014 d1=-97.0 d12=-194.0 z=-1.602633764957265
- **ROBUST_OUTLIER** `margin` value=3.573e+04 d1=0.0 d12=-42.0 z=-3.2844718260869565
- **PERSISTENT_UP** `interconnector_net` value=-452 d1=1310.0 d12=6333.0 z=3.106138204603348
- **ROBUST_OUTLIER** `interconnector_net` value=-452 d1=1310.0 d12=6333.0 z=3.106138204603348
- **CHANGE_POINT** `wind_gen` value=1.411e+04 d1=107.0 d12=249.0 z=0.9478989879464286
- **PERSISTENT_DOWN** `biomass_gen` value=3014 d1=-97.0 d12=-194.0 z=-1.602633764957265
- **REVERSAL** `ps_gen` value=223 d1=4.0 d12=-307.0 z=1.476241716981132
- **PERSISTENT_UP** `wind_gen` value=1.411e+04 d1=107.0 d12=249.0 z=0.9478989879464286
- **ACCELERATION** `wind_gen` value=1.411e+04 d1=107.0 d12=249.0 z=0.9478989879464286
- **PERSISTENT_DOWN** `thermal_base` value=7543 d1=-297.0 d12=-585.0 z=0.602514496149615
- **PERSISTENT_DOWN** `ccgt_gen` value=4229 d1=-301.0 d12=-586.0 z=0.5974898224478594

## Nearest historical live analogues

- `2026-09-16T00:52:57.444665Z` distance=0.797 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T00:57:07.708523Z` distance=0.797 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:01:32.433373Z` distance=0.797 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:05:42.750302Z` distance=0.797 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:09:54.472696Z` distance=0.797 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

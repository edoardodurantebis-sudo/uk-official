# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T02:17:31.561812Z`  
Memory snapshots: **409**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.608e+04 d1=0.0 d12=43.0 z=6.680220400684931
- **ROBUST_OUTLIER** `margin` value=3.608e+04 d1=0.0 d12=43.0 z=6.680220400684931
- **CHANGE_POINT** `ccgt_gen` value=3059 d1=-90.0 d12=-185.0 z=-1.5795013132911393
- **CHANGE_POINT** `thermal_base` value=6385 d1=-90.0 d12=-187.0 z=-1.5307282350299403
- **CHANGE_POINT** `biomass_gen` value=3230 d1=3.0 d12=-2.0 z=-0.8093877
- **CHANGE_POINT** `ps_gen` value=-12 d1=0.0 d12=-236.0 z=0.0
- **PERSISTENT_DOWN** `ccgt_gen` value=3059 d1=-90.0 d12=-185.0 z=-1.5795013132911393
- **PERSISTENT_DOWN** `thermal_base` value=6385 d1=-90.0 d12=-187.0 z=-1.5307282350299403
- **PERSISTENT_DOWN** `wind_gen` value=1.004e+04 d1=-105.0 d12=-283.0 z=-0.9812773702791461
- **REVERSAL** `biomass_gen` value=3230 d1=3.0 d12=-2.0 z=-0.8093877
- **ACCELERATION** `biomass_gen` value=3230 d1=3.0 d12=-2.0 z=-0.8093877
- **PERSISTENT_DOWN** `interconnector_net` value=3897 d1=-28.0 d12=-462.0 z=-0.0720951039192399
- **PERSISTENT_DOWN** `nuclear_gen` value=3326 d1=0.0 d12=-2.0 z=0.0
- **ACCELERATION** `nuclear_gen` value=3326 d1=0.0 d12=-2.0 z=0.0

## Nearest historical live analogues

- `2026-09-16T01:22:27.619756Z` distance=0.096 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T00:52:57.444665Z` distance=0.309 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T00:57:07.708523Z` distance=0.309 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:01:32.433373Z` distance=0.309 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:05:42.750302Z` distance=0.309 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T02:00:10.670180Z`  
Memory snapshots: **405**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.22e+04 d1=0.0 d12=-44.0 z=-48.563262
- **PERSISTENT_DOWN** `ind_demand` value=-1.22e+04 d1=0.0 d12=-44.0 z=-48.563262
- **ROBUST_OUTLIER** `ind_demand` value=-1.22e+04 d1=0.0 d12=-44.0 z=-48.563262
- **PERSISTENT_UP** `margin` value=3.608e+04 d1=0.0 d12=420.0 z=6.295237666666667
- **ROBUST_OUTLIER** `margin` value=3.608e+04 d1=0.0 d12=420.0 z=6.295237666666667
- **CHANGE_POINT** `ccgt_gen` value=3145 d1=0.0 d12=-98.0 z=-0.7490190041436464
- **CHANGE_POINT** `thermal_base` value=6471 d1=0.0 d12=-104.0 z=-0.7454886710526315
- **CHANGE_POINT** `interconnector_net` value=4571 d1=0.0 d12=246.0 z=0.6481348683068018
- **CHANGE_POINT** `ps_gen` value=-12 d1=0.0 d12=-215.0 z=-0.10263974456521739
- **PERSISTENT_UP** `biomass_gen` value=3232 d1=0.0 d12=2.0 z=-0.885267796875
- **ACCELERATION** `biomass_gen` value=3232 d1=0.0 d12=2.0 z=-0.885267796875
- **PERSISTENT_DOWN** `wind_gen` value=1.022e+04 d1=0.0 d12=-285.0 z=-0.8116936478632478
- **PERSISTENT_DOWN** `ccgt_gen` value=3145 d1=0.0 d12=-98.0 z=-0.7490190041436464
- **ACCELERATION** `ccgt_gen` value=3145 d1=0.0 d12=-98.0 z=-0.7490190041436464
- **PERSISTENT_DOWN** `thermal_base` value=6471 d1=0.0 d12=-104.0 z=-0.7454886710526315

## Nearest historical live analogues

- `2026-09-16T00:52:57.444665Z` distance=0.313 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T00:57:07.708523Z` distance=0.313 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:01:32.433373Z` distance=0.313 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:05:42.750302Z` distance=0.313 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T23:32:16.606471Z` distance=0.349 → {'next30m_imbalance_delta': 39.0, 'next30m_margin_delta': -78.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

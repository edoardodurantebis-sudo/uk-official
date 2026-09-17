# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T07:17:45.458689Z`  
Memory snapshots: **785**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.213e+04 d1=0.0 d12=-311.0 z=-6.668745431451613
- **ROBUST_OUTLIER** `ind_demand` value=-1.213e+04 d1=0.0 d12=-311.0 z=-6.668745431451613
- **CHANGE_POINT** `margin` value=3.573e+04 d1=0.0 d12=-42.0 z=-3.2844718260869565
- **CHANGE_POINT** `interconnector_net` value=-400 d1=52.0 d12=6385.0 z=3.123707702450091
- **CHANGE_POINT** `biomass_gen` value=2950 d1=-64.0 d12=-234.0 z=-1.886616257246377
- **CHANGE_POINT** `ps_gen` value=223 d1=0.0 d12=-308.0 z=1.4731533451882843
- **ROBUST_OUTLIER** `margin` value=3.573e+04 d1=0.0 d12=-42.0 z=-3.2844718260869565
- **PERSISTENT_UP** `interconnector_net` value=-400 d1=52.0 d12=6385.0 z=3.123707702450091
- **ROBUST_OUTLIER** `interconnector_net` value=-400 d1=52.0 d12=6385.0 z=3.123707702450091
- **CHANGE_POINT** `wind_gen` value=1.408e+04 d1=-31.0 d12=209.0 z=0.863995188077634
- **PERSISTENT_DOWN** `biomass_gen` value=2950 d1=-64.0 d12=-234.0 z=-1.886616257246377
- **PERSISTENT_DOWN** `ps_gen` value=223 d1=0.0 d12=-308.0 z=1.4731533451882843
- **REVERSAL** `wind_gen` value=1.408e+04 d1=-31.0 d12=209.0 z=0.863995188077634
- **ACCELERATION** `wind_gen` value=1.408e+04 d1=-31.0 d12=209.0 z=0.863995188077634
- **PERSISTENT_UP** `nuclear_gen` value=3315 d1=1.0 d12=5.0 z=0.67448975

## Nearest historical live analogues

- `2026-09-17T06:23:11.376027Z` distance=0.555 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T00:52:57.444665Z` distance=0.797 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T00:57:07.708523Z` distance=0.797 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:01:32.433373Z` distance=0.797 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:05:42.750302Z` distance=0.797 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

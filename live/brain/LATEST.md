# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T09:14:03.439788Z`  
Memory snapshots: **508**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.574e+04 d1=0.0 d12=-815.0 z=-57.12285811309524
- **ROBUST_OUTLIER** `ind_demand` value=-1.268e+04 d1=0.0 d12=-15.0 z=-17.274431930555558
- **CHANGE_POINT** `interconnector_net` value=1.028e+04 d1=25.0 d12=179.0 z=1.48159689082256
- **PERSISTENT_DOWN** `biomass_gen` value=3240 d1=-2.0 d12=-3.0 z=2.697959
- **ACCELERATION** `biomass_gen` value=3240 d1=-2.0 d12=-3.0 z=2.697959
- **CHANGE_POINT** `thermal_base` value=1.055e+04 d1=-232.0 d12=-920.0 z=-0.2774496843971631
- **CHANGE_POINT** `ccgt_gen` value=7215 d1=-234.0 d12=-921.0 z=-0.2769963352396514
- **CHANGE_POINT** `demand_forecast` value=1.851e+04 d1=0.0 d12=0.0 z=None
- **PERSISTENT_UP** `interconnector_net` value=1.028e+04 d1=25.0 d12=179.0 z=1.48159689082256
- **PERSISTENT_DOWN** `wind_gen` value=6265 d1=-10.0 d12=-647.0 z=-1.1796694313547802
- **ACCELERATION** `nuclear_gen` value=3332 d1=2.0 d12=1.0 z=1.0117346249999999
- **PERSISTENT_DOWN** `thermal_base` value=1.055e+04 d1=-232.0 d12=-920.0 z=-0.2774496843971631
- **PERSISTENT_DOWN** `ccgt_gen` value=7215 d1=-234.0 d12=-921.0 z=-0.2769963352396514

## Nearest historical live analogues

- `2026-09-16T08:17:56.653795Z` distance=0.515 → {'next30m_imbalance_delta': 235.0, 'next30m_margin_delta': 235.0, 'next30m_residual_proxy_delta': -321.0}
- `2026-09-16T07:23:21.620957Z` distance=0.529 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:27:32.881343Z` distance=0.529 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:31:44.991160Z` distance=0.529 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:35:56.436252Z` distance=0.529 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

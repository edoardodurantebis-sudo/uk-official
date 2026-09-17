# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T03:30:29.291178Z`  
Memory snapshots: **731**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2032 d1=0.0 d12=-5.0 z=-197.62549675
- **PERSISTENT_DOWN** `biomass_gen` value=2032 d1=0.0 d12=-5.0 z=-197.62549675
- **ROBUST_OUTLIER** `biomass_gen` value=2032 d1=0.0 d12=-5.0 z=-197.62549675
- **ROBUST_OUTLIER** `ind_demand` value=-1.152e+04 d1=0.0 d12=11.0 z=33.31979365
- **CHANGE_POINT** `margin` value=3.585e+04 d1=0.0 d12=1.0 z=11.051880240963856
- **ROBUST_OUTLIER** `margin` value=3.585e+04 d1=0.0 d12=1.0 z=11.051880240963856
- **CHANGE_POINT** `interconnector_net` value=-8260 d1=0.0 d12=-1794.0 z=-5.398929114955357
- **ROBUST_OUTLIER** `interconnector_net` value=-8260 d1=0.0 d12=-1794.0 z=-5.398929114955357
- **CHANGE_POINT** `nuclear_gen` value=3311 d1=0.0 d12=-1.0 z=-0.2697959
- **PERSISTENT_UP** `thermal_base` value=7072 d1=0.0 d12=24.0 z=-0.6972703257644911
- **ACCELERATION** `thermal_base` value=7072 d1=0.0 d12=24.0 z=-0.6972703257644911
- **PERSISTENT_UP** `ccgt_gen` value=3761 d1=0.0 d12=25.0 z=-0.6957894263157894
- **ACCELERATION** `ccgt_gen` value=3761 d1=0.0 d12=25.0 z=-0.6957894263157894
- **PERSISTENT_DOWN** `wind_gen` value=1.334e+04 d1=0.0 d12=-96.0 z=0.6859289605841709
- **ACCELERATION** `wind_gen` value=1.334e+04 d1=0.0 d12=-96.0 z=0.6859289605841709

## Nearest historical live analogues

- `2026-09-17T02:22:41.615797Z` distance=0.024 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:26:53.112988Z` distance=0.024 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:31:05.012181Z` distance=0.024 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:35:17.375315Z` distance=0.024 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T12:23:49.836209Z` distance=0.605 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 199.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

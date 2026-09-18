# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T12:40:17.975673Z`  
Memory snapshots: **1203**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **PERSISTENT_UP** `residual_proxy` value=9368 d1=0.0 d12=813.0 z=39.16858333928571
- **ROBUST_OUTLIER** `residual_proxy` value=9368 d1=0.0 d12=813.0 z=39.16858333928571
- **PERSISTENT_DOWN** `wind_forecast` value=6802 d1=0.0 d12=-813.0 z=-8.175909537162163
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=-813.0 z=-8.175909537162163
- **CHANGE_POINT** `wind_gen` value=1.46e+04 d1=0.0 d12=1706.0 z=3.545727029111645
- **CHANGE_POINT** `ind_generation` value=2.559e+04 d1=0.0 d12=-81.0 z=-3.1808323437499997
- **PERSISTENT_UP** `wind_gen` value=1.46e+04 d1=0.0 d12=1706.0 z=3.545727029111645
- **ROBUST_OUTLIER** `wind_gen` value=1.46e+04 d1=0.0 d12=1706.0 z=3.545727029111645
- **ROBUST_OUTLIER** `ind_generation` value=2.559e+04 d1=0.0 d12=-81.0 z=-3.1808323437499997
- **CHANGE_POINT** `biomass_gen` value=1039 d1=0.0 d12=-45.0 z=-1.0739597613895215
- **CHANGE_POINT** `margin` value=3.81e+04 d1=0.0 d12=-20.0 z=0.952716771875
- **CHANGE_POINT** `thermal_base` value=5772 d1=0.0 d12=-8.0 z=-0.8171550320211516
- **CHANGE_POINT** `imbalance` value=8916 d1=0.0 d12=-81.0 z=-0.7085757557427259
- **CHANGE_POINT** `ps_gen` value=-480 d1=0.0 d12=235.0 z=-0.3893590919182949
- **PERSISTENT_UP** `interconnector_net` value=5563 d1=0.0 d12=491.0 z=0.8902532411787514

## Nearest historical live analogues

- `2026-09-18T11:24:04.514292Z` distance=0.546 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:28:15.080322Z` distance=0.546 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:32:27.606520Z` distance=0.546 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:36:39.120027Z` distance=0.546 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:40:49.072894Z` distance=0.546 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

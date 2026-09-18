# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T12:48:39.473091Z`  
Memory snapshots: **1205**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=9368 d1=0.0 d12=813.0 z=39.16858333928571
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=-813.0 z=-8.175909537162163
- **CHANGE_POINT** `wind_gen` value=1.502e+04 d1=225.0 d12=1723.0 z=4.217787644357743
- **CHANGE_POINT** `ind_generation` value=2.559e+04 d1=0.0 d12=-33.0 z=-2.4974770236175114
- **PERSISTENT_UP** `wind_gen` value=1.502e+04 d1=225.0 d12=1723.0 z=4.217787644357743
- **ROBUST_OUTLIER** `wind_gen` value=1.502e+04 d1=225.0 d12=1723.0 z=4.217787644357743
- **CHANGE_POINT** `biomass_gen` value=1036 d1=-2.0 d12=-4.0 z=-1.0529912932098764
- **CHANGE_POINT** `ccgt_gen` value=2430 d1=-3.0 d12=-4.0 z=-0.6923754534472599
- **CHANGE_POINT** `thermal_base` value=5772 d1=0.0 d12=2.0 z=-0.6909114125593824
- **CHANGE_POINT** `margin` value=3.81e+04 d1=0.0 d12=0.0 z=0.67448975
- **CHANGE_POINT** `ps_gen` value=-717 d1=-2.0 d12=6.0 z=-0.6610670684079601
- **CHANGE_POINT** `imbalance` value=8916 d1=0.0 d12=-33.0 z=-0.04568032587792643
- **PERSISTENT_UP** `nuclear_gen` value=3342 d1=3.0 d12=6.0 z=1.5738094166666665
- **PERSISTENT_DOWN** `biomass_gen` value=1036 d1=-2.0 d12=-4.0 z=-1.0529912932098764
- **PERSISTENT_UP** `interconnector_net` value=5656 d1=44.0 d12=580.0 z=0.9456265838966202

## Nearest historical live analogues

- `2026-09-18T11:53:30.754266Z` distance=0.545 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:24:04.514292Z` distance=0.546 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:28:15.080322Z` distance=0.546 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:32:27.606520Z` distance=0.546 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:36:39.120027Z` distance=0.546 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T15:44:05.463300Z`  
Memory snapshots: **259**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=4890 d1=-55.0 d12=-3146.0 z=-10.942708707236843
- **CHANGE_POINT** `ccgt_gen` value=5643 d1=414.0 d12=3171.0 z=10.18622477938343
- **CHANGE_POINT** `thermal_base` value=8965 d1=415.0 d12=3164.0 z=10.085104866156787
- **PERSISTENT_DOWN** `interconnector_net` value=4890 d1=-55.0 d12=-3146.0 z=-10.942708707236843
- **ROBUST_OUTLIER** `interconnector_net` value=4890 d1=-55.0 d12=-3146.0 z=-10.942708707236843
- **PERSISTENT_UP** `ccgt_gen` value=5643 d1=414.0 d12=3171.0 z=10.18622477938343
- **ROBUST_OUTLIER** `ccgt_gen` value=5643 d1=414.0 d12=3171.0 z=10.18622477938343
- **PERSISTENT_UP** `thermal_base` value=8965 d1=415.0 d12=3164.0 z=10.085104866156787
- **ROBUST_OUTLIER** `thermal_base` value=8965 d1=415.0 d12=3164.0 z=10.085104866156787
- **REVERSAL** `ps_gen` value=-135 d1=1.0 d12=-82.0 z=3.491706357971015
- **ROBUST_OUTLIER** `ps_gen` value=-135 d1=1.0 d12=-82.0 z=3.491706357971015
- **CHANGE_POINT** `margin` value=3.465e+04 d1=0.0 d12=24.0 z=-0.9692247668067228
- **REVERSAL** `nuclear_gen` value=3322 d1=1.0 d12=-7.0 z=-1.3489794999999998
- **PERSISTENT_UP** `wind_gen` value=1.044e+04 d1=89.0 d12=233.0 z=-0.3435530525179856
- **ACCELERATION** `wind_gen` value=1.044e+04 d1=89.0 d12=233.0 z=-0.3435530525179856

## Nearest historical live analogues

- `2026-09-15T14:23:51.987860Z` distance=0.018 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T14:28:05.259603Z` distance=0.018 → {'next30m_imbalance_delta': 50.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T14:32:25.430629Z` distance=0.018 → {'next30m_imbalance_delta': 50.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T14:36:41.684254Z` distance=0.018 → {'next30m_imbalance_delta': 50.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T14:40:55.475538Z` distance=0.018 → {'next30m_imbalance_delta': 50.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

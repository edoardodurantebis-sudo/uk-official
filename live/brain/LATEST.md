# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T15:48:17.714680Z`  
Memory snapshots: **260**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=6043 d1=400.0 d12=3413.0 z=11.22590069460501
- **CHANGE_POINT** `thermal_base` value=9365 d1=400.0 d12=3403.0 z=11.116829149139578
- **CHANGE_POINT** `interconnector_net` value=4888 d1=-2.0 d12=-3284.0 z=-10.946258653289473
- **PERSISTENT_UP** `ccgt_gen` value=6043 d1=400.0 d12=3413.0 z=11.22590069460501
- **ROBUST_OUTLIER** `ccgt_gen` value=6043 d1=400.0 d12=3413.0 z=11.22590069460501
- **PERSISTENT_UP** `thermal_base` value=9365 d1=400.0 d12=3403.0 z=11.116829149139578
- **ROBUST_OUTLIER** `thermal_base` value=9365 d1=400.0 d12=3403.0 z=11.116829149139578
- **PERSISTENT_DOWN** `interconnector_net` value=4888 d1=-2.0 d12=-3284.0 z=-10.946258653289473
- **ROBUST_OUTLIER** `interconnector_net` value=4888 d1=-2.0 d12=-3284.0 z=-10.946258653289473
- **REVERSAL** `ps_gen` value=-136 d1=-1.0 d12=42.0 z=3.4877962724637683
- **ROBUST_OUTLIER** `ps_gen` value=-136 d1=-1.0 d12=42.0 z=3.4877962724637683
- **CHANGE_POINT** `margin` value=3.465e+04 d1=0.0 d12=24.0 z=-0.9692247668067228
- **PERSISTENT_UP** `biomass_gen` value=1742 d1=5.0 d12=0.0 z=0.5093085867346939
- **ACCELERATION** `biomass_gen` value=1742 d1=5.0 d12=0.0 z=0.5093085867346939
- **PERSISTENT_UP** `wind_gen` value=1.044e+04 d1=3.0 d12=136.0 z=-0.2907467702060222

## Nearest historical live analogues

- `2026-09-15T14:23:51.987860Z` distance=0.018 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T14:28:05.259603Z` distance=0.018 → {'next30m_imbalance_delta': 50.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T14:32:25.430629Z` distance=0.018 → {'next30m_imbalance_delta': 50.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T14:36:41.684254Z` distance=0.018 → {'next30m_imbalance_delta': 50.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T14:40:55.475538Z` distance=0.018 → {'next30m_imbalance_delta': 50.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

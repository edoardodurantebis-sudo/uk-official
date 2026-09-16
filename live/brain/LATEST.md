# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T02:46:53.510772Z`  
Memory snapshots: **416**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=1461.0 z=36.105039558823535
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=1461.0 z=36.105039558823535
- **CHANGE_POINT** `ccgt_gen` value=2693 d1=-75.0 d12=-452.0 z=-4.756017467948718
- **CHANGE_POINT** `thermal_base` value=6023 d1=-75.0 d12=-448.0 z=-4.6202547875
- **PERSISTENT_DOWN** `ccgt_gen` value=2693 d1=-75.0 d12=-452.0 z=-4.756017467948718
- **ROBUST_OUTLIER** `ccgt_gen` value=2693 d1=-75.0 d12=-452.0 z=-4.756017467948718
- **PERSISTENT_DOWN** `thermal_base` value=6023 d1=-75.0 d12=-448.0 z=-4.6202547875
- **ROBUST_OUTLIER** `thermal_base` value=6023 d1=-75.0 d12=-448.0 z=-4.6202547875
- **CHANGE_POINT** `interconnector_net` value=3420 d1=26.0 d12=-1151.0 z=-0.7932174273758099
- **PERSISTENT_DOWN** `wind_gen` value=1.001e+04 d1=-137.0 d12=-212.0 z=-0.8776031406250001
- **ACCELERATION** `wind_gen` value=1.001e+04 d1=-137.0 d12=-212.0 z=-0.8776031406250001
- **REVERSAL** `interconnector_net` value=3420 d1=26.0 d12=-1151.0 z=-0.7932174273758099
- **REVERSAL** `biomass_gen` value=3231 d1=3.0 d12=-1.0 z=-0.7153679166666667
- **ACCELERATION** `biomass_gen` value=3231 d1=3.0 d12=-1.0 z=-0.7153679166666667
- **PERSISTENT_UP** `nuclear_gen` value=3330 d1=0.0 d12=4.0 z=0.6744897499999999

## Nearest historical live analogues

- `2026-09-16T01:51:47.907050Z` distance=0.979 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:22:27.619756Z` distance=1.012 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:26:39.733829Z` distance=1.012 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 43.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:30:51.171877Z` distance=1.012 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 43.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:35:00.797772Z` distance=1.012 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 43.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

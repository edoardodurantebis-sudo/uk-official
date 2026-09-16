# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T02:42:43.321930Z`  
Memory snapshots: **415**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=1461.0 z=36.105039558823535
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=1461.0 z=36.105039558823535
- **CHANGE_POINT** `ccgt_gen` value=2768 d1=-26.0 d12=-474.0 z=-4.107469631410256
- **CHANGE_POINT** `thermal_base` value=6098 d1=-25.0 d12=-473.0 z=-3.9673403307453414
- **PERSISTENT_DOWN** `ccgt_gen` value=2768 d1=-26.0 d12=-474.0 z=-4.107469631410256
- **ROBUST_OUTLIER** `ccgt_gen` value=2768 d1=-26.0 d12=-474.0 z=-4.107469631410256
- **PERSISTENT_DOWN** `thermal_base` value=6098 d1=-25.0 d12=-473.0 z=-3.9673403307453414
- **ROBUST_OUTLIER** `thermal_base` value=6098 d1=-25.0 d12=-473.0 z=-3.9673403307453414
- **CHANGE_POINT** `interconnector_net` value=3394 d1=25.0 d12=-1203.0 z=-0.8310937416306696
- **PERSISTENT_DOWN** `biomass_gen` value=3228 d1=-3.0 d12=-5.0 z=-0.8331932205882353
- **ACCELERATION** `biomass_gen` value=3228 d1=-3.0 d12=-5.0 z=-0.8331932205882353
- **REVERSAL** `interconnector_net` value=3394 d1=25.0 d12=-1203.0 z=-0.8310937416306696
- **PERSISTENT_DOWN** `wind_gen` value=1.015e+04 d1=-20.0 d12=-173.0 z=-0.7631481702977488
- **PERSISTENT_UP** `nuclear_gen` value=3330 d1=1.0 d12=1.0 z=0.6744897499999999
- **ACCELERATION** `nuclear_gen` value=3330 d1=1.0 d12=1.0 z=0.6744897499999999

## Nearest historical live analogues

- `2026-09-16T01:22:27.619756Z` distance=1.029 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:26:39.733829Z` distance=1.029 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 43.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:30:51.171877Z` distance=1.029 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 43.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:35:00.797772Z` distance=1.029 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 43.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:39:11.726100Z` distance=1.029 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 43.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

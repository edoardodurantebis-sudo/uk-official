# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T02:56:45.854768Z`  
Memory snapshots: **2034**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.756e+04 d1=0.0 d12=1730.0 z=30.71522553846154
- **PERSISTENT_UP** `margin` value=3.756e+04 d1=0.0 d12=1730.0 z=30.71522553846154
- **ROBUST_OUTLIER** `margin` value=3.756e+04 d1=0.0 d12=1730.0 z=30.71522553846154
- **CHANGE_POINT** `ccgt_gen` value=4793 d1=7.0 d12=-578.0 z=-1.7036364745244565
- **CHANGE_POINT** `thermal_base` value=8134 d1=12.0 d12=-578.0 z=-1.6884938559892329
- **CHANGE_POINT** `ind_demand` value=-1.18e+04 d1=0.0 d12=26.0 z=1.4613944583333334
- **CHANGE_POINT** `interconnector_net` value=1.252e+04 d1=-1.0 d12=176.0 z=1.1504608667349328
- **CHANGE_POINT** `imbalance` value=-4865 d1=0.0 d12=34.0 z=1.0516925485781992
- **CHANGE_POINT** `ind_generation` value=1.574e+04 d1=0.0 d12=34.0 z=1.0516925485781992
- **PERSISTENT_DOWN** `wind_gen` value=3728 d1=-7.0 d12=-144.0 z=-2.0795457094017094
- **REVERSAL** `ccgt_gen` value=4793 d1=7.0 d12=-578.0 z=-1.7036364745244565
- **REVERSAL** `thermal_base` value=8134 d1=12.0 d12=-578.0 z=-1.6884938559892329
- **REVERSAL** `interconnector_net` value=1.252e+04 d1=-1.0 d12=176.0 z=1.1504608667349328
- **PERSISTENT_UP** `nuclear_gen` value=3341 d1=5.0 d12=0.0 z=1.1241495833333335
- **ACCELERATION** `nuclear_gen` value=3341 d1=5.0 d12=0.0 z=1.1241495833333335

## Nearest historical live analogues

- `2026-09-21T01:53:20.720277Z` distance=0.825 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:57:30.190951Z` distance=0.825 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:01:42.969969Z` distance=0.825 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:23:21.503053Z` distance=0.828 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:28:09.159328Z` distance=0.828 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

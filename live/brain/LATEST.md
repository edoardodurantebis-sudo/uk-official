# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T02:50:56.858450Z`  
Memory snapshots: **1692**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.761e+04 d1=1.0 d12=1589.0 z=29.77390467857143
- **PERSISTENT_UP** `margin` value=3.761e+04 d1=1.0 d12=1589.0 z=29.77390467857143
- **ROBUST_OUTLIER** `margin` value=3.761e+04 d1=1.0 d12=1589.0 z=29.77390467857143
- **CHANGE_POINT** `ind_demand` value=-1.22e+04 d1=0.0 d12=0.0 z=-14.886952339285713
- **ROBUST_OUTLIER** `ind_demand` value=-1.22e+04 d1=0.0 d12=0.0 z=-14.886952339285713
- **REVERSAL** `biomass_gen` value=1168 d1=16.0 d12=-54.0 z=5.263063958333333
- **ACCELERATION** `biomass_gen` value=1168 d1=16.0 d12=-54.0 z=5.263063958333333
- **ROBUST_OUTLIER** `biomass_gen` value=1168 d1=16.0 d12=-54.0 z=5.263063958333333
- **CHANGE_POINT** `interconnector_net` value=-1.105e+04 d1=2.0 d12=-1090.0 z=-1.2539339728059333
- **CHANGE_POINT** `thermal_base` value=7184 d1=-113.0 d12=-361.0 z=-0.30719335148514854
- **CHANGE_POINT** `ccgt_gen` value=3855 d1=-111.0 d12=-358.0 z=-0.304527088619403
- **REVERSAL** `interconnector_net` value=-1.105e+04 d1=2.0 d12=-1090.0 z=-1.2539339728059333
- **PERSISTENT_UP** `ps_gen` value=-695 d1=2.0 d12=120.0 z=-1.1332643096846848
- **PERSISTENT_DOWN** `nuclear_gen` value=3329 d1=-2.0 d12=-3.0 z=-1.1241495833333335
- **PERSISTENT_DOWN** `thermal_base` value=7184 d1=-113.0 d12=-361.0 z=-0.30719335148514854

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.329 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.329 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.329 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

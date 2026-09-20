# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T03:21:25.229596Z`  
Memory snapshots: **1699**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=-62.0 d12=-61.0 z=28.579094264285715
- **PERSISTENT_DOWN** `margin` value=3.754e+04 d1=-62.0 d12=-61.0 z=28.579094264285715
- **ACCELERATION** `margin` value=3.754e+04 d1=-62.0 d12=-61.0 z=28.579094264285715
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=-62.0 d12=-61.0 z=28.579094264285715
- **PERSISTENT_DOWN** `ind_demand` value=-1.229e+04 d1=-9.0 d12=-90.0 z=-17.896461366666664
- **ROBUST_OUTLIER** `ind_demand` value=-1.229e+04 d1=-9.0 d12=-90.0 z=-17.896461366666664
- **ROBUST_OUTLIER** `biomass_gen` value=1223 d1=0.0 d12=-7.0 z=4.258142361111111
- **CHANGE_POINT** `interconnector_net` value=-1.153e+04 d1=-3.0 d12=-981.0 z=-1.481801371021336
- **CHANGE_POINT** `thermal_base` value=6930 d1=-15.0 d12=-669.0 z=-0.6028406556776557
- **CHANGE_POINT** `ccgt_gen` value=3597 d1=-19.0 d12=-669.0 z=-0.6005934465073529
- **PERSISTENT_DOWN** `interconnector_net` value=-1.153e+04 d1=-3.0 d12=-981.0 z=-1.481801371021336
- **REVERSAL** `ps_gen` value=-697 d1=-5.0 d12=6.0 z=-0.9049988770430907
- **ACCELERATION** `ps_gen` value=-697 d1=-5.0 d12=6.0 z=-0.9049988770430907
- **PERSISTENT_DOWN** `imbalance` value=-3815 d1=-66.0 d12=-60.0 z=-0.6376994
- **ACCELERATION** `imbalance` value=-3815 d1=-66.0 d12=-60.0 z=-0.6376994

## Nearest historical live analogues

- `2026-09-20T02:20:49.967105Z` distance=0.105 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:25:01.524399Z` distance=0.105 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:48:55.634175Z` distance=0.369 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.369 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.369 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

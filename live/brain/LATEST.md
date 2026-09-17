# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T22:11:14.458850Z`  
Memory snapshots: **997**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1723 d1=0.0 d12=-1159.0 z=-5.831072677419355
- **CHANGE_POINT** `ps_gen` value=-254 d1=0.0 d12=-608.0 z=-4.162359205882352
- **ROBUST_OUTLIER** `biomass_gen` value=1723 d1=0.0 d12=-1159.0 z=-5.831072677419355
- **PERSISTENT_DOWN** `interconnector_net` value=-6962 d1=-325.0 d12=-2649.0 z=-4.2327413367924525
- **ROBUST_OUTLIER** `interconnector_net` value=-6962 d1=-325.0 d12=-2649.0 z=-4.2327413367924525
- **PERSISTENT_DOWN** `ps_gen` value=-254 d1=0.0 d12=-608.0 z=-4.162359205882352
- **ROBUST_OUTLIER** `ps_gen` value=-254 d1=0.0 d12=-608.0 z=-4.162359205882352
- **CHANGE_POINT** `ccgt_gen` value=4646 d1=66.0 d12=-243.0 z=-0.32481914270887385
- **CHANGE_POINT** `thermal_base` value=7970 d1=72.0 d12=-236.0 z=-0.3195317044284243
- **PERSISTENT_UP** `nuclear_gen` value=3324 d1=6.0 d12=7.0 z=0.67448975
- **ACCELERATION** `nuclear_gen` value=3324 d1=6.0 d12=7.0 z=0.67448975
- **REVERSAL** `ccgt_gen` value=4646 d1=66.0 d12=-243.0 z=-0.32481914270887385
- **REVERSAL** `thermal_base` value=7970 d1=72.0 d12=-236.0 z=-0.3195317044284243
- **REVERSAL** `wind_gen` value=1.493e+04 d1=66.0 d12=-151.0 z=0.050934008581235694

## Nearest historical live analogues

- `2026-09-17T20:22:00.773279Z` distance=0.003 → {'next30m_imbalance_delta': -22.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T20:26:16.510508Z` distance=0.003 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T20:30:29.039368Z` distance=0.003 → {'next30m_imbalance_delta': 16.0, 'next30m_margin_delta': 10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T20:34:40.503953Z` distance=0.003 → {'next30m_imbalance_delta': 16.0, 'next30m_margin_delta': 10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T20:38:54.540186Z` distance=0.003 → {'next30m_imbalance_delta': 16.0, 'next30m_margin_delta': 10.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

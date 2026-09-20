# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T08:33:55.972696Z`  
Memory snapshots: **1773**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=585 d1=-85.0 d12=-316.0 z=-14.64944404385965
- **PERSISTENT_DOWN** `biomass_gen` value=585 d1=-85.0 d12=-316.0 z=-14.64944404385965
- **ROBUST_OUTLIER** `biomass_gen` value=585 d1=-85.0 d12=-316.0 z=-14.64944404385965
- **CHANGE_POINT** `ccgt_gen` value=2902 d1=-162.0 d12=-910.0 z=-3.4264079300000003
- **CHANGE_POINT** `thermal_base` value=6248 d1=-157.0 d12=-893.0 z=-3.393646999285714
- **PERSISTENT_UP** `interconnector_net` value=-3245 d1=1668.0 d12=3508.0 z=5.0370507263157895
- **ACCELERATION** `interconnector_net` value=-3245 d1=1668.0 d12=3508.0 z=5.0370507263157895
- **ROBUST_OUTLIER** `interconnector_net` value=-3245 d1=1668.0 d12=3508.0 z=5.0370507263157895
- **PERSISTENT_UP** `nuclear_gen` value=3346 d1=5.0 d12=17.0 z=4.0469384999999996
- **ROBUST_OUTLIER** `nuclear_gen` value=3346 d1=5.0 d12=17.0 z=4.0469384999999996
- **CHANGE_POINT** `ps_gen` value=-935 d1=1.0 d12=-13.0 z=-1.6539349720744683
- **PERSISTENT_DOWN** `ccgt_gen` value=2902 d1=-162.0 d12=-910.0 z=-3.4264079300000003
- **ROBUST_OUTLIER** `ccgt_gen` value=2902 d1=-162.0 d12=-910.0 z=-3.4264079300000003
- **PERSISTENT_DOWN** `thermal_base` value=6248 d1=-157.0 d12=-893.0 z=-3.393646999285714
- **ROBUST_OUTLIER** `thermal_base` value=6248 d1=-157.0 d12=-893.0 z=-3.393646999285714

## Nearest historical live analogues

- `2026-09-20T05:53:50.250426Z` distance=0.063 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:58:00.386850Z` distance=0.063 → {'next30m_imbalance_delta': -80.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:02:09.934243Z` distance=0.063 → {'next30m_imbalance_delta': -80.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:06:21.393634Z` distance=0.063 → {'next30m_imbalance_delta': -80.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:11:07.730851Z` distance=0.063 → {'next30m_imbalance_delta': -80.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

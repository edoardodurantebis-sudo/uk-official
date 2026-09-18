# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T01:03:26.672918Z`  
Memory snapshots: **1038**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `imbalance` value=1.013e+04 d1=0.0 d12=-10.0 z=28.396018474999998
- **CHANGE_POINT** `ind_generation` value=2.694e+04 d1=0.0 d12=-10.0 z=28.396018474999998
- **ROBUST_OUTLIER** `imbalance` value=1.013e+04 d1=0.0 d12=-10.0 z=28.396018474999998
- **ROBUST_OUTLIER** `ind_generation` value=2.694e+04 d1=0.0 d12=-10.0 z=28.396018474999998
- **PERSISTENT_DOWN** `ind_demand` value=-1.122e+04 d1=0.0 d12=-40.0 z=-20.90918225
- **ROBUST_OUTLIER** `ind_demand` value=-1.122e+04 d1=0.0 d12=-40.0 z=-20.90918225
- **CHANGE_POINT** `nuclear_gen` value=3330 d1=1.0 d12=5.0 z=2.02346925
- **CHANGE_POINT** `biomass_gen` value=1957 d1=-2.0 d12=-2.0 z=-0.5312983621517772
- **PERSISTENT_DOWN** `wind_gen` value=1.404e+04 d1=-57.0 d12=-363.0 z=-2.380017703703704
- **CHANGE_POINT** `interconnector_net` value=-5206 d1=253.0 d12=748.0 z=0.07870180298639114
- **CHANGE_POINT** `ps_gen` value=296 d1=0.0 d12=241.0 z=0.055185525
- **PERSISTENT_UP** `nuclear_gen` value=3330 d1=1.0 d12=5.0 z=2.02346925
- **ACCELERATION** `nuclear_gen` value=3330 d1=1.0 d12=5.0 z=2.02346925
- **PERSISTENT_DOWN** `ccgt_gen` value=3781 d1=-15.0 d12=-181.0 z=-0.7575549901477832
- **PERSISTENT_DOWN** `thermal_base` value=7111 d1=-14.0 d12=-176.0 z=-0.7502657589506172

## Nearest historical live analogues

- `2026-09-18T00:04:42.630537Z` distance=0.066 → {'next30m_imbalance_delta': -25.0, 'next30m_margin_delta': 27.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:08:54.899390Z` distance=0.066 → {'next30m_imbalance_delta': -25.0, 'next30m_margin_delta': 27.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:24:17.596696Z` distance=3.578 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:28:33.240401Z` distance=3.578 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T18:32:46.898081Z` distance=3.578 → {'next30m_imbalance_delta': 19.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

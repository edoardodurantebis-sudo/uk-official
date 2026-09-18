# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T09:04:44.857257Z`  
Memory snapshots: **1152**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1878 d1=-95.0 d12=-287.0 z=-12.014348671875
- **PERSISTENT_DOWN** `biomass_gen` value=1878 d1=-95.0 d12=-287.0 z=-12.014348671875
- **ROBUST_OUTLIER** `biomass_gen` value=1878 d1=-95.0 d12=-287.0 z=-12.014348671875
- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=4.0 z=-4.42465276
- **PERSISTENT_DOWN** `wind_gen` value=1.203e+04 d1=-165.0 d12=-439.0 z=-3.584612192488263
- **ACCELERATION** `wind_gen` value=1.203e+04 d1=-165.0 d12=-439.0 z=-3.584612192488263
- **ROBUST_OUTLIER** `wind_gen` value=1.203e+04 d1=-165.0 d12=-439.0 z=-3.584612192488263
- **ROBUST_OUTLIER** `imbalance` value=9602 d1=0.0 d12=-616.0 z=-3.24766814625
- **CHANGE_POINT** `ps_gen` value=224 d1=-3.0 d12=-146.0 z=-1.0043342672413793
- **CHANGE_POINT** `thermal_base` value=6879 d1=-50.0 d12=-695.0 z=-0.5662084358744395
- **CHANGE_POINT** `ccgt_gen` value=3547 d1=-45.0 d12=-701.0 z=-0.5599651275692582
- **REVERSAL** `interconnector_net` value=2997 d1=125.0 d12=-227.0 z=2.4700398972403352
- **ACCELERATION** `interconnector_net` value=2997 d1=125.0 d12=-227.0 z=2.4700398972403352
- **CHANGE_POINT** `ts_demand_forecast` value=1.764e+04 d1=0.0 d12=1274.0 z=None
- **PERSISTENT_DOWN** `ps_gen` value=224 d1=-3.0 d12=-146.0 z=-1.0043342672413793

## Nearest historical live analogues

- `2026-09-18T07:23:09.699179Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:27:20.707745Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:31:32.031758Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:35:44.221296Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:39:57.955920Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

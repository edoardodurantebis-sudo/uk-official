# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T09:57:46.729760Z`  
Memory snapshots: **823**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.441e+04 d1=0.0 d12=-1644.0 z=-13.769226467857143
- **PERSISTENT_DOWN** `margin` value=3.441e+04 d1=0.0 d12=-1644.0 z=-13.769226467857143
- **ROBUST_OUTLIER** `margin` value=3.441e+04 d1=0.0 d12=-1644.0 z=-13.769226467857143
- **CHANGE_POINT** `imbalance` value=6663 d1=0.0 d12=-778.0 z=-4.428171836956522
- **CHANGE_POINT** `ind_demand` value=-1.301e+04 d1=0.0 d12=-879.0 z=-2.504043196875
- **ROBUST_OUTLIER** `imbalance` value=6663 d1=0.0 d12=-778.0 z=-4.428171836956522
- **PERSISTENT_DOWN** `wind_gen` value=1.56e+04 d1=-65.0 d12=-110.0 z=4.280260998011928
- **ACCELERATION** `wind_gen` value=1.56e+04 d1=-65.0 d12=-110.0 z=4.280260998011928
- **ROBUST_OUTLIER** `wind_gen` value=1.56e+04 d1=-65.0 d12=-110.0 z=4.280260998011928
- **CHANGE_POINT** `interconnector_net` value=2368 d1=-16.0 d12=-1900.0 z=1.0375276682744634
- **CHANGE_POINT** `ind_generation` value=2.652e+04 d1=0.0 d12=78.0 z=0.8916983135593219
- **PERSISTENT_DOWN** `thermal_base` value=5126 d1=-1.0 d12=-383.0 z=-2.8108290796221325
- **PERSISTENT_DOWN** `ccgt_gen` value=1810 d1=-1.0 d12=-382.0 z=-2.7918638647925036
- **PERSISTENT_DOWN** `ind_demand` value=-1.301e+04 d1=0.0 d12=-879.0 z=-2.504043196875
- **REVERSAL** `biomass_gen` value=2011 d1=-23.0 d12=310.0 z=-1.4699039571713148

## Nearest historical live analogues

- `2026-09-16T08:52:24.970739Z` distance=1.061 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=1.061 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=1.061 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:05:03.473837Z` distance=1.061 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:09:50.095639Z` distance=1.061 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

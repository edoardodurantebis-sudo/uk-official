# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T23:36:30.492110Z`  
Memory snapshots: **1646**  
Current physical regime: **TIGHT**

Regime read: margin low, wind falling.

## Active patterns

- **REVERSAL** `ps_gen` value=-251 d1=3.0 d12=-118.0 z=-85.22376370588235
- **ROBUST_OUTLIER** `ps_gen` value=-251 d1=3.0 d12=-118.0 z=-85.22376370588235
- **ROBUST_OUTLIER** `ind_demand` value=-1.189e+04 d1=0.0 d12=-14.0 z=-10.11734625
- **CHANGE_POINT** `wind_gen` value=1.601e+04 d1=-60.0 d12=773.0 z=3.3784799549180327
- **PERSISTENT_DOWN** `thermal_base` value=6526 d1=-16.0 d12=-683.0 z=-3.8422322487139917
- **ROBUST_OUTLIER** `thermal_base` value=6526 d1=-16.0 d12=-683.0 z=-3.8422322487139917
- **PERSISTENT_DOWN** `ccgt_gen` value=3190 d1=-18.0 d12=-680.0 z=-3.82348790797546
- **ROBUST_OUTLIER** `ccgt_gen` value=3190 d1=-18.0 d12=-680.0 z=-3.82348790797546
- **REVERSAL** `wind_gen` value=1.601e+04 d1=-60.0 d12=773.0 z=3.3784799549180327
- **ROBUST_OUTLIER** `wind_gen` value=1.601e+04 d1=-60.0 d12=773.0 z=3.3784799549180327
- **CHANGE_POINT** `biomass_gen` value=909 d1=1.0 d12=-17.0 z=0.0
- **PERSISTENT_DOWN** `interconnector_net` value=-8381 d1=-2.0 d12=-735.0 z=-1.349476270208065
- **ACCELERATION** `interconnector_net` value=-8381 d1=-2.0 d12=-735.0 z=-1.349476270208065
- **REVERSAL** `nuclear_gen` value=3336 d1=2.0 d12=-3.0 z=0.337244875
- **ACCELERATION** `nuclear_gen` value=3336 d1=2.0 d12=-3.0 z=0.337244875

## Nearest historical live analogues

- `2026-09-19T19:24:22.442601Z` distance=0.106 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -119.0}
- `2026-09-19T19:28:35.593770Z` distance=0.106 → {'next30m_imbalance_delta': -36.0, 'next30m_margin_delta': 40.0, 'next30m_residual_proxy_delta': -119.0}
- `2026-09-19T18:21:25.144867Z` distance=0.110 → {'next30m_imbalance_delta': -611.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T18:25:36.560673Z` distance=0.110 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T18:29:47.180961Z` distance=0.110 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

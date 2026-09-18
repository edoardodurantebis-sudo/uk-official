# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T18:37:47.234328Z`  
Memory snapshots: **1259**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=4803 d1=70.0 d12=-400.0 z=26.41942054661017
- **CHANGE_POINT** `thermal_base` value=8144 d1=71.0 d12=-398.0 z=26.214412552521008
- **REVERSAL** `ccgt_gen` value=4803 d1=70.0 d12=-400.0 z=26.41942054661017
- **ROBUST_OUTLIER** `ccgt_gen` value=4803 d1=70.0 d12=-400.0 z=26.41942054661017
- **REVERSAL** `thermal_base` value=8144 d1=71.0 d12=-398.0 z=26.214412552521008
- **ROBUST_OUTLIER** `thermal_base` value=8144 d1=71.0 d12=-398.0 z=26.214412552521008
- **CHANGE_POINT** `ind_generation` value=2.623e+04 d1=0.0 d12=655.0 z=18.09392068478261
- **ROBUST_OUTLIER** `ind_generation` value=2.623e+04 d1=0.0 d12=655.0 z=18.09392068478261
- **CHANGE_POINT** `interconnector_net` value=-306 d1=0.0 d12=1237.0 z=-9.820009416124838
- **PERSISTENT_UP** `interconnector_net` value=-306 d1=0.0 d12=1237.0 z=-9.820009416124838
- **ACCELERATION** `interconnector_net` value=-306 d1=0.0 d12=1237.0 z=-9.820009416124838
- **ROBUST_OUTLIER** `interconnector_net` value=-306 d1=0.0 d12=1237.0 z=-9.820009416124838
- **PERSISTENT_DOWN** `ps_gen` value=403 d1=-45.0 d12=-275.0 z=7.071818552295918
- **ROBUST_OUTLIER** `ps_gen` value=403 d1=-45.0 d12=-275.0 z=7.071818552295918
- **ROBUST_OUTLIER** `ind_demand` value=-1.074e+04 d1=0.0 d12=31.0 z=6.07040775

## Nearest historical live analogues

- `2026-09-18T15:24:41.804681Z` distance=0.109 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T15:29:30.162883Z` distance=0.109 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T15:33:43.267823Z` distance=0.109 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T15:37:58.638986Z` distance=0.109 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:42:43.021012Z` distance=0.109 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

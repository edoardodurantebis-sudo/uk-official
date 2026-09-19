# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T08:35:12.226662Z`  
Memory snapshots: **1432**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low, wind rising.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.78e+04 d1=0.0 d12=-610.0 z=102.522442
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-3.0 z=-50.58673125
- **PERSISTENT_UP** `interconnector_net` value=40 d1=0.0 d12=3943.0 z=26.950050302919706
- **ACCELERATION** `interconnector_net` value=40 d1=0.0 d12=3943.0 z=26.950050302919706
- **ROBUST_OUTLIER** `interconnector_net` value=40 d1=0.0 d12=3943.0 z=26.950050302919706
- **ROBUST_OUTLIER** `ps_gen` value=-423 d1=0.0 d12=-2.0 z=17.761563416666668
- **ROBUST_OUTLIER** `margin` value=3.762e+04 d1=0.0 d12=589.0 z=-14.07997353125
- **CHANGE_POINT** `wind_gen` value=1.514e+04 d1=0.0 d12=-550.0 z=-3.1899135701320134
- **CHANGE_POINT** `ind_generation` value=2.679e+04 d1=0.0 d12=-76.0 z=-2.348223574074074
- **PERSISTENT_DOWN** `wind_gen` value=1.514e+04 d1=0.0 d12=-550.0 z=-3.1899135701320134
- **ROBUST_OUTLIER** `wind_gen` value=1.514e+04 d1=0.0 d12=-550.0 z=-3.1899135701320134
- **PERSISTENT_DOWN** `residual_proxy` value=8953 d1=0.0 d12=-725.0 z=-3.094968789556962
- **ROBUST_OUTLIER** `residual_proxy` value=8953 d1=0.0 d12=-725.0 z=-3.094968789556962
- **PERSISTENT_UP** `thermal_base` value=6740 d1=0.0 d12=194.0 z=0.5733162875000001
- **PERSISTENT_UP** `ccgt_gen` value=3401 d1=0.0 d12=189.0 z=0.555354332201087

## Nearest historical live analogues

- `2026-09-19T07:23:46.754706Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:27:59.733660Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:32:11.773694Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:36:22.503128Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:40:34.209614Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T10:53:09.372285Z`  
Memory snapshots: **836**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `wind_forecast` value=1.903e+04 d1=0.0 d12=-223.0 z=-15.041121425
- **PERSISTENT_DOWN** `ts_demand_forecast` value=1.66e+04 d1=-3265.0 d12=-3265.0 z=-14.803583730434783
- **ACCELERATION** `ts_demand_forecast` value=1.66e+04 d1=-3265.0 d12=-3265.0 z=-14.803583730434783
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.66e+04 d1=-3265.0 d12=-3265.0 z=-14.803583730434783
- **CHANGE_POINT** `imbalance` value=6691 d1=0.0 d12=28.0 z=-3.639699405660377
- **PERSISTENT_DOWN** `residual_proxy` value=-2935 d1=-2159.0 d12=-1936.0 z=-5.346906634083045
- **ACCELERATION** `residual_proxy` value=-2935 d1=-2159.0 d12=-1936.0 z=-5.346906634083045
- **ROBUST_OUTLIER** `residual_proxy` value=-2935 d1=-2159.0 d12=-1936.0 z=-5.346906634083045
- **ROBUST_OUTLIER** `imbalance` value=6691 d1=0.0 d12=28.0 z=-3.639699405660377
- **PERSISTENT_UP** `margin` value=3.681e+04 d1=2375.0 d12=2399.0 z=3.5789252040816324
- **ACCELERATION** `margin` value=3.681e+04 d1=2375.0 d12=2399.0 z=3.5789252040816324
- **ROBUST_OUTLIER** `margin` value=3.681e+04 d1=2375.0 d12=2399.0 z=3.5789252040816324
- **CHANGE_POINT** `ccgt_gen` value=1816 d1=8.0 d12=5.0 z=-1.1657746105359317
- **CHANGE_POINT** `thermal_base` value=5127 d1=1.0 d12=1.0 z=-1.1645422906516445
- **CHANGE_POINT** `ind_demand` value=-1.304e+04 d1=0.0 d12=-30.0 z=-0.9076590552670623

## Nearest historical live analogues

- `2026-09-16T08:31:21.232151Z` distance=1.095 → {'next30m_imbalance_delta': -402.0, 'next30m_margin_delta': -815.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:35:35.956217Z` distance=1.095 → {'next30m_imbalance_delta': -402.0, 'next30m_margin_delta': -815.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:39:47.959049Z` distance=1.095 → {'next30m_imbalance_delta': -402.0, 'next30m_margin_delta': -815.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:44:00.472237Z` distance=1.095 → {'next30m_imbalance_delta': -402.0, 'next30m_margin_delta': -815.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:48:13.539661Z` distance=1.095 → {'next30m_imbalance_delta': -402.0, 'next30m_margin_delta': -815.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

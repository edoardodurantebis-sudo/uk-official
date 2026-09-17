# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T12:21:21.942046Z`  
Memory snapshots: **857**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.851e+04 d1=0.0 d12=-14.0 z=27.794598447916666
- **ROBUST_OUTLIER** `ind_generation` value=2.851e+04 d1=0.0 d12=-14.0 z=27.794598447916666
- **CHANGE_POINT** `imbalance` value=1.196e+04 d1=0.0 d12=-14.0 z=14.662272509345796
- **ROBUST_OUTLIER** `wind_forecast` value=1.903e+04 d1=0.0 d12=0.0 z=-15.041121425
- **ROBUST_OUTLIER** `imbalance` value=1.196e+04 d1=0.0 d12=-14.0 z=14.662272509345796
- **CHANGE_POINT** `demand_forecast` value=1.604e+04 d1=0.0 d12=0.0 z=-4.089440593835617
- **CHANGE_POINT** `residual_proxy` value=-2989 d1=0.0 d12=0.0 z=-3.7809425422535208
- **CHANGE_POINT** `ts_demand_forecast` value=1.654e+04 d1=0.0 d12=0.0 z=-2.3466053650472336
- **ROBUST_OUTLIER** `demand_forecast` value=1.604e+04 d1=0.0 d12=0.0 z=-4.089440593835617
- **CHANGE_POINT** `wind_gen` value=1.416e+04 d1=-104.0 d12=-936.0 z=-1.9640314559386973
- **ROBUST_OUTLIER** `residual_proxy` value=-2989 d1=0.0 d12=0.0 z=-3.7809425422535208
- **CHANGE_POINT** `ps_gen` value=-947 d1=5.0 d12=-5.0 z=-0.6591604375000001
- **PERSISTENT_DOWN** `wind_gen` value=1.416e+04 d1=-104.0 d12=-936.0 z=-1.9640314559386973
- **PERSISTENT_DOWN** `margin` value=3.645e+04 d1=-270.0 d12=-636.0 z=1.6093088771929824
- **ACCELERATION** `margin` value=3.645e+04 d1=-270.0 d12=-636.0 z=1.6093088771929824

## Nearest historical live analogues

- `2026-09-17T10:57:20.878127Z` distance=0.216 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:01:31.274983Z` distance=0.216 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:05:43.396655Z` distance=0.216 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:09:56.284661Z` distance=0.216 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:14:08.992825Z` distance=0.216 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

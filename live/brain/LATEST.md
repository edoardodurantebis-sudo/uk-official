# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T13:08:19.757086Z`  
Memory snapshots: **222**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=5698 d1=0.0 d12=48.0 z=14.97960203021978
- **ROBUST_OUTLIER** `imbalance` value=5698 d1=0.0 d12=48.0 z=14.97960203021978
- **CHANGE_POINT** `ind_generation` value=2.48e+04 d1=0.0 d12=48.0 z=10.00203026048387
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=0.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `ind_generation` value=2.48e+04 d1=0.0 d12=48.0 z=10.00203026048387
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=0.0 z=-6.6449730925925925
- **CHANGE_POINT** `margin` value=3.517e+04 d1=0.0 d12=-10.0 z=1.872329406354515
- **CHANGE_POINT** `wind_gen` value=1.004e+04 d1=-35.0 d12=-930.0 z=-1.5457056770833333
- **ROBUST_OUTLIER** `residual_proxy` value=756 d1=0.0 d12=-249.0 z=-3.155063532560707
- **CHANGE_POINT** `ps_gen` value=-739 d1=151.0 d12=352.0 z=1.068096097260274
- **CHANGE_POINT** `interconnector_net` value=1.092e+04 d1=-146.0 d12=-371.0 z=-0.23402370508054524
- **PERSISTENT_DOWN** `wind_gen` value=1.004e+04 d1=-35.0 d12=-930.0 z=-1.5457056770833333
- **PERSISTENT_UP** `ps_gen` value=-739 d1=151.0 d12=352.0 z=1.068096097260274
- **REVERSAL** `thermal_base` value=4788 d1=-24.0 d12=1.0 z=-0.7051483749999999
- **ACCELERATION** `thermal_base` value=4788 d1=-24.0 d12=1.0 z=-0.7051483749999999

## Nearest historical live analogues

- `2026-09-15T11:52:29.344058Z` distance=0.396 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:56:43.921407Z` distance=0.396 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T12:00:57.047099Z` distance=0.396 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T12:05:17.663793Z` distance=0.396 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': -249.0}
- `2026-09-15T12:09:30.579354Z` distance=0.396 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': -249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

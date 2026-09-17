# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T11:51:58.101795Z`  
Memory snapshots: **850**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.852e+04 d1=0.0 d12=-19.0 z=29.902378916666667
- **ROBUST_OUTLIER** `ind_generation` value=2.852e+04 d1=0.0 d12=-19.0 z=29.902378916666667
- **CHANGE_POINT** `imbalance` value=1.198e+04 d1=0.0 d12=35.0 z=19.160807006797583
- **ROBUST_OUTLIER** `imbalance` value=1.198e+04 d1=0.0 d12=35.0 z=19.160807006797583
- **ROBUST_OUTLIER** `wind_forecast` value=1.903e+04 d1=0.0 d12=0.0 z=-15.041121425
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.654e+04 d1=0.0 d12=-54.0 z=-6.955338302
- **CHANGE_POINT** `residual_proxy` value=-2989 d1=0.0 d12=-54.0 z=-3.7809425422535208
- **CHANGE_POINT** `margin` value=3.672e+04 d1=-366.0 d12=-90.0 z=2.3300555
- **ROBUST_OUTLIER** `demand_forecast` value=1.604e+04 d1=0.0 d12=-54.0 z=-4.089440593835617
- **ROBUST_OUTLIER** `residual_proxy` value=-2989 d1=0.0 d12=-54.0 z=-3.7809425422535208
- **CHANGE_POINT** `ind_demand` value=-1.126e+04 d1=0.0 d12=0.0 z=0.8646278100890208
- **PERSISTENT_DOWN** `margin` value=3.672e+04 d1=-366.0 d12=-90.0 z=2.3300555
- **ACCELERATION** `margin` value=3.672e+04 d1=-366.0 d12=-90.0 z=2.3300555
- **CHANGE_POINT** `wind_gen` value=1.516e+04 d1=-51.0 d12=-319.0 z=-0.23047890954773867
- **REVERSAL** `thermal_base` value=5115 d1=2.0 d12=-39.0 z=-0.6953323517167382

## Nearest historical live analogues

- `2026-09-17T10:57:20.878127Z` distance=0.057 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T05:33:01.983577Z` distance=0.984 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T05:37:13.562379Z` distance=0.984 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T05:41:25.151994Z` distance=0.984 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T05:45:36.025806Z` distance=0.984 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

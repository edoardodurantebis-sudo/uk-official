# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T11:22:30.108358Z`  
Memory snapshots: **843**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.854e+04 d1=0.0 d12=1986.0 z=34.39897725
- **ROBUST_OUTLIER** `ind_generation` value=2.854e+04 d1=0.0 d12=1986.0 z=34.39897725
- **CHANGE_POINT** `imbalance` value=1.194e+04 d1=0.0 d12=5251.0 z=29.209153340277776
- **ROBUST_OUTLIER** `imbalance` value=1.194e+04 d1=0.0 d12=5251.0 z=29.209153340277776
- **PERSISTENT_DOWN** `ts_demand_forecast` value=1.654e+04 d1=-54.0 d12=-3319.0 z=-15.120300656521739
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.654e+04 d1=-54.0 d12=-3319.0 z=-15.120300656521739
- **ROBUST_OUTLIER** `wind_forecast` value=1.903e+04 d1=0.0 d12=0.0 z=-15.041121425
- **PERSISTENT_DOWN** `residual_proxy` value=-2989 d1=-54.0 d12=-2213.0 z=-6.693478998878923
- **ROBUST_OUTLIER** `residual_proxy` value=-2989 d1=-54.0 d12=-2213.0 z=-6.693478998878923
- **CHANGE_POINT** `margin` value=3.709e+04 d1=276.0 d12=2651.0 z=4.528716892857143
- **PERSISTENT_UP** `margin` value=3.709e+04 d1=276.0 d12=2651.0 z=4.528716892857143
- **ROBUST_OUTLIER** `margin` value=3.709e+04 d1=276.0 d12=2651.0 z=4.528716892857143
- **PERSISTENT_DOWN** `demand_forecast` value=1.604e+04 d1=-54.0 d12=-2213.0 z=-4.089440593835617
- **ROBUST_OUTLIER** `demand_forecast` value=1.604e+04 d1=-54.0 d12=-2213.0 z=-4.089440593835617
- **CHANGE_POINT** `ind_demand` value=-1.126e+04 d1=0.0 d12=1771.0 z=0.8646278100890208

## Nearest historical live analogues

- `2026-09-17T05:33:01.983577Z` distance=1.102 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T05:37:13.562379Z` distance=1.102 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T05:41:25.151994Z` distance=1.102 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T05:45:36.025806Z` distance=1.102 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:52:02.690108Z` distance=1.113 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

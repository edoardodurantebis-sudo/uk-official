# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T11:35:04.831562Z`  
Memory snapshots: **846**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.852e+04 d1=0.0 d12=1967.0 z=34.078594618749996
- **ROBUST_OUTLIER** `ind_generation` value=2.852e+04 d1=0.0 d12=1967.0 z=34.078594618749996
- **CHANGE_POINT** `imbalance` value=1.198e+04 d1=0.0 d12=5286.0 z=28.88042475
- **PERSISTENT_UP** `imbalance` value=1.198e+04 d1=0.0 d12=5286.0 z=28.88042475
- **ROBUST_OUTLIER** `imbalance` value=1.198e+04 d1=0.0 d12=5286.0 z=28.88042475
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.654e+04 d1=0.0 d12=-3319.0 z=-15.120300656521739
- **ROBUST_OUTLIER** `wind_forecast` value=1.903e+04 d1=0.0 d12=0.0 z=-15.041121425
- **CHANGE_POINT** `margin` value=3.709e+04 d1=0.0 d12=2651.0 z=4.528716892857143
- **ROBUST_OUTLIER** `margin` value=3.709e+04 d1=0.0 d12=2651.0 z=4.528716892857143
- **ROBUST_OUTLIER** `demand_forecast` value=1.604e+04 d1=0.0 d12=-2213.0 z=-4.089440593835617
- **ROBUST_OUTLIER** `residual_proxy` value=-2989 d1=0.0 d12=-2213.0 z=-3.7809425422535208
- **CHANGE_POINT** `ind_demand` value=-1.126e+04 d1=0.0 d12=1771.0 z=0.8646278100890208
- **CHANGE_POINT** `ps_gen` value=-942 d1=0.0 d12=6.0 z=-0.8442504296046287
- **CHANGE_POINT** `wind_gen` value=1.51e+04 d1=0.0 d12=-580.0 z=-0.3152254501718213
- **PERSISTENT_DOWN** `thermal_base` value=5125 d1=0.0 d12=-1.0 z=-0.8525149256505576

## Nearest historical live analogues

- `2026-09-17T05:33:01.983577Z` distance=1.090 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T05:37:13.562379Z` distance=1.090 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T05:41:25.151994Z` distance=1.090 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T05:45:36.025806Z` distance=1.090 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:52:02.690108Z` distance=1.092 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

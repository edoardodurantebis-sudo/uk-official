# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T12:04:34.286599Z`  
Memory snapshots: **853**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.851e+04 d1=0.0 d12=-33.0 z=29.69253766111111
- **PERSISTENT_DOWN** `ind_generation` value=2.851e+04 d1=0.0 d12=-33.0 z=29.69253766111111
- **ROBUST_OUTLIER** `ind_generation` value=2.851e+04 d1=0.0 d12=-33.0 z=29.69253766111111
- **CHANGE_POINT** `imbalance` value=1.196e+04 d1=0.0 d12=21.0 z=20.10151299522293
- **ROBUST_OUTLIER** `imbalance` value=1.196e+04 d1=0.0 d12=21.0 z=20.10151299522293
- **ROBUST_OUTLIER** `wind_forecast` value=1.903e+04 d1=0.0 d12=0.0 z=-15.041121425
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.654e+04 d1=0.0 d12=-54.0 z=-6.955338302
- **ROBUST_OUTLIER** `demand_forecast` value=1.604e+04 d1=0.0 d12=-54.0 z=-4.089440593835617
- **ROBUST_OUTLIER** `residual_proxy` value=-2989 d1=0.0 d12=-54.0 z=-3.7809425422535208
- **CHANGE_POINT** `ind_demand` value=-1.126e+04 d1=0.0 d12=0.0 z=0.8646278100890208
- **CHANGE_POINT** `wind_gen` value=1.488e+04 d1=-28.0 d12=-330.0 z=-0.7304818748403576
- **CHANGE_POINT** `ps_gen` value=-942 d1=-3.0 d12=-7.0 z=-0.6549269955863808
- **ACCELERATION** `nuclear_gen` value=3306 d1=-7.0 d12=0.0 z=-1.5738094166666665
- **PERSISTENT_DOWN** `wind_gen` value=1.488e+04 d1=-28.0 d12=-330.0 z=-0.7304818748403576
- **ACCELERATION** `thermal_base` value=5120 d1=-10.0 d12=-28.0 z=-0.6879387903323263

## Nearest historical live analogues

- `2026-09-17T10:57:20.878127Z` distance=0.057 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:01:31.274983Z` distance=0.057 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:05:43.396655Z` distance=0.057 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:09:56.284661Z` distance=0.057 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T05:33:01.983577Z` distance=0.984 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': -74.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

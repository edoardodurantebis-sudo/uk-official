# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T09:41:05.251440Z`  
Memory snapshots: **1789**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.598e+04 d1=0.0 d12=2908.0 z=23.615572371875
- **ROBUST_OUTLIER** `ind_generation` value=1.598e+04 d1=0.0 d12=2908.0 z=23.615572371875
- **CHANGE_POINT** `margin` value=3.889e+04 d1=0.0 d12=1400.0 z=20.9858288125
- **ROBUST_OUTLIER** `margin` value=3.889e+04 d1=0.0 d12=1400.0 z=20.9858288125
- **CHANGE_POINT** `imbalance` value=-4187 d1=0.0 d12=2908.0 z=7.064392644736842
- **CHANGE_POINT** `ind_demand` value=-1.238e+04 d1=0.0 d12=-77.0 z=-6.7448975
- **ROBUST_OUTLIER** `imbalance` value=-4187 d1=0.0 d12=2908.0 z=7.064392644736842
- **ROBUST_OUTLIER** `ind_demand` value=-1.238e+04 d1=0.0 d12=-77.0 z=-6.7448975
- **PERSISTENT_DOWN** `ccgt_gen` value=2274 d1=0.0 d12=-349.0 z=-4.57585492266187
- **ROBUST_OUTLIER** `ccgt_gen` value=2274 d1=0.0 d12=-349.0 z=-4.57585492266187
- **PERSISTENT_DOWN** `thermal_base` value=5611 d1=0.0 d12=-346.0 z=-4.449736828454332
- **ROBUST_OUTLIER** `thermal_base` value=5611 d1=0.0 d12=-346.0 z=-4.449736828454332
- **PERSISTENT_DOWN** `interconnector_net` value=-4457 d1=0.0 d12=-1213.0 z=1.9512085208385481
- **PERSISTENT_DOWN** `wind_gen` value=1.486e+04 d1=-29.0 d12=-139.0 z=-1.1417983481228668
- **REVERSAL** `ps_gen` value=-929 d1=-1.0 d12=6.0 z=-0.7603339

## Nearest historical live analogues

- `2026-09-20T07:22:31.595881Z` distance=0.323 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:26:42.911856Z` distance=0.323 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:30:56.792344Z` distance=0.323 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:35:11.628590Z` distance=0.323 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:39:23.525158Z` distance=0.323 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

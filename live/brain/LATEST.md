# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T10:46:52.474569Z`  
Memory snapshots: **530**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ps_gen` value=-5 d1=0.0 d12=-229.0 z=-30.7567326
- **CHANGE_POINT** `imbalance` value=5373 d1=0.0 d12=6.0 z=-7.449460041401275
- **ROBUST_OUTLIER** `imbalance` value=5373 d1=0.0 d12=6.0 z=-7.449460041401275
- **ROBUST_OUTLIER** `ind_demand` value=-1.511e+04 d1=0.0 d12=-1226.0 z=-4.953071194444444
- **PERSISTENT_DOWN** `nuclear_gen` value=3317 d1=0.0 d12=-10.0 z=-4.0469384999999996
- **ACCELERATION** `nuclear_gen` value=3317 d1=0.0 d12=-10.0 z=-4.0469384999999996
- **ROBUST_OUTLIER** `nuclear_gen` value=3317 d1=0.0 d12=-10.0 z=-4.0469384999999996
- **ROBUST_OUTLIER** `residual_proxy` value=-1246 d1=0.0 d12=-433.0 z=-3.6989533423566883
- **CHANGE_POINT** `wind_gen` value=4881 d1=-32.0 d12=-710.0 z=-1.6202228028969956
- **CHANGE_POINT** `ind_generation` value=2.601e+04 d1=0.0 d12=6.0 z=-1.6059279761904761
- **ROBUST_OUTLIER** `wind_forecast` value=1.976e+04 d1=0.0 d12=433.0 z=3.2392692452229297
- **CHANGE_POINT** `thermal_base` value=9423 d1=-32.0 d12=-209.0 z=-1.1882736088615022
- **CHANGE_POINT** `ccgt_gen` value=6106 d1=-32.0 d12=-199.0 z=-1.1770895695830887
- **PERSISTENT_DOWN** `wind_gen` value=4881 d1=-32.0 d12=-710.0 z=-1.6202228028969956
- **PERSISTENT_DOWN** `thermal_base` value=9423 d1=-32.0 d12=-209.0 z=-1.1882736088615022

## Nearest historical live analogues

- `2026-09-16T09:51:49.097467Z` distance=2.954 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:22:28.850484Z` distance=2.957 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:26:41.423464Z` distance=2.957 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:30:50.292124Z` distance=2.957 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:35:00.318078Z` distance=2.957 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

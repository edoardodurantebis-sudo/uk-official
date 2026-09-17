# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T00:03:44.260171Z`  
Memory snapshots: **682**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=-657.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=657.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6615 d1=-125.0 d12=-885.0 z=-4.919263150943396
- **PERSISTENT_DOWN** `interconnector_net` value=-6615 d1=-125.0 d12=-885.0 z=-4.919263150943396
- **ROBUST_OUTLIER** `interconnector_net` value=-6615 d1=-125.0 d12=-885.0 z=-4.919263150943396
- **PERSISTENT_DOWN** `ccgt_gen` value=4732 d1=-281.0 d12=-1168.0 z=-3.397087644977169
- **ROBUST_OUTLIER** `ccgt_gen` value=4732 d1=-281.0 d12=-1168.0 z=-3.397087644977169
- **PERSISTENT_DOWN** `thermal_base` value=8053 d1=-277.0 d12=-1160.0 z=-3.3770580193621864
- **ROBUST_OUTLIER** `thermal_base` value=8053 d1=-277.0 d12=-1160.0 z=-3.3770580193621864
- **CHANGE_POINT** `imbalance` value=6451 d1=0.0 d12=-168.0 z=-0.607040775
- **CHANGE_POINT** `ind_generation` value=2.557e+04 d1=0.0 d12=-168.0 z=-0.16429878525641026
- **PERSISTENT_UP** `nuclear_gen` value=3321 d1=4.0 d12=8.0 z=2.0984125555555555
- **PERSISTENT_UP** `wind_gen` value=1.171e+04 d1=51.0 d12=791.0 z=1.232292932440406
- **PERSISTENT_UP** `ps_gen` value=-247 d1=1.0 d12=3.0 z=-0.8181910211132437
- **PERSISTENT_DOWN** `imbalance` value=6451 d1=0.0 d12=-168.0 z=-0.607040775

## Nearest historical live analogues

- `2026-09-16T14:21:30.462993Z` distance=0.273 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.274 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:29:54.321922Z` distance=0.274 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:34:06.314775Z` distance=0.274 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:38:16.233128Z` distance=0.274 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T04:48:27.539229Z`  
Memory snapshots: **445**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=7147 d1=0.0 d12=126.0 z=19.8542111025641
- **CHANGE_POINT** `ind_generation` value=2.627e+04 d1=0.0 d12=126.0 z=19.8542111025641
- **ROBUST_OUTLIER** `imbalance` value=7147 d1=0.0 d12=126.0 z=19.8542111025641
- **ROBUST_OUTLIER** `ind_generation` value=2.627e+04 d1=0.0 d12=126.0 z=19.8542111025641
- **CHANGE_POINT** `ccgt_gen` value=4100 d1=178.0 d12=1319.0 z=9.335794634920635
- **CHANGE_POINT** `thermal_base` value=7424 d1=175.0 d12=1315.0 z=9.007032353846153
- **PERSISTENT_UP** `ccgt_gen` value=4100 d1=178.0 d12=1319.0 z=9.335794634920635
- **ROBUST_OUTLIER** `ccgt_gen` value=4100 d1=178.0 d12=1319.0 z=9.335794634920635
- **CHANGE_POINT** `interconnector_net` value=-948 d1=-75.0 d12=-2705.0 z=-7.156438222192225
- **PERSISTENT_UP** `thermal_base` value=7424 d1=175.0 d12=1315.0 z=9.007032353846153
- **ROBUST_OUTLIER** `thermal_base` value=7424 d1=175.0 d12=1315.0 z=9.007032353846153
- **PERSISTENT_DOWN** `interconnector_net` value=-948 d1=-75.0 d12=-2705.0 z=-7.156438222192225
- **ROBUST_OUTLIER** `interconnector_net` value=-948 d1=-75.0 d12=-2705.0 z=-7.156438222192225
- **CHANGE_POINT** `wind_gen` value=9210 d1=-58.0 d12=-402.0 z=-1.6791284141749723
- **CHANGE_POINT** `ind_demand` value=-1.22e+04 d1=0.0 d12=3.0 z=-0.574033829787234

## Nearest historical live analogues

- `2026-09-16T03:53:53.579562Z` distance=0.007 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:32:58.473492Z` distance=0.019 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:37:08.879637Z` distance=0.019 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:41:19.622154Z` distance=0.019 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:45:29.518871Z` distance=0.019 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

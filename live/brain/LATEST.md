# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T05:59:40.455597Z`  
Memory snapshots: **462**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=8316 d1=200.0 d12=2208.0 z=12.40670838517179
- **CHANGE_POINT** `thermal_base` value=1.165e+04 d1=199.0 d12=2211.0 z=12.399390232368898
- **PERSISTENT_UP** `ccgt_gen` value=8316 d1=200.0 d12=2208.0 z=12.40670838517179
- **ROBUST_OUTLIER** `ccgt_gen` value=8316 d1=200.0 d12=2208.0 z=12.40670838517179
- **PERSISTENT_UP** `thermal_base` value=1.165e+04 d1=199.0 d12=2211.0 z=12.399390232368898
- **ROBUST_OUTLIER** `thermal_base` value=1.165e+04 d1=199.0 d12=2211.0 z=12.399390232368898
- **PERSISTENT_UP** `imbalance` value=7214 d1=0.0 d12=11.0 z=12.337974042307692
- **ROBUST_OUTLIER** `imbalance` value=7214 d1=0.0 d12=11.0 z=12.337974042307692
- **PERSISTENT_UP** `ind_generation` value=2.634e+04 d1=0.0 d12=11.0 z=12.337974042307692
- **ROBUST_OUTLIER** `ind_generation` value=2.634e+04 d1=0.0 d12=11.0 z=12.337974042307692
- **CHANGE_POINT** `interconnector_net` value=-1875 d1=34.0 d12=-678.0 z=-3.6209628665574596
- **CHANGE_POINT** `wind_gen` value=7929 d1=-148.0 d12=-1395.0 z=-3.170959227224576
- **REVERSAL** `interconnector_net` value=-1875 d1=34.0 d12=-678.0 z=-3.6209628665574596
- **ROBUST_OUTLIER** `interconnector_net` value=-1875 d1=34.0 d12=-678.0 z=-3.6209628665574596
- **PERSISTENT_DOWN** `wind_gen` value=7929 d1=-148.0 d12=-1395.0 z=-3.170959227224576

## Nearest historical live analogues

- `2026-09-16T03:32:58.473492Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:37:08.879637Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:41:19.622154Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:45:29.518871Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:49:41.884820Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

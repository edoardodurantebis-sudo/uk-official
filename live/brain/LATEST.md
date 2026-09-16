# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T05:55:30.704372Z`  
Memory snapshots: **461**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=8116 d1=0.0 d12=2546.0 z=12.724157986486487
- **CHANGE_POINT** `thermal_base` value=1.145e+04 d1=0.0 d12=2552.0 z=12.411373535310734
- **PERSISTENT_UP** `ccgt_gen` value=8116 d1=0.0 d12=2546.0 z=12.724157986486487
- **ROBUST_OUTLIER** `ccgt_gen` value=8116 d1=0.0 d12=2546.0 z=12.724157986486487
- **PERSISTENT_UP** `thermal_base` value=1.145e+04 d1=0.0 d12=2552.0 z=12.411373535310734
- **ROBUST_OUTLIER** `thermal_base` value=1.145e+04 d1=0.0 d12=2552.0 z=12.411373535310734
- **PERSISTENT_UP** `imbalance` value=7214 d1=0.0 d12=11.0 z=12.337974042307692
- **ACCELERATION** `imbalance` value=7214 d1=0.0 d12=11.0 z=12.337974042307692
- **ROBUST_OUTLIER** `imbalance` value=7214 d1=0.0 d12=11.0 z=12.337974042307692
- **PERSISTENT_UP** `ind_generation` value=2.634e+04 d1=0.0 d12=11.0 z=12.337974042307692
- **ACCELERATION** `ind_generation` value=2.634e+04 d1=0.0 d12=11.0 z=12.337974042307692
- **ROBUST_OUTLIER** `ind_generation` value=2.634e+04 d1=0.0 d12=11.0 z=12.337974042307692
- **CHANGE_POINT** `interconnector_net` value=-1909 d1=0.0 d12=-821.0 z=-4.509388059131736
- **CHANGE_POINT** `wind_gen` value=8077 d1=0.0 d12=-1107.0 z=-2.9671820849256902
- **PERSISTENT_DOWN** `interconnector_net` value=-1909 d1=0.0 d12=-821.0 z=-4.509388059131736

## Nearest historical live analogues

- `2026-09-16T03:32:58.473492Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:37:08.879637Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:41:19.622154Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:45:29.518871Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:49:41.884820Z` distance=0.285 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

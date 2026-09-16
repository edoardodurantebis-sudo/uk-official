# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T05:30:25.684923Z`  
Memory snapshots: **455**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=7024 d1=0.0 d12=3195.0 z=30.472483348214286
- **CHANGE_POINT** `thermal_base` value=1.034e+04 d1=0.0 d12=3189.0 z=29.0183885625
- **PERSISTENT_UP** `ccgt_gen` value=7024 d1=0.0 d12=3195.0 z=30.472483348214286
- **ROBUST_OUTLIER** `ccgt_gen` value=7024 d1=0.0 d12=3195.0 z=30.472483348214286
- **PERSISTENT_UP** `thermal_base` value=1.034e+04 d1=0.0 d12=3189.0 z=29.0183885625
- **ROBUST_OUTLIER** `thermal_base` value=1.034e+04 d1=0.0 d12=3189.0 z=29.0183885625
- **ROBUST_OUTLIER** `imbalance` value=7173 d1=0.0 d12=26.0 z=16.73308613829787
- **ROBUST_OUTLIER** `ind_generation` value=2.629e+04 d1=0.0 d12=26.0 z=16.73308613829787
- **PERSISTENT_DOWN** `interconnector_net` value=-1355 d1=0.0 d12=-507.0 z=-7.201149919362994
- **ROBUST_OUTLIER** `interconnector_net` value=-1355 d1=0.0 d12=-507.0 z=-7.201149919362994
- **CHANGE_POINT** `wind_gen` value=8816 d1=0.0 d12=-577.0 z=-2.1157597517103763
- **CHANGE_POINT** `ps_gen` value=223 d1=0.0 d12=0.0 z=0.67448975
- **PERSISTENT_DOWN** `nuclear_gen` value=3321 d1=0.0 d12=-6.0 z=-2.360714125
- **ACCELERATION** `nuclear_gen` value=3321 d1=0.0 d12=-6.0 z=-2.360714125
- **PERSISTENT_UP** `margin` value=3.755e+04 d1=0.0 d12=5.0 z=2.3591081970238097

## Nearest historical live analogues

- `2026-09-16T03:32:58.473492Z` distance=0.033 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:37:08.879637Z` distance=0.033 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:41:19.622154Z` distance=0.033 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:45:29.518871Z` distance=0.033 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:49:41.884820Z` distance=0.033 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

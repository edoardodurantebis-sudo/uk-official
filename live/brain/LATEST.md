# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T01:55:42.934824Z`  
Memory snapshots: **1679**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.22e+04 d1=0.0 d12=-248.0 z=-108.930094625
- **ROBUST_OUTLIER** `ind_demand` value=-1.22e+04 d1=0.0 d12=-248.0 z=-108.930094625
- **CHANGE_POINT** `biomass_gen` value=1222 d1=6.0 d12=322.0 z=6.366774458333333
- **PERSISTENT_UP** `biomass_gen` value=1222 d1=6.0 d12=322.0 z=6.366774458333333
- **ROBUST_OUTLIER** `biomass_gen` value=1222 d1=6.0 d12=322.0 z=6.366774458333333
- **CHANGE_POINT** `ps_gen` value=-815 d1=4.0 d12=-561.0 z=-1.5754872518656717
- **CHANGE_POINT** `margin` value=3.602e+04 d1=0.0 d12=-9.0 z=-0.82624994375
- **CHANGE_POINT** `wind_gen` value=1.528e+04 d1=-78.0 d12=-284.0 z=0.12922009724238026
- **REVERSAL** `ps_gen` value=-815 d1=4.0 d12=-561.0 z=-1.5754872518656717
- **PERSISTENT_DOWN** `interconnector_net` value=-9959 d1=-28.0 d12=-515.0 z=-0.895112390604973
- **PERSISTENT_DOWN** `margin` value=3.602e+04 d1=0.0 d12=-9.0 z=-0.82624994375
- **ACCELERATION** `margin` value=3.602e+04 d1=0.0 d12=-9.0 z=-0.82624994375
- **REVERSAL** `nuclear_gen` value=3332 d1=-4.0 d12=1.0 z=-0.6744897499999999
- **ACCELERATION** `nuclear_gen` value=3332 d1=-4.0 d12=1.0 z=-0.6744897499999999
- **ACCELERATION** `imbalance` value=-3757 d1=0.0 d12=6.0 z=0.5820938938356165

## Nearest historical live analogues

- `2026-09-20T00:52:41.291035Z` distance=0.279 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T00:56:51.475200Z` distance=0.279 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 17.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T01:01:05.027789Z` distance=0.279 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 17.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T00:23:21.732789Z` distance=0.317 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T00:27:32.378354Z` distance=0.317 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 42.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

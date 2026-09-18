# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T00:13:07.727056Z`  
Memory snapshots: **1026**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `imbalance` value=1.014e+04 d1=0.0 d12=394.0 z=18.422001296875
- **CHANGE_POINT** `ind_generation` value=2.695e+04 d1=0.0 d12=394.0 z=18.422001296875
- **ROBUST_OUTLIER** `imbalance` value=1.014e+04 d1=0.0 d12=394.0 z=18.422001296875
- **ROBUST_OUTLIER** `ind_generation` value=2.695e+04 d1=0.0 d12=394.0 z=18.422001296875
- **ROBUST_OUTLIER** `ind_demand` value=-1.118e+04 d1=0.0 d12=0.0 z=-7.41938725
- **CHANGE_POINT** `wind_gen` value=1.44e+04 d1=124.0 d12=-417.0 z=-1.6831529280510018
- **CHANGE_POINT** `ps_gen` value=55 d1=1.0 d12=0.0 z=-0.7124001809133489
- **REVERSAL** `wind_gen` value=1.44e+04 d1=124.0 d12=-417.0 z=-1.6831529280510018
- **PERSISTENT_UP** `nuclear_gen` value=3325 d1=2.0 d12=7.0 z=1.1241495833333335
- **ACCELERATION** `nuclear_gen` value=3325 d1=2.0 d12=7.0 z=1.1241495833333335
- **PERSISTENT_UP** `interconnector_net` value=-5954 d1=33.0 d12=1236.0 z=-0.7958926945731943
- **ACCELERATION** `ps_gen` value=55 d1=1.0 d12=0.0 z=-0.7124001809133489
- **REVERSAL** `ccgt_gen` value=3962 d1=-139.0 d12=328.0 z=-0.6930415309430256
- **REVERSAL** `thermal_base` value=7287 d1=-137.0 d12=335.0 z=-0.6896839363369246
- **PERSISTENT_UP** `frequency` value=50.05 d1=0.0 d12=0.07600000000000051 z=None

## Nearest historical live analogues

- `2026-09-17T19:23:15.447841Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:27:27.221396Z` distance=3.578 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 26.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T18:57:56.745109Z` distance=3.578 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

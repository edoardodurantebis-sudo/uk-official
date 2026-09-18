# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T00:21:32.376170Z`  
Memory snapshots: **1028**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `imbalance` value=1.014e+04 d1=0.0 d12=394.0 z=18.422001296875
- **CHANGE_POINT** `ind_generation` value=2.695e+04 d1=0.0 d12=394.0 z=18.422001296875
- **ROBUST_OUTLIER** `imbalance` value=1.014e+04 d1=0.0 d12=394.0 z=18.422001296875
- **ROBUST_OUTLIER** `ind_generation` value=2.695e+04 d1=0.0 d12=394.0 z=18.422001296875
- **ROBUST_OUTLIER** `ind_demand` value=-1.118e+04 d1=0.0 d12=0.0 z=-7.41938725
- **CHANGE_POINT** `wind_gen` value=1.427e+04 d1=-115.0 d12=-344.0 z=-2.005040568306011
- **CHANGE_POINT** `ps_gen` value=175 d1=112.0 d12=123.0 z=-0.32258205434782605
- **PERSISTENT_DOWN** `wind_gen` value=1.427e+04 d1=-115.0 d12=-344.0 z=-2.005040568306011
- **REVERSAL** `biomass_gen` value=1957 d1=-1.0 d12=23.0 z=-1.2998392361927145
- **REVERSAL** `ccgt_gen` value=3860 d1=-38.0 d12=14.0 z=-0.7612193914441148
- **ACCELERATION** `ccgt_gen` value=3860 d1=-38.0 d12=14.0 z=-0.7612193914441148
- **PERSISTENT_UP** `interconnector_net` value=-5940 d1=27.0 d12=224.0 z=-0.7595651187688821
- **REVERSAL** `thermal_base` value=7183 d1=-38.0 d12=19.0 z=-0.7590506564659427
- **ACCELERATION** `thermal_base` value=7183 d1=-38.0 d12=19.0 z=-0.7590506564659427
- **ACCELERATION** `nuclear_gen` value=3323 d1=0.0 d12=5.0 z=0.6744897499999999

## Nearest historical live analogues

- `2026-09-17T18:57:56.745109Z` distance=3.578 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:10:36.600451Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:14:49.284800Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

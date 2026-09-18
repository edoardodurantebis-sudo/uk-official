# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T00:04:42.630537Z`  
Memory snapshots: **1024**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `imbalance` value=1.014e+04 d1=0.0 d12=425.0 z=18.422001296875
- **CHANGE_POINT** `ind_generation` value=2.695e+04 d1=0.0 d12=425.0 z=18.422001296875
- **PERSISTENT_UP** `imbalance` value=1.014e+04 d1=0.0 d12=425.0 z=18.422001296875
- **ROBUST_OUTLIER** `imbalance` value=1.014e+04 d1=0.0 d12=425.0 z=18.422001296875
- **PERSISTENT_UP** `ind_generation` value=2.695e+04 d1=0.0 d12=425.0 z=18.422001296875
- **ROBUST_OUTLIER** `ind_generation` value=2.695e+04 d1=0.0 d12=425.0 z=18.422001296875
- **ROBUST_OUTLIER** `ind_demand` value=-1.118e+04 d1=0.0 d12=-7.0 z=-7.41938725
- **CHANGE_POINT** `wind_gen` value=1.421e+04 d1=-67.0 d12=-849.0 z=-2.1622986520947176
- **CHANGE_POINT** `ps_gen` value=54 d1=-2.0 d12=-1.0 z=-0.7657740770676691
- **PERSISTENT_DOWN** `wind_gen` value=1.421e+04 d1=-67.0 d12=-849.0 z=-2.1622986520947176
- **PERSISTENT_UP** `biomass_gen` value=1961 d1=1.0 d12=206.0 z=-1.9791845694444445
- **PERSISTENT_DOWN** `nuclear_gen` value=3314 d1=-2.0 d12=-4.0 z=-1.3489794999999998
- **ACCELERATION** `nuclear_gen` value=3314 d1=-2.0 d12=-4.0 z=-1.3489794999999998
- **PERSISTENT_UP** `interconnector_net` value=-6044 d1=106.0 d12=1102.0 z=-0.8196281663608267
- **PERSISTENT_DOWN** `ps_gen` value=54 d1=-2.0 d12=-1.0 z=-0.7657740770676691

## Nearest historical live analogues

- `2026-09-17T19:23:15.447841Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:27:27.221396Z` distance=3.578 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 26.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T18:57:56.745109Z` distance=3.578 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

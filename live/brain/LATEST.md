# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T00:08:54.899390Z`  
Memory snapshots: **1025**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `imbalance` value=1.014e+04 d1=0.0 d12=425.0 z=18.422001296875
- **CHANGE_POINT** `ind_generation` value=2.695e+04 d1=0.0 d12=425.0 z=18.422001296875
- **ROBUST_OUTLIER** `imbalance` value=1.014e+04 d1=0.0 d12=425.0 z=18.422001296875
- **ROBUST_OUTLIER** `ind_generation` value=2.695e+04 d1=0.0 d12=425.0 z=18.422001296875
- **ROBUST_OUTLIER** `ind_demand` value=-1.118e+04 d1=0.0 d12=-7.0 z=-7.41938725
- **CHANGE_POINT** `wind_gen` value=1.428e+04 d1=71.0 d12=-668.0 z=-1.987840465391621
- **CHANGE_POINT** `ps_gen` value=54 d1=0.0 d12=-1.0 z=-0.7470509944987774
- **REVERSAL** `wind_gen` value=1.428e+04 d1=71.0 d12=-668.0 z=-1.987840465391621
- **REVERSAL** `biomass_gen` value=1959 d1=-2.0 d12=174.0 z=-1.768367226550681
- **PERSISTENT_UP** `interconnector_net` value=-5987 d1=57.0 d12=1205.0 z=-0.8044898988026266
- **PERSISTENT_DOWN** `ps_gen` value=54 d1=0.0 d12=-1.0 z=-0.7470509944987774
- **ACCELERATION** `ps_gen` value=54 d1=0.0 d12=-1.0 z=-0.7470509944987774
- **PERSISTENT_UP** `nuclear_gen` value=3323 d1=9.0 d12=4.0 z=0.6744897499999999
- **ACCELERATION** `nuclear_gen` value=3323 d1=9.0 d12=4.0 z=0.6744897499999999
- **REVERSAL** `ccgt_gen` value=4101 d1=-36.0 d12=468.0 z=-0.6009329320837391

## Nearest historical live analogues

- `2026-09-17T19:23:15.447841Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:27:27.221396Z` distance=3.578 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 26.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T18:57:56.745109Z` distance=3.578 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

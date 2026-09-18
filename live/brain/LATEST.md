# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T00:17:19.325122Z`  
Memory snapshots: **1027**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `imbalance` value=1.014e+04 d1=0.0 d12=394.0 z=18.422001296875
- **CHANGE_POINT** `ind_generation` value=2.695e+04 d1=0.0 d12=394.0 z=18.422001296875
- **ROBUST_OUTLIER** `imbalance` value=1.014e+04 d1=0.0 d12=394.0 z=18.422001296875
- **ROBUST_OUTLIER** `ind_generation` value=2.695e+04 d1=0.0 d12=394.0 z=18.422001296875
- **ROBUST_OUTLIER** `ind_demand` value=-1.118e+04 d1=0.0 d12=0.0 z=-7.41938725
- **CHANGE_POINT** `wind_gen` value=1.438e+04 d1=-16.0 d12=-272.0 z=-1.7224674489981784
- **CHANGE_POINT** `ps_gen` value=63 d1=8.0 d12=9.0 z=-0.67448975
- **ACCELERATION** `wind_gen` value=1.438e+04 d1=-16.0 d12=-272.0 z=-1.7224674489981784
- **REVERSAL** `biomass_gen` value=1958 d1=-1.0 d12=73.0 z=-1.3424230990279464
- **REVERSAL** `interconnector_net` value=-5967 d1=-13.0 d12=1226.0 z=-0.7826759997613137
- **REVERSAL** `ccgt_gen` value=3898 d1=-64.0 d12=139.0 z=-0.7357767198765431
- **ACCELERATION** `ccgt_gen` value=3898 d1=-64.0 d12=139.0 z=-0.7357767198765431
- **REVERSAL** `thermal_base` value=7221 d1=-66.0 d12=143.0 z=-0.7336905268737673
- **ACCELERATION** `thermal_base` value=7221 d1=-66.0 d12=143.0 z=-0.7336905268737673
- **PERSISTENT_UP** `ps_gen` value=63 d1=8.0 d12=9.0 z=-0.67448975

## Nearest historical live analogues

- `2026-09-17T19:23:15.447841Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:27:27.221396Z` distance=3.578 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 26.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T18:57:56.745109Z` distance=3.578 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=3.578 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T04:26:53.312473Z`  
Memory snapshots: **1373**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `imbalance` value=9764 d1=0.0 d12=342.0 z=7.52730561
- **CHANGE_POINT** `ind_generation` value=2.696e+04 d1=0.0 d12=342.0 z=7.52730561
- **ROBUST_OUTLIER** `imbalance` value=9764 d1=0.0 d12=342.0 z=7.52730561
- **ROBUST_OUTLIER** `ind_generation` value=2.696e+04 d1=0.0 d12=342.0 z=7.52730561
- **CHANGE_POINT** `ind_demand` value=-1.087e+04 d1=0.0 d12=12.0 z=3.8221085833333333
- **ROBUST_OUTLIER** `biomass_gen` value=693 d1=0.0 d12=-9.0 z=-4.320644485507246
- **CHANGE_POINT** `ccgt_gen` value=3059 d1=1.0 d12=3.0 z=-1.826814949488491
- **PERSISTENT_UP** `ind_demand` value=-1.087e+04 d1=0.0 d12=12.0 z=3.8221085833333333
- **ACCELERATION** `ind_demand` value=-1.087e+04 d1=0.0 d12=12.0 z=3.8221085833333333
- **ROBUST_OUTLIER** `ind_demand` value=-1.087e+04 d1=0.0 d12=12.0 z=3.8221085833333333
- **CHANGE_POINT** `interconnector_net` value=-1.1e+04 d1=0.0 d12=135.0 z=-0.6483397463235294
- **PERSISTENT_UP** `nuclear_gen` value=3345 d1=5.0 d12=1.0 z=2.0234692499999998
- **ACCELERATION** `nuclear_gen` value=3345 d1=5.0 d12=1.0 z=2.0234692499999998
- **CHANGE_POINT** `ps_gen` value=-545 d1=1.0 d12=-1.0 z=-0.005439433467741935
- **PERSISTENT_UP** `ccgt_gen` value=3059 d1=1.0 d12=3.0 z=-1.826814949488491

## Nearest historical live analogues

- `2026-09-19T03:32:06.717243Z` distance=0.011 → {'next30m_imbalance_delta': 380.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:23:44.436802Z` distance=0.308 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 748.0}
- `2026-09-19T03:27:55.750125Z` distance=0.308 → {'next30m_imbalance_delta': 380.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 748.0}
- `2026-09-19T02:54:16.089654Z` distance=0.308 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:58:27.254129Z` distance=0.308 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

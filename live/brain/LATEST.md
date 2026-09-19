# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T05:17:26.637585Z`  
Memory snapshots: **1385**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.086e+04 d1=0.0 d12=4.0 z=4.72142825
- **ROBUST_OUTLIER** `imbalance` value=9720 d1=0.0 d12=-44.0 z=4.721428250000001
- **ROBUST_OUTLIER** `ind_demand` value=-1.086e+04 d1=0.0 d12=4.0 z=4.72142825
- **ROBUST_OUTLIER** `ind_generation` value=2.691e+04 d1=0.0 d12=-50.0 z=4.6340842535971225
- **PERSISTENT_UP** `biomass_gen` value=694 d1=0.0 d12=1.0 z=-3.4909954333333335
- **ROBUST_OUTLIER** `biomass_gen` value=694 d1=0.0 d12=1.0 z=-3.4909954333333335
- **CHANGE_POINT** `margin` value=3.832e+04 d1=0.0 d12=2.0 z=0.9556397860721443
- **CHANGE_POINT** `ccgt_gen` value=3427 d1=-4.0 d12=368.0 z=-0.0011130193894389438
- **CHANGE_POINT** `thermal_base` value=6765 d1=-3.0 d12=361.0 z=0.0
- **PERSISTENT_DOWN** `wind_gen` value=1.596e+04 d1=-34.0 d12=-64.0 z=-0.36029705632911396
- **REVERSAL** `nuclear_gen` value=3338 d1=1.0 d12=-7.0 z=-0.337244875
- **ACCELERATION** `nuclear_gen` value=3338 d1=1.0 d12=-7.0 z=-0.337244875
- **REVERSAL** `interconnector_net` value=-1.088e+04 d1=-21.0 d12=124.0 z=0.06733085070052539
- **PERSISTENT_UP** `ps_gen` value=-542 d1=1.0 d12=3.0 z=0.013935738636363637
- **REVERSAL** `ccgt_gen` value=3427 d1=-4.0 d12=368.0 z=-0.0011130193894389438

## Nearest historical live analogues

- `2026-09-19T04:22:41.594365Z` distance=0.004 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:53:09.975185Z` distance=0.013 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:57:21.988080Z` distance=0.013 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T04:01:33.750127Z` distance=0.013 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T04:05:47.150254Z` distance=0.013 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

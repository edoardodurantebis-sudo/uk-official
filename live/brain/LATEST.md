# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T23:53:48.658666Z`  
Memory snapshots: **375**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.208e+04 d1=1.0 d12=1.0 z=-37.32176616666667
- **PERSISTENT_UP** `ind_demand` value=-1.208e+04 d1=1.0 d12=1.0 z=-37.32176616666667
- **ACCELERATION** `ind_demand` value=-1.208e+04 d1=1.0 d12=1.0 z=-37.32176616666667
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=1.0 d12=1.0 z=-37.32176616666667
- **CHANGE_POINT** `thermal_base` value=6562 d1=3.0 d12=12.0 z=-4.286916918080466
- **CHANGE_POINT** `ccgt_gen` value=3227 d1=0.0 d12=10.0 z=-4.2784992012312895
- **CHANGE_POINT** `biomass_gen` value=3224 d1=5.0 d12=-25.0 z=-2.4139633157894735
- **PERSISTENT_UP** `thermal_base` value=6562 d1=3.0 d12=12.0 z=-4.286916918080466
- **ROBUST_OUTLIER** `thermal_base` value=6562 d1=3.0 d12=12.0 z=-4.286916918080466
- **ROBUST_OUTLIER** `ccgt_gen` value=3227 d1=0.0 d12=10.0 z=-4.2784992012312895
- **CHANGE_POINT** `interconnector_net` value=3967 d1=-20.0 d12=-201.0 z=1.86159171
- **PERSISTENT_UP** `imbalance` value=5865 d1=39.0 d12=64.0 z=3.170101825
- **ACCELERATION** `imbalance` value=5865 d1=39.0 d12=64.0 z=3.170101825
- **ROBUST_OUTLIER** `imbalance` value=5865 d1=39.0 d12=64.0 z=3.170101825
- **PERSISTENT_UP** `ind_generation` value=2.499e+04 d1=38.0 d12=64.0 z=3.170101825

## Nearest historical live analogues

- `2026-09-15T18:20:25.201646Z` distance=0.721 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:50:55.506503Z` distance=0.721 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.721 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:59:22.215947Z` distance=0.721 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:03:35.364442Z` distance=0.721 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

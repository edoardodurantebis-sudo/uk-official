# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T00:06:21.657987Z`  
Memory snapshots: **378**  
Current physical regime: **BALANCED**

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=1.0 z=-37.32176616666667
- **CHANGE_POINT** `imbalance` value=5865 d1=0.0 d12=64.0 z=3.170101825
- **CHANGE_POINT** `ind_generation` value=2.499e+04 d1=0.0 d12=64.0 z=3.170101825
- **CHANGE_POINT** `biomass_gen` value=3220 d1=1.0 d12=-31.0 z=-2.697959
- **ROBUST_OUTLIER** `imbalance` value=5865 d1=0.0 d12=64.0 z=3.170101825
- **ROBUST_OUTLIER** `ind_generation` value=2.499e+04 d1=0.0 d12=64.0 z=3.170101825
- **CHANGE_POINT** `interconnector_net` value=4110 d1=186.0 d12=0.0 z=1.1142704516300497
- **REVERSAL** `biomass_gen` value=3220 d1=1.0 d12=-31.0 z=-2.697959
- **ACCELERATION** `thermal_base` value=6560 d1=1.0 d12=4.0 z=-2.583969802912158
- **ACCELERATION** `ccgt_gen` value=3228 d1=0.0 d12=-2.0 z=-2.580442379006665
- **CHANGE_POINT** `wind_gen` value=1.034e+04 d1=-42.0 d12=-457.0 z=-0.3714773279305828
- **PERSISTENT_UP** `interconnector_net` value=4110 d1=186.0 d12=0.0 z=1.1142704516300497
- **ACCELERATION** `interconnector_net` value=4110 d1=186.0 d12=0.0 z=1.1142704516300497
- **PERSISTENT_DOWN** `wind_gen` value=1.034e+04 d1=-42.0 d12=-457.0 z=-0.3714773279305828
- **PERSISTENT_UP** `ps_gen` value=202 d1=93.0 d12=30.0 z=0.17252254829931973

## Nearest historical live analogues

- `2026-09-15T18:20:25.201646Z` distance=0.721 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:50:55.506503Z` distance=0.721 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.721 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:59:22.215947Z` distance=0.721 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:03:35.364442Z` distance=0.721 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

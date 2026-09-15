# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T18:54:05.101210Z`  
Memory snapshots: **304**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3297 d1=-2.0 d12=74.0 z=38.72070787037037
- **REVERSAL** `biomass_gen` value=3297 d1=-2.0 d12=74.0 z=38.72070787037037
- **ROBUST_OUTLIER** `biomass_gen` value=3297 d1=-2.0 d12=74.0 z=38.72070787037037
- **REVERSAL** `ind_demand` value=-1.191e+04 d1=-1.0 d12=8.0 z=4.72142825
- **ROBUST_OUTLIER** `ind_demand` value=-1.191e+04 d1=-1.0 d12=8.0 z=4.72142825
- **CHANGE_POINT** `margin` value=3.559e+04 d1=0.0 d12=-81.0 z=1.9977744023809523
- **CHANGE_POINT** `ccgt_gen` value=1.09e+04 d1=48.0 d12=473.0 z=1.2908715363594256
- **CHANGE_POINT** `thermal_base` value=1.422e+04 d1=50.0 d12=479.0 z=1.2886846775127374
- **CHANGE_POINT** `ps_gen` value=804 d1=1.0 d12=296.0 z=0.9906568203124999
- **CHANGE_POINT** `interconnector_net` value=-1623 d1=-49.0 d12=287.0 z=-0.9660335271075439
- **CHANGE_POINT** `imbalance` value=5739 d1=2.0 d12=-36.0 z=-0.41996531603773585
- **CHANGE_POINT** `ind_generation` value=2.486e+04 d1=2.0 d12=-36.0 z=-0.41996531603773585
- **PERSISTENT_DOWN** `margin` value=3.559e+04 d1=0.0 d12=-81.0 z=1.9977744023809523
- **ACCELERATION** `margin` value=3.559e+04 d1=0.0 d12=-81.0 z=1.9977744023809523
- **PERSISTENT_UP** `ccgt_gen` value=1.09e+04 d1=48.0 d12=473.0 z=1.2908715363594256

## Nearest historical live analogues

- `2026-09-15T17:50:55.506503Z` distance=0.062 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.062 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:59:22.215947Z` distance=0.062 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:22:30.581865Z` distance=0.151 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:26:42.593420Z` distance=0.151 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

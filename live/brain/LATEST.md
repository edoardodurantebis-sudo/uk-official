# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T02:07:49.654352Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.243e+04 d1=0.0 d12=3.0 z=15.176019375
- **ROBUST_OUTLIER** `ind_demand` value=-1.243e+04 d1=0.0 d12=3.0 z=15.176019375
- **CHANGE_POINT** `biomass_gen` value=2842 d1=-17.0 d12=-75.0 z=-7.6442171666666665
- **PERSISTENT_DOWN** `biomass_gen` value=2842 d1=-17.0 d12=-75.0 z=-7.6442171666666665
- **ROBUST_OUTLIER** `biomass_gen` value=2842 d1=-17.0 d12=-75.0 z=-7.6442171666666665
- **CHANGE_POINT** `imbalance` value=-7980 d1=0.0 d12=18.0 z=2.221848588235294
- **CHANGE_POINT** `ind_generation` value=1.319e+04 d1=0.0 d12=18.0 z=2.221848588235294
- **PERSISTENT_UP** `wind_gen` value=5175 d1=133.0 d12=462.0 z=2.4680880538116594
- **PERSISTENT_DOWN** `interconnector_net` value=832 d1=-672.0 d12=-1055.0 z=-1.701056653611557
- **ACCELERATION** `interconnector_net` value=832 d1=-672.0 d12=-1055.0 z=-1.701056653611557
- **ACCELERATION** `ccgt_gen` value=9581 d1=-51.0 d12=-149.0 z=-0.655298854961832
- **ACCELERATION** `thermal_base` value=1.332e+04 d1=-38.0 d12=-138.0 z=-0.6513591001371742
- **PERSISTENT_UP** `nuclear_gen` value=3735 d1=13.0 d12=11.0 z=0.08431121875
- **ACCELERATION** `nuclear_gen` value=3735 d1=13.0 d12=11.0 z=0.08431121875

## Nearest historical live analogues

- `2026-09-23T00:50:49.821360Z` distance=0.012 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:55:39.096200Z` distance=0.012 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:59:50.808074Z` distance=0.012 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T01:04:02.744778Z` distance=0.012 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T01:08:15.509687Z` distance=0.012 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

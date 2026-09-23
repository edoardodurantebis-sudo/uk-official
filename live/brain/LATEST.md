# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T05:38:40.844898Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `margin` value=3.858e+04 d1=0.0 d12=57.0 z=45.4943336375
- **ROBUST_OUTLIER** `margin` value=3.858e+04 d1=0.0 d12=57.0 z=45.4943336375
- **CHANGE_POINT** `biomass_gen` value=2559 d1=-8.0 d12=-322.0 z=-8.837192234693878
- **PERSISTENT_DOWN** `biomass_gen` value=2559 d1=-8.0 d12=-322.0 z=-8.837192234693878
- **ROBUST_OUTLIER** `biomass_gen` value=2559 d1=-8.0 d12=-322.0 z=-8.837192234693878
- **PERSISTENT_UP** `nuclear_gen` value=3802 d1=5.0 d12=11.0 z=7.159968115384615
- **ACCELERATION** `nuclear_gen` value=3802 d1=5.0 d12=11.0 z=7.159968115384615
- **ROBUST_OUTLIER** `nuclear_gen` value=3802 d1=5.0 d12=11.0 z=7.159968115384615
- **CHANGE_POINT** `imbalance` value=-7937 d1=0.0 d12=100.0 z=2.2857708194444446
- **CHANGE_POINT** `ind_generation` value=1.324e+04 d1=0.0 d12=100.0 z=2.2857708194444446
- **PERSISTENT_DOWN** `wind_gen` value=8286 d1=-43.0 d12=-824.0 z=1.5211572298569278
- **REVERSAL** `interconnector_net` value=-4115 d1=-36.0 d12=1514.0 z=-1.0134685318123393
- **ACCELERATION** `interconnector_net` value=-4115 d1=-36.0 d12=1514.0 z=-1.0134685318123393
- **ACCELERATION** `ps_gen` value=144 d1=0.0 d12=0.0 z=-0.337244875
- **PERSISTENT_UP** `ccgt_gen` value=9400 d1=144.0 d12=1811.0 z=-0.11319453502080444

## Nearest historical live analogues

- `2026-09-23T03:32:33.216215Z` distance=0.026 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T03:36:43.352003Z` distance=0.026 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T03:40:54.258660Z` distance=0.026 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T03:45:06.650607Z` distance=0.026 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T03:49:19.033601Z` distance=0.026 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

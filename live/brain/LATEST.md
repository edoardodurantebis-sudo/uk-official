# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T19:36:02.892054Z`  
Memory snapshots: **314**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high, wind falling.

## Active patterns

- **PERSISTENT_DOWN** `biomass_gen` value=3266 d1=-6.0 d12=-33.0 z=29.648223358695653
- **ROBUST_OUTLIER** `biomass_gen` value=3266 d1=-6.0 d12=-33.0 z=29.648223358695653
- **PERSISTENT_UP** `residual_proxy` value=942 d1=0.0 d12=116.0 z=6.7052216323529406
- **ACCELERATION** `residual_proxy` value=942 d1=0.0 d12=116.0 z=6.7052216323529406
- **ROBUST_OUTLIER** `residual_proxy` value=942 d1=0.0 d12=116.0 z=6.7052216323529406
- **ROBUST_OUTLIER** `ind_demand` value=-1.191e+04 d1=0.0 d12=-2.0 z=4.0469384999999996
- **CHANGE_POINT** `margin` value=3.564e+04 d1=0.0 d12=-11.0 z=1.982413352173913
- **CHANGE_POINT** `ps_gen` value=423 d1=-1.0 d12=-380.0 z=0.5035631549689441
- **CHANGE_POINT** `interconnector_net` value=677 d1=-3.0 d12=2251.0 z=-0.3375780111952585
- **PERSISTENT_UP** `wind_gen` value=1.051e+04 d1=73.0 d12=594.0 z=1.0450885137362638
- **REVERSAL** `thermal_base` value=1.383e+04 d1=1.0 d12=-334.0 z=0.6348207053740327
- **REVERSAL** `ccgt_gen` value=1.051e+04 d1=2.0 d12=-342.0 z=0.6333835077253219
- **PERSISTENT_DOWN** `ps_gen` value=423 d1=-1.0 d12=-380.0 z=0.5035631549689441
- **REVERSAL** `interconnector_net` value=677 d1=-3.0 d12=2251.0 z=-0.3375780111952585
- **ACCELERATION** `interconnector_net` value=677 d1=-3.0 d12=2251.0 z=-0.3375780111952585

## Nearest historical live analogues

- `2026-09-15T18:24:34.306197Z` distance=0.084 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:28:44.303435Z` distance=0.084 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:32:54.292117Z` distance=0.084 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:37:05.511843Z` distance=0.084 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:41:17.608634Z` distance=0.084 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

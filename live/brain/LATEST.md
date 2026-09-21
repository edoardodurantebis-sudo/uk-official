# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T16:30:33.763317Z`  
Memory snapshots: **2226**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.633e+04 d1=0.0 d12=2296.0 z=6.386662280082987
- **CHANGE_POINT** `ccgt_gen` value=1.283e+04 d1=0.0 d12=2286.0 z=6.3672055556244835
- **PERSISTENT_UP** `thermal_base` value=1.633e+04 d1=0.0 d12=2296.0 z=6.386662280082987
- **ROBUST_OUTLIER** `thermal_base` value=1.633e+04 d1=0.0 d12=2296.0 z=6.386662280082987
- **PERSISTENT_UP** `ccgt_gen` value=1.283e+04 d1=0.0 d12=2286.0 z=6.3672055556244835
- **ROBUST_OUTLIER** `ccgt_gen` value=1.283e+04 d1=0.0 d12=2286.0 z=6.3672055556244835
- **CHANGE_POINT** `interconnector_net` value=1.02e+04 d1=0.0 d12=-768.0 z=-3.433466160146699
- **ROBUST_OUTLIER** `interconnector_net` value=1.02e+04 d1=0.0 d12=-768.0 z=-3.433466160146699
- **CHANGE_POINT** `wind_gen` value=3146 d1=0.0 d12=-244.0 z=-1.29502032
- **CHANGE_POINT** `ind_generation` value=1.839e+04 d1=0.0 d12=36.0 z=0.7402936280487804
- **CHANGE_POINT** `imbalance` value=-3071 d1=0.0 d12=36.0 z=0.7169772933070866
- **PERSISTENT_DOWN** `wind_gen` value=3146 d1=0.0 d12=-244.0 z=-1.29502032
- **PERSISTENT_UP** `ind_generation` value=1.839e+04 d1=0.0 d12=36.0 z=0.7402936280487804
- **PERSISTENT_UP** `imbalance` value=-3071 d1=0.0 d12=36.0 z=0.7169772933070866
- **PERSISTENT_UP** `biomass_gen` value=2963 d1=0.0 d12=12.0 z=-0.3747165277777778

## Nearest historical live analogues

- `2026-09-21T15:26:27.469405Z` distance=0.010 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -51.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T15:30:37.860005Z` distance=0.010 → {'next30m_imbalance_delta': 28.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -51.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T15:34:50.537935Z` distance=0.010 → {'next30m_imbalance_delta': 28.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -51.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T13:57:37.194603Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:01:53.716346Z` distance=0.021 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

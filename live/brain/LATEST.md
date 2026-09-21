# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T16:21:51.126384Z`  
Memory snapshots: **2224**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.613e+04 d1=72.0 d12=2481.0 z=6.740001022686026
- **CHANGE_POINT** `ccgt_gen` value=1.263e+04 d1=78.0 d12=2472.0 z=6.575976615707965
- **PERSISTENT_UP** `thermal_base` value=1.613e+04 d1=72.0 d12=2481.0 z=6.740001022686026
- **ROBUST_OUTLIER** `thermal_base` value=1.613e+04 d1=72.0 d12=2481.0 z=6.740001022686026
- **PERSISTENT_UP** `ccgt_gen` value=1.263e+04 d1=78.0 d12=2472.0 z=6.575976615707965
- **ROBUST_OUTLIER** `ccgt_gen` value=1.263e+04 d1=78.0 d12=2472.0 z=6.575976615707965
- **CHANGE_POINT** `interconnector_net` value=1.02e+04 d1=1.0 d12=-960.0 z=-3.433466160146699
- **REVERSAL** `interconnector_net` value=1.02e+04 d1=1.0 d12=-960.0 z=-3.433466160146699
- **ROBUST_OUTLIER** `interconnector_net` value=1.02e+04 d1=1.0 d12=-960.0 z=-3.433466160146699
- **CHANGE_POINT** `wind_gen` value=3209 d1=20.0 d12=-129.0 z=-1.042864921153846
- **CHANGE_POINT** `imbalance` value=-3079 d1=0.0 d12=28.0 z=0.67448975
- **CHANGE_POINT** `ind_generation` value=1.838e+04 d1=0.0 d12=28.0 z=0.5292646842105263
- **CHANGE_POINT** `margin` value=3.628e+04 d1=70.0 d12=19.0 z=0.05188382692307693
- **CHANGE_POINT** `nuclear_gen` value=3503 d1=-6.0 d12=9.0 z=0.0
- **REVERSAL** `wind_gen` value=3209 d1=20.0 d12=-129.0 z=-1.042864921153846

## Nearest historical live analogues

- `2026-09-21T15:26:27.469405Z` distance=0.010 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -51.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T13:57:37.194603Z` distance=0.027 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:01:53.716346Z` distance=0.027 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:06:06.412176Z` distance=0.027 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:10:22.067665Z` distance=0.027 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

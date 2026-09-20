# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T19:47:11.439179Z`  
Memory snapshots: **1932**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.527e+04 d1=0.0 d12=-197.0 z=-11.6012237
- **ROBUST_OUTLIER** `ind_generation` value=1.527e+04 d1=0.0 d12=-197.0 z=-11.6012237
- **CHANGE_POINT** `imbalance` value=-5338 d1=0.0 d12=-197.0 z=-7.997521321428572
- **ROBUST_OUTLIER** `imbalance` value=-5338 d1=0.0 d12=-197.0 z=-7.997521321428572
- **CHANGE_POINT** `ccgt_gen` value=8260 d1=-17.0 d12=-481.0 z=1.3162389261192153
- **CHANGE_POINT** `thermal_base` value=1.159e+04 d1=-18.0 d12=-482.0 z=1.3138904378612717
- **CHANGE_POINT** `margin` value=3.558e+04 d1=0.0 d12=182.0 z=-1.0321737083333333
- **CHANGE_POINT** `ps_gen` value=227 d1=0.0 d12=4.0 z=0.67448975
- **CHANGE_POINT** `interconnector_net` value=1.092e+04 d1=1.0 d12=1042.0 z=0.3644378115115375
- **PERSISTENT_DOWN** `ccgt_gen` value=8260 d1=-17.0 d12=-481.0 z=1.3162389261192153
- **PERSISTENT_DOWN** `thermal_base` value=1.159e+04 d1=-18.0 d12=-482.0 z=1.3138904378612717
- **PERSISTENT_UP** `wind_gen` value=5767 d1=71.0 d12=211.0 z=-1.2112203994501178
- **PERSISTENT_DOWN** `nuclear_gen` value=3332 d1=-1.0 d12=-1.0 z=-1.0117346249999999
- **ACCELERATION** `nuclear_gen` value=3332 d1=-1.0 d12=-1.0 z=-1.0117346249999999
- **REVERSAL** `biomass_gen` value=2360 d1=-4.0 d12=16.0 z=0.6796059807206067

## Nearest historical live analogues

- `2026-09-20T17:52:35.892709Z` distance=0.080 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T17:56:46.494195Z` distance=0.080 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:00:58.540331Z` distance=0.080 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:05:11.055248Z` distance=0.080 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:09:24.806977Z` distance=0.080 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

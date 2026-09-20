# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T19:42:58.995529Z`  
Memory snapshots: **1931**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.527e+04 d1=0.0 d12=-180.0 z=-11.6012237
- **ROBUST_OUTLIER** `ind_generation` value=1.527e+04 d1=0.0 d12=-180.0 z=-11.6012237
- **CHANGE_POINT** `imbalance` value=-5338 d1=0.0 d12=-180.0 z=-7.997521321428572
- **ROBUST_OUTLIER** `imbalance` value=-5338 d1=0.0 d12=-180.0 z=-7.997521321428572
- **CHANGE_POINT** `ccgt_gen` value=8277 d1=-17.0 d12=-504.0 z=1.5516288867713006
- **CHANGE_POINT** `thermal_base` value=1.161e+04 d1=-20.0 d12=-509.0 z=1.549003203514422
- **CHANGE_POINT** `margin` value=3.558e+04 d1=0.0 d12=182.0 z=-1.089975436
- **CHANGE_POINT** `ps_gen` value=227 d1=0.0 d12=4.0 z=0.67448975
- **CHANGE_POINT** `interconnector_net` value=1.092e+04 d1=-1.0 d12=1041.0 z=0.36399369090202177
- **PERSISTENT_DOWN** `ccgt_gen` value=8277 d1=-17.0 d12=-504.0 z=1.5516288867713006
- **PERSISTENT_DOWN** `thermal_base` value=1.161e+04 d1=-20.0 d12=-509.0 z=1.549003203514422
- **PERSISTENT_UP** `residual_proxy` value=1.838e+04 d1=0.0 d12=389.0 z=1.5254448415697675
- **REVERSAL** `wind_gen` value=5696 d1=7.0 d12=-7.0 z=-1.3742998021166133
- **ACCELERATION** `wind_gen` value=5696 d1=7.0 d12=-7.0 z=-1.3742998021166133
- **PERSISTENT_UP** `biomass_gen` value=2364 d1=1.0 d12=23.0 z=0.6883254371794871

## Nearest historical live analogues

- `2026-09-20T17:52:35.892709Z` distance=0.080 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T17:56:46.494195Z` distance=0.080 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:00:58.540331Z` distance=0.080 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:05:11.055248Z` distance=0.080 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:09:24.806977Z` distance=0.080 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

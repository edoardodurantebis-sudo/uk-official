# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T19:08:12.709568Z`  
Memory snapshots: **1923**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.54e+04 d1=0.0 d12=-59.0 z=-2.2920713628318583
- **PERSISTENT_DOWN** `thermal_base` value=1.206e+04 d1=-5.0 d12=-305.0 z=3.8892094500800853
- **ROBUST_OUTLIER** `thermal_base` value=1.206e+04 d1=-5.0 d12=-305.0 z=3.8892094500800853
- **PERSISTENT_DOWN** `ccgt_gen` value=8721 d1=-8.0 d12=-306.0 z=3.8642567302177375
- **ROBUST_OUTLIER** `ccgt_gen` value=8721 d1=-8.0 d12=-306.0 z=3.8642567302177375
- **CHANGE_POINT** `wind_gen` value=5413 d1=-15.0 d12=-1218.0 z=-1.5793648070494186
- **CHANGE_POINT** `ind_generation` value=1.547e+04 d1=0.0 d12=24.0 z=1.493513017857143
- **CHANGE_POINT** `biomass_gen` value=2359 d1=13.0 d12=76.0 z=1.158553549158378
- **CHANGE_POINT** `imbalance` value=-5141 d1=0.0 d12=24.0 z=1.1522533229166667
- **PERSISTENT_DOWN** `wind_gen` value=5413 d1=-15.0 d12=-1218.0 z=-1.5793648070494186
- **PERSISTENT_UP** `biomass_gen` value=2359 d1=13.0 d12=76.0 z=1.158553549158378
- **PERSISTENT_UP** `nuclear_gen` value=3337 d1=3.0 d12=1.0 z=0.67448975
- **ACCELERATION** `nuclear_gen` value=3337 d1=3.0 d12=1.0 z=0.67448975
- **REVERSAL** `ps_gen` value=224 d1=1.0 d12=-274.0 z=0.4570012183673469
- **PERSISTENT_UP** `interconnector_net` value=1.036e+04 d1=443.0 d12=426.0 z=0.44000344307131284

## Nearest historical live analogues

- `2026-09-20T17:52:35.892709Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T17:56:46.494195Z` distance=0.026 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:00:58.540331Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:05:11.055248Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:09:24.806977Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

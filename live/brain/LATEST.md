# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T22:40:35.446598Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.402e+04 d1=-96.0 d12=-2854.0 z=-9.319510043541365
- **CHANGE_POINT** `ccgt_gen` value=1.028e+04 d1=-98.0 d12=-2853.0 z=-9.265973020893371
- **PERSISTENT_DOWN** `thermal_base` value=1.402e+04 d1=-96.0 d12=-2854.0 z=-9.319510043541365
- **ROBUST_OUTLIER** `thermal_base` value=1.402e+04 d1=-96.0 d12=-2854.0 z=-9.319510043541365
- **PERSISTENT_DOWN** `ccgt_gen` value=1.028e+04 d1=-98.0 d12=-2853.0 z=-9.265973020893371
- **ROBUST_OUTLIER** `ccgt_gen` value=1.028e+04 d1=-98.0 d12=-2853.0 z=-9.265973020893371
- **CHANGE_POINT** `wind_gen` value=2727 d1=33.0 d12=262.0 z=1.7468230634765625
- **PERSISTENT_UP** `ps_gen` value=146 d1=1.0 d12=3.0 z=-2.4441679415254236
- **REVERSAL** `interconnector_net` value=5361 d1=-26.0 d12=601.0 z=-1.8220591163194444
- **REVERSAL** `nuclear_gen` value=3739 d1=2.0 d12=-1.0 z=1.7986393333333333
- **ACCELERATION** `nuclear_gen` value=3739 d1=2.0 d12=-1.0 z=1.7986393333333333
- **PERSISTENT_UP** `wind_gen` value=2727 d1=33.0 d12=262.0 z=1.7468230634765625
- **PERSISTENT_UP** `biomass_gen` value=2915 d1=0.0 d12=3.0 z=0.498535902173913
- **ACCELERATION** `biomass_gen` value=2915 d1=0.0 d12=3.0 z=0.498535902173913

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.011 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:24:47.718083Z` distance=0.011 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:28:58.806773Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:33:11.512074Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:37:22.236065Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

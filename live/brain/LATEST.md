# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T19:12:26.889125Z`  
Memory snapshots: **1924**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.54e+04 d1=0.0 d12=-29.0 z=-2.2920713628318583
- **CHANGE_POINT** `wind_gen` value=5416 d1=3.0 d12=-1024.0 z=-1.5956343289181179
- **CHANGE_POINT** `ind_generation` value=1.547e+04 d1=0.0 d12=24.0 z=1.4527471538461538
- **CHANGE_POINT** `imbalance` value=-5141 d1=0.0 d12=24.0 z=1.2779805789473684
- **CHANGE_POINT** `biomass_gen` value=2364 d1=5.0 d12=64.0 z=1.023413069434629
- **PERSISTENT_DOWN** `ccgt_gen` value=8694 d1=-27.0 d12=-394.0 z=2.995339726704055
- **PERSISTENT_DOWN** `thermal_base` value=1.204e+04 d1=-23.0 d12=-393.0 z=2.9912154130434785
- **PERSISTENT_UP** `nuclear_gen` value=3341 d1=4.0 d12=1.0 z=2.0234692499999998
- **ACCELERATION** `nuclear_gen` value=3341 d1=4.0 d12=1.0 z=2.0234692499999998
- **REVERSAL** `wind_gen` value=5416 d1=3.0 d12=-1024.0 z=-1.5956343289181179
- **PERSISTENT_UP** `biomass_gen` value=2364 d1=5.0 d12=64.0 z=1.023413069434629
- **PERSISTENT_UP** `interconnector_net` value=1.04e+04 d1=44.0 d12=470.0 z=0.4942104574642432
- **ACCELERATION** `interconnector_net` value=1.04e+04 d1=44.0 d12=470.0 z=0.4942104574642432
- **PERSISTENT_UP** `ps_gen` value=226 d1=2.0 d12=1.0 z=0.45563433461538466
- **ACCELERATION** `ps_gen` value=226 d1=2.0 d12=1.0 z=0.45563433461538466

## Nearest historical live analogues

- `2026-09-20T17:52:35.892709Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T17:56:46.494195Z` distance=0.026 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:00:58.540331Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:05:11.055248Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:09:24.806977Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

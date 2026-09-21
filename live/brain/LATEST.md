# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T20:07:37.693850Z`  
Memory snapshots: **2277**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-2779 d1=0.0 d12=305.0 z=3.5468857543103445
- **CHANGE_POINT** `ind_generation` value=1.868e+04 d1=0.0 d12=305.0 z=3.5468857543103445
- **CHANGE_POINT** `biomass_gen` value=3018 d1=2.0 d12=3.0 z=3.159451986842105
- **ROBUST_OUTLIER** `margin` value=3.604e+04 d1=0.0 d12=-93.0 z=-4.482093177419355
- **ROBUST_OUTLIER** `ind_demand` value=-1.226e+04 d1=0.0 d12=18.0 z=4.0469385
- **ROBUST_OUTLIER** `imbalance` value=-2779 d1=0.0 d12=305.0 z=3.5468857543103445
- **ROBUST_OUTLIER** `ind_generation` value=1.868e+04 d1=0.0 d12=305.0 z=3.5468857543103445
- **PERSISTENT_UP** `biomass_gen` value=3018 d1=2.0 d12=3.0 z=3.159451986842105
- **ROBUST_OUTLIER** `biomass_gen` value=3018 d1=2.0 d12=3.0 z=3.159451986842105
- **CHANGE_POINT** `interconnector_net` value=8951 d1=-490.0 d12=561.0 z=-0.3185887755319149
- **CHANGE_POINT** `thermal_base` value=1.666e+04 d1=68.0 d12=26.0 z=0.20977739637857576
- **CHANGE_POINT** `ccgt_gen` value=1.315e+04 d1=67.0 d12=28.0 z=0.20740968099273607
- **REVERSAL** `nuclear_gen` value=3514 d1=1.0 d12=-2.0 z=1.1803570625
- **ACCELERATION** `nuclear_gen` value=3514 d1=1.0 d12=-2.0 z=1.1803570625
- **PERSISTENT_UP** `ps_gen` value=704 d1=178.0 d12=177.0 z=1.1604260802063788

## Nearest historical live analogues

- `2026-09-21T18:51:48.360935Z` distance=0.054 → {'next30m_imbalance_delta': 40.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T18:56:00.829155Z` distance=0.054 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:00:12.997275Z` distance=0.054 → {'next30m_imbalance_delta': 290.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:04:23.644038Z` distance=0.054 → {'next30m_imbalance_delta': 290.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:08:34.146689Z` distance=0.054 → {'next30m_imbalance_delta': 290.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': -1.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T20:20:20.064570Z`  
Memory snapshots: **2280**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `nuclear_gen` value=3532 d1=0.0 d12=22.0 z=4.2155609375
- **CHANGE_POINT** `imbalance` value=-2779 d1=0.0 d12=15.0 z=3.6762729617117116
- **CHANGE_POINT** `ind_generation` value=1.868e+04 d1=0.0 d12=15.0 z=3.6762729617117116
- **PERSISTENT_UP** `nuclear_gen` value=3532 d1=0.0 d12=22.0 z=4.2155609375
- **ACCELERATION** `nuclear_gen` value=3532 d1=0.0 d12=22.0 z=4.2155609375
- **ROBUST_OUTLIER** `nuclear_gen` value=3532 d1=0.0 d12=22.0 z=4.2155609375
- **ROBUST_OUTLIER** `ind_demand` value=-1.226e+04 d1=0.0 d12=0.0 z=4.0469385
- **ROBUST_OUTLIER** `imbalance` value=-2779 d1=0.0 d12=15.0 z=3.6762729617117116
- **ROBUST_OUTLIER** `ind_generation` value=1.868e+04 d1=0.0 d12=15.0 z=3.6762729617117116
- **PERSISTENT_DOWN** `biomass_gen` value=3010 d1=0.0 d12=-11.0 z=2.3125362857142857
- **ACCELERATION** `biomass_gen` value=3010 d1=0.0 d12=-11.0 z=2.3125362857142857
- **PERSISTENT_UP** `margin` value=3.609e+04 d1=52.0 d12=4.0 z=-1.5209082598039216
- **ACCELERATION** `margin` value=3.609e+04 d1=52.0 d12=4.0 z=-1.5209082598039216
- **PERSISTENT_DOWN** `ps_gen` value=397 d1=0.0 d12=-129.0 z=0.1846285408388521
- **ACCELERATION** `ps_gen` value=397 d1=0.0 d12=-129.0 z=0.1846285408388521

## Nearest historical live analogues

- `2026-09-21T19:25:28.829877Z` distance=0.002 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1.0}
- `2026-09-21T19:21:16.242485Z` distance=0.022 → {'next30m_imbalance_delta': 290.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1.0}
- `2026-09-21T18:51:48.360935Z` distance=0.031 → {'next30m_imbalance_delta': 40.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T18:56:00.829155Z` distance=0.031 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:00:12.997275Z` distance=0.031 → {'next30m_imbalance_delta': 290.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T03:25:39.544534Z`  
Memory snapshots: **1700**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=-61.0 z=28.579094264285715
- **PERSISTENT_DOWN** `margin` value=3.754e+04 d1=0.0 d12=-61.0 z=28.579094264285715
- **ACCELERATION** `margin` value=3.754e+04 d1=0.0 d12=-61.0 z=28.579094264285715
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=-61.0 z=28.579094264285715
- **PERSISTENT_DOWN** `ind_demand` value=-1.229e+04 d1=0.0 d12=-90.0 z=-17.896461366666664
- **ROBUST_OUTLIER** `ind_demand` value=-1.229e+04 d1=0.0 d12=-90.0 z=-17.896461366666664
- **REVERSAL** `biomass_gen` value=1224 d1=1.0 d12=-6.0 z=3.6399188232758624
- **ROBUST_OUTLIER** `biomass_gen` value=1224 d1=1.0 d12=-6.0 z=3.6399188232758624
- **CHANGE_POINT** `ps_gen` value=-702 d1=-5.0 d12=1.0 z=-0.8894587054093567
- **CHANGE_POINT** `imbalance` value=-3815 d1=0.0 d12=-60.0 z=-0.6376994
- **CHANGE_POINT** `ind_generation` value=1.614e+04 d1=0.0 d12=-60.0 z=-0.6376994
- **CHANGE_POINT** `ccgt_gen` value=3613 d1=16.0 d12=-623.0 z=-0.5923641323644934
- **CHANGE_POINT** `thermal_base` value=6947 d1=17.0 d12=-625.0 z=-0.5907708817330211
- **REVERSAL** `interconnector_net` value=-1.152e+04 d1=2.0 d12=-472.0 z=-1.4629279257607555
- **REVERSAL** `ps_gen` value=-702 d1=-5.0 d12=1.0 z=-0.8894587054093567

## Nearest historical live analogues

- `2026-09-20T02:20:49.967105Z` distance=0.105 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:25:01.524399Z` distance=0.105 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:29:13.820300Z` distance=0.105 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:48:55.634175Z` distance=0.369 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.369 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

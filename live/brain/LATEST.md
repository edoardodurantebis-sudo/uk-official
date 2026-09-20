# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T03:34:04.391029Z`  
Memory snapshots: **1702**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=-61.0 z=28.579094264285715
- **ROBUST_OUTLIER** `ind_demand` value=-1.229e+04 d1=0.0 d12=-90.0 z=-17.896461366666664
- **CHANGE_POINT** `ps_gen` value=-699 d1=3.0 d12=-4.0 z=-0.8835421286549707
- **CHANGE_POINT** `imbalance` value=-3815 d1=0.0 d12=-60.0 z=-0.6376994
- **CHANGE_POINT** `ind_generation` value=1.614e+04 d1=0.0 d12=-60.0 z=-0.6376994
- **REVERSAL** `biomass_gen` value=1220 d1=-4.0 d12=39.0 z=2.620133259615385
- **CHANGE_POINT** `thermal_base` value=7018 d1=71.0 d12=-358.0 z=-0.5469323664139162
- **CHANGE_POINT** `ccgt_gen` value=3686 d1=73.0 d12=-358.0 z=-0.5404371765890779
- **PERSISTENT_DOWN** `interconnector_net` value=-1.188e+04 d1=-359.0 d12=-832.0 z=-1.7786924459231095
- **ACCELERATION** `interconnector_net` value=-1.188e+04 d1=-359.0 d12=-832.0 z=-1.7786924459231095
- **REVERSAL** `ps_gen` value=-699 d1=3.0 d12=-4.0 z=-0.8835421286549707
- **ACCELERATION** `ps_gen` value=-699 d1=3.0 d12=-4.0 z=-0.8835421286549707
- **REVERSAL** `thermal_base` value=7018 d1=71.0 d12=-358.0 z=-0.5469323664139162
- **REVERSAL** `ccgt_gen` value=3686 d1=73.0 d12=-358.0 z=-0.5404371765890779
- **PERSISTENT_DOWN** `nuclear_gen` value=3332 d1=-2.0 d12=0.0 z=-0.4496598333333333

## Nearest historical live analogues

- `2026-09-20T02:20:49.967105Z` distance=1.035 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:25:01.524399Z` distance=1.035 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:29:13.820300Z` distance=1.035 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:33:25.726465Z` distance=1.035 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:37:39.122581Z` distance=1.035 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

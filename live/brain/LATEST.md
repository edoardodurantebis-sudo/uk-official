# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T04:37:31.798282Z`  
Memory snapshots: **2397**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.779e+04 d1=0.0 d12=0.0 z=21.259916920000002
- **ROBUST_OUTLIER** `margin` value=3.779e+04 d1=0.0 d12=0.0 z=21.259916920000002
- **PERSISTENT_DOWN** `interconnector_net` value=-4620 d1=-32.0 d12=-3169.0 z=-7.807877728292331
- **ACCELERATION** `interconnector_net` value=-4620 d1=-32.0 d12=-3169.0 z=-7.807877728292331
- **ROBUST_OUTLIER** `interconnector_net` value=-4620 d1=-32.0 d12=-3169.0 z=-7.807877728292331
- **CHANGE_POINT** `ccgt_gen` value=1.289e+04 d1=194.0 d12=1570.0 z=4.472861310258964
- **CHANGE_POINT** `thermal_base` value=1.653e+04 d1=192.0 d12=1557.0 z=4.346128505836576
- **CHANGE_POINT** `imbalance` value=-3324 d1=0.0 d12=-680.0 z=-3.5011681679389315
- **CHANGE_POINT** `ind_generation` value=1.814e+04 d1=0.0 d12=-680.0 z=-3.5011681679389315
- **PERSISTENT_UP** `ccgt_gen` value=1.289e+04 d1=194.0 d12=1570.0 z=4.472861310258964
- **ROBUST_OUTLIER** `ccgt_gen` value=1.289e+04 d1=194.0 d12=1570.0 z=4.472861310258964
- **PERSISTENT_UP** `thermal_base` value=1.653e+04 d1=192.0 d12=1557.0 z=4.346128505836576
- **ROBUST_OUTLIER** `thermal_base` value=1.653e+04 d1=192.0 d12=1557.0 z=4.346128505836576
- **CHANGE_POINT** `biomass_gen` value=3030 d1=-1.0 d12=-17.0 z=-1.6187753999999999
- **ROBUST_OUTLIER** `imbalance` value=-3324 d1=0.0 d12=-680.0 z=-3.5011681679389315

## Nearest historical live analogues

- `2026-09-22T03:33:35.816390Z` distance=0.023 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:37:48.990972Z` distance=0.023 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:42:37.215255Z` distance=0.023 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:20:28.289850Z` distance=0.199 → {'next30m_imbalance_delta': 15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -2141.0}
- `2026-09-22T03:24:38.283330Z` distance=0.199 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': -2141.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T05:03:14.010868Z`  
Memory snapshots: **2403**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.779e+04 d1=0.0 d12=-5.0 z=16.4617654609375
- **ROBUST_OUTLIER** `margin` value=3.779e+04 d1=0.0 d12=-5.0 z=16.4617654609375
- **CHANGE_POINT** `ccgt_gen` value=1.345e+04 d1=74.0 d12=1380.0 z=5.977698999501992
- **CHANGE_POINT** `thermal_base` value=1.71e+04 d1=74.0 d12=1383.0 z=5.8289561663424125
- **REVERSAL** `interconnector_net` value=-4302 d1=248.0 d12=-1129.0 z=-6.208305283817171
- **ROBUST_OUTLIER** `interconnector_net` value=-4302 d1=248.0 d12=-1129.0 z=-6.208305283817171
- **PERSISTENT_UP** `ccgt_gen` value=1.345e+04 d1=74.0 d12=1380.0 z=5.977698999501992
- **ROBUST_OUTLIER** `ccgt_gen` value=1.345e+04 d1=74.0 d12=1380.0 z=5.977698999501992
- **PERSISTENT_UP** `thermal_base` value=1.71e+04 d1=74.0 d12=1383.0 z=5.8289561663424125
- **ROBUST_OUTLIER** `thermal_base` value=1.71e+04 d1=74.0 d12=1383.0 z=5.8289561663424125
- **CHANGE_POINT** `imbalance` value=-3312 d1=0.0 d12=-76.0 z=-2.8406395240384614
- **CHANGE_POINT** `ind_generation` value=1.815e+04 d1=0.0 d12=-76.0 z=-2.8406395240384614
- **CHANGE_POINT** `biomass_gen` value=3029 d1=1.0 d12=-17.0 z=-1.7536733500000001
- **PERSISTENT_DOWN** `ind_demand` value=-1.252e+04 d1=0.0 d12=-18.0 z=-3.21057121
- **ROBUST_OUTLIER** `ind_demand` value=-1.252e+04 d1=0.0 d12=-18.0 z=-3.21057121

## Nearest historical live analogues

- `2026-09-22T03:55:16.196094Z` distance=0.021 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:59:30.332417Z` distance=0.021 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T04:03:43.712214Z` distance=0.021 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T04:08:00.116133Z` distance=0.021 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:33:35.816390Z` distance=0.027 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

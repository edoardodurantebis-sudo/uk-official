# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T02:16:31.634997Z`  
Memory snapshots: **2364**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `wind_gen` value=3962 d1=116.0 d12=339.0 z=3.093167837890625
- **CHANGE_POINT** `biomass_gen` value=3044 d1=-2.0 d12=-5.0 z=1.2526238214285714
- **PERSISTENT_UP** `wind_gen` value=3962 d1=116.0 d12=339.0 z=3.093167837890625
- **ROBUST_OUTLIER** `wind_gen` value=3962 d1=116.0 d12=339.0 z=3.093167837890625
- **CHANGE_POINT** `imbalance` value=-2707 d1=0.0 d12=-8.0 z=-0.6355768798076924
- **CHANGE_POINT** `ind_generation` value=1.875e+04 d1=0.0 d12=-8.0 z=-0.6355768798076924
- **CHANGE_POINT** `ps_gen` value=-164 d1=10.0 d12=117.0 z=-0.38221085833333335
- **CHANGE_POINT** `margin` value=3.617e+04 d1=0.0 d12=0.0 z=0.005865128260869565
- **ACCELERATION** `biomass_gen` value=3044 d1=-2.0 d12=-5.0 z=1.2526238214285714
- **PERSISTENT_UP** `thermal_base` value=1.454e+04 d1=81.0 d12=116.0 z=-0.6526591665736607
- **PERSISTENT_UP** `ccgt_gen` value=1.089e+04 d1=79.0 d12=119.0 z=-0.6505819500537057
- **REVERSAL** `nuclear_gen` value=3652 d1=2.0 d12=-3.0 z=0.5246031388888889
- **ACCELERATION** `nuclear_gen` value=3652 d1=2.0 d12=-3.0 z=0.5246031388888889
- **PERSISTENT_DOWN** `interconnector_net` value=3773 d1=0.0 d12=-735.0 z=-0.43910537311780334
- **ACCELERATION** `interconnector_net` value=3773 d1=0.0 d12=-735.0 z=-0.43910537311780334

## Nearest historical live analogues

- `2026-09-22T01:21:15.207271Z` distance=0.031 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T00:51:37.339006Z` distance=0.031 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T00:55:53.060568Z` distance=0.031 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T01:00:07.633002Z` distance=0.031 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T01:04:25.209064Z` distance=0.031 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

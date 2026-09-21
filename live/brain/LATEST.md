# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T11:57:55.882170Z`  
Memory snapshots: **2162**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **PERSISTENT_UP** `ps_gen` value=108 d1=1.0 d12=8.0 z=26.30510025
- **ACCELERATION** `ps_gen` value=108 d1=1.0 d12=8.0 z=26.30510025
- **ROBUST_OUTLIER** `ps_gen` value=108 d1=1.0 d12=8.0 z=26.30510025
- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=0.0 d12=2.0 z=14.786890673076924
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=2.0 z=14.786890673076924
- **PERSISTENT_DOWN** `ccgt_gen` value=6490 d1=-107.0 d12=-193.0 z=-4.0364145464539005
- **ROBUST_OUTLIER** `ccgt_gen` value=6490 d1=-107.0 d12=-193.0 z=-4.0364145464539005
- **PERSISTENT_DOWN** `thermal_base` value=9996 d1=-113.0 d12=-206.0 z=-3.7564449333781966
- **ROBUST_OUTLIER** `thermal_base` value=9996 d1=-113.0 d12=-206.0 z=-3.7564449333781966
- **CHANGE_POINT** `nuclear_gen` value=3506 d1=-6.0 d12=-13.0 z=1.3489795
- **CHANGE_POINT** `wind_gen` value=3630 d1=126.0 d12=306.0 z=0.2326301382653061
- **PERSISTENT_DOWN** `nuclear_gen` value=3506 d1=-6.0 d12=-13.0 z=1.3489795
- **ACCELERATION** `nuclear_gen` value=3506 d1=-6.0 d12=-13.0 z=1.3489795
- **REVERSAL** `interconnector_net` value=1.13e+04 d1=-24.0 d12=35.0 z=1.0972153562421185
- **REVERSAL** `biomass_gen` value=3011 d1=2.0 d12=-5.0 z=-0.29977322222222225

## Nearest historical live analogues

- `2026-09-21T10:54:44.355248Z` distance=0.080 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:58:55.909932Z` distance=0.080 → {'next30m_imbalance_delta': 856.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T11:03:12.814990Z` distance=0.080 → {'next30m_imbalance_delta': 856.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:48:55.634175Z` distance=0.474 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.474 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

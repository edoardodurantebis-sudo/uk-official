# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T04:54:50.378428Z`  
Memory snapshots: **2401**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.779e+04 d1=0.0 d12=-5.0 z=16.4617654609375
- **REVERSAL** `interconnector_net` value=-4602 d1=20.0 d12=-2594.0 z=-7.751496416243655
- **ROBUST_OUTLIER** `interconnector_net` value=-4602 d1=20.0 d12=-2594.0 z=-7.751496416243655
- **CHANGE_POINT** `ccgt_gen` value=1.325e+04 d1=55.0 d12=1949.0 z=5.451005808266932
- **CHANGE_POINT** `thermal_base` value=1.69e+04 d1=50.0 d12=1947.0 z=5.311934840466926
- **PERSISTENT_UP** `ccgt_gen` value=1.325e+04 d1=55.0 d12=1949.0 z=5.451005808266932
- **ROBUST_OUTLIER** `ccgt_gen` value=1.325e+04 d1=55.0 d12=1949.0 z=5.451005808266932
- **PERSISTENT_UP** `thermal_base` value=1.69e+04 d1=50.0 d12=1947.0 z=5.311934840466926
- **ROBUST_OUTLIER** `thermal_base` value=1.69e+04 d1=50.0 d12=1947.0 z=5.311934840466926
- **CHANGE_POINT** `imbalance` value=-3312 d1=12.0 d12=-76.0 z=-2.8406395240384614
- **CHANGE_POINT** `ind_generation` value=1.815e+04 d1=12.0 d12=-76.0 z=-2.8406395240384614
- **CHANGE_POINT** `biomass_gen` value=3030 d1=1.0 d12=-14.0 z=-1.6187753999999999
- **PERSISTENT_DOWN** `ind_demand` value=-1.252e+04 d1=-3.0 d12=-18.0 z=-3.21057121
- **ROBUST_OUTLIER** `ind_demand` value=-1.252e+04 d1=-3.0 d12=-18.0 z=-3.21057121
- **REVERSAL** `imbalance` value=-3312 d1=12.0 d12=-76.0 z=-2.8406395240384614

## Nearest historical live analogues

- `2026-09-22T03:55:16.196094Z` distance=0.021 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:59:30.332417Z` distance=0.021 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:33:35.816390Z` distance=0.027 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:37:48.990972Z` distance=0.027 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:42:37.215255Z` distance=0.027 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

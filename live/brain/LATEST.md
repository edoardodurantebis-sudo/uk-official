# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T02:26:51.602433Z`  
Memory snapshots: **2027**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.755e+04 d1=0.0 d12=1723.0 z=25.400996968085106
- **PERSISTENT_UP** `margin` value=3.755e+04 d1=0.0 d12=1723.0 z=25.400996968085106
- **ACCELERATION** `margin` value=3.755e+04 d1=0.0 d12=1723.0 z=25.400996968085106
- **ROBUST_OUTLIER** `margin` value=3.755e+04 d1=0.0 d12=1723.0 z=25.400996968085106
- **CHANGE_POINT** `ind_demand` value=-1.18e+04 d1=0.0 d12=27.0 z=1.4613944583333334
- **CHANGE_POINT** `thermal_base` value=8348 d1=6.0 d12=-280.0 z=-1.2206838968298108
- **CHANGE_POINT** `ccgt_gen` value=5006 d1=8.0 d12=-284.0 z=-1.2173536061190737
- **PERSISTENT_DOWN** `wind_gen` value=3940 d1=-35.0 d12=-215.0 z=-2.0908031243600687
- **REVERSAL** `nuclear_gen` value=3342 d1=-2.0 d12=4.0 z=2.0234692499999998
- **ACCELERATION** `nuclear_gen` value=3342 d1=-2.0 d12=4.0 z=2.0234692499999998
- **ACCELERATION** `imbalance` value=-4904 d1=0.0 d12=2.0 z=1.5224197214285713
- **ACCELERATION** `ind_generation` value=1.571e+04 d1=0.0 d12=2.0 z=1.5224197214285713
- **PERSISTENT_UP** `ind_demand` value=-1.18e+04 d1=0.0 d12=27.0 z=1.4613944583333334
- **ACCELERATION** `ind_demand` value=-1.18e+04 d1=0.0 d12=27.0 z=1.4613944583333334
- **PERSISTENT_UP** `interconnector_net` value=1.237e+04 d1=2.0 d12=121.0 z=1.259230694161575

## Nearest historical live analogues

- `2026-09-21T01:23:21.503053Z` distance=0.869 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:28:09.159328Z` distance=0.869 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:32:22.156789Z` distance=0.869 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T00:03:26.283660Z` distance=0.870 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T00:07:41.732348Z` distance=0.870 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T05:17:04.184189Z`  
Memory snapshots: **2067**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `nuclear_gen` value=3450 d1=16.0 d12=74.0 z=18.7170905625
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=7.0 z=19.531622675847455
- **PERSISTENT_UP** `nuclear_gen` value=3450 d1=16.0 d12=74.0 z=18.7170905625
- **ROBUST_OUTLIER** `nuclear_gen` value=3450 d1=16.0 d12=74.0 z=18.7170905625
- **CHANGE_POINT** `imbalance` value=-4036 d1=0.0 d12=-54.0 z=7.162832866564417
- **CHANGE_POINT** `ind_generation` value=1.657e+04 d1=0.0 d12=-54.0 z=7.162832866564417
- **ROBUST_OUTLIER** `imbalance` value=-4036 d1=0.0 d12=-54.0 z=7.162832866564417
- **ROBUST_OUTLIER** `ind_generation` value=1.657e+04 d1=0.0 d12=-54.0 z=7.162832866564417
- **PERSISTENT_UP** `thermal_base` value=1.173e+04 d1=308.0 d12=956.0 z=4.905220111473272
- **ROBUST_OUTLIER** `thermal_base` value=1.173e+04 d1=308.0 d12=956.0 z=4.905220111473272
- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=4.0 z=4.777635729166667
- **PERSISTENT_UP** `ccgt_gen` value=8282 d1=292.0 d12=882.0 z=4.755197170289855
- **ROBUST_OUTLIER** `ccgt_gen` value=8282 d1=292.0 d12=882.0 z=4.755197170289855
- **REVERSAL** `interconnector_net` value=6018 d1=68.0 d12=-1225.0 z=-2.474427523545091
- **CHANGE_POINT** `ps_gen` value=-266 d1=0.0 d12=-31.0 z=None

## Nearest historical live analogues

- `2026-09-21T04:21:09.590737Z` distance=0.006 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T03:51:43.129687Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T03:55:57.406713Z` distance=0.021 → {'next30m_imbalance_delta': 61.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T04:00:09.627125Z` distance=0.021 → {'next30m_imbalance_delta': 61.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T04:04:21.572514Z` distance=0.021 → {'next30m_imbalance_delta': 61.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

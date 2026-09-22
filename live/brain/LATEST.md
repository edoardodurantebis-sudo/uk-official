# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T23:01:39.891099Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.249e+04 d1=0.0 d12=-15.0 z=-10.791836
- **PERSISTENT_DOWN** `ind_demand` value=-1.249e+04 d1=0.0 d12=-15.0 z=-10.791836
- **ROBUST_OUTLIER** `ind_demand` value=-1.249e+04 d1=0.0 d12=-15.0 z=-10.791836
- **PERSISTENT_DOWN** `thermal_base` value=1.379e+04 d1=-34.0 d12=-1307.0 z=-9.775696144412192
- **ROBUST_OUTLIER** `thermal_base` value=1.379e+04 d1=-34.0 d12=-1307.0 z=-9.775696144412192
- **PERSISTENT_DOWN** `ccgt_gen` value=1.005e+04 d1=-32.0 d12=-1308.0 z=-9.714984929394813
- **ROBUST_OUTLIER** `ccgt_gen` value=1.005e+04 d1=-32.0 d12=-1308.0 z=-9.714984929394813
- **CHANGE_POINT** `wind_gen` value=3007 d1=58.0 d12=489.0 z=1.9452789862412176
- **CHANGE_POINT** `margin` value=3.723e+04 d1=0.0 d12=20.0 z=1.1428854097222223
- **REVERSAL** `ps_gen` value=147 d1=-1.0 d12=3.0 z=-2.4418815355932204
- **PERSISTENT_UP** `wind_gen` value=3007 d1=58.0 d12=489.0 z=1.9452789862412176
- **PERSISTENT_DOWN** `interconnector_net` value=5149 d1=-175.0 d12=-22.0 z=-1.574228875466418
- **ACCELERATION** `interconnector_net` value=5149 d1=-175.0 d12=-22.0 z=-1.574228875466418
- **PERSISTENT_DOWN** `imbalance` value=-8056 d1=0.0 d12=-2.0 z=-0.8912900267857143
- **PERSISTENT_DOWN** `ind_generation` value=1.312e+04 d1=0.0 d12=-2.0 z=-0.8912900267857143

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.020 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:54:12.694588Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:58:28.957668Z` distance=0.021 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:02:41.905609Z` distance=0.021 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:06:53.543524Z` distance=0.021 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

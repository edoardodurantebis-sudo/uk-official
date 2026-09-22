# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T08:09:33.225367Z`  
Memory snapshots: **2447**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.269e+04 d1=0.0 d12=-238.0 z=-5.855797375
- **ROBUST_OUTLIER** `ind_demand` value=-1.269e+04 d1=0.0 d12=-238.0 z=-5.855797375
- **CHANGE_POINT** `imbalance` value=-3831 d1=0.0 d12=-691.0 z=-2.5330022676630435
- **CHANGE_POINT** `interconnector_net` value=8079 d1=718.0 d12=3885.0 z=1.5972388726370135
- **CHANGE_POINT** `ps_gen` value=-170 d1=-1.0 d12=3.0 z=0.25293365624999997
- **CHANGE_POINT** `thermal_base` value=1.691e+04 d1=-207.0 d12=-891.0 z=0.08765258502304148
- **CHANGE_POINT** `ccgt_gen` value=1.325e+04 d1=-214.0 d12=-901.0 z=0.08275566120848708
- **CHANGE_POINT** `ts_demand_forecast` value=2.123e+04 d1=0.0 d12=-476.0 z=None
- **PERSISTENT_UP** `interconnector_net` value=8079 d1=718.0 d12=3885.0 z=1.5972388726370135
- **PERSISTENT_UP** `nuclear_gen` value=3658 d1=7.0 d12=10.0 z=1.1241495833333335
- **ACCELERATION** `nuclear_gen` value=3658 d1=7.0 d12=10.0 z=1.1241495833333335
- **PERSISTENT_DOWN** `biomass_gen` value=3029 d1=-1.0 d12=-2.0 z=-0.4496598333333333
- **ACCELERATION** `biomass_gen` value=3029 d1=-1.0 d12=-2.0 z=-0.4496598333333333
- **PERSISTENT_UP** `wind_gen` value=3569 d1=94.0 d12=37.0 z=0.29006554015544045
- **ACCELERATION** `wind_gen` value=3569 d1=94.0 d12=37.0 z=0.29006554015544045

## Nearest historical live analogues

- `2026-09-22T04:54:50.378428Z` distance=0.204 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T04:59:01.331890Z` distance=0.204 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:03:14.010868Z` distance=0.204 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:07:26.495356Z` distance=0.204 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': -696.0}
- `2026-09-22T05:11:39.965439Z` distance=0.204 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': -696.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

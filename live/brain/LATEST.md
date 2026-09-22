# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T08:05:20.198964Z`  
Memory snapshots: **2446**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.269e+04 d1=0.0 d12=-238.0 z=-5.855797375
- **ROBUST_OUTLIER** `ind_demand` value=-1.269e+04 d1=0.0 d12=-238.0 z=-5.855797375
- **CHANGE_POINT** `imbalance` value=-3831 d1=0.0 d12=-691.0 z=-2.5330022676630435
- **CHANGE_POINT** `ind_generation` value=1.788e+04 d1=0.0 d12=-445.0 z=-1.6136985954301075
- **CHANGE_POINT** `interconnector_net` value=7361 d1=0.0 d12=3295.0 z=1.443375920929309
- **CHANGE_POINT** `ps_gen` value=-169 d1=0.0 d12=3.0 z=0.3174069411764706
- **CHANGE_POINT** `thermal_base` value=1.712e+04 d1=0.0 d12=-697.0 z=0.27445128671749597
- **CHANGE_POINT** `ccgt_gen` value=1.347e+04 d1=0.0 d12=-700.0 z=0.27267763774687626
- **CHANGE_POINT** `ts_demand_forecast` value=2.123e+04 d1=0.0 d12=-230.0 z=None
- **PERSISTENT_UP** `interconnector_net` value=7361 d1=0.0 d12=3295.0 z=1.443375920929309
- **PERSISTENT_UP** `nuclear_gen` value=3651 d1=0.0 d12=3.0 z=-0.4496598333333333
- **ACCELERATION** `nuclear_gen` value=3651 d1=0.0 d12=3.0 z=-0.4496598333333333
- **PERSISTENT_DOWN** `wind_gen` value=3475 d1=0.0 d12=-27.0 z=-0.4331585550458716
- **ACCELERATION** `wind_gen` value=3475 d1=0.0 d12=-27.0 z=-0.4331585550458716
- **PERSISTENT_UP** `ps_gen` value=-169 d1=0.0 d12=3.0 z=0.3174069411764706

## Nearest historical live analogues

- `2026-09-22T04:54:50.378428Z` distance=0.205 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T04:59:01.331890Z` distance=0.205 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:03:14.010868Z` distance=0.205 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:07:26.495356Z` distance=0.205 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': -696.0}
- `2026-09-22T05:11:39.965439Z` distance=0.205 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': -696.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

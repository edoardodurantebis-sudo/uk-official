# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T07:56:55.538215Z`  
Memory snapshots: **2444**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.269e+04 d1=0.0 d12=-238.0 z=-5.855797375
- **ROBUST_OUTLIER** `ind_demand` value=-1.269e+04 d1=0.0 d12=-238.0 z=-5.855797375
- **CHANGE_POINT** `imbalance` value=-3831 d1=0.0 d12=-691.0 z=-2.5330022676630435
- **CHANGE_POINT** `ind_generation` value=1.788e+04 d1=0.0 d12=-445.0 z=-1.6136985954301075
- **CHANGE_POINT** `interconnector_net` value=7051 d1=-4.0 d12=3717.0 z=1.3769448415011913
- **CHANGE_POINT** `ccgt_gen` value=1.35e+04 d1=-99.0 d12=-690.0 z=0.3824544113913338
- **CHANGE_POINT** `thermal_base` value=1.715e+04 d1=-99.0 d12=-697.0 z=0.3807048571914315
- **PERSISTENT_DOWN** `nuclear_gen` value=3643 d1=0.0 d12=-7.0 z=-2.248299166666667
- **ACCELERATION** `nuclear_gen` value=3643 d1=0.0 d12=-7.0 z=-2.248299166666667
- **CHANGE_POINT** `ps_gen` value=-170 d1=2.0 d12=-10.0 z=0.22482991666666663
- **REVERSAL** `interconnector_net` value=7051 d1=-4.0 d12=3717.0 z=1.3769448415011913
- **PERSISTENT_DOWN** `residual_proxy` value=8391 d1=0.0 d12=-228.0 z=-0.8954432887931034
- **REVERSAL** `wind_gen` value=3493 d1=-14.0 d12=54.0 z=-0.4319765814606742
- **ACCELERATION** `wind_gen` value=3493 d1=-14.0 d12=54.0 z=-0.4319765814606742
- **PERSISTENT_DOWN** `ccgt_gen` value=1.35e+04 d1=-99.0 d12=-690.0 z=0.3824544113913338

## Nearest historical live analogues

- `2026-09-22T04:54:50.378428Z` distance=0.205 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T04:59:01.331890Z` distance=0.205 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:03:14.010868Z` distance=0.205 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:07:26.495356Z` distance=0.205 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': -696.0}
- `2026-09-22T05:11:39.965439Z` distance=0.205 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': -696.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

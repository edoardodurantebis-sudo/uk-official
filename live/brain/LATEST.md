# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T08:13:46.608813Z`  
Memory snapshots: **2448**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.269e+04 d1=0.0 d12=0.0 z=-5.855797375
- **ROBUST_OUTLIER** `ind_demand` value=-1.269e+04 d1=0.0 d12=0.0 z=-5.855797375
- **CHANGE_POINT** `imbalance` value=-3831 d1=0.0 d12=0.0 z=-2.5330022676630435
- **CHANGE_POINT** `ps_gen` value=-169 d1=1.0 d12=4.0 z=0.3147618833333333
- **CHANGE_POINT** `thermal_base` value=1.653e+04 d1=-383.0 d12=-1226.0 z=-0.21788103589232305
- **CHANGE_POINT** `ccgt_gen` value=1.288e+04 d1=-378.0 d12=-1233.0 z=-0.21744744179104478
- **CHANGE_POINT** `ts_demand_forecast` value=2.123e+04 d1=0.0 d12=-476.0 z=None
- **PERSISTENT_UP** `interconnector_net` value=8338 d1=259.0 d12=4168.0 z=1.6527409680301826
- **PERSISTENT_DOWN** `biomass_gen` value=3027 d1=-2.0 d12=-3.0 z=-0.8993196666666666
- **PERSISTENT_UP** `wind_gen` value=3606 d1=37.0 d12=83.0 z=0.5486781904145078
- **ACCELERATION** `wind_gen` value=3606 d1=37.0 d12=83.0 z=0.5486781904145078
- **PERSISTENT_UP** `ps_gen` value=-169 d1=1.0 d12=4.0 z=0.3147618833333333
- **ACCELERATION** `ps_gen` value=-169 d1=1.0 d12=4.0 z=0.3147618833333333
- **PERSISTENT_DOWN** `thermal_base` value=1.653e+04 d1=-383.0 d12=-1226.0 z=-0.21788103589232305
- **PERSISTENT_DOWN** `ccgt_gen` value=1.288e+04 d1=-378.0 d12=-1233.0 z=-0.21744744179104478

## Nearest historical live analogues

- `2026-09-22T04:54:50.378428Z` distance=0.204 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T04:59:01.331890Z` distance=0.204 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:03:14.010868Z` distance=0.204 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:07:26.495356Z` distance=0.204 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': -696.0}
- `2026-09-22T05:11:39.965439Z` distance=0.204 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': -696.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

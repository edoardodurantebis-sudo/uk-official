# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T03:40:54.258660Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `margin` value=3.857e+04 d1=0.0 d12=-111.0 z=90.51652444999999
- **ROBUST_OUTLIER** `margin` value=3.857e+04 d1=0.0 d12=-111.0 z=90.51652444999999
- **CHANGE_POINT** `ind_demand` value=-1.242e+04 d1=0.0 d12=5.0 z=4.6464849444444445
- **CHANGE_POINT** `interconnector_net` value=-3770 d1=21.0 d12=-3303.0 z=-3.004075235946982
- **ROBUST_OUTLIER** `ind_demand` value=-1.242e+04 d1=0.0 d12=5.0 z=4.6464849444444445
- **CHANGE_POINT** `wind_gen` value=6695 d1=234.0 d12=1339.0 z=1.5054787557189542
- **CHANGE_POINT** `ps_gen` value=144 d1=15.0 d12=4.0 z=-1.1241495833333335
- **REVERSAL** `interconnector_net` value=-3770 d1=21.0 d12=-3303.0 z=-3.004075235946982
- **ROBUST_OUTLIER** `interconnector_net` value=-3770 d1=21.0 d12=-3303.0 z=-3.004075235946982
- **PERSISTENT_UP** `biomass_gen` value=2884 d1=4.0 d12=13.0 z=-2.9227889166666667
- **PERSISTENT_DOWN** `nuclear_gen` value=3717 d1=-4.0 d12=-10.0 z=-2.398185777777778
- **PERSISTENT_UP** `wind_gen` value=6695 d1=234.0 d12=1339.0 z=1.5054787557189542
- **PERSISTENT_DOWN** `thermal_base` value=1.285e+04 d1=-31.0 d12=-338.0 z=-1.2664879478417266
- **PERSISTENT_DOWN** `ccgt_gen` value=9136 d1=-27.0 d12=-328.0 z=-1.2620015030413625
- **PERSISTENT_UP** `ps_gen` value=144 d1=15.0 d12=4.0 z=-1.1241495833333335

## Nearest historical live analogues

- `2026-09-21T07:19:16.764355Z` distance=0.390 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:53:56.422040Z` distance=0.419 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:06:37.268181Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

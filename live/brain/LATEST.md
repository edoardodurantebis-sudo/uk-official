# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T12:31:54.173156Z`  
Memory snapshots: **2170**  
Current physical regime: **BALANCED**

Regime read: wind falling.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=0.0 d12=4.0 z=14.890658326923075
- **PERSISTENT_UP** `ind_demand` value=-1.224e+04 d1=0.0 d12=4.0 z=14.890658326923075
- **ACCELERATION** `ind_demand` value=-1.224e+04 d1=0.0 d12=4.0 z=14.890658326923075
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=4.0 z=14.890658326923075
- **CHANGE_POINT** `ps_gen` value=228 d1=0.0 d12=236.0 z=8.843310055555555
- **ROBUST_OUTLIER** `ps_gen` value=228 d1=0.0 d12=236.0 z=8.843310055555555
- **PERSISTENT_DOWN** `ccgt_gen` value=6201 d1=-90.0 d12=-804.0 z=-3.5910403226970034
- **ROBUST_OUTLIER** `ccgt_gen` value=6201 d1=-90.0 d12=-804.0 z=-3.5910403226970034
- **PERSISTENT_DOWN** `thermal_base` value=9713 d1=-91.0 d12=-809.0 z=-3.311899565762004
- **ROBUST_OUTLIER** `thermal_base` value=9713 d1=-91.0 d12=-809.0 z=-3.311899565762004
- **CHANGE_POINT** `wind_gen` value=3986 d1=103.0 d12=579.0 z=1.1950503039419087
- **CHANGE_POINT** `margin` value=3.668e+04 d1=0.0 d12=0.0 z=-0.8755341339210748
- **PERSISTENT_DOWN** `nuclear_gen` value=3512 d1=-1.0 d12=-5.0 z=2.44502534375
- **ACCELERATION** `nuclear_gen` value=3512 d1=-1.0 d12=-5.0 z=2.44502534375
- **PERSISTENT_DOWN** `wind_forecast` value=8616 d1=-307.0 d12=-307.0 z=-1.6051810329457366

## Nearest historical live analogues

- `2026-09-21T11:32:38.703181Z` distance=0.027 → {'next30m_imbalance_delta': 1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T11:36:50.598890Z` distance=0.027 → {'next30m_imbalance_delta': 1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T11:24:15.280087Z` distance=0.083 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 182.0, 'next30m_residual_proxy_delta': -104.0}
- `2026-09-21T11:28:26.888729Z` distance=0.083 → {'next30m_imbalance_delta': 1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 178.0, 'next30m_residual_proxy_delta': -104.0}
- `2026-09-21T10:54:44.355248Z` distance=0.083 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

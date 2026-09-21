# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T12:27:33.509322Z`  
Memory snapshots: **2169**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=4.0 d12=4.0 z=14.890658326923075
- **PERSISTENT_UP** `ind_demand` value=-1.224e+04 d1=4.0 d12=4.0 z=14.890658326923075
- **ACCELERATION** `ind_demand` value=-1.224e+04 d1=4.0 d12=4.0 z=14.890658326923075
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=4.0 d12=4.0 z=14.890658326923075
- **CHANGE_POINT** `ps_gen` value=228 d1=0.0 d12=236.0 z=8.843310055555555
- **ROBUST_OUTLIER** `ps_gen` value=228 d1=0.0 d12=236.0 z=8.843310055555555
- **PERSISTENT_DOWN** `ccgt_gen` value=6291 d1=-175.0 d12=-836.0 z=-3.4639812855951058
- **ROBUST_OUTLIER** `ccgt_gen` value=6291 d1=-175.0 d12=-836.0 z=-3.4639812855951058
- **PERSISTENT_DOWN** `thermal_base` value=9804 d1=-178.0 d12=-838.0 z=-3.2038263125
- **ROBUST_OUTLIER** `thermal_base` value=9804 d1=-178.0 d12=-838.0 z=-3.2038263125
- **CHANGE_POINT** `wind_gen` value=3883 d1=44.0 d12=504.0 z=0.9790980241935484
- **CHANGE_POINT** `margin` value=3.668e+04 d1=0.0 d12=0.0 z=-0.8755341339210748
- **PERSISTENT_DOWN** `nuclear_gen` value=3513 d1=-3.0 d12=-2.0 z=2.697959
- **ACCELERATION** `nuclear_gen` value=3513 d1=-3.0 d12=-2.0 z=2.697959
- **REVERSAL** `interconnector_net` value=1.127e+04 d1=8.0 d12=-29.0 z=1.0515391433203631

## Nearest historical live analogues

- `2026-09-21T11:32:38.703181Z` distance=0.005 → {'next30m_imbalance_delta': 1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T11:24:15.280087Z` distance=0.080 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 182.0, 'next30m_residual_proxy_delta': -104.0}
- `2026-09-21T11:28:26.888729Z` distance=0.080 → {'next30m_imbalance_delta': 1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 178.0, 'next30m_residual_proxy_delta': -104.0}
- `2026-09-21T10:54:44.355248Z` distance=0.080 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:58:55.909932Z` distance=0.080 → {'next30m_imbalance_delta': 856.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

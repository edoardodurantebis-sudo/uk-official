# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T06:02:11.446633Z`  
Memory snapshots: **2417**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=1.418e+04 d1=104.0 d12=710.0 z=4.980323305555555
- **CHANGE_POINT** `thermal_base` value=1.783e+04 d1=93.0 d12=700.0 z=4.975856029113924
- **PERSISTENT_UP** `ccgt_gen` value=1.418e+04 d1=104.0 d12=710.0 z=4.980323305555555
- **ROBUST_OUTLIER** `ccgt_gen` value=1.418e+04 d1=104.0 d12=710.0 z=4.980323305555555
- **PERSISTENT_UP** `thermal_base` value=1.783e+04 d1=93.0 d12=700.0 z=4.975856029113924
- **ROBUST_OUTLIER** `thermal_base` value=1.783e+04 d1=93.0 d12=700.0 z=4.975856029113924
- **CHANGE_POINT** `ps_gen` value=-172 d1=-1.0 d12=1.0 z=0.680735025462963
- **CHANGE_POINT** `imbalance` value=-3209 d1=0.0 d12=103.0 z=-0.6406398926579925
- **CHANGE_POINT** `ind_generation` value=1.825e+04 d1=0.0 d12=103.0 z=-0.6406398926579925
- **CHANGE_POINT** `wind_gen` value=3676 d1=-9.0 d12=220.0 z=0.148387745
- **CHANGE_POINT** `ind_demand` value=-1.248e+04 d1=0.0 d12=46.0 z=-0.028103739583333332
- **PERSISTENT_UP** `interconnector_net` value=-1769 d1=179.0 d12=1331.0 z=-1.5741623678702248
- **PERSISTENT_DOWN** `nuclear_gen` value=3650 d1=-11.0 d12=-10.0 z=-0.8993196666666666
- **ACCELERATION** `nuclear_gen` value=3650 d1=-11.0 d12=-10.0 z=-0.8993196666666666
- **PERSISTENT_UP** `biomass_gen` value=3030 d1=1.0 d12=1.0 z=-0.8331932205882353

## Nearest historical live analogues

- `2026-09-22T03:33:35.816390Z` distance=0.074 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:37:48.990972Z` distance=0.074 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:42:37.215255Z` distance=0.074 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:46:49.421565Z` distance=0.074 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:51:00.662974Z` distance=0.075 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

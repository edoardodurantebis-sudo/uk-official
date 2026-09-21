# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T12:23:20.404986Z`  
Memory snapshots: **2168**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=0.0 d12=0.0 z=14.786890673076924
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=0.0 z=14.786890673076924
- **CHANGE_POINT** `ps_gen` value=228 d1=0.0 d12=236.0 z=8.843310055555555
- **ROBUST_OUTLIER** `ps_gen` value=228 d1=0.0 d12=236.0 z=8.843310055555555
- **PERSISTENT_DOWN** `ccgt_gen` value=6466 d1=-108.0 d12=-674.0 z=-3.212106878627232
- **ROBUST_OUTLIER** `ccgt_gen` value=6466 d1=-108.0 d12=-674.0 z=-3.212106878627232
- **PERSISTENT_UP** `nuclear_gen` value=3516 d1=0.0 d12=1.0 z=3.2038263125
- **ACCELERATION** `nuclear_gen` value=3516 d1=0.0 d12=1.0 z=3.2038263125
- **ROBUST_OUTLIER** `nuclear_gen` value=3516 d1=0.0 d12=1.0 z=3.2038263125
- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=0.0 z=1.0682912189440994
- **PERSISTENT_DOWN** `thermal_base` value=9982 d1=-108.0 d12=-673.0 z=-2.9547048354363827
- **CHANGE_POINT** `margin` value=3.668e+04 d1=4.0 d12=0.0 z=-0.8755341339210748
- **CHANGE_POINT** `wind_gen` value=3839 d1=72.0 d12=524.0 z=0.8701658972527473
- **REVERSAL** `interconnector_net` value=1.126e+04 d1=-20.0 d12=12.0 z=1.0375419500648508
- **ACCELERATION** `interconnector_net` value=1.126e+04 d1=-20.0 d12=12.0 z=1.0375419500648508

## Nearest historical live analogues

- `2026-09-21T11:24:15.280087Z` distance=0.080 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 182.0, 'next30m_residual_proxy_delta': -104.0}
- `2026-09-21T11:28:26.888729Z` distance=0.080 → {'next30m_imbalance_delta': 1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 178.0, 'next30m_residual_proxy_delta': -104.0}
- `2026-09-21T10:54:44.355248Z` distance=0.080 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:58:55.909932Z` distance=0.080 → {'next30m_imbalance_delta': 856.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T11:03:12.814990Z` distance=0.080 → {'next30m_imbalance_delta': 856.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

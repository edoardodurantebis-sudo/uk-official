# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T19:34:52.635712Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low, wind rising.

## Active patterns

- **PERSISTENT_DOWN** `residual_proxy` value=7061 d1=-77.0 d12=-77.0 z=-23.157481416666666
- **ACCELERATION** `residual_proxy` value=7061 d1=-77.0 d12=-77.0 z=-23.157481416666666
- **ROBUST_OUTLIER** `residual_proxy` value=7061 d1=-77.0 d12=-77.0 z=-23.157481416666666
- **CHANGE_POINT** `imbalance` value=-8035 d1=0.0 d12=-27.0 z=-5.171088083333333
- **ROBUST_OUTLIER** `imbalance` value=-8035 d1=0.0 d12=-27.0 z=-5.171088083333333
- **CHANGE_POINT** `margin` value=3.712e+04 d1=0.0 d12=-35.0 z=-1.5635898750000001
- **ROBUST_OUTLIER** `ind_generation` value=1.314e+04 d1=0.0 d12=-27.0 z=-3.4473920555555555
- **CHANGE_POINT** `thermal_base` value=1.912e+04 d1=-34.0 d12=104.0 z=0.7132535287356322
- **CHANGE_POINT** `ccgt_gen` value=1.539e+04 d1=-37.0 d12=102.0 z=0.7124604199455207
- **CHANGE_POINT** `ps_gen` value=1359 d1=-6.0 d12=-151.0 z=0.5041977834158415
- **REVERSAL** `thermal_base` value=1.912e+04 d1=-34.0 d12=104.0 z=0.7132535287356322
- **REVERSAL** `ccgt_gen` value=1.539e+04 d1=-37.0 d12=102.0 z=0.7124604199455207
- **ACCELERATION** `ccgt_gen` value=1.539e+04 d1=-37.0 d12=102.0 z=0.7124604199455207
- **PERSISTENT_DOWN** `ps_gen` value=1359 d1=-6.0 d12=-151.0 z=0.5041977834158415
- **PERSISTENT_UP** `interconnector_net` value=6976 d1=851.0 d12=1669.0 z=-0.31708577910958907

## Nearest historical live analogues

- `2026-09-22T16:53:15.798478Z` distance=0.018 → {'next30m_imbalance_delta': -11.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T16:57:29.073662Z` distance=0.018 → {'next30m_imbalance_delta': 16.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 25.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:01:43.529354Z` distance=0.018 → {'next30m_imbalance_delta': 16.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 25.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:05:59.746986Z` distance=0.018 → {'next30m_imbalance_delta': 16.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 25.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:10:14.885436Z` distance=0.018 → {'next30m_imbalance_delta': 16.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 25.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

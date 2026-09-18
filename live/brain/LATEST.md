# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T08:26:15.822729Z`  
Memory snapshots: **1143**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **PERSISTENT_UP** `ind_demand` value=-1.174e+04 d1=0.0 d12=3.0 z=-6.541277952830188
- **ACCELERATION** `ind_demand` value=-1.174e+04 d1=0.0 d12=3.0 z=-6.541277952830188
- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=3.0 z=-6.541277952830188
- **CHANGE_POINT** `imbalance` value=9625 d1=0.0 d12=-593.0 z=-3.1701018249999997
- **PERSISTENT_DOWN** `wind_gen` value=1.226e+04 d1=-42.0 d12=-80.0 z=-3.8673257732774675
- **ACCELERATION** `wind_gen` value=1.226e+04 d1=-42.0 d12=-80.0 z=-3.8673257732774675
- **ROBUST_OUTLIER** `wind_gen` value=1.226e+04 d1=-42.0 d12=-80.0 z=-3.8673257732774675
- **PERSISTENT_DOWN** `interconnector_net` value=3156 d1=0.0 d12=-277.0 z=3.770320680831974
- **ROBUST_OUTLIER** `interconnector_net` value=3156 d1=0.0 d12=-277.0 z=3.770320680831974
- **CHANGE_POINT** `margin` value=3.765e+04 d1=0.0 d12=-112.0 z=-1.6793418265306121
- **PERSISTENT_DOWN** `imbalance` value=9625 d1=0.0 d12=-593.0 z=-3.1701018249999997
- **ACCELERATION** `imbalance` value=9625 d1=0.0 d12=-593.0 z=-3.1701018249999997
- **ROBUST_OUTLIER** `imbalance` value=9625 d1=0.0 d12=-593.0 z=-3.1701018249999997
- **CHANGE_POINT** `ps_gen` value=597 d1=53.0 d12=-2.0 z=0.64306191218638
- **CHANGE_POINT** `thermal_base` value=7355 d1=31.0 d12=-343.0 z=0.3258920772277228

## Nearest historical live analogues

- `2026-09-18T07:23:09.699179Z` distance=0.068 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:27:20.707745Z` distance=0.068 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:31:32.031758Z` distance=0.068 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T06:53:49.549140Z` distance=0.424 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T06:58:01.482012Z` distance=0.424 → {'next30m_imbalance_delta': -347.0, 'next30m_margin_delta': -189.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

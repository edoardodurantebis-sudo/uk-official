# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T08:22:03.400207Z`  
Memory snapshots: **1142**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **PERSISTENT_UP** `ind_demand` value=-1.174e+04 d1=3.0 d12=3.0 z=-6.541277952830188
- **ACCELERATION** `ind_demand` value=-1.174e+04 d1=3.0 d12=3.0 z=-6.541277952830188
- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=3.0 d12=3.0 z=-6.541277952830188
- **CHANGE_POINT** `imbalance` value=9625 d1=-593.0 d12=-593.0 z=-3.1701018249999997
- **PERSISTENT_DOWN** `interconnector_net` value=3156 d1=-1.0 d12=-277.0 z=3.8857212047435468
- **ROBUST_OUTLIER** `interconnector_net` value=3156 d1=-1.0 d12=-277.0 z=3.8857212047435468
- **PERSISTENT_DOWN** `wind_gen` value=1.23e+04 d1=-116.0 d12=-57.0 z=-3.7220923336397056
- **ACCELERATION** `wind_gen` value=1.23e+04 d1=-116.0 d12=-57.0 z=-3.7220923336397056
- **ROBUST_OUTLIER** `wind_gen` value=1.23e+04 d1=-116.0 d12=-57.0 z=-3.7220923336397056
- **CHANGE_POINT** `margin` value=3.765e+04 d1=-112.0 d12=-112.0 z=-1.6793418265306121
- **PERSISTENT_DOWN** `imbalance` value=9625 d1=-593.0 d12=-593.0 z=-3.1701018249999997
- **ACCELERATION** `imbalance` value=9625 d1=-593.0 d12=-593.0 z=-3.1701018249999997
- **ROBUST_OUTLIER** `imbalance` value=9625 d1=-593.0 d12=-593.0 z=-3.1701018249999997
- **CHANGE_POINT** `ps_gen` value=544 d1=163.0 d12=-55.0 z=0.3868041577060932
- **PERSISTENT_UP** `residual_proxy` value=8681 d1=0.0 d12=140.0 z=1.9859975972222221

## Nearest historical live analogues

- `2026-09-18T07:23:09.699179Z` distance=0.068 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:27:20.707745Z` distance=0.068 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T06:53:49.549140Z` distance=0.424 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T06:58:01.482012Z` distance=0.424 → {'next30m_imbalance_delta': -347.0, 'next30m_margin_delta': -189.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T07:02:14.066477Z` distance=0.424 → {'next30m_imbalance_delta': -347.0, 'next30m_margin_delta': -189.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

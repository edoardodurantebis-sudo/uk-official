# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T03:40:35.454286Z`  
Memory snapshots: **1075**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `margin` value=3.817e+04 d1=0.0 d12=-46.0 z=11.292488185567011
- **ROBUST_OUTLIER** `margin` value=3.817e+04 d1=0.0 d12=-46.0 z=11.292488185567011
- **CHANGE_POINT** `interconnector_net` value=-6990 d1=0.0 d12=-1667.0 z=-2.300689276053864
- **PERSISTENT_DOWN** `interconnector_net` value=-6990 d1=0.0 d12=-1667.0 z=-2.300689276053864
- **PERSISTENT_UP** `nuclear_gen` value=3339 d1=3.0 d12=9.0 z=1.686224375
- **ACCELERATION** `wind_gen` value=1.373e+04 d1=-33.0 d12=-287.0 z=-1.3460469358695653
- **PERSISTENT_DOWN** `ps_gen` value=166 d1=-14.0 d12=-268.0 z=-0.3731219893617021
- **ACCELERATION** `ps_gen` value=166 d1=-14.0 d12=-268.0 z=-0.3731219893617021
- **REVERSAL** `ccgt_gen` value=3696 d1=-51.0 d12=276.0 z=-0.1829124745762712
- **REVERSAL** `thermal_base` value=7035 d1=-48.0 d12=285.0 z=-0.16079167414860682
- **PERSISTENT_UP** `biomass_gen` value=1928 d1=4.0 d12=178.0 z=-0.060970824858757065
- **PERSISTENT_UP** `residual_proxy` value=8469 d1=0.0 d12=11023.0 z=None
- **PERSISTENT_DOWN** `wind_forecast` value=7845 d1=0.0 d12=-11023.0 z=None

## Nearest historical live analogues

- `2026-09-14T23:53:08.620374Z` distance=5.377 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:57:18.949614Z` distance=5.377 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:32:10.678260Z` distance=5.428 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:36:23.316269Z` distance=5.428 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:40:34.642541Z` distance=5.428 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.

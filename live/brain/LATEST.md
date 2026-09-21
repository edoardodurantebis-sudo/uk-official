# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T16:09:03.909955Z`  
Memory snapshots: **2221**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.588e+04 d1=192.0 d12=2597.0 z=6.42907471324864
- **CHANGE_POINT** `ccgt_gen` value=1.237e+04 d1=187.0 d12=2585.0 z=6.267979526327434
- **PERSISTENT_UP** `thermal_base` value=1.588e+04 d1=192.0 d12=2597.0 z=6.42907471324864
- **ROBUST_OUTLIER** `thermal_base` value=1.588e+04 d1=192.0 d12=2597.0 z=6.42907471324864
- **PERSISTENT_UP** `ccgt_gen` value=1.237e+04 d1=187.0 d12=2585.0 z=6.267979526327434
- **ROBUST_OUTLIER** `ccgt_gen` value=1.237e+04 d1=187.0 d12=2585.0 z=6.267979526327434
- **CHANGE_POINT** `interconnector_net` value=1.034e+04 d1=-262.0 d12=-894.0 z=-2.978309262836186
- **PERSISTENT_DOWN** `interconnector_net` value=1.034e+04 d1=-262.0 d12=-894.0 z=-2.978309262836186
- **CHANGE_POINT** `margin` value=3.621e+04 d1=0.0 d12=-47.0 z=-0.854945341008772
- **CHANGE_POINT** `imbalance` value=-3079 d1=0.0 d12=128.0 z=0.67448975
- **CHANGE_POINT** `nuclear_gen` value=3507 d1=5.0 d12=12.0 z=0.4817783928571429
- **CHANGE_POINT** `ind_generation` value=1.838e+04 d1=0.0 d12=83.0 z=0.4354973188976378
- **PERSISTENT_DOWN** `wind_gen` value=3304 d1=-50.0 d12=-42.0 z=-0.5908124501879699
- **ACCELERATION** `wind_gen` value=3304 d1=-50.0 d12=-42.0 z=-0.5908124501879699
- **PERSISTENT_UP** `nuclear_gen` value=3507 d1=5.0 d12=12.0 z=0.4817783928571429

## Nearest historical live analogues

- `2026-09-21T14:23:01.446169Z` distance=0.033 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:27:16.085310Z` distance=0.033 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:31:28.406523Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:35:41.380076Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:39:54.228512Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
